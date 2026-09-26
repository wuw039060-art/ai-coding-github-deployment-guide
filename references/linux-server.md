# Linux 与服务器运行手册

这份参考收纳 systemd 的操作级材料。示例服务名是 `notes-api`，执行时必须替换为主机上真实存在且属于当前项目的单元。`systemctl` 的启停和配置修改会改变服务器状态；只读检查与变更命令不要混在一次复制粘贴中。

## 最小状态与日志命令

```bash
systemctl status notes-api --no-pager
systemctl is-active notes-api
systemctl is-enabled notes-api
sudo journalctl -u notes-api -n 100 --no-pager
sudo journalctl -u notes-api --since "30 minutes ago" --no-pager
sudo journalctl -u notes-api -b --no-pager
sudo journalctl -u notes-api -b -1 --no-pager
```

`status` 给出 systemd 当前看到的状态和少量最近日志；`journalctl` 用于缩小时间、启动批次和优先级。命令成功只证明管理器接受了请求，不证明用户功能可用。`status` 进入翻页器时按 `q` 退出，或使用 `--no-pager`。

实时跟随日志可以这样查看。

```bash
sudo journalctl -u notes-api -f
```

先记录主机名、环境与开始时间，用 `Ctrl+C` 结束查看；它不会停止服务。日志可能含令牌、个人数据和内部地址，分享前脱敏。

## 启动、重启、重新加载与开机启动

```bash
sudo systemctl start notes-api
sudo systemctl stop notes-api
sudo systemctl restart notes-api
sudo systemctl reload notes-api
sudo systemctl enable notes-api
sudo systemctl disable notes-api
```

- `start` / `stop` 改变当前运行状态。
- `restart` 中断并创建新进程，新的环境变量通常在这时读取。
- `reload` 是否受支持由程序和 unit 决定；先查 `CanReload` 和软件文档。
- `enable` / `disable` 改变未来启动关系，不等同于现在已经运行或停止。

受控重启后至少验证服务状态、此次启动日志、本机健康地址、公开入口和一个核心用户操作。

## 最小 unit 与文件位置

```ini
[Unit]
Description=Notes API
After=network.target

[Service]
Type=simple
User=notes
Group=notes
WorkingDirectory=/srv/notes/current
ExecStart=/srv/notes/current/bin/notes-api
Restart=on-failure
RestartSec=5s

[Install]
WantedBy=multi-user.target
```

自建系统级单元通常放在 `/etc/systemd/system/`。发行版软件包可能在 `/usr/lib/systemd/system/` 或 `/lib/systemd/system/` 提供原始单元。优先使用软件包维护的单元，并用 drop-in 只覆盖差异。

```bash
systemctl cat notes-api
sudo systemctl edit notes-api
systemctl show notes-api --property=User,Group,WorkingDirectory,ExecStart,Restart
```

不要复制整份上游 unit 只为改一个字段。`systemctl cat` 显示原始文件和覆盖片段；`systemctl show` 显示 systemd 当前理解的最终属性。

## 修改 unit 的安全顺序

1. 记录当前版本、`systemctl cat`、状态、健康结果和回滚发布。
2. 备份要修改的精确配置；确认服务用户、工作目录、程序与环境文件都存在。
3. 静态检查指定 unit。

   ```bash
   systemd-analyze verify /etc/systemd/system/notes-api.service
   ```

4. 让 systemd 重读 unit。

   ```bash
   sudo systemctl daemon-reload
   ```

5. 在维护窗口重启或重新加载目标服务。
6. 查状态、本次启动日志、本机健康地址、公开入口和真实业务。
7. 任一步失败就停止流量推进，恢复旧配置或旧发布，重新加载并完成同样的验证。

静态验证不检查数据库凭据、端口占用或业务结果。修改中的旧进程仍正常时，不要因为验证器报错就先停止服务。

## 启动失败与重启循环

日志先找第一条根因，包括程序路径不存在、用户无权限、工作目录错误、端口占用、环境文件缺失、依赖服务不可达或应用启动异常。后续重复退出多半只是同一根因的结果。

短时间连续失败可能触发频率限制。根因修好后才执行下面的命令。

```bash
sudo systemctl reset-failed notes-api
sudo systemctl start notes-api
```

`reset-failed` 只清计数，不修应用。不要关闭限制掩盖循环。先保留状态与代表日志，必要时停止日志风暴，再修正配置。

`ExecStart` 默认不是交互式 shell，不会按终端习惯解释管道、重定向、通配符和 shell 内建命令。优先指向一个明确程序和参数；复杂准备逻辑放入受版本控制、可单独测试的脚本，并写明解释器。不要把秘密放在命令行参数中。

## 服务类型与重启策略

- `Type=simple` 表示前台长期进程，systemd 在进程启动后视为开始。
- `Type=notify` 表示程序就绪后向 systemd 发通知。
- `Type=oneshot` 表示执行一次后退出，可能显示 `active (exited)`。

`Restart=on-failure` 适合异常退出后恢复；`always` 连正常退出也会再次启动，不适合一次性任务。`RestartSec` 留出重试间隔。长期服务要配持续失败告警；自动恢复不是根因已经消失的证据。

程序应支持优雅关闭。停止超时要覆盖最长安全事务与清理过程，不能为了快直接设成零。反向代理或负载均衡器应先停止把新请求送往旧实例。

## 环境、目录与秘密

systemd 不自动继承 SSH 终端变量。使用 `Environment` 或 `EnvironmentFile` 时，秘密文件应在 Git 之外、权限受限且可轮换。记录变量名和存放系统，不记录值。修改环境文件后需要新进程才能读取。

相对路径取决于 `WorkingDirectory`。终端中从项目目录启动正常、systemd 中找不到 `./config.json` 时，应查最终工作目录和服务用户权限，不把配置复制到多个未知位置。使用 `current` 符号链接发布时，回滚还要检查链接目标、目录权限和依赖兼容。

## timer 与一次性任务

`.timer` 决定何时触发，实际工作通常由同名 `.service` 完成。

```bash
systemctl list-timers --all
systemctl status notes-backup.timer
systemctl status notes-backup.service
sudo journalctl -u notes-backup.service -n 100 --no-pager
```

timer 为 active 或已触发，不证明备份有效。还要验证目标文件、大小、校验和与恢复过程。服务器时区影响触发时间，用 `timedatectl` 只读确认；事故记录写带时区的时间。

## 日志容量与保留

```bash
sudo journalctl --disk-usage
sudo journalctl -u notes-api -p err --since today
```

清理日志是删除操作。先修复持续写入原因、保存事故证据并确认保留规则，再执行精确清理。应用同时写文件和标准输出时可能产生两套日志，应明确主要入口与各自保留策略。泄露秘密时先停止继续写入并轮换秘密，不能只删除日志。

## 依赖、资源与服务归属

`After` 主要表达顺序，不证明数据库、DNS 或互联网已经可用。少写不真实的强依赖，让应用对暂时不可用做有限重试并用健康检查表达就绪。资源限制可以保护主机，也可能因过小杀死正常进程；先测峰值、留余量并配置告警。

系统服务与 `systemctl --user` 的用户服务是两个范围。生产 Web 应用通常使用系统级 unit 和专用服务用户。不要在两层创建同名服务，也不要把留在 `tmux` 的手工进程当正式服务。前台调试前确认端口、PID 和 systemd 状态，结束后只保留预期管理器启动的进程。

## 服务运行手册模板

```text
单元名：
运行用户与组：
工作目录：
启动命令：
配置与环境文件（不写秘密值）：
监听端口：
本机健康地址：
公开入口：
查看状态：
最近 / 实时日志：
重启 / reload：
预计中断：
回滚版本与命令：
发布后核心验证：
```

## 视频入口

- systemctl 与 journalctl 练习见[全书视频索引里的 Linux 服务日志](../book/frontmatter/videos.md)。中文主入口使用 B 站 journalctl 命令讲解，YouTube 的 systemctl 与 journalctl 演示作为备用入口；服务名、权限和输出以练习主机为准。
