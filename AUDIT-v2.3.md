# 《AI 写代码之后》v2.3.0 Editorial Audit

**Status:** FROZEN — recovered v2.2.0 baseline; no chapter prose compressed yet.

- Manifest SHA256: `db9156899ef36d338ca1570059e23886927bfe39aeac91fb116487f0c3322bf2`
- Chapters audited: 104
- Recovered visible characters: 710456
- v2.3 target: 380000–420000 visible characters
- Reduction required to 400000-character midpoint: 43.70%
- Exact duplicate paragraphs over 80 characters: 0
- Risk-command candidates: 82
- Volatile-fact candidates: 538
- Invalid chapter references: 0

## Volume baseline

| Volume | Visible characters | v2.3 page target |
|---:|---:|---:|
| 1 | 32720 | 22–25 |
| 2 | 56424 | 36–40 |
| 3 | 63814 | 38–42 |
| 4 | 54147 | 34–38 |
| 5 | 49538 | 30–34 |
| 6 | 74398 | 42–48 |
| 7 | 50858 | 32–36 |
| 8 | 70723 | 40–46 |
| 9 | 67679 | 40–44 |
| 10 | 190155 | 90–100 |

## Six-chapter pilot baseline

| Chapter | Current chars | 40% reduction | 45% reduction | Source |
|---:|---:|---:|---:|---|
| 001 | 8364 | 5018 | 4600 | `chapters/001-从本地文件到公开可用的产品.md` |
| 019 | 8825 | 5295 | 4854 | `chapters/019-浏览器开发者工具-状态码和网络请求.md` |
| 040 | 11399 | 6839 | 6269 | `chapters/040-systemd-systemctl-journalctl-和服务日志.md` |
| 054 | 9316 | 5590 | 5124 | `chapters/054-google-play-内部测试与发布流程.md` |
| 070 | 8795 | 5277 | 4837 | `chapters/070-计划-权限-diff-测试和验证证据.md` |
| 091 | 5015 | 3009 | 2758 | `chapters/091-sli-slo-sla-与-error-budget.md` |

## Chapter baseline

| ID | Volume | Level | Visible chars | Paragraphs | Code blocks | Images | Links | Title |
|---:|---:|---|---:|---:|---:|---:|---:|---|
| 001 | 1 | core | 8364 | 83 | 0 | 2 | 0 | 从本地文件到公开可用的产品 |
| 002 | 1 | core | 8021 | 81 | 0 | 1 | 0 | 本地电脑、GitHub、部署平台、服务器和用户设备 |
| 003 | 1 | core | 7310 | 82 | 0 | 1 | 0 | 静态网站、动态网站、服务器程序和手机 App |
| 004 | 1 | core | 9025 | 99 | 7 | 1 | 0 | 文件、路径、终端和图形界面的最低限度知识 |
| 005 | 2 | core | 6977 | 78 | 1 | 1 | 0 | Git、GitHub、项目文件夹和仓库 |
| 006 | 2 | core | 6940 | 74 | 0 | 1 | 0 | GitHub 账号、公开仓库、私有仓库和网页上传 |
| 007 | 2 | core | 7550 | 72 | 0 | 1 | 1 | 用 GitHub Desktop 管理本地项目 |
| 008 | 2 | core | 7141 | 74 | 0 | 1 | 0 | Commit、Push、Pull、Clone 和 Sync |
| 009 | 2 | core | 6720 | 74 | 1 | 1 | 0 | 分支、合并、冲突、撤销与恢复 |
| 010 | 2 | core | 6995 | 85 | 2 | 1 | 0 | README、Releases、Issues、Actions、许可证和项目维护状态 |
| 011 | 2 | core | 6542 | 68 | 0 | 1 | 0 | 下载、检查并运行别人的项目 |
| 012 | 2 | core | 7559 | 90 | 2 | 1 | 0 | .gitignore、秘密泄露和历史中的敏感信息 |
| 013 | 3 | core | 7544 | 87 | 0 | 1 | 0 | 浏览器、客户端和服务器 |
| 014 | 3 | core | 8459 | 101 | 3 | 1 | 0 | IP、域名、DNS、端口和 URL |
| 015 | 3 | core | 8002 | 91 | 0 | 1 | 0 | HTTP、HTTPS、TLS、请求与响应 |
| 016 | 3 | core | 8040 | 96 | 0 | 1 | 0 | Cookie、Session、Token、缓存和 CDN |
| 017 | 3 | core | 7810 | 105 | 3 | 1 | 0 | HTML、CSS、JavaScript、前端和后端 |
| 018 | 3 | core | 7910 | 106 | 1 | 1 | 0 | API、数据库、文件存储和实时通信 |
| 019 | 3 | core | 8825 | 107 | 1 | 1 | 1 | 浏览器开发者工具、状态码和网络请求 |
| 020 | 3 | core | 7224 | 99 | 0 | 1 | 0 | 动态应用的完整架构图 |
| 021 | 4 | core | 7750 | 85 | 3 | 1 | 0 | 源代码、依赖、运行时、构建和构建产物 |
| 022 | 4 | core | 7390 | 85 | 3 | 1 | 0 | 包管理器、锁文件、版本号和环境差异 |
| 023 | 4 | core | 6425 | 84 | 3 | 1 | 0 | 本地预览与静态网站发布 |
| 024 | 4 | core | 6480 | 73 | 0 | 1 | 0 | GitHub Pages 与 Cloudflare Pages |
| 025 | 4 | core | 6607 | 81 | 0 | 1 | 1 | Vercel、Render 等自动部署平台 |
| 026 | 4 | core | 6694 | 81 | 2 | 1 | 0 | Build Command、Output Directory 和环境变量 |
| 027 | 4 | core | 6090 | 81 | 0 | 1 | 0 | Preview、Production、部署日志和回滚 |
| 028 | 4 | core | 6711 | 86 | 2 | 1 | 0 | 自定义域名、DNS、HTTPS、费用与地区差异 |
| 029 | 5 | core | 7522 | 108 | 1 | 1 | 0 | 后端为什么存在以及 API 怎样工作 |
| 030 | 5 | core | 7248 | 106 | 0 | 1 | 0 | REST、WebSocket、身份认证和权限控制 |
| 031 | 5 | core | 7300 | 106 | 1 | 1 | 0 | SQL、NoSQL、PostgreSQL 与 SQLite |
| 032 | 5 | core | 6560 | 101 | 1 | 1 | 0 | 数据库迁移、连接、备份和恢复 |
| 033 | 5 | core | 7355 | 115 | 0 | 1 | 0 | 文件上传、对象存储、邮件、推送和 AI API |
| 034 | 5 | core | 7442 | 106 | 0 | 1 | 0 | Supabase、Firebase 与后端即服务 |
| 035 | 5 | core | 6111 | 98 | 0 | 1 | 0 | 托管方案、自建方案和平台依赖 |
| 036 | 6 | core | 8391 | 94 | 0 | 1 | 0 | VPS、云服务器及购买时需要看的参数 |
| 037 | 6 | core | 10151 | 145 | 17 | 2 | 1 | 第一次使用 SSH 登录服务器 |
| 038 | 6 | core | 9716 | 149 | 20 | 1 | 0 | Linux 文件、目录、用户、root、sudo 和权限 |
| 039 | 6 | core | 8916 | 146 | 20 | 1 | 0 | 软件包、进程、端口、磁盘和内存 |
| 040 | 6 | core | 11399 | 171 | 27 | 2 | 1 | systemd、systemctl、journalctl 和服务日志 |
| 041 | 6 | core | 8973 | 135 | 13 | 1 | 0 | 防火墙、Caddy、Nginx、域名与 HTTPS |
| 042 | 6 | core | 8494 | 115 | 1 | 1 | 0 | 部署、更新、回滚、备份和恢复 |
| 043 | 6 | core | 8358 | 119 | 0 | 1 | 0 | 自建服务器增加了哪些长期责任 |
| 044 | 7 | core | 6984 | 88 | 2 | 1 | 0 | 运行环境问题与 Docker 的基本模型 |
| 045 | 7 | core | 7423 | 107 | 6 | 1 | 0 | 镜像、容器、Dockerfile 和 Registry |
| 046 | 7 | core | 7244 | 107 | 7 | 1 | 0 | 端口映射、Volume、Bind Mount 和数据持久化 |
| 047 | 7 | core | 8509 | 116 | 9 | 2 | 1 | Docker Compose 与多容器应用 |
| 048 | 7 | core | 7467 | 111 | 8 | 1 | 0 | 容器状态、日志、健康检查和重启策略 |
| 049 | 7 | core | 7056 | 112 | 5 | 1 | 0 | 更新、回滚、清理与数据丢失风险 |
| 050 | 7 | core | 6175 | 93 | 0 | 1 | 0 | Docker、虚拟机和 Kubernetes 的边界 |
| 051 | 8 | core | 7774 | 88 | 0 | 1 | 0 | App 客户端、后端和本地数据 |
| 052 | 8 | core | 9113 | 117 | 8 | 1 | 0 | Flutter 项目、依赖、Debug、Profile 和 Release |
| 053 | 8 | core | 9036 | 113 | 4 | 1 | 0 | APK、AAB、包名、版本号和 Android 签名 |
| 054 | 8 | core | 9316 | 116 | 1 | 2 | 1 | Google Play 内部测试与发布流程 |
| 055 | 8 | core | 8605 | 97 | 1 | 1 | 0 | iOS、macOS、Xcode、证书和 Provisioning Profile |
| 056 | 8 | core | 10326 | 116 | 2 | 3 | 2 | Archive、TestFlight 与 App Store Connect |
| 057 | 8 | core | 8034 | 110 | 1 | 1 | 0 | 商店素材、权限、隐私政策和审核反馈 |
| 058 | 8 | core | 8519 | 117 | 0 | 1 | 0 | App 更新、崩溃日志和后端停机 |
| 059 | 9 | core | 6984 | 66 | 0 | 1 | 0 | 从现象到故障层级的统一判断方法 |
| 060 | 9 | core | 6480 | 71 | 0 | 1 | 1 | Console、Network、Build Log 和 Runtime Log |
| 061 | 9 | core | 7156 | 68 | 6 | 1 | 0 | 服务器、Docker、数据库和代理日志 |
| 062 | 9 | core | 6922 | 57 | 3 | 1 | 0 | Flutter、Logcat、Xcode 与商店上传错误 |
| 063 | 9 | core | 6819 | 70 | 2 | 1 | 0 | 复现、调用栈、最小复现、最近改动和回滚 |
| 064 | 9 | core | 6654 | 72 | 2 | 1 | 0 | 怎样向 AI 或开发者提交完整报错 |
| 065 | 9 | core | 7052 | 72 | 5 | 1 | 0 | Secret、.env、SSH 密钥和最小权限 |
| 066 | 9 | core | 6625 | 67 | 2 | 1 | 0 | 防火墙、数据库暴露、输入验证和文件上传 |
| 067 | 9 | core | 6920 | 72 | 2 | 1 | 0 | 备份、恢复测试、监控、费用和安全下线 |
| 068 | 9 | core | 6067 | 63 | 0 | 1 | 0 | 每周、每月和每季度维护清单 |
| 069 | 10 | core | 8965 | 93 | 1 | 1 | 0 | 让 AI 先理解项目结构 |
| 070 | 10 | core | 8795 | 92 | 1 | 1 | 0 | 计划、权限、Diff、测试和验证证据 |
| 071 | 10 | core | 7921 | 82 | 2 | 1 | 0 | 安全地生成配置、部署文档和回滚方案 |
| 072 | 10 | core | 8788 | 97 | 1 | 1 | 0 | AI 声称完成以后还要检查什么 |
| 073 | 10 | core | 8746 | 89 | 0 | 1 | 0 | 生产环境中的人工确认边界 |
| 074 | 10 | core | 9050 | 100 | 0 | 1 | 0 | 不懂代码时怎样保留最终判断能力 |
| 075 | 10 | optional | 3080 | 38 | 2 | 1 | 0 | 代码能运行以后，架构问题才开始出现 |
| 076 | 10 | optional | 2550 | 29 | 0 | 0 | 0 | 模块、内聚、耦合、依赖方向与公开接口 |
| 077 | 10 | optional | 4377 | 49 | 0 | 1 | 0 | 领域边界、数据所有权与跨模块协作 |
| 078 | 10 | optional | 4475 | 42 | 0 | 1 | 0 | 分层架构、按功能组织与 Vertical Slice |
| 079 | 10 | optional | 4980 | 51 | 0 | 1 | 0 | 模块化单体怎样控制变化范围 |
| 080 | 10 | optional | 5264 | 56 | 0 | 1 | 0 | 微服务真正增加了哪些工程责任 |
| 081 | 10 | optional | 5138 | 55 | 0 | 1 | 0 | 架构异味与 AI 生成项目的复杂度增长 |
| 082 | 10 | optional | 4318 | 50 | 0 | 1 | 0 | 复杂度预算与什么时候不要增加新组件 |
| 083 | 10 | optional | 4583 | 66 | 1 | 1 | 0 | 用 ADR 保存选择、代价与重新评估条件 |
| 084 | 10 | optional | 5002 | 65 | 0 | 1 | 0 | 怎样让两个工程方案真正对打 |
| 085 | 10 | advanced | 6967 | 78 | 0 | 1 | 0 | REST、GraphQL、Polling、SSE 与 WebSocket |
| 086 | 10 | advanced | 6106 | 74 | 0 | 1 | 0 | SQLite、PostgreSQL、SQL 与文档数据库 |
| 087 | 10 | advanced | 6322 | 79 | 0 | 1 | 0 | BaaS、自建后端、托管平台、VPS 与 Serverless |
| 088 | 10 | advanced | 6421 | 65 | 2 | 1 | 0 | 直接进程、Docker、Compose 与 Kubernetes |
| 089 | 10 | advanced | 5579 | 69 | 3 | 1 | 0 | 局部故障、超时、重试放大与退避 |
| 090 | 10 | advanced | 5089 | 60 | 0 | 1 | 0 | 背压、负载丢弃、隔离与队列语义 |
| 091 | 10 | advanced | 5015 | 74 | 4 | 1 | 0 | SLI、SLO、SLA 与 Error Budget |
| 092 | 10 | advanced | 4714 | 58 | 2 | 1 | 0 | 日志、指标、追踪与 OpenTelemetry |
| 093 | 10 | advanced | 4598 | 66 | 3 | 1 | 0 | 性能基线、分位数、剖析、压测与成本 |
| 094 | 10 | advanced | 4977 | 72 | 3 | 1 | 0 | 契约、性质、模糊、变异与回归测试 |
| 095 | 10 | advanced | 4670 | 75 | 2 | 1 | 0 | 独立测试依据与可信的第二意见 |
| 096 | 10 | advanced | 4735 | 82 | 3 | 1 | 0 | 怎样阅读事故复盘并提取可迁移经验 |
| 097 | 10 | reference | 3888 | 47 | 3 | 1 | 0 | 先画成熟开源仓库的 Repository Map |
| 098 | 10 | reference | 3581 | 48 | 4 | 1 | 0 | 沿用户动作阅读测试、历史、Issue 与 PR |
| 099 | 10 | reference | 3601 | 49 | 2 | 1 | 0 | PocketBase 与 Supabase 的边界选择 |
| 100 | 10 | reference | 4047 | 55 | 2 | 1 | 0 | Immich 与 PostHog 中的后台任务和工程组织 |
| 101 | 10 | reference | 3453 | 46 | 2 | 1 | 0 | 怎样正确使用技术社区中的争议与经验 |
| 102 | 10 | reference | 3319 | 46 | 1 | 1 | 0 | Repository Health Review 与长期清理 |
| 103 | 10 | reference | 3405 | 50 | 2 | 1 | 0 | 审查 AI 的范围扩张、依赖与架构漂移 |
| 104 | 10 | reference | 3636 | 55 | 1 | 1 | 0 | 把工程判断变成可持续的项目治理 |

## Exact duplicate paragraphs (>80 chars)

- None

## Risk-command candidates

| Chapter | Location | Reason | Candidate |
|---:|---|---|---|
| 002 | `chapters/002-本地电脑-github-部署平台-服务器和用户设备.md:95` | database migration | 数据库结构也有版本。新代码开始读取一列数据以前，生产数据库必须完成相应迁移。若代码先上线，应用会报“列不存在”。若数据库先删除旧列，尚未更新的 App 又可能继续请求它。数据库迁移、代码部署和客户端更新需要安排顺序。 |
| 027 | `chapters/027-preview-production-部署日志和回滚.md:43` | database migration | 数据库迁移、用户写入、发送的邮件、支付事件、对象存储文件、DNS 修改和第三方配置通常不随应用版本回滚。Render 官方也明确指出磁盘、自定义域名和重定向规则等变化不会随回滚恢复。 |
| 027 | `chapters/027-preview-production-部署日志和回滚.md:97` | database migration | 迁移分为兼容添加、数据转换和破坏性删除；三类恢复难度不同；新增可空列通常与旧代码兼容；把整列数据转换成新格式后，旧代码能否读取要实测；删除列或合并数据可能无法自动恢复。应用回滚前查看本次部署是否执行迁移、迁移成功到哪一步、是否已有新写入。没有这些证据时，不要直接运行所谓 down migration。 |
| 032 | `chapters/032-数据库迁移-连接-备份和恢复.md:1` | database migration | # 数据库迁移、连接、备份和恢复 |
| 038 | `chapters/038-linux-文件-目录-用户-root-sudo-和权限.md:76` | privileged or destructive shell command | `whoami` 显示当前用户名。`id` 显示用户编号、主要组和附加组。若输出包含 `sudo` 组，通常表示该用户可以按系统规则使用 `sudo`，仍需通过密码或平台配置验证。不要仅凭用户名叫 `admin` 就认为它有管理员权限。系统真正依据用户编号、组和 sudo 规则。 |
| 038 | `chapters/038-linux-文件-目录-用户-root-sudo-和权限.md:87` | privileged or destructive shell command | sudo systemctl status ssh |
| 038 | `chapters/038-linux-文件-目录-用户-root-sudo-和权限.md:137` | privileged or destructive shell command | sudo chown notesapp:web /srv/notes/uploads |
| 038 | `chapters/038-linux-文件-目录-用户-root-sudo-和权限.md:209` | privileged or destructive shell command | rm /home/ubuntu/permission-lab/note.old.txt |
| 038 | `chapters/038-linux-文件-目录-用户-root-sudo-和权限.md:293` | privileged or destructive shell command | rm -- ./-example.txt |
| 038 | `chapters/038-linux-文件-目录-用户-root-sudo-和权限.md:322` | privileged or destructive shell command | ## sudo 记录与命令历史的边界 |
| 038 | `chapters/038-linux-文件-目录-用户-root-sudo-和权限.md:324` | privileged or destructive shell command | sudo 日志通常记录谁在何时执行了什么程序，shell 历史记录用户输入。两者都可能因配置不同而不完整。不要把密码或令牌写在命令参数中。它可能出现在历史、进程列表和审计日志。需要输入秘密时使用程序支持的标准输入、受限环境文件或秘密管理。完成后检查临时文件和日志。 |
| 039 | `chapters/039-软件包-进程-端口-磁盘和内存.md:24` | privileged or destructive shell command | sudo apt update |
| 039 | `chapters/039-软件包-进程-端口-磁盘和内存.md:41` | privileged or destructive shell command | 遇到网页让你运行 `curl 某地址 \| sudo bash` 时要停下来。这个形式会下载远程内容并立刻以管理员权限执行。网页内容今天和明天可能不同，终端历史也不会保存脚本全文。更稳妥的做法是使用项目官方仓库说明，检查下载地址和签名，先保存并阅读脚本，再在测试机验证。不了解来源时不要执行。 |
| 039 | `chapters/039-软件包-进程-端口-磁盘和内存.md:90` | privileged or destructive shell command | sudo ss -lntp |
| 039 | `chapters/039-软件包-进程-端口-磁盘和内存.md:96` | privileged or destructive shell command | sudo ss -lntp '( sport = :3000 )' |
| 039 | `chapters/039-软件包-进程-端口-磁盘和内存.md:118` | privileged or destructive shell command | sudo ufw status verbose |
| 039 | `chapters/039-软件包-进程-端口-磁盘和内存.md:132` | privileged or destructive shell command | sudo du -xhd 1 /var |
| 039 | `chapters/039-软件包-进程-端口-磁盘和内存.md:172` | privileged or destructive shell command | sudo ss -lntp '( sport = :3000 )' |
| 039 | `chapters/039-软件包-进程-端口-磁盘和内存.md:189` | privileged or destructive shell command | sudo ss -lntp |
| 039 | `chapters/039-软件包-进程-端口-磁盘和内存.md:239` | privileged or destructive shell command | sudo ss -lnup |
| 039 | `chapters/039-软件包-进程-端口-磁盘和内存.md:259` | privileged or destructive shell command | sudo lsof +L1 |
| 040 | `chapters/040-systemd-systemctl-journalctl-和服务日志.md:20` | privileged or destructive shell command | sudo systemctl status ssh |
| 040 | `chapters/040-systemd-systemctl-journalctl-和服务日志.md:37` | privileged or destructive shell command | sudo systemctl --no-pager status ssh |
| 040 | `chapters/040-systemd-systemctl-journalctl-和服务日志.md:45` | privileged or destructive shell command | sudo systemctl start notes-api |
| 040 | `chapters/040-systemd-systemctl-journalctl-和服务日志.md:51` | privileged or destructive shell command | sudo systemctl stop notes-api |
| 040 | `chapters/040-systemd-systemctl-journalctl-和服务日志.md:57` | privileged or destructive shell command | sudo systemctl restart notes-api |
| 040 | `chapters/040-systemd-systemctl-journalctl-和服务日志.md:63` | privileged or destructive shell command | sudo systemctl reload caddy |
| 040 | `chapters/040-systemd-systemctl-journalctl-和服务日志.md:73` | privileged or destructive shell command | sudo systemctl enable notes-api |
| 040 | `chapters/040-systemd-systemctl-journalctl-和服务日志.md:124` | privileged or destructive shell command | sudo systemctl daemon-reload |
| 040 | `chapters/040-systemd-systemctl-journalctl-和服务日志.md:130` | privileged or destructive shell command | sudo systemctl restart notes-api |
| 040 | `chapters/040-systemd-systemctl-journalctl-和服务日志.md:131` | privileged or destructive shell command | sudo systemctl status notes-api |
| 040 | `chapters/040-systemd-systemctl-journalctl-和服务日志.md:141` | privileged or destructive shell command | sudo journalctl -u notes-api |
| 040 | `chapters/040-systemd-systemctl-journalctl-和服务日志.md:147` | privileged or destructive shell command | sudo journalctl -u notes-api -n 50 --no-pager |
| 040 | `chapters/040-systemd-systemctl-journalctl-和服务日志.md:157` | privileged or destructive shell command | sudo journalctl -u notes-api -f |
| 040 | `chapters/040-systemd-systemctl-journalctl-和服务日志.md:163` | privileged or destructive shell command | sudo journalctl -fu ssh.service |
| 040 | `chapters/040-systemd-systemctl-journalctl-和服务日志.md:173` | privileged or destructive shell command | sudo journalctl -u notes-api --since "2026-08-05 09:00" |
| 040 | `chapters/040-systemd-systemctl-journalctl-和服务日志.md:179` | privileged or destructive shell command | sudo journalctl -b -u notes-api |
| 040 | `chapters/040-systemd-systemctl-journalctl-和服务日志.md:185` | privileged or destructive shell command | sudo journalctl -b -1 -u notes-api |
| 040 | `chapters/040-systemd-systemctl-journalctl-和服务日志.md:211` | privileged or destructive shell command | sudo journalctl --disk-usage |
| 040 | `chapters/040-systemd-systemctl-journalctl-和服务日志.md:250` | privileged or destructive shell command | sudo systemctl reset-failed notes-api |
| 040 | `chapters/040-systemd-systemctl-journalctl-和服务日志.md:251` | privileged or destructive shell command | sudo systemctl start notes-api |
| 040 | `chapters/040-systemd-systemctl-journalctl-和服务日志.md:273` | privileged or destructive shell command | sudo journalctl -u notes-backup.service -n 100 --no-pager |
| 040 | `chapters/040-systemd-systemctl-journalctl-和服务日志.md:311` | privileged or destructive shell command | sudo journalctl -u notes-api -p err --since today |
| 041 | `chapters/041-防火墙-caddy-nginx-域名与-https.md:26` | privileged or destructive shell command | sudo ufw status numbered |
| 041 | `chapters/041-防火墙-caddy-nginx-域名与-https.md:38` | privileged or destructive shell command | sudo ufw allow 22/tcp |
| 041 | `chapters/041-防火墙-caddy-nginx-域名与-https.md:43` | firewall change | 本章不要求读者在未知规则的现有服务器上直接运行 `ufw enable`。启用动作会改变网络行为，应在新测试实例中练习。 |
| 041 | `chapters/041-防火墙-caddy-nginx-域名与-https.md:50` | privileged or destructive shell command | sudo ufw allow 80/tcp |
| 041 | `chapters/041-防火墙-caddy-nginx-域名与-https.md:51` | privileged or destructive shell command | sudo ufw allow 443/tcp |
| 041 | `chapters/041-防火墙-caddy-nginx-域名与-https.md:57` | privileged or destructive shell command | sudo ufw status numbered |
| 041 | `chapters/041-防火墙-caddy-nginx-域名与-https.md:85` | privileged or destructive shell command | sudo caddy validate --config /etc/caddy/Caddyfile |
| 041 | `chapters/041-防火墙-caddy-nginx-域名与-https.md:91` | privileged or destructive shell command | sudo systemctl reload caddy |
| 041 | `chapters/041-防火墙-caddy-nginx-域名与-https.md:92` | privileged or destructive shell command | sudo systemctl status caddy |
| 041 | `chapters/041-防火墙-caddy-nginx-域名与-https.md:123` | privileged or destructive shell command | sudo nginx -t |
| 041 | `chapters/041-防火墙-caddy-nginx-域名与-https.md:129` | privileged or destructive shell command | sudo systemctl reload nginx |
| 041 | `chapters/041-防火墙-caddy-nginx-域名与-https.md:130` | privileged or destructive shell command | sudo systemctl status nginx |
| 041 | `chapters/041-防火墙-caddy-nginx-域名与-https.md:191` | firewall change | `ufw status numbered` 会列出编号；删除一条后，后续编号可能重新排列；一次只删除一条，再重新获取列表；不要根据旧截图连续删除多个编号。规则删除会改变网络访问，执行前确认不是当前 SSH 入口。误删后若仍保留会话，可以立即恢复。会话已断开时要使用云控制台。 |
| 042 | `chapters/042-部署-更新-回滚-备份和恢复.md:200` | database migration | 每次生产发布保存提交编号、构建编号、产物校验值、配置变更、数据库迁移、开始与结束时间。再保存测试结果、服务状态摘要、健康请求、关键业务验收和观察期指标。日志需脱敏，秘密不进入证据包。 |
| 049 | `chapters/049-更新-回滚-清理与数据丢失风险.md:219` | database migration | 写旧新镜像摘要、Compose 提交、数据库迁移、卷与备份、开始结束时间。保存 pull 或 build、config、ps、健康、日志和业务验收。内容脱敏。失败时写回滚摘要、数据处理和用户影响。清理写删除对象与恢复来源。 |
| 061 | `chapters/061-服务器-docker-数据库和代理日志.md:83` | privileged or destructive shell command | sudo nginx -T |
| 061 | `chapters/061-服务器-docker-数据库和代理日志.md:84` | privileged or destructive shell command | sudo tail -n 200 /var/log/nginx/access.log |
| 061 | `chapters/061-服务器-docker-数据库和代理日志.md:85` | privileged or destructive shell command | sudo tail -n 200 /var/log/nginx/error.log |
| 061 | `chapters/061-服务器-docker-数据库和代理日志.md:117` | Docker bulk cleanup | 不要在事故中直接运行 `docker system prune` 或删除 `/var/log`。Docker prune 会删除未使用对象，不等同于只清日志，若理解错误可能影响回滚所需镜像；删除数据库或代理日志则会破坏证据。更安全的顺序是先确认哪个目录增长、保存事故区间、按组件文档执行轮转或压缩，再验证磁盘与服务。数据库数据目录尤其不能当作普通日志目录清理。 |
| 063 | `chapters/063-复现-调用栈-最小复现-最近改动和回滚.md:55` | database migration | 故障刚好发生在一次发布后，最近提交值得优先检查，却仍只是线索。完整变更面还包括依赖解析结果、环境变量、证书与密钥、DNS、数据库迁移、平台策略、流量、数据规模、系统更新和外部 API。没有人主动部署，证书到期或云平台调整也可能改变运行结果。 |
| 066 | `chapters/066-防火墙-数据库暴露-输入验证和文件上传.md:22` | privileged or destructive shell command | sudo ufw status verbose |
| 066 | `chapters/066-防火墙-数据库暴露-输入验证和文件上传.md:23` | privileged or destructive shell command | sudo ss -lntp |
| 066 | `chapters/066-防火墙-数据库暴露-输入验证和文件上传.md:31` | privileged or destructive shell command | sudo ufw allow 22/tcp |
| 066 | `chapters/066-防火墙-数据库暴露-输入验证和文件上传.md:32` | privileged or destructive shell command | sudo ufw allow 80/tcp |
| 066 | `chapters/066-防火墙-数据库暴露-输入验证和文件上传.md:33` | privileged or destructive shell command | sudo ufw allow 443/tcp |
| 066 | `chapters/066-防火墙-数据库暴露-输入验证和文件上传.md:34` | privileged or destructive shell command | sudo ufw enable |
| 066 | `chapters/066-防火墙-数据库暴露-输入验证和文件上传.md:35` | privileged or destructive shell command | sudo ufw status numbered |
| 068 | `chapters/068-每周-每月和每季度维护清单.md:27` | database migration | 本周部署与配置变化要和异常时间对齐。核对生产实际版本、失败部署、回滚、数据库迁移、DNS 与秘密轮换。若某项临时开关、额外日志级别或防火墙规则已超过到期时间，立即进入审查，不让事故绕过长期留下。 |
| 068 | `chapters/068-每周-每月和每季度维护清单.md:95` | database migration | 发布重大版本、数据库迁移、更换云平台或新增文件上传后，也应临时执行相关月度或季度项目。系统风险发生变化，清单要随之更新。例如新增远程 URL 导入，就要增加 SSRF 测试；引入 iOS 发布，就要增加证书、Profile、Archive 和 App Store Connect 成员检查。 |
| 070 | `chapters/070-计划-权限-diff-测试和验证证据.md:55` | database migration | AI 应只修改实现验收标准所需的行，并删除自己造成的无用代码。不要顺手格式化整个文件、更新全部依赖、改命名或重写相邻模块。Diff 越小，人越容易审查，失败时也更容易回滚。“最小”不等于故意留下半套实现。若新增字段需要验证、数据库迁移、API、界面和测试，这些都属于必要范围。计划应提前说明跨层变化，避免只改前端制造暂时演示。最小修改衡量的是与需求的直接关系，… |
| 072 | `chapters/072-ai-声称完成以后还要检查什么.md:27` | database migration | Diff 展示版本控制文件的真实变化。先看文件列表、增删规模和二进制，再逐块审查。任务是改一处按钮，却出现锁文件、数据库迁移、CI、格式化数百行或删除测试，就需要解释。未跟踪文件不会总出现在普通 Diff 中，还要结合 `git status`。 |
| 073 | `chapters/073-生产环境中的人工确认边界.md:37` | database migration | 审批提示中的命令要翻译成业务后果。`apply migration` 可能锁表和改变数据，`sync --delete` 可能删除远端文件，`terraform apply` 可能创建费用或销毁资源。确认人需要看到计划、准确目标、Diff 与回退，不能只看命令语法。网络访问也要限制。AI 搜索官方文档与向生产 API 发请求都使用网络，但风险完全不同。允许浏… |
| 073 | `chapters/073-生产环境中的人工确认边界.md:105` | database migration | 为常见生产动作列执行者、技术审查者、业务批准者、知会对象与回滚负责人。代码部署、数据库迁移、DNS、商店发布、费用扩容和永久删除可以有不同角色。矩阵记录角色，不把每次流程绑死在某个姓名；值班表再映射当前人员。 |
| 087 | `chapters/087-baas-自建后端-托管平台-vps-与-serverless.md:23` | database migration | 托管应用平台接收仓库或容器，负责构建、启动、域名、证书、日志入口和部分扩缩容。项目仍要提供正确启动命令、环境变量、数据库迁移、健康检查和应用监控。平台处理基础设施，不会替代码判断订单是否可以退款。 |
| 099 | `chapters/099-pocketbase-与-supabase-的边界选择.md:33` | database migration | 这套结构适合需要关系约束、SQL 查询、数据库迁移、细粒度行级权限和既有 Postgres 工具的项目。能力增加也带来更多概念。前端使用公开密钥不代表可以跳过权限策略，服务角色密钥不能放进客户端。表能查询不代表备份覆盖了对象存储，数据库恢复也不保证外部邮件和第三方付款状态自动一致。 |
| 103 | `chapters/103-审查-ai-的范围扩张-依赖与架构漂移.md:20` | database migration | 允许修改  表单、用户接口、数据库迁移、相关测试 |
| 103 | `chapters/103-审查-ai-的范围扩张-依赖与架构漂移.md:30` | database migration | 先看新增、修改、删除文件和总差异，不急着逐行读。按功能代码、测试、依赖清单、锁文件、数据库迁移、部署配置、工作流、权限和文档分类。任何超出约定的类别先标记。 |
| 103 | `chapters/103-审查-ai-的范围扩张-依赖与架构漂移.md:44` | database migration | 数据库迁移、对象存储、环境变量、缓存键和队列消息会跨版本存在。代码回滚不一定撤销数据变化。审查迁移前向和回退方向，确认旧版本能否读取新数据，部署顺序是否允许新旧进程短暂共存。 |
| 104 | `chapters/104-把工程判断变成可持续的项目治理.md:40` | database migration | 发布记录应包含提交、制品校验、数据库迁移、配置变化、部署时间、操作者、验证和回滚点。几个月后出现故障时，这些信息比“当时应该测过”可靠。 |

## Volatile-fact candidates

| Chapter | Location | Reason | Candidate |
|---:|---|---|---|
| 001 | `chapters/001-从本地文件到公开可用的产品.md:86` | time-sensitive fact candidate | “减少责任”不等于选择功能最少的平台。它表示把与产品目标无关、但必须长期完成的工作交给可靠服务。静态托管通常替你处理文件分发与证书。托管数据库通常替你处理数据库进程和部分备份能力。你仍要管理账户权限、数据结构、费用和恢复验证。 |
| 001 | `chapters/001-从本地文件到公开可用的产品.md:90` | time-sensitive fact candidate | 数据位置要单独决定。网页放在静态托管，不妨碍账号和数据放在 Supabase 或其他后端。后端运行在 VPS，也不要求数据库一定装在同一台机器。把组件拆开可以减少单台机器故障的影响，也会增加账户、网络和费用管理。初学者应先选能说清责任的位置组合。 |
| 001 | `chapters/001-从本地文件到公开可用的产品.md:110` | time-sensitive fact candidate | \| 费用 \| 哪些资源可能收费 \| 官方账单页面与预算提醒 \| |
| 001 | `chapters/001-从本地文件到公开可用的产品.md:129` | time-sensitive fact candidate | 因此 App 出错时要先问位置。应用打不开，可能是客户端崩溃。登录失败，可能是后端、网络或认证服务。商店拒绝上传，可能是签名、版本号、权限声明或商店政策。所有错误都显示在手机上，不代表错误都发生在手机里。 |
| 003 | `chapters/003-静态网站-动态网站-服务器程序和手机-app.md:49` | time-sensitive fact candidate | 前端是用户设备上直接呈现和交互的部分。网页前端在浏览器中运行，App 前端在移动操作系统中运行。后端在用户设备之外处理需要集中管理或保密的工作；这条边界最重要的判断是信任；用户能够查看、修改或伪造客户端发出的请求；前端隐藏一个按钮，不能阻止用户直接调用接口。价格、账户归属、管理员权限和付费状态等关键规则必须由后端重新检查。 |
| 003 | `chapters/003-静态网站-动态网站-服务器程序和手机-app.md:112` | time-sensitive fact candidate | 平台函数仍是后端。它要验证输入，限制滥用，记录错误并保护秘密。平台还可能限制单次执行时间、内存、并发、可用地区和临时磁盘。限制与费用会变化，选择前要查当日官方文档。长时间视频处理、持续 WebSocket 连接或需要本地持久磁盘的程序，未必适合普通短时函数。某些平台提供其他运行产品，名称容易相似，最终应按具体产品说明判断。 |
| 003 | `chapters/003-静态网站-动态网站-服务器程序和手机-app.md:114` | time-sensitive fact candidate | JavaScript 可以在浏览器中完成很多工作。表格计算、图片预览、表单即时检查和界面筛选都可以不经过后端。这样响应快，也减少服务器请求。安全与权威数据需要另一种判断。假设商城前端收到商品价格 100 元，并在浏览器中计算折扣。用户可以修改请求，把付款金额改成 1 元；后端若直接相信客户端金额，就会产生严重错误；后端必须根据商品和优惠规则重新计算应付金额。 |
| 003 | `chapters/003-静态网站-动态网站-服务器程序和手机-app.md:118` | time-sensitive fact candidate | “能运行”只描述技术可能性。“应该放哪里”还要考虑秘密、权限、费用、延迟、离线需求和维护责任。 |
| 003 | `chapters/003-静态网站-动态网站-服务器程序和手机-app.md:135` | time-sensitive fact candidate | 一个“上传 PDF 后提问”的网页看起来只有一个聊天框，内部至少可能有六个组成部分。浏览器前端负责选择文件、显示上传进度和聊天记录；上传接口检查文件类型与大小，把文件存入对象存储；后台任务提取文字并建立检索数据；数据库保存用户、文档和任务状态；问答 API 找到相关内容，再调用 AI 服务；用量系统记录额度和费用。 |
| 003 | `chapters/003-静态网站-动态网站-服务器程序和手机-app.md:149` | time-sensitive fact candidate | 学习项目容易过早加入账号和数据库。一个计算器、作品集、活动说明页或只在本机使用的表格工具，可能靠静态文件和浏览器本地数据就能完成目标。暂时不建后端，可以减少账户安全、数据库备份、服务器费用和隐私政策等责任。等到确实需要跨设备同步、多人共享、集中权限或私密凭据时，再增加远程服务。 |
| 004 | `chapters/004-文件-路径-终端和图形界面的最低限度知识.md:76` | time-sensitive fact candidate | 先把压缩包解压到一个明确的普通目录，再阅读 README。不要解压到系统目录，也不要使用名称过长、层级很深的临时路径。项目要求 Node.js、Python、Flutter 或 Docker 时，要分别安装对应工具，并核对支持版本。 |
| 004 | `chapters/004-文件-路径-终端和图形界面的最低限度知识.md:217` | time-sensitive fact candidate | “端口被占用”表示另一个进程已经监听同一入口。它可能是上一次开发服务器没有停止，也可能是其他程序。先查看占用者，再决定停止旧进程或使用新端口；不要用管理员权限强行解决；服务器上还要考虑防火墙和监听地址。程序监听 `127.0.0.1` 时，通常只接受本机连接，适合由同机反向代理转发。监听公网地址会扩大可访问范围。第六卷会结合防火墙详细解释，现在不要为了让远程… |
| 005 | `chapters/005-git-github-项目文件夹和仓库.md:77` | time-sensitive fact candidate | 排查时先看引入变化的提交 Diff，再读相邻提交与 Pull Request 讨论。例如价格计算突然错误，某次提交改了公式。提交说明写“重构计算”，Issue 又说明要支持新折扣。只有把代码变化与需求放在一起，才能判断修复方向。 |
| 006 | `chapters/006-github-账号-公开仓库-私有仓库和网页上传.md:21` | time-sensitive fact candidate | 仓库可见性与部署可见性分开。私有仓库可以构建出公开网站。公开仓库也可以部署到需要登录的内部系统。改变仓库可见性前，要查看 Pages、Actions、Fork、规则和组织政策可能受到的影响，以当日官方提示为准。 |
| 006 | `chapters/006-github-账号-公开仓库-私有仓库和网页上传.md:29` | time-sensitive fact candidate | 如果仓库名已存在，GitHub 会要求换名。同一所有者下不能用同一个仓库名重复创建。若页面提示组织策略阻止某种可见性，说明当前组织有额外规则，应联系组织管理员，不要改放到个人账号绕过政策。 |
| 006 | `chapters/006-github-账号-公开仓库-私有仓库和网页上传.md:74` | time-sensitive fact candidate | 个人练习、作品集和单人开源项目可以放在个人账号。多人长期维护、由公司或社团拥有的项目，更适合组织。组织能够用团队分配权限，并保留资源归属。判断时问谁在成员离开后继续拥有项目，谁支付服务费用，谁负责安全事件。若答案是某个组织，仓库、域名、部署和商店资源最好使用相符的组织账户体系。 |
| 006 | `chapters/006-github-账号-公开仓库-私有仓库和网页上传.md:148` | time-sensitive fact candidate | GitHub 的网络可达性可能因地区、网络运营商和时间而变化。页面加载慢或下载中断时，先保留本地项目与提交，不要连续重复创建仓库。确认远程页面是否真的出现新提交，再决定重试。第三方镜像或加速服务会接触你请求的仓库内容。私有仓库、令牌和发布资产不要交给来源不明的中转服务。组织项目还要遵守所在机构的网络与数据政策。 |
| 007 | `chapters/007-用-github-desktop-管理本地项目.md:140` | time-sensitive fact candidate | - **界面时效**　视频使用 2025 年界面，截至 2026 年 8 月 6 日，核心区域与 GitHub 当前文档仍一致；新增功能或菜单细节以当前官方文档为准 |
| 008 | `chapters/008-commit-push-pull-clone-和-sync.md:79` | time-sensitive fact candidate | 视频、数据集和构建包进入普通 Git 历史后，每次 Clone 可能都要传输历史版本。删除当前文件也不能自动缩小旧历史。Git LFS 可以把大文件内容放到专门存储，并在 Git 中保留指针。它有配额、费用和平台支持要求，使用前查当前官方文档。已经进入历史的大文件迁移仍会影响协作者。 |
| 009 | `chapters/009-分支-合并-冲突-撤销与恢复.md:92` | time-sensitive fact candidate | 合并提交说明可以写明冲突区域和最终选择。Pull Request 讨论中链接需求、截图或测试结果。以后出现回归时，维护者能知道这段内容经过何种取舍；例如两个分支修改登录超时；最终采用 30 分钟，不应只写“解决冲突”。记录“采用安全评审确认的 30 分钟，并补充过期测试”更有用。具体数值还应来自配置或政策来源。 |
| 009 | `chapters/009-分支-合并-冲突-撤销与恢复.md:160` | time-sensitive fact candidate | AI 可以解释冲突两边来自哪些提交，提出候选合并内容，列出撤销方案的影响。它也能检查文件是否还残留冲突标记。让 AI 修改前，要求它保留两边原文、说明业务依据，并在独立分支工作。没有业务信息时，它不能替你决定活动时间、价格、权限和生产数据。 |
| 010 | `chapters/010-readme-releases-issues-actions-许可证和项目维护状态.md:15` | time-sensitive fact candidate | README 不应把所有技术细节塞在一页。复杂项目可以链接到 `docs` 目录、贡献指南、安全政策和变更记录。入口页保留读者第一次运行所需的最短路径。例如，一个项目只写“运行 `npm start`”，却没说明需要哪个 Node.js 版本、在哪个目录运行、成功后打开什么地址。读者无法判断命令报错来自环境还是项目。补充前提与预期结果会比增加宣传语更有用。 |
| 010 | `chapters/010-readme-releases-issues-actions-许可证和项目维护状态.md:43` | time-sensitive fact candidate | GitHub Release 建立在标签之上，可以包含版本说明、二进制文件与其他下载资产。GitHub 也会提供对应源码压缩包。Tag 译为标签，用一个稳定名称指向某个提交，例如 `v1.2.0`。Release 在这个版本上增加面向使用者的说明。仓库最新提交可能正在开发，最新稳定 Release 可能更适合普通用户。 |
| 010 | `chapters/010-readme-releases-issues-actions-许可证和项目维护状态.md:60` | time-sensitive fact candidate | 应用版本 1.4.2 |
| 010 | `chapters/010-readme-releases-issues-actions-许可证和项目维护状态.md:102` | time-sensitive fact candidate | 仓库 Tag 指向源码提交，Release 围绕 Tag 提供说明和资产，部署平台又有自己的部署编号。三者要能互相追溯。例如 Release `v1.2.0` 对应提交 `abc123`，Windows 安装包由同一提交的 Actions 构建，生产部署也记录 `abc123`。用户报错时提供版本号，维护者能找到源码和日志。 |
| 010 | `chapters/010-readme-releases-issues-actions-许可证和项目维护状态.md:104` | time-sensitive fact candidate | 如果安装包由另一个未记录目录手工构建，版本名相同也可能内容不同。可重复构建、签名和哈希能减少这种不确定。紧急修复发布 `v1.2.1` 后，说明受影响版本与升级建议。不要悄悄替换 `v1.2.0` 资产，让已经下载的人无法确认内容。 |
| 010 | `chapters/010-readme-releases-issues-actions-许可证和项目维护状态.md:118` | time-sensitive fact candidate | 维护者定期检查模板是否仍对应当前界面和支持版本。用户选择“其他”时仍可提交，避免模板成为阻止有效报告的门槛。模板中不要求粘贴令牌、完整配置和私人数据。日志说明提供遮盖方法与安全报告入口。 |
| 010 | `chapters/010-readme-releases-issues-actions-许可证和项目维护状态.md:122` | time-sensitive fact candidate | 许多项目使用类似 `1.4.2` 的版本号，通常分别表示主要版本、次要版本和修复版本。是否严格遵守语义化版本由项目决定，不能仅凭数字断言兼容。Pre-release 常用于测试版本，例如 alpha、beta 或 release candidate。它可能包含新功能，也可能有未解决问题。生产环境应按项目说明选择稳定版本，并在升级前查看变更与迁移要求。 |
| 010 | `chapters/010-readme-releases-issues-actions-许可证和项目维护状态.md:124` | time-sensitive fact candidate | Latest 标签是 GitHub 界面或维护者设置的一种提示。自动工具选择版本时，还要结合是否为预发布、系统架构和项目自己的发布政策。 |
| 010 | `chapters/010-readme-releases-issues-actions-许可证和项目维护状态.md:160` | time-sensitive fact candidate | 第一分钟确认所有者、官方链接与仓库是否归档；接着读 README 的用途、系统要求和支持版本；查看最新稳定 Release 与发布日期；打开 Actions 看最近默认分支结果。搜索与你系统和目标功能相关的 Issue，例如 Windows、Apple Silicon、Docker 或具体错误。打开许可证，确认使用范围。最后查看安装命令会执行哪些脚本，是否需… |
| 011 | `chapters/011-下载-检查并运行别人的项目.md:59` | time-sensitive fact candidate | 查看 Compose 文件和 `docker run` 参数。挂载 `C:\`、`/`、用户主目录或 Docker socket 都会给容器很大访问范围。`privileged` 模式与添加系统能力也要有明确原因。端口映射 `127.0.0.1:8080:8080` 通常只从本机访问，绑定所有网络接口会扩大范围。语法因工具与平台而异，最终用 Docker 实… |
| 011 | `chapters/011-下载-检查并运行别人的项目.md:65` | time-sensitive fact candidate | 隐私声明应说明收集什么、用途、保留时间和第三方。页面没有更新日期或与代码行为不一致时，需要向维护者询问。处理健康、财务、身份和客户资料时，个人试验标准不够。还要遵守组织政策、合同与适用法律，并选择经过批准的工具和部署位置。 |
| 011 | `chapters/011-下载-检查并运行别人的项目.md:79` | time-sensitive fact candidate | 扩展可以读取和修改网页，具体能力取决于权限声明。有些扩展要求访问所有网站，有些只在点击后访问当前页面。安装前看商店发布者、官方网站、隐私政策、更新时间和权限。源码在 GitHub 时，商店版本是否对应同一提交还要确认。 |
| 011 | `chapters/011-下载-检查并运行别人的项目.md:83` | time-sensitive fact candidate | 项目源码有开源许可证，模型权重可能使用另一许可证，训练数据又有额外限制。Release 中的大模型文件不能只按代码 LICENSE 判断。运行模型要看硬件内存、磁盘、推理框架与量化格式。下载几 GB 文件前确认来源、哈希和存储空间。不要把模型缓存误当成可随意删除的普通日志，重新下载可能耗费时间和费用。 |
| 012 | `chapters/012-gitignore-秘密泄露和历史中的敏感信息.md:81` | time-sensitive fact candidate | 调试时打印完整请求头，可能把 Authorization Token 写进本地、部署或第三方日志。删除代码中的日志语句后，旧日志仍可能保留。先轮换已暴露凭据，再按日志平台能力限制访问与保留。不要直接删除所有日志，安全调查可能需要证据。组织环境应按事件响应和保留政策处理。 |
| 012 | `chapters/012-gitignore-秘密泄露和历史中的敏感信息.md:83` | time-sensitive fact candidate | 今后的日志只记录必要字段。令牌可以完全省略，或记录不可逆的短识别值用于关联。请求正文含密码、身份证或支付信息时，不应默认记录。错误监控与 AI 分析服务也是外部接收者。发送日志前使用过滤器，并确认服务的数据政策和地区要求。 |
| 013 | `chapters/013-浏览器-客户端和服务器.md:23` | time-sensitive fact candidate | 客户端持有用户界面与当前输入，不能被服务端完全信任。用户能修改浏览器请求，也能使用另一个程序直接调用 API。价格、权限、所有权和支付状态等规则要由服务端重新检查。 |
| 013 | `chapters/013-浏览器-客户端和服务器.md:93` | time-sensitive fact candidate | 只有某个浏览器版本失败时，用同一账号、网络和 URL 做对照。检查浏览器特性、扩展、隐私设置和缓存。收集客户端信息要遵守隐私政策，避免为了调试建立不必要的设备指纹。 |
| 014 | `chapters/014-ip-域名-dns-端口和-url.md:15` | time-sensitive fact candidate | `127.0.0.1` 是 IPv4 回环地址，通常指当前设备自身。`localhost` 常解析到回环地址。开发服务器只监听回环地址时，其他设备不能直接访问。`0.0.0.0` 在服务监听配置中常表示所有 IPv4 网络接口，不是一个让用户在浏览器中访问的普通目标地址。把服务监听到所有接口会扩大访问范围，需要防火墙和认证。 |
| 014 | `chapters/014-ip-域名-dns-端口和-url.md:17` | time-sensitive fact candidate | 家庭公网 IP 可能由运营商动态分配，断线或过一段时间会变化。云平台提供的实例 IP 是否固定，取决于产品和配置。删除、停止或重建实例可能改变地址。域名可以通过 DNS 记录指向当前地址。地址变化时，记录也要更新。生产服务若依赖固定入口，应使用平台提供的固定 IP、负载均衡或域名目标，并核对费用。 |
| 014 | `chapters/014-ip-域名-dns-端口和-url.md:53` | time-sensitive fact candidate | 程序显示 `127.0.0.1:3000`，说明只监听本机回环接口的 3000 端口。同机反向代理可以访问，远程电脑不能直接连接。显示 `0.0.0.0:3000`，表示监听所有 IPv4 接口。是否真能从公网访问，还要看云安全组、系统防火墙、路由和服务认证。 |
| 014 | `chapters/014-ip-域名-dns-端口和-url.md:62` | time-sensitive fact candidate | https://api.example.com:8443/v1/orders?status=open#recent |
| 014 | `chapters/014-ip-域名-dns-端口和-url.md:65` | time-sensitive fact candidate | `https` 是协议方案；`api.example.com` 是主机；`8443` 是显式端口；`/v1/orders` 是路径；`status=open` 是查询参数；`recent` 是片段标识。片段通常由浏览器在本地使用，不会作为普通 HTTP 请求目标的一部分发送给服务器。查询参数会进入请求，应避免放入密码和长期令牌，因为 URL 可能进入历史、日… |
| 014 | `chapters/014-ip-域名-dns-端口和-url.md:89` | time-sensitive fact candidate | 后端启动日志显示监听 `127.0.0.1:3000`。Caddy 配置转发到 `localhost:3001`，用户请求得到 502。应用正常运行，但代理连接了错误端口。修改代理上游为 3000，重新加载配置并验证。没有必要让应用改为公网监听，也不应开放 3000 防火墙。 |
| 014 | `chapters/014-ip-域名-dns-端口和-url.md:149` | time-sensitive fact candidate | 路由器端口转发把公网入口送到内网设备；防火墙决定流量是否允许；应用还要监听正确地址；三项任一缺失都会无法连接。三项都开放也不代表服务安全，仍需要认证、TLS 和更新。个人开发不要把本地数据库与开发服务器直接转发公网。需要演示时使用受控部署或有身份保护的隧道，并查其数据政策。 |
| 014 | `chapters/014-ip-域名-dns-端口和-url.md:169` | time-sensitive fact candidate | 企业网络可能让同一域名在内网解析私有地址，在公网解析公开地址，称为 Split DNS。办公室正常、手机网络失败，比较两个解析器。不要把内网私有 IP 当成公网目标发布。VPN 会改变 DNS 与路由。排错记录是否连接 VPN、使用哪个网络。关闭 VPN 仅作对照，不能违反组织安全政策。 |
| 014 | `chapters/014-ip-域名-dns-端口和-url.md:195` | time-sensitive fact candidate | 面向中国大陆提供公开网站时，域名、服务器位置、备案与内容要求可能涉及当地法规和服务商政策。是否需要备案取决于部署位置、服务类型和当时规则。这类信息会变化，本书在部署章节只引用检索日的官方主管部门与服务商资料，并写明截至日期。不要依据旧博客把结论写成永久不变。 |
| 015 | `chapters/015-http-https-tls-请求与响应.md:118` | time-sensitive fact candidate | 代理会有缓冲和超时配置。它若等待完整正文，客户端看不到逐步输出。CDN 也可能不支持某种流式方式。客户端断开后，后端是否停止生成要实现取消信号。付费 AI 调用继续运行会产生费用。 |
| 015 | `chapters/015-http-https-tls-请求与响应.md:142` | time-sensitive fact candidate | HTTP/1.1、HTTP/2 与 HTTP/3 改善连接与多请求传输方式。浏览器和平台通常自动协商。页面不需要为了使用新版本改 API 路径。代理、CDN 与源站之间也可能使用不同版本。排错关注实际协商、连接失败与平台支持，不根据宣传假定所有用户一致。防火墙或网络可能让 HTTP/3 回退。 |
| 016 | `chapters/016-cookie-session-token-缓存和-cdn.md:72` | time-sensitive fact candidate | 缓存键还要包含影响响应的因素，例如 Host、路径、查询和必要 Headers。配置遗漏会把本应不同的响应合并。不要用客户端参数声明“不要缓存”作为唯一保护，源站和 CDN 政策才是控制点。 |
| 016 | `chapters/016-cookie-session-token-缓存和-cdn.md:148` | time-sensitive fact candidate | 隐私政策列出名称、用途、期限和第三方。实际 Cookie 与文档定期比较。开发调试 Cookie 不能进入生产。过时域名 Cookie 清理并缩小 Domain 与 Path。 |
| 016 | `chapters/016-cookie-session-token-缓存和-cdn.md:192` | time-sensitive fact candidate | 网站替换 `/images/logo.png`，CDN 仍缓存旧文件。维护者清浏览器无效，因为 CDN 响应本身就是旧内容。比较源站直连与公开 CDN 响应哈希，可以定位。按平台清除单个 URL，或发布新文件名 `logo-v2.png` 并更新页面。内容哈希文件名更可靠，例如 `logo.a1b2.svg`。内容变化生成新地址，旧缓存不会覆盖新文件。 |
| 018 | `chapters/018-api-数据库-文件存储和实时通信.md:63` | time-sensitive fact candidate | 分开后会出现一致性问题。数据库记录创建，文件上传失败，会留下空记录。文件成功，数据库写入失败，会留下孤儿对象。可以使用待处理状态、幂等任务和定期清理。删除用户时也要协调记录与对象，并遵守保留政策。 |
| 018 | `chapters/018-api-数据库-文件存储和实时通信.md:87` | time-sensitive fact candidate | Firebase 提供另一套托管后端产品，数据模型与服务组合不同。第三十四章会比较。组合平台减少安装与运维，仍要配置权限、数据模型、备份、地区和费用。默认示例不能直接成为生产安全策略。 |
| 018 | `chapters/018-api-数据库-文件存储和实时通信.md:127` | time-sensitive fact candidate | 上传对象后立即读取行为由平台保证决定。应用需要处理暂时不可见或处理未完成。生命周期规则可以把旧版本转低成本层或删除临时文件。规则是自动删除，配置前用测试 Bucket 和明确前缀。对象版本控制能恢复覆盖或删除，增加存储费用。是否启用与保留多久按数据价值。 |
| 018 | `chapters/018-api-数据库-文件存储和实时通信.md:141` | time-sensitive fact candidate | ## API 限流保护稳定与费用 |
| 018 | `chapters/018-api-数据库-文件存储和实时通信.md:183` | time-sensitive fact candidate | Soft Delete 用删除时间标记记录，允许短期恢复。查询必须默认排除，权限仍保护内容。保留期结束后硬删除数据库、对象和派生索引。备份按政策过期。法律保留可能暂停删除，需要明确授权。 |
| 019 | `chapters/019-浏览器开发者工具-状态码和网络请求.md:87` | time-sensitive fact candidate | 导出后打开文本检查，不只依赖工具的 Sanitized 选项。临时分享链接也要限制访问和到期。问题解决后按数据政策删除调试文件。 |
| 019 | `chapters/019-浏览器开发者工具-状态码和网络请求.md:210` | time-sensitive fact candidate | - **界面时效**　截至 2026 年 8 月 6 日，视频中的核心面板和入口仍符合当前 Chrome；面板细项位置以当前 Chrome DevTools 文档为准 |
| 020 | `chapters/020-动态应用的完整架构图.md:41` | time-sensitive fact candidate | 客户端预览不代表服务器接受。后端验证身份、配额和元数据，生成安全对象 Key 与临时授权。客户端直接上传可以减少后端带宽。上传完成后，后端验证对象并创建记录。后台任务扫描、转码或生成缩略图。 |
| 020 | `chapters/020-动态应用的完整架构图.md:83` | time-sensitive fact candidate | CDN 按流量或请求，应用按运行时间与资源，数据库按实例、存储和备份，对象存储还会有容量与传输，外部 API 按调用。免费额度会变化，也可能在超过后自动计费。为每个组件写账单所有者、预算提醒和关闭入口。 |
| 020 | `chapters/020-动态应用的完整架构图.md:85` | time-sensitive fact candidate | 用户上传与 AI API 容易被滥用。认证、配额、大小限制和速率限制同时保护成本与稳定性。下线时停止计算仍可能保留数据库、快照、对象和域名费用。第六十七章给完整清单。 |
| 020 | `chapters/020-动态应用的完整架构图.md:87` | time-sensitive fact candidate | 用户请求删除账号，后端验证身份并记录请求。事务删除或匿名化业务数据，对象存储清理文件，搜索索引与缓存同步。备份按保留政策在到期后清除。外部邮件和分析服务中的数据按各自能力处理。审计记录保留范围要符合法律与安全要求。 |
| 020 | `chapters/020-动态应用的完整架构图.md:99` | time-sensitive fact candidate | 备份每天一次，最坏可能丢近一天数据。声称零丢失需要同步复制、事务与故障场景证据，不能口头承诺。高目标增加费用和复杂度。个人项目从可靠备份、监控和简洁架构开始。 |
| 020 | `chapters/020-动态应用的完整架构图.md:105` | time-sensitive fact candidate | 用户同一邮箱通过不同方式登录时，账号合并要明确验证，避免接管。提供备用恢复方式。提供商密钥轮换、回调域名和同意页面进入责任表。隐私政策说明数据来源。 |
| 020 | `chapters/020-动态应用的完整架构图.md:142` | time-sensitive fact candidate | 告警要有负责人、严重度和静默规则。频繁误报会被忽略。维护窗口明确标记。监控本身也会故障，定期测试告警通道。费用与隐私进入责任表。 |
| 020 | `chapters/020-动态应用的完整架构图.md:146` | time-sensitive fact candidate | 能从一个用户动作画出设备、入口、应用、数据和外部服务。每条箭头有协议、权限与日志。能从“打不开”“操作失败”“任务卡住”进入不同故障树。知道静态首页正常不能证明后端正常；图有日期、环境和待验证项；责任表覆盖账号、备份、费用与下线；实际控制台证据优先于源码推测。 |
| 020 | `chapters/020-动态应用的完整架构图.md:148` | time-sensitive fact candidate | 新增文件上传，需要在图中加入对象存储、上传授权和后台扫描。责任表加入 Bucket、费用、备份和删除。新增登录，加入身份提供商、Cookie 或 Token、回调和会话存储。故障树加入 401、403 与回调失败。 |
| 022 | `chapters/022-包管理器-锁文件-版本号和环境差异.md:25` | time-sensitive fact candidate | 常见语义化版本写成 `3.7.2`。三个数字通常依次代表主版本、次版本和修订版本。兼容性承诺由软件维护者给出，不能只凭数字保证。修订版本常用于兼容的错误修复，次版本常增加兼容功能，主版本常包含不兼容变化。npm 的初学者说明也采用这一模型。 |
| 022 | `chapters/022-包管理器-锁文件-版本号和环境差异.md:27` | time-sensitive fact candidate | 项目清单还会使用范围符号。`1.2.3` 倾向于锁定一个版本，`^1.2.3` 通常允许安装同一主版本内的更新，`~1.2.3` 通常允许同一次版本内的修订更新。零开头版本有额外规则，最终以包管理器的版本范围规则为准。范围不等于实际安装版本。锁文件才记录一次解析后的具体结果。删除锁文件再安装，虽然清单没有变化，也可能拿到更晚的依赖。 |
| 022 | `chapters/022-包管理器-锁文件-版本号和环境差异.md:46` | time-sensitive fact candidate | 若显示找不到命令，说明当前终端无法定位程序。先核对安装与 PATH，关闭并重新打开终端。不要从陌生网站下载所谓修复工具。记录版本时把前缀和完整数字都保留。`v20` 太宽泛，`v20.19.4` 才能用于复现。 |
| 022 | `chapters/022-包管理器-锁文件-版本号和环境差异.md:110` | time-sensitive fact candidate | 假设清单允许 `^2.4.0`，锁文件记录 `2.4.3`。电脑甲按锁文件安装 2.4.3。有人删除锁文件后，电脑乙可能解析到后来发布的 2.9.0。两个版本理论上位于兼容范围，维护者仍可能在边缘行为上出现差异。若乙的构建失败，只比较 `package.json` 会认为环境相同，实际依赖已经不同。 |
| 022 | `chapters/022-包管理器-锁文件-版本号和环境差异.md:112` | time-sensitive fact candidate | 恢复锁文件并严格安装，可以验证差异是否来自依赖解析。若需要升级到 2.9.0，应把它作为一次明确更新，审查变更、运行测试并提交新锁文件。主版本变化更要单独处理。一次同时升级框架、运行时和几十个插件，会让错误难以定位。按依赖关系分批更新，每批都有可返回的提交。 |
| 023 | `chapters/023-本地预览与静态网站发布.md:140` | time-sensitive fact candidate | 静态托管描述文件提供方式，不限制浏览器脚本发请求。天气页面可以托管成静态文件，再从浏览器调用天气 API。这会遇到跨域、密钥暴露、配额和第三方停机。需要秘密的 API 不应由浏览器直接持有私钥。 |
| 024 | `chapters/024-github-pages-与-cloudflare-pages.md:55` | time-sensitive fact candidate | 若项目依赖服务端长进程、私有网络或本地磁盘，这两个静态发布入口都不是完整答案。先画清后端需求，再选择动态托管或服务器。选择还要考虑账号权限、地区网络、域名管理、构建限制与费用。所有额度和价格都可能变化，本书不把当前免费层写成永久承诺。 |
| 025 | `chapters/025-vercel-render-等自动部署平台.md:31` | time-sensitive fact candidate | 托管平台通常承担构建机器、发布入口、TLS 证书、部署历史和基础运行设施。动态服务还可能提供健康检查、日志和伸缩选项。你仍负责源代码、依赖、配置、数据、权限、秘密、业务监控和费用。平台显示绿色，只说明它的部署检查通过，不代表注册、支付和数据恢复可用。 |
| 025 | `chapters/025-vercel-render-等自动部署平台.md:51` | time-sensitive fact candidate | 价格、免费额度和休眠规则变化频繁。正式决策时打开官方定价与限制页，写明查询日期和预计用量，不沿用本书截稿时数字。中国大陆访问还可能受到网络、备案、支付和节点差异影响。面向大陆公众提供服务时，应根据实际服务器位置、域名接入商和现行规定咨询官方渠道。本书不会把全球平台的默认流程写成大陆上线的完整合规答案。 |
| 025 | `chapters/025-vercel-render-等自动部署平台.md:69` | time-sensitive fact candidate | 云平台会通过环境变量提供端口。后端应读取该值，不能固定只监听本机开发端口。监听 `127.0.0.1` 只接受容器内部本机连接，平台代理可能无法访问。许多平台要求绑定 `0.0.0.0`，具体按运行时示例配置。不要为了测试在云服务器防火墙随意开放端口。托管服务的公网入口通常由平台代理提供。 |
| 025 | `chapters/025-vercel-render-等自动部署平台.md:79` | time-sensitive fact candidate | 某些计划会在空闲时暂停服务，下一次请求需要等待启动。是否存在、等待多久和适用计划会变化。访问慢不一定是代码性能问题。对照部署平台事件和实例启动日志，判断是否冷启动。需要稳定响应的业务应按当前官方计划评估资源和费用，不把免费层当生产保证。 |
| 025 | `chapters/025-vercel-render-等自动部署平台.md:134` | time-sensitive fact candidate | ## 费用告警从第一天开始 |
| 025 | `chapters/025-vercel-render-等自动部署平台.md:136` | time-sensitive fact candidate | 自动部署会消耗构建资源，爬虫和异常请求会消耗流量与函数执行。个人小站也可能因误配置产生费用。创建项目时查看官方计费维度，设置预算或用量告警。测试 Webhook 时避免循环触发部署。账单突然增长，先按服务、日期和用量类型拆分。不要立即删除生产资源，先限制异常入口并保存证据。 |
| 025 | `chapters/025-vercel-render-等自动部署平台.md:138` | time-sensitive fact candidate | 价格数字只在决策记录写查询日期。项目每季度重新估算真实用量。 |
| 025 | `chapters/025-vercel-render-等自动部署平台.md:140` | time-sensitive fact candidate | 交接文档列仓库、生产分支、平台项目、服务类型、区域、构建与启动命令、环境变量名称、域名和数据位置。再列部署、回滚、备份、费用告警和状态页入口。秘密只说明存放位置和负责人。让另一位维护者按文档找到最新日志并完成一次预览部署。只有作者自己会操作，说明文档还不够。 |
| 025 | `chapters/025-vercel-render-等自动部署平台.md:160` | time-sensitive fact candidate | 亲自检查仓库授权、生产分支、环境变量、持久数据位置和费用告警。动态服务部署后完成一次受控重启和数据验证。下一章会逐项解释 Build Command、Output Directory 和环境变量。它们是自动部署中最常填错的三个位置。 |
| 025 | `chapters/025-vercel-render-等自动部署平台.md:173` | time-sensitive fact candidate | - **界面时效**　视频由 Vercel 于 2026 年发布，截至 2026 年 8 月 6 日符合当前主界面；套餐、计费、默认值与功能可用性仍要打开官方页面重新核对 |
| 027 | `chapters/027-preview-production-部署日志和回滚.md:83` | time-sensitive fact candidate | 长时间排队时查看平台状态和账号配额。长时间构建时查看日志是否仍增长，避免同时触发多个重复部署。取消部署前确认它不会承担数据库迁移或其他一次性任务。发布流程不应把不可逆迁移隐藏在无人知晓的构建脚本里。 |
| 027 | `chapters/027-preview-production-部署日志和回滚.md:168` | time-sensitive fact candidate | 亲自选择回滚目标，确认正式域名实际指向，检查核心流程和外部数据。执行前保存当前状态，执行后确认自动部署开关。下一章会把平台自带网址连接到自己的域名，并说明 DNS、HTTPS、费用和地区差异为什么需要单独核对。 |
| 028 | `chapters/028-自定义域名-dns-https-费用与地区差异.md:1` | time-sensitive fact candidate | # 自定义域名、DNS、HTTPS、费用与地区差异 |
| 028 | `chapters/028-自定义域名-dns-https-费用与地区差异.md:59` | time-sensitive fact candidate | 域名通常按周期续费，首年促销价与续费价可能不同。隐私保护、溢价域名、转移和赎回也可能产生费用。托管平台可能按构建分钟、带宽、请求、函数执行、团队席位或额外功能收费。免费额度、超额价格和休眠规则会调整。 |
| 028 | `chapters/028-自定义域名-dns-https-费用与地区差异.md:61` | time-sensitive fact candidate | 截至 2026 年 8 月 5 日，本书不写死任何平台的永久免费承诺。真正购买前打开注册商和平台官方定价页，记录币种、税费、续费价、配额与超额处理。为域名开启自动续费和到期提醒，并保留可用支付方式。域名过期会同时影响网站、邮件、API 和登录回调。 |
| 028 | `chapters/028-自定义域名-dns-https-费用与地区差异.md:139` | time-sensitive fact candidate | ## 费用与续费的记录表 |
| 028 | `chapters/028-自定义域名-dns-https-费用与地区差异.md:141` | time-sensitive fact candidate | 记录域名、注册商、注册日期、到期日、自动续费、续费价格查询日期、支付负责人和恢复联系人。托管费用另记计划名称、计费维度、预算告警与查询日期。不要把促销首年价填成长期成本。账号开启多因素认证，恢复码安全离线保存。域名控制权高于单个网站项目，权限应更严格。 |
| 028 | `chapters/028-自定义域名-dns-https-费用与地区差异.md:178` | time-sensitive fact candidate | ## 域名与费用判断要绑定检索日期 |
| 029 | `chapters/029-后端为什么存在以及-api-怎样工作.md:19` | time-sensitive fact candidate | 前端负责用户看见和操作的界面；它收集输入、展示状态、发出请求并处理响应；后端负责决定请求是否允许，以及数据怎样变化；它不相信前端已经验证过的价格、用户 ID 和角色；假设预约页面让用户选择下午三点。前端可以先显示该时段可用，后端收到提交后仍要再次检查。两个人可能同时看见最后一个名额。 |
| 029 | `chapters/029-后端为什么存在以及-api-怎样工作.md:67` | time-sensitive fact candidate | 前端限制字数有助于用户操作，攻击者可以绕过界面直接发请求。后端必须验证类型、长度、范围和业务关系。用户提交 `user_id` 时，后端不能据此决定身份。身份来自已验证会话，资源归属由服务器查询。价格也不能由前端最终决定。客户端提交商品与数量，后端从可信数据计算金额。 |
| 029 | `chapters/029-后端为什么存在以及-api-怎样工作.md:125` | time-sensitive fact candidate | 每个端点记录方法、路径、认证、请求字段、成功响应、错误代码和示例。字段说明类型、是否必需、范围和时区。错误示例与成功示例同样重要。前端需要知道配额用尽、资源冲突和会话过期怎样表现。 |
| 029 | `chapters/029-后端为什么存在以及-api-怎样工作.md:223` | time-sensitive fact candidate | 亲自确认后端不信任客户端身份、价格和权限。使用两个测试账号验证彼此不能读取或修改资源。检查生产秘密只在服务端，错误响应不泄露堆栈，重复提交不会重复扣费或占用名额。下一章会比较 REST、WebSocket、身份认证和授权，把“谁在请求”和“能做什么”拆开。 |
| 030 | `chapters/030-rest-websocket-身份认证和权限控制.md:137` | time-sensitive fact candidate | 攻击者会尝试泄露名单中的邮箱密码组合。单纯按账号永久锁定会被用来拒绝服务。组合限流、风险检测、MFA、泄露密码检查和用户通知。异常成功登录触发会话审查。验证码接口限制发送与验证次数，防止短信费用攻击。 |
| 031 | `chapters/031-sql-nosql-postgresql-与-sqlite.md:52` | time-sensitive fact candidate | 托管 PostgreSQL 由供应商处理部分安装、补丁和备份，自建则由你承担。两种方式都要设计权限、监控和恢复。截至 2026 年 8 月 11 日，PostgreSQL 官方 `current` 文档指向 18，书中命令仍要绑定实际测试的具体小版本。 |
| 031 | `chapters/031-sql-nosql-postgresql-与-sqlite.md:70` | time-sensitive fact candidate | 文档模型常为了读取方便复制显示名称、统计和摘要。源数据改变后，要同步所有副本。订单保存购买时商品名称与价格是有意快照。用户主页复制实时粉丝数则要处理更新延迟。为每份重复数据指定权威来源和更新机制。没有这两项，重复会变成矛盾。 |
| 031 | `chapters/031-sql-nosql-postgresql-与-sqlite.md:80` | time-sensitive fact candidate | 商品表保存 SKU 和名称，仓库表保存地点，库存表用商品 ID 与仓库 ID 组成唯一关系并保存数量。下单时后端在事务中锁定或原子更新库存，条件是余量足够。更新影响零行时返回缺货。订单项保存成交时名称和价格快照，避免商品后来改名影响历史凭证。 |
| 031 | `chapters/031-sql-nosql-postgresql-与-sqlite.md:184` | time-sensitive fact candidate | 线上事务数据库处理用户请求，复杂全表报表会与业务争资源。数据量大时复制到分析系统。导出过程去除或限制个人信息，控制分析账号权限。指标定义版本化。分析延迟不适合决定实时库存。报表写“截至时间”。 |
| 031 | `chapters/031-sql-nosql-postgresql-与-sqlite.md:190` | time-sensitive fact candidate | 列出实体、关系、唯一规则、跨实体事务、主要查询、写入并发、离线和数据增长。列出运行位置、连接方式、备份、恢复、地区、费用和团队经验。用最小模型实现两个最难查询与一个并发写入。在接近真实数据量的测试库测量。 |
| 031 | `chapters/031-sql-nosql-postgresql-与-sqlite.md:200` | time-sensitive fact candidate | 重复邮箱出现，检查唯一约束，不只检查前端。删除用户留下孤立订单，检查外键与删除策略。SQLite 在云端偶尔锁住，查看并发写入、事务时长和多实例。不要直接关闭锁保护。文档数据库费用突然增长，检查查询扫描、实时监听和客户端循环。费用模型按供应商当前文档核对。 |
| 032 | `chapters/032-数据库迁移-连接-备份和恢复.md:87` | time-sensitive fact candidate | 自动备份频率、保留天数、区域、加密、时间点恢复、导出能力和恢复权限。价格与计划限制按当前官方页面确认。“每天备份”还要问时间、失败通知和最近一次成功。保留七天不等于七个可用恢复点。 |
| 032 | `chapters/032-数据库迁移-连接-备份和恢复.md:131` | time-sensitive fact candidate | 保留策略可包含每日、每周和每月恢复点。旧备份逐步过期，避免无限增长。删除备份前确认法律、合同、调查和用户删除要求。保留更多不总是更安全。不可变或对象锁能降低勒索与误删风险，也会阻止提前删除。启用前理解费用和合规。 |
| 032 | `chapters/032-数据库迁移-连接-备份和恢复.md:137` | time-sensitive fact candidate | 生产和备份在同一磁盘，磁盘故障会一起丢。仅有云平台快照，账号被删除也可能一起消失。重要数据保留至少一份受独立权限保护的副本，必要时在不同区域或供应商。跨地区存储涉及数据驻留和传输费用。先确认允许位置。 |
| 033 | `chapters/033-文件上传-对象存储-邮件-推送和-ai-api.md:3` | time-sensitive fact candidate | 现代应用的数据不只在数据库。用户上传图片，对象存储保存文件；邮件服务发送确认信；推送服务把通知送到设备；AI API 接收任务并返回生成结果。每增加一个外部服务，就增加权限、费用、失败和恢复边界。 |
| 033 | `chapters/033-文件上传-对象存储-邮件-推送和-ai-api.md:23` | time-sensitive fact candidate | 客户端先向后端请求上传。后端验证登录、用途、大小上限和配额，生成对象 Key 与临时上传授权。客户端把文件直接上传对象存储，减少后端转发大文件的负担。上传完成后通知后端。后端确认对象存在、大小和类型，必要时进入病毒扫描、图片解码和转码队列。验证完成前状态为待处理，不对其他用户公开。 |
| 033 | `chapters/033-文件上传-对象存储-邮件-推送和-ai-api.md:45` | time-sensitive fact candidate | 隐私删除要求与灾难恢复备份可能存在保留冲突，政策要透明并符合法律与合同。 |
| 033 | `chapters/033-文件上传-对象存储-邮件-推送和-ai-api.md:73` | time-sensitive fact candidate | AI API 与地图、邮件相似，后端持有密钥并发送请求。不同之处在于输入可能很大，输出不确定，费用随 Token、媒体和模型变化。客户端把任务交给自己的后端。后端验证用户、配额和内容，去除不应发送的个人信息，再调用供应商。 |
| 033 | `chapters/033-文件上传-对象存储-邮件-推送和-ai-api.md:75` | time-sensitive fact candidate | 响应经过格式校验和安全检查后保存必要结果。高风险操作不能直接执行模型输出。供应商 API 版本、模型名称、价格、数据保留和地区能力会变化。正式接入只引用其当前官方文档并记录检索日期。 |
| 033 | `chapters/033-文件上传-对象存储-邮件-推送和-ai-api.md:77` | time-sensitive fact candidate | 网页和 App 包都能被用户检查。即使变量来自构建环境，只要进入客户端就会暴露。后端使用按项目限制的密钥，设置额度和费用告警。不同环境使用不同密钥。泄露后立即撤销并轮换，查看调用日志与费用。只从仓库删除不能撤回已复制凭据。 |
| 033 | `chapters/033-文件上传-对象存储-邮件-推送和-ai-api.md:85` | time-sensitive fact candidate | 记录供应商请求 ID、模型版本、参数类别和费用数据，不在日志保存完整敏感提示词。 |
| 033 | `chapters/033-文件上传-对象存储-邮件-推送和-ai-api.md:99` | time-sensitive fact candidate | AI 费用异常，按用户、端点、模型和时间分析，限制入口并轮换可能泄露密钥。 |
| 033 | `chapters/033-文件上传-对象存储-邮件-推送和-ai-api.md:177` | time-sensitive fact candidate | 费用可能包含存储容量、请求次数、数据取回、出站流量、图片处理和早删费用。只看每 GB 存储价会漏掉下载。缩略图减少移动端出站，缓存公开资源减少重复读取。私有文件缓存策略仍以权限为先。生命周期把不常访问对象转为冷存储或过期，恢复速度和最低保存期会不同。 |
| 033 | `chapters/033-文件上传-对象存储-邮件-推送和-ai-api.md:179` | time-sensitive fact candidate | 设置预算告警，按 Bucket、前缀或标签区分测试和生产用量。价格写查询日期。 |
| 033 | `chapters/033-文件上传-对象存储-邮件-推送和-ai-api.md:187` | time-sensitive fact candidate | 每个用户、组织和文件类型设置大小与数量上限。检查在授权前完成，最终对象仍核实大小。并发上传可能同时通过“剩余配额”检查。数据库使用预留或事务计数，避免超额。删除进入保留期时，配额是否立即释放由产品决定。界面说明占用计算方式。 |
| 033 | `chapters/033-文件上传-对象存储-邮件-推送和-ai-api.md:189` | time-sensitive fact candidate | 管理员扩容有审计和费用提示，不能让用户修改自己的配额字段。 |
| 033 | `chapters/033-文件上传-对象存储-邮件-推送和-ai-api.md:223` | time-sensitive fact candidate | 文件、邮件、推送和 AI 各有独立权限、状态、重试、费用和退出记录。非关键服务失败不破坏核心业务事实。私有文件用授权 URL，上传经过多层验证。邮件与推送尊重用户偏好，AI 密钥只在后端并设置配额。 |
| 033 | `chapters/033-文件上传-对象存储-邮件-推送和-ai-api.md:227` | time-sensitive fact candidate | 亲自使用未登录账号测试私有文件，验证过期 URL，检查退信与无效推送 Token。对 AI API 设置硬额度和服务端限流。每个外部服务都记录负责人、密钥位置、费用、数据地区、备份与退出方案。 |
| 034 | `chapters/034-supabase-firebase-与后端即服务.md:3` | time-sensitive fact candidate | 后端即服务常缩写为 BaaS。供应商把数据库、身份认证、文件存储、实时通信和函数等能力组合起来，通过控制台、SDK 和 API 提供。个人项目可以更快得到可用后端，仍要设计数据、权限、费用和恢复。 |
| 034 | `chapters/034-supabase-firebase-与后端即服务.md:27` | time-sensitive fact candidate | Cloud Functions 或其他 Google Cloud 计算服务运行可信后端代码。不同产品有各自区域、费用和配额。 |
| 034 | `chapters/034-supabase-firebase-与后端即服务.md:55` | time-sensitive fact candidate | ## 实时监听的费用与生命周期 |
| 034 | `chapters/034-supabase-firebase-与后端即服务.md:71` | time-sensitive fact candidate | 客户端可以直接用 Supabase Storage 或 Firebase Storage SDK 上传，服务根据用户身份与规则判断。复杂业务可以先调用自有后端，取得短时授权，再上传。后端管理配额、文件状态与后处理。 |
| 034 | `chapters/034-supabase-firebase-与后端即服务.md:85` | time-sensitive fact candidate | ## 一个费用失控例子 |
| 034 | `chapters/034-supabase-firebase-与后端即服务.md:89` | time-sensitive fact candidate | 设置预算告警和用量监控，按操作估算每位用户产生的读取、写入、存储和函数调用。免费额度只能作为当前计划条件，不能写进产品永久承诺。截至 2026 年 8 月 5 日，Firebase Cloud Storage Web 入门还说明新项目使用相关功能需要特定付费计划。封版与实际开通时都要复查。 |
| 034 | `chapters/034-supabase-firebase-与后端即服务.md:99` | time-sensitive fact candidate | 同一项目同时使用两者会增加身份、数据同步和费用复杂度。只有明确缺口时再组合。 |
| 034 | `chapters/034-supabase-firebase-与后端即服务.md:109` | time-sensitive fact candidate | 所有项目开启预算告警和审计日志。测试项目也防止泄露后产生费用。 |
| 034 | `chapters/034-supabase-firebase-与后端即服务.md:111` | time-sensitive fact candidate | 数据库、函数和存储地区影响延迟、费用与数据驻留。部分产品创建后难以更改。让频繁通信的组件靠近。函数跨洲访问数据库，会让每个请求增加网络延迟。Firebase 不同产品可用地区未必完全一致，Supabase 项目也有区域。创建前查看当前官方列表。 |
| 034 | `chapters/034-supabase-firebase-与后端即服务.md:131` | time-sensitive fact candidate | App Check 尝试确认请求来自合法应用实例，可降低脚本滥用。它不是用户身份，也不能代替 Security Rules。攻击者仍可能控制合法设备或滥用已登录账号。业务配额和服务端授权继续存在。 |
| 034 | `chapters/034-supabase-firebase-与后端即服务.md:141` | time-sensitive fact candidate | 身份提供商处理验证，业务数据中的联系字段要从可信结果同步。用户不能直接把“已验证”设为真。邮箱变化可能影响登录、通知和组织邀请。旧地址是否保留审计要按隐私政策。手机号重新分配会产生风险，高价值账号不要只靠短信长期认证。 |
| 034 | `chapters/034-supabase-firebase-与后端即服务.md:157` | time-sensitive fact candidate | 数据库事件或消息触发函数可能至少执行一次。处理逻辑用事件 ID 去重。发送邮件、扣减配额和生成文件都设计幂等。函数超时后不能假设没有完成。失败进入重试或死信处理，设置最大次数和告警。无限重试会持续收费。 |
| 034 | `chapters/034-supabase-firebase-与后端即服务.md:193` | time-sensitive fact candidate | 用两个账号做相同越权、断网和费用操作计数。记录开发时间、查询难度、导出与恢复。试验完成后选择更符合数据与团队的一项，安全删除另一测试项目和密钥。结果不泛化到所有应用。 |
| 034 | `chapters/034-supabase-firebase-与后端即服务.md:203` | time-sensitive fact candidate | 费用、地区、备份和退出有查询日期与负责人，平台删除不会是第一次研究数据导出。 |
| 034 | `chapters/034-supabase-firebase-与后端即服务.md:207` | time-sensitive fact candidate | AI 可以把业务规则翻译成 RLS 或 Security Rules 草案，比较数据模型，生成模拟器测试与费用估算表。规则必须由人审查并用未登录、普通用户、他人用户和管理员测试。AI 不能批准公开数据或删除项目。 |
| 035 | `chapters/035-托管方案-自建方案和平台依赖.md:11` | time-sensitive fact candidate | 应用至少包含计算、数据库、文件存储、域名、TLS、身份、日志、备份、监控和费用。托管平台可能处理服务器硬件、操作系统、数据库进程和自动备份。你仍处理数据模型、权限、密钥、业务监控和恢复验证。 |
| 035 | `chapters/035-托管方案-自建方案和平台依赖.md:21` | time-sensitive fact candidate | 你要安装受支持版本、配置存储与内存、限制网络、创建受限用户、监控连接与查询、安排备份和升级。磁盘满会让写入失败，证书过期会断开连接，系统补丁需要维护窗口。单台服务器故障时，应用和数据库可能一起离线。 |
| 035 | `chapters/035-托管方案-自建方案和平台依赖.md:45` | time-sensitive fact candidate | 托管账单看起来高，自建云主机月费看起来低。比较时还要计入更新、监控、备份、事故和学习时间。自建数据库每月节省一些费用，却需要一次深夜恢复，成本可能远高于差价。反过来，稳定高用量在按请求计费平台上可能昂贵，固定资源自建或专用托管更合适。 |
| 035 | `chapters/035-托管方案-自建方案和平台依赖.md:47` | time-sensitive fact candidate | 用真实用量估算存储、带宽、读写、计算、备份和支持。价格统一标注查询日期。 |
| 035 | `chapters/035-托管方案-自建方案和平台依赖.md:49` | time-sensitive fact candidate | ## 免费额度怎样看 |
| 035 | `chapters/035-托管方案-自建方案和平台依赖.md:51` | time-sensitive fact candidate | 免费层适合练习和早期验证，常有休眠、资源、带宽、构建、地区和商业使用限制。产品进入真实用户阶段前，按预期增长模拟超额费用。设置硬限制或预算告警。免费政策随时可能调整。本书截至 2026 年 8 月 5 日只记录方法，不承诺任何平台永久免费。 |
| 035 | `chapters/035-托管方案-自建方案和平台依赖.md:92` | time-sensitive fact candidate | 选一个虚构留言板，只实现注册、私人留言和图片上传。分别记录托管方案与自建方案的设置步骤。托管方案测试账号、权限、备份导出、费用告警和删除项目影响。自建方案只在隔离服务器测试安装、更新、备份和恢复时间。 |
| 035 | `chapters/035-托管方案-自建方案和平台依赖.md:110` | time-sensitive fact candidate | \| 费用 \| 计量与账单 \| 预算与异常处理 \| |
| 035 | `chapters/035-托管方案-自建方案和平台依赖.md:122` | time-sensitive fact candidate | 组件之间跨区域会增加延迟和费用。日志与请求 ID 要跨平台传递。混合减少单一锁定，也增加多供应商账号和故障。按具体收益采用。 |
| 035 | `chapters/035-托管方案-自建方案和平台依赖.md:158` | time-sensitive fact candidate | 账单和免费额度变化纳入季度复查。 |
| 035 | `chapters/035-托管方案-自建方案和平台依赖.md:164` | time-sensitive fact candidate | ## 一个费用迁移案例 |
| 035 | `chapters/035-托管方案-自建方案和平台依赖.md:166` | time-sensitive fact candidate | 图片应用在 BaaS 上增长，下载带宽成为主要费用。团队先优化缩略图、缓存和重复请求，账单明显下降。随后评估把公开图片迁到更合适对象存储，数据库和 Auth 保持不变。通过新 URL 逐步切流量。 |
| 035 | `chapters/035-托管方案-自建方案和平台依赖.md:168` | time-sensitive fact candidate | 没有因为一项费用立刻重写整个后端。优化和局部迁移的工时低于全面替换。决策记录使用三个月真实用量，不基于单日峰值。 |
| 035 | `chapters/035-托管方案-自建方案和平台依赖.md:196` | time-sensitive fact candidate | 写业务目标、预计用户与数据、团队能力、候选方案、当前价格查询日期和主要风险。对每个候选填写数据模型、地区、权限、备份、恢复、费用、支持和退出。未知项不能当作零风险。记录选择理由、未选择理由和重新评估触发条件，例如月账单、连接数或合规变化。 |
| 035 | `chapters/035-托管方案-自建方案和平台依赖.md:206` | time-sensitive fact candidate | 每个组件都有供应商与团队责任、负责人、备份、费用和退出。选择基于真实需求与能力。托管方案完成权限和恢复演练，自建方案完成重启、更新和异地恢复演练。未验证项清楚标记。决策记录包含查询日期和复查条件，用户能判断何时需要改变，而非被某个平台永久绑定。 |
| 035 | `chapters/035-托管方案-自建方案和平台依赖.md:208` | time-sensitive fact candidate | AI 可以生成责任矩阵、平台退出清单、费用模型和迁移风险表，也能根据官方文档找出未回答条件。它不能保证供应商长期价格和政策，也不能替团队承担夜间运维。最终选择由预算、数据和人员责任共同决定。 |
| 036 | `chapters/036-vps-云服务器及购买时需要看的参数.md:28` | time-sensitive fact candidate | - 监控进程、磁盘、内存和费用 |
| 036 | `chapters/036-vps-云服务器及购买时需要看的参数.md:48` | time-sensitive fact candidate | 磁盘性能还包括读写延迟、吞吐量和随机操作能力。一个只读静态站点对磁盘要求很低，频繁写入的小数据库更敏感。部分低价实例的磁盘性能会受共享资源影响，不能只看容量。还要区分系统盘、附加块存储和对象存储；系统盘随虚拟机存在，适合操作系统和应用文件；块存储像额外硬盘，适合需要文件系统的持久数据；对象存储通过接口保存文件，适合图片和备份；三者的备份、网络和费用模型不同。 |
| 036 | `chapters/036-vps-云服务器及购买时需要看的参数.md:52` | time-sensitive fact candidate | 第三件是端口。网站常用 80 和 443，SSH 常用 22。端口能否访问同时受云平台防火墙和服务器内防火墙影响。只修改其中一层，连接仍可能失败；第四件是区域；服务器离主要用户越远，网络往返通常越慢；区域还影响产品可用性、数据驻留、价格和备案要求。中国大陆用户要另外核对跨境网络、域名备案、支付方式和当地法规。 |
| 036 | `chapters/036-vps-云服务器及购买时需要看的参数.md:66` | time-sensitive fact candidate | 常见处理器架构包括 x86_64 和 ARM64。许多开源软件同时提供两种版本，但某些二进制工具、旧插件或容器镜像只支持其中一种。ARM 实例有时价格更合适。若依赖没有 ARM 构建，节省的主机费用可能变成兼容工作。购买前检查应用运行时、数据库、容器镜像和监控代理的支持列表。 |
| 036 | `chapters/036-vps-云服务器及购买时需要看的参数.md:75` | time-sensitive fact candidate | 4. 包含流量、带宽上限和超额价格 |
| 036 | `chapters/036-vps-云服务器及购买时需要看的参数.md:76` | time-sensitive fact candidate | 5. 公网 IPv4 与静态地址政策 |
| 036 | `chapters/036-vps-云服务器及购买时需要看的参数.md:83` | time-sensitive fact candidate | AWS Lightsail 的实例资料同样把 vCPU、内存、SSD 和传输量作为套餐组成。数字与价格会变化。本书截至 2026 年 8 月 5 日只保留比较方法，不把任何套餐写成永久推荐。 |
| 036 | `chapters/036-vps-云服务器及购买时需要看的参数.md:108` | time-sensitive fact candidate | 购买时要查四件事。副本包含哪些磁盘，保留多久，恢复会创建新实例还是覆盖旧实例，费用怎样计算。数据库正在写入时，整机快照也可能需要数据库恢复步骤。例如，一个图片站把应用放在系统盘，把上传文件放在附加磁盘。若自动备份只覆盖系统盘，恢复后页面程序存在，用户图片却全部缺失。创建前画出数据位置，逐项对应到备份范围。 |
| 036 | `chapters/036-vps-云服务器及购买时需要看的参数.md:116` | time-sensitive fact candidate | 很多平台按实例分配资源计费。操作系统内执行关机，虚拟机资源仍被保留，费用可能继续产生。控制台停止实例后，磁盘、快照、静态 IP 和备份也可能继续收费。删除通常会释放计算实例，关联磁盘是否一同删除取决于选项。误勾删除磁盘可能造成不可恢复的数据损失，漏删磁盘则会继续收费。 |
| 036 | `chapters/036-vps-云服务器及购买时需要看的参数.md:118` | time-sensitive fact candidate | 开始使用前做一次费用实验。创建明确标记为测试的最小实例，记录一小时或一天后的费用明细，再按平台流程停止和删除。确认账单中每项资源的状态。实验不能使用真实生产数据。 |
| 036 | `chapters/036-vps-云服务器及购买时需要看的参数.md:122` | time-sensitive fact candidate | 平台可能提供新用户抵扣、固定期限试用或有限免费额度。资格、地区、验证方式和到期行为会变化。不要围绕“永久免费”设计无法迁移的系统。购买当日保存官方条款和检索日期，设置预算告警，并准备权益结束后的月成本。 |
| 036 | `chapters/036-vps-云服务器及购买时需要看的参数.md:136` | time-sensitive fact candidate | 把应用和数据库放在一台小服务器上，部署最简单，也共享 CPU、内存、磁盘和故障范围。应用构建占满内存时，数据库也会受到影响。使用托管数据库能把数据服务移出主机，增加网络费用和平台依赖，却减少数据库进程的日常管理。数据量小不代表恢复不重要，个人日记的几百兆数据也可能无法重建。 |
| 036 | `chapters/036-vps-云服务器及购买时需要看的参数.md:144` | time-sensitive fact candidate | 若因预算和学习目的选择 VPS，内存要同时容纳系统、应用和数据库，真实需求通过测试确定。构建尽量放到 CI，数据库每日备份到异地对象存储，报名窗口前做一次恢复演练。规格数字不是案例的核心。核心是从高峰、数据后果和团队能力推出资源与责任，不能从最低价格反推系统。 |
| 036 | `chapters/036-vps-云服务器及购买时需要看的参数.md:152` | time-sensitive fact candidate | 在测试环境准备接近真实的数据量和关键操作。测量应用启动、首页请求、写入、文件上传和后台任务。记录 CPU、可用内存、磁盘等待和响应时间。逐步增加并发，不要一开始就发起可能压垮生产环境的压力测试。测试账号与真实用户数据分开，限制外部 API 调用，避免产生费用或垃圾邮件。 |
| 036 | `chapters/036-vps-云服务器及购买时需要看的参数.md:164` | time-sensitive fact candidate | 价格使用“截至某日”的格式并链接官方定价页。不要把付款卡号、账号密码、私钥或恢复码放进项目文档。 |
| 036 | `chapters/036-vps-云服务器及购买时需要看的参数.md:178` | time-sensitive fact candidate | 面板管理端口不要无限制暴露公网。使用多因素认证、来源限制和当前支持版本。本书使用原生服务说明系统关系，不要求安装控制面板。读懂底层位置以后，即使使用面板，也能判断它修改了什么。 |
| 036 | `chapters/036-vps-云服务器及购买时需要看的参数.md:184` | time-sensitive fact candidate | 接着创建项目专用用户与目录，配置备份和费用告警。应用部署、域名切换和公网开放放在这些基础之后。这套顺序让每次修改都有已知起点。直接运行一键部署脚本，会在还没理解实例时同时改变账号、软件和网络。 |
| 036 | `chapters/036-vps-云服务器及购买时需要看的参数.md:204` | time-sensitive fact candidate | 先问项目是否需要长期运行的服务器进程。再确认区域、架构和最低内存。随后检查网络、磁盘、备份和救援入口。最后才比较价格。购买以后，把责任清单放进项目文档。至少写明谁更新系统、谁收费用告警、备份在哪里、怎样恢复、实例到期或关闭前怎样导出数据。 |
| 037 | `chapters/037-第一次使用-ssh-登录服务器.md:51` | time-sensitive fact candidate | 假设服务商给出的用户名是 `ubuntu`，服务器地址是示例文档专用地址 `203.0.113.10`。实际操作时替换成自己的信息。在本地 Windows PowerShell、Windows Terminal 或 macOS 终端运行。 |
| 037 | `chapters/037-第一次使用-ssh-登录服务器.md:54` | time-sensitive fact candidate | ssh ubuntu@203.0.113.10 |
| 037 | `chapters/037-第一次使用-ssh-登录服务器.md:57` | time-sensitive fact candidate | `ssh` 启动客户端。`ubuntu` 是远程用户名。`@` 把用户名和地址分开。`203.0.113.10` 是远程服务器地址。若私钥不在默认位置，用 `-i` 指定文件。以下示例路径只作说明。 |
| 037 | `chapters/037-第一次使用-ssh-登录服务器.md:60` | time-sensitive fact candidate | ssh -i ~/.ssh/project_server ubuntu@203.0.113.10 |
| 037 | `chapters/037-第一次使用-ssh-登录服务器.md:66` | time-sensitive fact candidate | ssh -p 2222 ubuntu@203.0.113.10 |
| 037 | `chapters/037-第一次使用-ssh-登录服务器.md:184` | time-sensitive fact candidate | ssh -i "C:\Users\你的名字\My Keys\server.pem" ubuntu@203.0.113.10 |
| 037 | `chapters/037-第一次使用-ssh-登录服务器.md:211` | time-sensitive fact candidate | HostName 203.0.113.10 |
| 037 | `chapters/037-第一次使用-ssh-登录服务器.md:246` | time-sensitive fact candidate | ssh-keygen -R 203.0.113.10 |
| 037 | `chapters/037-第一次使用-ssh-登录服务器.md:280` | time-sensitive fact candidate | ssh -v ubuntu@203.0.113.10 |
| 037 | `chapters/037-第一次使用-ssh-登录服务器.md:288` | time-sensitive fact candidate | scp test.txt ubuntu@203.0.113.10:~/ |
| 037 | `chapters/037-第一次使用-ssh-登录服务器.md:299` | time-sensitive fact candidate | 公司、学校和公共网络可能禁止外连 22 端口。服务器和密钥完全正常，本地仍会超时。在获得允许的另一条网络测试，可以区分本地限制与服务器故障。不要绕过组织网络政策，也不要把 SSH 随意搬到 443 与网站争用。 |
| 037 | `chapters/037-第一次使用-ssh-登录服务器.md:350` | time-sensitive fact candidate | - **界面时效**　SSH、Ubuntu 与 UFW 命令截至 2026 年 8 月 6 日仍可按当前官方文档核对；Hetzner 控制台按钮可能变化，因此标记为部分符合当前界面 |
| 039 | `chapters/039-软件包-进程-端口-磁盘和内存.md:99` | time-sensitive fact candidate | 看到 `127.0.0.1:3000` 表示只接受本机连接，适合由同机 Caddy 或 Nginx 反向代理。看到 `0.0.0.0:3000` 表示所有 IPv4 接口都可接受连接，是否能从公网访问还受防火墙影响。数据库通常不应为了省事监听所有接口并向公网开放。应用和数据库在同一台机器时，优先监听本机地址。 |
| 039 | `chapters/039-软件包-进程-端口-磁盘和内存.md:106` | time-sensitive fact candidate | curl -i http://127.0.0.1:3000/health |
| 039 | `chapters/039-软件包-进程-端口-磁盘和内存.md:109` | time-sensitive fact candidate | `curl` 发出请求；`-i` 同时显示响应头；地址 `127.0.0.1` 表示当前服务器自己。`/health` 是示例健康检查路径，项目没有这个路径时应使用实际地址。成功时应看到 HTTP 状态行和预期正文；连接被拒绝说明没有服务在该地址端口接受连接；超时或返回 500 时查看应用日志和依赖。 |
| 039 | `chapters/039-软件包-进程-端口-磁盘和内存.md:232` | time-sensitive fact candidate | `127.0.0.1` 只代表本机 IPv4 回环。`::1` 是本机 IPv6 回环。`0.0.0.0` 常表示所有 IPv4 接口，`::` 常表示所有 IPv6 接口，具体双栈行为受系统设置影响。代理与应用都在同一主机时，应用监听本机地址即可。容器、独立数据库或私有网络会需要不同地址，第七卷会说明端口映射。 |
| 039 | `chapters/039-软件包-进程-端口-磁盘和内存.md:250` | time-sensitive fact candidate | 除了 inode，用量还可能受用户配额、只读挂载和文件权限影响。云磁盘本身也可能达到供应商限制或出现故障。完整错误信息很重要。`No space left on device`、`Read-only file system` 和 `Permission denied` 指向不同方向。先运行 `df -h`、`df -ih`，再检查目标目录权限和挂载。不要用删… |
| 039 | `chapters/039-软件包-进程-端口-磁盘和内存.md:274` | time-sensitive fact candidate | 应用日志显示启动成功，浏览器连接超时。`ss` 显示应用监听 `127.0.0.1:3000`，本机 `curl` 成功。这说明软件、进程、端口和应用响应都正常。公网不应该直接访问 3000，下一步检查 Caddy 是否监听 443，以及两层防火墙是否允许 443。 |
| 039 | `chapters/039-软件包-进程-端口-磁盘和内存.md:330` | time-sensitive fact candidate | 大量下载、备份上传或攻击流量会占用网络。应用进程健康，本地请求很快，外部用户仍感到缓慢。检查平台网络图表、代理访问日志和出站费用。找出主要路径、文件类型和来源。静态大文件可以放到对象存储与 CDN，备份安排低峰并限制带宽。异常来源可在确认后限流或阻止。 |
| 040 | `chapters/040-systemd-systemctl-journalctl-和服务日志.md:406` | time-sensitive fact candidate | 第一次登录成功以后，可以用这段视频练习 `systemctl` 与 `journalctl`。视频发布时间较早，但命令行界面和本章采用的核心命令截至 2026 年 8 月 6 日仍在 systemd 当前手册中；具体服务名要换成练习主机真实存在的名称。 |
| 041 | `chapters/041-防火墙-caddy-nginx-域名与-https.md:13` | time-sensitive fact candidate | 用户输入 `https://example.com`。DNS 先返回服务器地址。浏览器连接服务器的 443 端口。云平台防火墙检查这条连接，Ubuntu 防火墙再次检查。Caddy 或 Nginx 接受连接并完成 TLS，然后把 HTTP 请求转发到 `127.0.0.1:3000`。应用生成响应，沿原路返回。 |
| 041 | `chapters/041-防火墙-caddy-nginx-域名与-https.md:17` | time-sensitive fact candidate | 防火墙按地址、端口和协议决定网络包是否通过。它不知道 `/login` 应该交给哪个页面，也不会生成网站内容。反向代理理解 HTTP 请求，可以按域名或路径选择上游。它不应该代替应用做完整业务授权。一个安全的常见布局是，云防火墙和 UFW 只允许 SSH、HTTP、HTTPS。应用端口 3000 只监听 `127.0.0.1`，数据库端口也只允许必要来源。 |
| 041 | `chapters/041-防火墙-caddy-nginx-域名与-https.md:68` | time-sensitive fact candidate | 前置条件包括域名已解析到服务器、80 和 443 可从公网访问、应用在 `127.0.0.1:3000` 正常响应、服务器时间正确。Caddy 官方反向代理快速入门也把 DNS 与端口可达列为自动 HTTPS 的条件。 |
| 041 | `chapters/041-防火墙-caddy-nginx-域名与-https.md:74` | time-sensitive fact candidate | reverse_proxy 127.0.0.1:3000 |
| 041 | `chapters/041-防火墙-caddy-nginx-域名与-https.md:111` | time-sensitive fact candidate | proxy_pass http://127.0.0.1:3000; |
| 041 | `chapters/041-防火墙-caddy-nginx-域名与-https.md:140` | time-sensitive fact candidate | curl -i http://127.0.0.1:3000/health |
| 041 | `chapters/041-防火墙-caddy-nginx-域名与-https.md:143` | time-sensitive fact candidate | 失败时检查应用服务和日志。成功时再核对代理中的上游地址、端口和协议。如果应用只监听某个容器网络地址，主机上的代理可能无法使用 `127.0.0.1` 访问。第七卷会解释容器网络。不要通过把 3000 端口直接开放公网来绕过 502。那会改变系统安全边界，也没有修复代理与应用之间的错误。 |
| 042 | `chapters/042-部署-更新-回滚-备份和恢复.md:88` | time-sensitive fact candidate | Ubuntu 备份指南要求计划中明确备份什么、频率、位置和恢复方式，并考虑异地和冗余副本。备份计划还要写保留周期、加密、访问人和删除方式。无限保留会增加费用与隐私风险。 |
| 042 | `chapters/042-部署-更新-回滚-备份和恢复.md:96` | time-sensitive fact candidate | 云主机快照保存某一时刻的磁盘状态，适合重建实例。它可能包含操作系统、应用和数据，也可能遗漏附加磁盘。数据库备份理解数据库结构和事务，更适合精确恢复数据。对象存储版本控制能帮助找回被覆盖或删除的文件，但需要启用并承担额外费用。 |
| 042 | `chapters/042-部署-更新-回滚-备份和恢复.md:100` | time-sensitive fact candidate | 至少一份副本应离开当前服务器和当前故障域。服务器磁盘和同盘备份会一起损坏。对象存储适合保存加密备份，AWS S3 官方文档描述了对象、桶、权限和版本控制等模型。使用任何供应商都要限制凭据、设置生命周期和监控费用。 |
| 042 | `chapters/042-部署-更新-回滚-备份和恢复.md:180` | time-sensitive fact candidate | 只保留最新一份，最新备份可能已经包含误删或损坏。可以保留最近若干日、每周和每月时间点。具体数量取决于数据变化、法规、费用和恢复点目标。对象存储生命周期能自动转移或删除旧备份，规则配置错误也会提前删除。 |
| 042 | `chapters/042-部署-更新-回滚-备份和恢复.md:206` | time-sensitive fact candidate | 用户看到的产品版本、Git 标签、构建编号和部署编号可以不同，但必须能够相互映射。例如产品版本为 `1.4.0`，构建记录保存完整提交哈希，部署平台再生成一次部署编号。健康页显示产品版本和短提交号。 |
| 042 | `chapters/042-部署-更新-回滚-备份和恢复.md:228` | time-sensitive fact candidate | 每年至少在新实例走一次重建，低风险项目也可以用临时测试机演练。完成后删除测试资源并检查费用。演练会验证备份独立性。若重建必须先登录已经丢失的旧服务器，方案存在循环依赖。 |
| 043 | `chapters/043-自建服务器增加了哪些长期责任.md:5` | time-sensitive fact candidate | 这章不增加更多命令，而是把责任变成日历、证据和退出条件。能买服务器的人很多，能持续知道它是否安全、可恢复、费用可控，才算真正拥有它。 |
| 043 | `chapters/043-自建服务器增加了哪些长期责任.md:22` | time-sensitive fact candidate | 6. 费用与续订 |
| 043 | `chapters/043-自建服务器增加了哪些长期责任.md:59` | time-sensitive fact candidate | CPU、内存和磁盘是基础指标。服务进程、端口和日志是运行指标。首页、登录和关键接口是用户结果。只监控“服务器能 ping 通”会漏掉应用故障。只监控首页会漏掉磁盘增长和备份失败。最小监控至少包括外部 HTTPS 可达、服务状态、磁盘阈值、内存压力、错误率、证书有效期、备份任务结果和费用异常。 |
| 043 | `chapters/043-自建服务器增加了哪些长期责任.md:73` | time-sensitive fact candidate | 记录磁盘、数据库、上传文件和日志每周增长量。估算达到阈值的日期，提前扩容或清理。CPU 持续高时检查请求量、慢查询和后台任务。内存持续高时检查进程增长和最近版本。网络费用上升时查大文件、爬虫和缓存命中。 |
| 043 | `chapters/043-自建服务器增加了哪些长期责任.md:77` | time-sensitive fact candidate | ## 费用本身需要监控 |
| 043 | `chapters/043-自建服务器增加了哪些长期责任.md:79` | time-sensitive fact candidate | 云账单可能因出站流量、快照、闲置磁盘、静态 IP、对象存储请求和日志增加。实例月费只是其中一项；启用预算告警，按项目和环境加标签；测试资源设置到期日期，过期后先确认再删除。截至 2026 年 8 月 5 日，各平台价格、免费额度和计费条件仍会变化。本书不保存永久价格表。采购和扩容时必须重新查看官方定价页。 |
| 043 | `chapters/043-自建服务器增加了哪些长期责任.md:109` | time-sensitive fact candidate | 每周查看外部可用性、磁盘、备份结果和异常日志。高风险项目频率应更高。每月检查系统更新、账号密钥、开放端口、证书、域名、费用和容量趋势。每季度执行恢复演练，检查依赖支持周期，复核事故联系人和运行手册。 |
| 043 | `chapters/043-自建服务器增加了哪些长期责任.md:139` | time-sensitive fact candidate | 日志太短，数周后才发现的攻击无法追查。日志太长，会增加磁盘、费用和个人数据暴露。按日志类型设期限。安全审计、应用错误、访问日志和调试日志的用途不同。禁止长期打开详细调试并记录请求正文。故障排查临时开启后写到期时间，问题结束立即恢复。 |
| 043 | `chapters/043-自建服务器增加了哪些长期责任.md:145` | time-sensitive fact candidate | 服务器上的监控代理随服务器一起宕机时，可能无法发出告警。至少有一个外部服务从互联网检查正式地址。告警渠道的令牌会过期，群成员会变化。每月发送一次测试告警，确认实际有人收到。监控平台账单失败也可能停止服务。把监控订阅纳入费用清单。 |
| 043 | `chapters/043-自建服务器增加了哪些长期责任.md:175` | time-sensitive fact candidate | 应用能运行，不表示邮件、短信、支付或 AI API 凭据仍有效。第三方配额和策略变化会让部分功能静默失败。为每项外部依赖记录官方状态页、凭据位置、限额、超时和失败行为。关键操作应有幂等与重试上限。 |
| 043 | `chapters/043-自建服务器增加了哪些长期责任.md:185` | time-sensitive fact candidate | 低风险展示站不需要二十四小时人工值班。可以设置外部可用性检查、磁盘和费用告警，每周看一次备份结果。存储真实用户数据、付费订单或关键文件后，责任立即上升。需要更频繁监控、恢复演练和清楚联系渠道。 |
| 043 | `chapters/043-自建服务器增加了哪些长期责任.md:231` | time-sensitive fact candidate | 每季度统计云账单、维护时间、事故时间和未完成风险。与托管替代方案比较同等功能与恢复能力。自建月费低，若需要频繁夜间处理和无法休假，人的成本很高。托管费用高，若产品需要特殊系统能力，迁移也可能损失功能。 |
| 044 | `chapters/044-运行环境问题与-docker-的基本模型.md:19` | time-sensitive fact candidate | 某个 Python 程序在作者电脑使用 Python 3.13 和一个系统图像库。另一台电脑只有 Python 3.11，安装依赖时找不到对应编译工具。作者可以编写 Dockerfile，选择明确的 Python 基础镜像，安装系统库和项目依赖，再写启动命令。团队在支持相同架构的 Docker 环境构建和运行，步骤更接近。 |
| 044 | `chapters/044-运行环境问题与-docker-的基本模型.md:138` | time-sensitive fact candidate | 容器内 `127.0.0.1` 指向这个容器自身，不是 Docker 主机，也不是另一个数据库容器。Web 容器连接 Compose 数据库应使用服务名 `db`。连接主机服务需要 Docker 平台提供的受控地址或网络方案，Windows、macOS 与 Linux 表现不同。 |
| 044 | `chapters/044-运行环境问题与-docker-的基本模型.md:158` | time-sensitive fact candidate | 容器应用先要监听正确地址，Docker 再发布主机端口，主机防火墙最后决定外部能否访问。应用只监听容器内 `127.0.0.1` 时，端口发布也可能无法从容器外到达。容器中通常需要监听 `0.0.0.0`，再由主机绑定限制公网。 |
| 044 | `chapters/044-运行环境问题与-docker-的基本模型.md:160` | time-sensitive fact candidate | 不要把两处 `0.0.0.0` 混为一谈。容器监听全部容器接口，与主机端口发布到全部主机接口是两个层次。从容器内、本机端口和外部 HTTPS 分别验证。 |
| 044 | `chapters/044-运行环境问题与-docker-的基本模型.md:178` | time-sensitive fact candidate | 第四层是外部访问。容器为 `Up` 只说明进程尚未退出。还要检查应用监听地址、端口发布、主机防火墙和反向代理。浏览器打不开不能直接推断 Docker 坏了；例如一个笔记服务显示 `Up`，本机访问发布端口却被拒绝；进入容器后发现程序只监听 `127.0.0.1`；修正应用监听为容器内 `0.0.0.0`，重建后本机端口恢复；这个例子说明状态、进程和网络是三种… |
| 045 | `chapters/045-镜像-容器-dockerfile-和-registry.md:29` | time-sensitive fact candidate | 这是教学结构，真实项目要核对 Node.js 支持版本、原生依赖和应用文件。 |
| 045 | `chapters/045-镜像-容器-dockerfile-和-registry.md:52` | time-sensitive fact candidate | docker build -t notes-api:1.0.0 . |
| 045 | `chapters/045-镜像-容器-dockerfile-和-registry.md:55` | time-sensitive fact candidate | `build` 启动构建。`-t` 给镜像添加名称和标签。`notes-api` 是本地仓库名，`1.0.0` 是示例标签。最后的点表示当前目录是构建上下文，不能漏掉。成功时末尾显示构建完成和镜像名称。失败时按具体步骤编号查看，是拉取基础镜像、复制文件、安装依赖还是应用构建失败。 |
| 045 | `chapters/045-镜像-容器-dockerfile-和-registry.md:81` | time-sensitive fact candidate | 标签是易读名称，例如 `1.0.0`、`20260805` 或 `latest`。标签可以被重新指向另一个镜像。摘要由镜像内容计算，形如 `sha256` 后的一长串值。它能不可变地标识具体内容。开发环境可以使用方便标签，生产发布至少记录拉取时的摘要。回滚时使用已验证摘要，避免同名标签内容已经变化。 |
| 045 | `chapters/045-镜像-容器-dockerfile-和-registry.md:94` | time-sensitive fact candidate | docker tag notes-api:1.0.0 alice/notes-api:1.0.0 |
| 045 | `chapters/045-镜像-容器-dockerfile-和-registry.md:95` | time-sensitive fact candidate | docker push alice/notes-api:1.0.0 |
| 045 | `chapters/045-镜像-容器-dockerfile-和-registry.md:166` | time-sensitive fact candidate | docker image history notes-api:1.0.0 |
| 045 | `chapters/045-镜像-容器-dockerfile-和-registry.md:176` | time-sensitive fact candidate | docker image inspect notes-api:1.0.0 |
| 046 | `chapters/046-端口映射-volume-bind-mount-和数据持久化.md:13` | time-sensitive fact candidate | 应用在容器内监听 3000，这个端口属于容器网络。主机没有发布时，从公网不能直接访问。端口发布形如 `主机地址:主机端口:容器端口`。例如 `127.0.0.1:8080:3000` 让主机本地 8080 转到容器 3000。反向代理运行在主机时，可以访问 `127.0.0.1:8080`。用户只访问 Caddy 的 443，应用端口不直接暴露。 |
| 046 | `chapters/046-端口映射-volume-bind-mount-和数据持久化.md:23` | time-sensitive fact candidate | -p 127.0.0.1:8080:80 \ |
| 046 | `chapters/046-端口映射-volume-bind-mount-和数据持久化.md:30` | time-sensitive fact candidate | curl -I http://127.0.0.1:8080 |
| 046 | `chapters/046-端口映射-volume-bind-mount-和数据持久化.md:104` | time-sensitive fact candidate | -p 127.0.0.1:8081:80 \ |
| 047 | `chapters/047-docker-compose-与多容器应用.md:18` | time-sensitive fact candidate | image: example/notes-api:1.0.0 |
| 047 | `chapters/047-docker-compose-与多容器应用.md:20` | time-sensitive fact candidate | - "127.0.0.1:8080:3000" |
| 047 | `chapters/047-docker-compose-与多容器应用.md:67` | time-sensitive fact candidate | Exited 后的数字是进程退出码。零常表示正常完成，长期服务退出为零也意味着它已经不再提供请求。端口列要检查主机绑定地址，避免数据库意外显示 `0.0.0.0`。 |
| 047 | `chapters/047-docker-compose-与多容器应用.md:151` | time-sensitive fact candidate | - **界面时效**　截至 2026 年 8 月 6 日，推荐区间采用的 `docker compose` 插件流程仍符合当前 Docker 文档；镜像标签、变量与 secrets 行为以当前 Compose 规范为准 |
| 048 | `chapters/048-容器状态-日志-健康检查和重启策略.md:76` | time-sensitive fact candidate | image: example/notes-api:1.0.0 |
| 048 | `chapters/048-容器状态-日志-健康检查和重启策略.md:78` | time-sensitive fact candidate | test: ["CMD", "wget", "-q", "--spider", "http://127.0.0.1:3000/health"] |
| 048 | `chapters/048-容器状态-日志-健康检查和重启策略.md:206` | time-sensitive fact candidate | CPU 限制可以防止一个容器占满主机。达到配额时进程被节流，不一定退出。用户看到响应变慢，日志没有错误。结合容器 CPU、节流指标和请求延迟判断。后台任务可以限制并错开高峰。Web 服务需要保留突发能力。 |
| 049 | `chapters/049-更新-回滚-清理与数据丢失风险.md:53` | time-sensitive fact candidate | Compose 文件把镜像从 `1.1.0` 改回已验证 `1.0.0` 或对应摘要，先运行 `config`，再 `up -d` 重建。Registry 中旧镜像必须仍可拉取。清理本地旧镜像前确认注册表和权限。回滚后验证卷数据格式。新版本完成不可逆数据库迁移时，旧代码可能无法运行。 |
| 050 | `chapters/050-docker-虚拟机和-kubernetes-的边界.md:47` | time-sensitive fact candidate | 云服务商可以管理控制面，仍要由用户负责节点或计算、工作负载、网络策略、权限、秘密、镜像和数据。版本升级、API 弃用和插件兼容需要计划。账单包含节点、负载均衡、磁盘、流量和日志。小项目的空闲集群也会产生固定成本。与托管应用平台、容器平台或单机 Compose 比较总费用和维护时间。 |
| 050 | `chapters/050-docker-虚拟机和-kubernetes-的边界.md:119` | time-sensitive fact candidate | Kubernetes 能按 CPU 或自定义指标调整副本。应用必须支持多副本，状态不能只放本地容器。数据库连接、会话、队列和第三方配额会随副本增加。扩容 Web 可能把数据库先压垮。错误指标会来回扩缩，造成启动风暴和费用。先做容量测试和限制。 |
| 050 | `chapters/050-docker-虚拟机和-kubernetes-的边界.md:153` | time-sensitive fact candidate | 托管 Kubernetes 可能对控制面、节点、负载均衡、公网 IP、磁盘、快照、出站和日志分别计费。为了高可用常需多节点和多区域资源，空闲容量也产生费用。再加维护与学习时间，与托管容器平台和 Compose 比较总成本。 |
| 050 | `chapters/050-docker-虚拟机和-kubernetes-的边界.md:155` | time-sensitive fact candidate | 价格与免费权益按采购日官方资料核对，本书不提供永久数字。 |
| 050 | `chapters/050-docker-虚拟机和-kubernetes-的边界.md:159` | time-sensitive fact candidate | 一些平台接受 Dockerfile 或镜像，替你管理主机、证书、扩缩和日志入口。它位于 Compose 与自管 Kubernetes 之间。平台限制端口、持久磁盘、后台任务和区域，需要核对。费用可能按实例或使用量。 |
| 051 | `chapters/051-app-客户端-后端和本地数据.md:102` | time-sensitive fact candidate | - 删除账号与删除 App 的结果在界面和隐私政策中一致。 |
| 051 | `chapters/051-app-客户端-后端和本地数据.md:120` | time-sensitive fact candidate | App 1.0 在设备上建立 `notes` 表，2.0 增加 `archived_at` 字段。新安装用户会直接得到最新结构，旧用户需要从旧 schema 迁移。迁移要按每个已发布版本顺序测试。使用旧版本创建真实测试数据，再安装新版本覆盖升级。确认记录数量、特殊字符、附件关系和同步状态。 |
| 051 | `chapters/051-app-客户端-后端和本地数据.md:158` | time-sensitive fact candidate | 用户删除照片后，后端先让记录对其他设备不可见，再排队删除对象与派生缩略图。备份按政策到期。各设备同步删除状态并清本地缓存。若上传中 App 被系统回收，重开后读取上传任务。若对象已存在但数据库没有记录，后台清理任务处理孤立对象。这个案例把进程生命周期、对象存储、同步和删除连在一起。 |
| 051 | `chapters/051-app-客户端-后端和本地数据.md:178` | time-sensitive fact candidate | 备份通常按保留周期到期，难以从历史介质立即抹除。隐私政策应说明这一边界，并限制备份访问与恢复使用。删除任务完成后做抽样验证。检查对象地址失效、跨设备同步、导出结果与账号权限。 |
| 051 | `chapters/051-app-客户端-后端和本地数据.md:188` | time-sensitive fact candidate | 再让另一位不了解实现的人解释这张图。若他无法回答“手机丢了数据还在不在”和“后端停了按钮会怎样”，说明图还缺关键事实。把最终图与隐私政策、测试用例和日志字段比较。四者说法不一致时，回到真实运行检查。 |
| 052 | `chapters/052-flutter-项目-依赖-debug-profile-和-release.md:33` | time-sensitive fact candidate | version: 1.2.0+17 |
| 052 | `chapters/052-flutter-项目-依赖-debug-profile-和-release.md:36` | time-sensitive fact candidate | sdk: ^3.8.0 |
| 052 | `chapters/052-flutter-项目-依赖-debug-profile-和-release.md:41` | time-sensitive fact candidate | http: ^1.4.0 |
| 052 | `chapters/052-flutter-项目-依赖-debug-profile-和-release.md:48` | time-sensitive fact candidate | `name` 是 Dart 包名，不等于商店展示名称。`version` 中的 `1.2.0` 是给用户看的版本，`17` 是构建编号。Android 和 iOS 会把它们映射到各自版本字段，但平台仍有自己的规则。`environment` 约束 Dart SDK；`dependencies` 列出运行所需包；`assets` 把图片等资源纳入构建。YAML… |
| 053 | `chapters/053-apk-aab-包名-版本号和-android-签名.md:27` | time-sensitive fact candidate | 版本名称可以是 `1.2.0`，用于商店和应用关于页面。版本代码是递增整数，用来判断更新顺序。Flutter 常在 `pubspec.yaml` 写成下面形式。 |
| 053 | `chapters/053-apk-aab-包名-版本号和-android-签名.md:30` | time-sensitive fact candidate | version: 1.2.0+17 |
| 053 | `chapters/053-apk-aab-包名-版本号和-android-签名.md:33` | time-sensitive fact candidate | `1.2.0` 映射为用户可见版本，`17` 映射为 Android 版本代码。每次向同一轨道上传新包，版本代码必须大于已使用值。已经上传过 `17`，即使删除草稿，也不要假定可以再次使用。版本名称没有强制使用语义化版本，但稳定规则能帮助用户和维护者。修复可以从 `1.2.0` 到 `1.2.1`，新功能可以到 `1.3.0`。真正决定 Play 接受更新顺… |
| 053 | `chapters/053-apk-aab-包名-版本号和-android-签名.md:35` | time-sensitive fact candidate | 关于页面最好显示两者，例如 `1.2.0 (17)`。收到故障报告时，可以准确对应商店制品与代码提交。 |
| 053 | `chapters/053-apk-aab-包名-版本号和-android-签名.md:116` | time-sensitive fact candidate | 三项检查若有一项失败，先停在相应位置。AAB 没生成就查构建日志，Play 拒绝上传就查版本代码、包名、签名与政策字段，设备安装或升级失败就保存 Play 提示、设备信息和应用日志。不要为了让安装通过临时改包名，包名变化会让系统把它当成另一个应用。 |
| 053 | `chapters/053-apk-aab-包名-版本号和-android-签名.md:122` | time-sensitive fact candidate | ## 目标 API 是商店政策，不是手机系统版本 |
| 053 | `chapters/053-apk-aab-包名-版本号和-android-签名.md:124` | time-sensitive fact candidate | `minSdk` 决定应用支持的最低 Android 版本，`targetSdk` 表示应用已针对某个 Android 行为级别适配，`compileSdk` 决定编译时可使用哪些 API。三者职责不同。Google Play 会逐年提高目标 API 要求。截至 2026 年 8 月 5 日，官方页面说明，从 2026 年 8 月 31 日起，手机和平板的新… |
| 053 | `chapters/053-apk-aab-包名-版本号和-android-签名.md:128` | time-sensitive fact candidate | > 目标 API 与截止日期属于高频变化政策。准备上传时打开官方页面重新核对，不把本章数字当作永久要求。 |
| 053 | `chapters/053-apk-aab-包名-版本号和-android-签名.md:160` | time-sensitive fact candidate | 应用签名密钥承担设备更新身份。由 Play 管理时，升级和灾难流程按当前官方政策处理。自行管理的其他商店签名密钥丢失，可能导致无法更新既有安装。每半年做一次恢复演练。确认备份可读取、密码可找到、证书指纹匹配，并且至少两名授权负责人知道流程。 |
| 053 | `chapters/053-apk-aab-包名-版本号和-android-签名.md:184` | time-sensitive fact candidate | 发布 2.0 前，至少准备当前生产 1.9 和一个更旧的仍活跃版本。分别创建包含中文、Emoji、附件和未同步任务的数据。从 Play 内部测试把它们升级到 2.0。检查安装没有签名错误，本地迁移完成，登录仍有效，后台任务没有重复，通知入口可用。 |
| 053 | `chapters/053-apk-aab-包名-版本号和-android-签名.md:186` | time-sensitive fact candidate | 再做 2.0 干净安装，确认首次启动和默认数据。最后在最低支持 Android、主流版本和最新版本重复核心冒烟。把组合写成表格。某一格没有设备条件时标为未验证，不能用另一版本结果填充。 |
| 053 | `chapters/053-apk-aab-包名-版本号和-android-签名.md:219` | time-sensitive fact candidate | 应用查询设备上其他应用、接收外部 Intent 或提供 Service 时，会涉及包可见性和组件导出。只声明核心功能需要的查询与 Intent filter。广泛查看安装列表可能触发隐私和 Play 政策问题。 |
| 054 | `chapters/054-google-play-内部测试与发布流程.md:7` | time-sensitive fact candidate | Play Console 开发者账号代表发布主体。账号中可以有多个应用，每个应用由固定包名识别。个人账号与组织账号需要的身份资料不同。创建后要保持法律名称、地址、联系邮箱和电话有效。组织账号通常涉及 D-U-N-S Number。政策会变化，实际注册以当日 Play Console 和官方帮助为准。 |
| 054 | `chapters/054-google-play-内部测试与发布流程.md:9` | time-sensitive fact candidate | 账号权限也要分工。负责上传的人不一定需要管理付款或删除应用。不要共享同一个 Google 密码，使用 Play Console 的用户与权限功能。截至 2026 年 8 月 5 日，Android 开发者验证正在展开，Google 的发布与准备文档已经提示 2026 年的新要求。注册、身份验证、设备验证与地区时间表应在创建账号时重新查官方页面。 |
| 054 | `chapters/054-google-play-内部测试与发布流程.md:11` | time-sensitive fact candidate | 至少确认应用名称、默认语言、应用或游戏、免费或付费、包名、开发者主体和联系邮箱。免费与付费选择可能影响以后改价方式。包含广告、购买、金融、健康、儿童或用户生成内容的应用还会触发额外政策。不要为了先看到控制台下一页而随意选择。 |
| 054 | `chapters/054-google-play-内部测试与发布流程.md:31` | time-sensitive fact candidate | 它不会证明应用符合所有生产政策，也不会自动满足新个人账号的生产访问条件。 |
| 054 | `chapters/054-google-play-内部测试与发布流程.md:49` | time-sensitive fact candidate | Closed testing 让受控但更广的测试者参与，可以按测试目标建立不同群组。它适合在公开前验证设备差异、使用流程和政策准备。截至 2026 年 8 月 5 日，2023 年 11 月 13 日之后创建的新个人开发者账号，要获得生产访问资格，官方要求应用完成封闭测试，至少 12 名测试者连续选择加入 14 天，然后申请生产访问。 |
| 054 | `chapters/054-google-play-内部测试与发布流程.md:51` | time-sensitive fact candidate | 政策可能发生变化 |
| 054 | `chapters/054-google-play-内部测试与发布流程.md:53` | time-sensitive fact candidate | > 测试人数、持续时间、适用账号和申请问题都属于当前政策。真正执行时必须重新打开官方页面，不能根据旧视频安排发布日期。 |
| 054 | `chapters/054-google-play-内部测试与发布流程.md:74` | time-sensitive fact candidate | 表单不是让 AI 根据应用名称猜答案。SDK 版本、后台开关和服务配置会改变实际行为。Google 当前帮助说明，仅活跃于内部测试轨道的应用对 Data safety 展示有豁免，但进入封闭、开放或生产的应用需要完成。政策与控制台任务仍以当日页面为准。 |
| 054 | `chapters/054-google-play-内部测试与发布流程.md:78` | time-sensitive fact candidate | Play 会检查 `targetSdkVersion`。截至 2026 年 8 月 5 日，官方政策页写明，从 2026 年 8 月 31 日起，手机和平板新应用和更新需面向 Android 16，也就是 API 36 或更高。提高目标 API 后，重新测试通知、后台执行、照片选择、存储和权限。AAB 上传被接受，只能说明达到静态门槛，不能证明行为不受影响。 |
| 054 | `chapters/054-google-play-内部测试与发布流程.md:85` | time-sensitive fact candidate | 版本 1.2.0 (17) |
| 054 | `chapters/054-google-play-内部测试与发布流程.md:90` | time-sensitive fact candidate | 3. 从 1.1.0 升级，确认旧记录仍在 |
| 054 | `chapters/054-google-play-内部测试与发布流程.md:102` | time-sensitive fact candidate | 目标 API 不足时，升级项目配置并测试行为变化。只编辑 AAB 文件不可行。权限或政策警告要回到应用行为和表单。通过删除文字掩盖真实数据收集，可能导致审核或后续执法问题。 |
| 054 | `chapters/054-google-play-内部测试与发布流程.md:104` | time-sensitive fact candidate | 账号持有人应确认开发者展示名称、支持邮箱、隐私政策、应用国家或地区、免费或付费、广告声明和内容分级。检查商店截图来自当前 Release，说明中的功能确实能用。审核人员需要登录时，提供专用测试账号与进入步骤，不能提供生产管理员账号。 |
| 054 | `chapters/054-google-play-内部测试与发布流程.md:123` | time-sensitive fact candidate | - **观看前需要完成**　使用独立练习应用，确认唯一包名、版本号、隐私政策和测试签名材料，录屏或截图时隐藏密钥口令 |
| 054 | `chapters/054-google-play-内部测试与发布流程.md:125` | time-sensitive fact candidate | - **界面时效**　视频使用 2026 年 Play Console，截至 2026 年 8 月 6 日可作为界面参考；测试人数、账号资格、政策问卷和审核要求必须重新打开官方页面核对 |
| 054 | `chapters/054-google-play-内部测试与发布流程.md:142` | time-sensitive fact candidate | 保存每项提交日期和负责人。应用新增功能或 SDK 后，回到相关任务更新。政策状态页出现问题时，先读取具体应用、版本、截止日和修正要求。不要因为首页还能访问就延后处理。 |
| 054 | `chapters/054-google-play-内部测试与发布流程.md:176` | time-sensitive fact candidate | 每位测试者不必执行完全相同步骤，可以按设备和场景分组。反馈仍使用同一模板，便于合并。持续 opt-in 的政策条件与真实测试质量要同时满足。不要用付费刷测试者服务冒充反馈，这会增加账号与数据风险。 |
| 054 | `chapters/054-google-play-内部测试与发布流程.md:184` | time-sensitive fact candidate | 记录政策名称、通知时间、涉及版本、截图和截止日。控制台文案可能更新，完整上下文能帮助团队沟通。先判断问题位于代码、商店资料、数据披露、账号资格还是权限使用。每类交给有证据的人处理。 |
| 054 | `chapters/054-google-play-内部测试与发布流程.md:186` | time-sensitive fact candidate | 提交申诉时说明应用实际行为、修正和验证。引用官方政策和具体页面。情绪化要求“立即恢复”不能帮助审核者确认事实。收到批准后仍检查生产版本。政策问题解决不表示最新 AAB 的业务测试自动通过。 |
| 054 | `chapters/054-google-play-内部测试与发布流程.md:188` | time-sensitive fact candidate | ## 国家、价格和税务属于另一组决定 |
| 054 | `chapters/054-google-play-内部测试与发布流程.md:190` | time-sensitive fact candidate | 选择分发国家会改变可见用户、内容要求、支付和支持范围。不要默认全世界都适合第一天开放。免费、付费、应用内购买和订阅涉及 Play Billing、商户资料、税务和退款政策。本书不提供固定费率结论。 |
| 054 | `chapters/054-google-play-内部测试与发布流程.md:192` | time-sensitive fact candidate | 在目标市场检查开发者与用户支付可用性、货币、结算账户和法律责任。价格页面截图只反映当时状态。测试轨道中的购买使用官方测试机制，不能向测试者收真实费用后再人工退款。 |
| 054 | `chapters/054-google-play-内部测试与发布流程.md:200` | time-sensitive fact candidate | 构建者上传 `1.2.0 (17)` 到内部轨道；测试者 A 从全新设备加入，安装并注册；测试者 B 保留 `1.1.0 (12)`，从 Play 升级；A 检查首次权限和新建数据；B 检查旧数据迁移、登录保持和推送；两人分别记录设备与时间。B 的 Google 登录失败，日志显示正式签名证书未登记。团队加入 Play 应用签名指纹，构建 `1.2.0 (1… |
| 054 | `chapters/054-google-play-内部测试与发布流程.md:222` | time-sensitive fact candidate | 权限与 SDK 变化可能触发新的政策任务。Release notes 不能替代表单更新。最后确认这是测试还是生产。浏览器多个标签同时打开不同应用时，先核对包名和应用名称。 |
| 054 | `chapters/054-google-play-内部测试与发布流程.md:230` | time-sensitive fact candidate | 测试处理、应用审核和政策复核时间受账号、应用风险、地区和提交内容影响。官方可能给出常见范围，但不是服务保证。发布计划为退回修改和重新审核预留时间。不要先向客户承诺周五必定上线，再在周四首次提交。 |
| 054 | `chapters/054-google-play-内部测试与发布流程.md:254` | time-sensitive fact candidate | 初学者要能建立应用记录、上传签名 AAB、配置内部测试、让测试者从 Play 安装，并读懂包名、版本、签名和政策错误。还要知道内部测试不等于生产资格，Data safety 来自真实数据流，账号政策和目标 API 必须按日期复核。 |
| 055 | `chapters/055-ios-macos-xcode-证书和-provisioning-profile.md:9` | time-sensitive fact candidate | > 本章涉及 Xcode、钥匙串、Archive 和 iOS 真机签名的步骤必须在 Mac 上完成。当前书稿工作环境是 Windows，没有真实 Apple Developer Program 账号，因此本章只依据截至 2026 年 8 月 5 日的 Apple 与 Flutter 官方资料核验。最终需要在用户控制的 Mac 和账号中实测。 |
| 055 | `chapters/055-ios-macos-xcode-证书和-provisioning-profile.md:15` | time-sensitive fact candidate | 截至 2026 年 8 月 5 日，Apple 官方会员比较页写明，Apple Developer Program 为每会员年 99 美元，支持当地货币的地区按当地货币收取。符合条件的非营利、教育或政府实体可能申请费用减免。 |
| 055 | `chapters/055-ios-macos-xcode-证书和-provisioning-profile.md:19` | time-sensitive fact candidate | > 费用、税费、支付方式、地区可用性和减免资格都要在付款当天核对官方页面。本书不把 99 美元写成永久价格。 |
| 055 | `chapters/055-ios-macos-xcode-证书和-provisioning-profile.md:91` | time-sensitive fact candidate | Flutter 的 `version: 1.2.0+17` 会映射到 iOS 的用户版本和 build number，也可以在构建命令中覆盖。Flutter iOS 发布文档说明，每次上传需要唯一 build number。 |
| 055 | `chapters/055-ios-macos-xcode-证书和-provisioning-profile.md:93` | time-sensitive fact candidate | Xcode General 页也能显示和编辑 Version 与 Build。团队要确定唯一事实来源，避免 `pubspec.yaml`、CI 参数和 Xcode 手工值互相覆盖。商店同一版本可以上传多个 build，例如 `1.2.0 (17)` 和 `1.2.0 (18)`。版本给用户看，build 用于区分同一版本的不同候选构建。 |
| 055 | `chapters/055-ios-macos-xcode-证书和-provisioning-profile.md:95` | time-sensitive fact candidate | 收到问题时同时记录两者。只有“1.2.0 崩溃”无法知道用户拿到哪个 build。 |
| 056 | `chapters/056-archive-testflight-与-app-store-connect.md:75` | time-sensitive fact candidate | 版本与构建　1.2.0 (18) |
| 056 | `chapters/056-archive-testflight-与-app-store-connect.md:76` | time-sensitive fact candidate | 设备与系统　iPhone 15，iOS 19.1 |
| 056 | `chapters/056-archive-testflight-与-app-store-connect.md:87` | time-sensitive fact candidate | 截至 2026 年 8 月 5 日，Apple Upload builds 页面列出的 iOS 构建要求为 Xcode 16 或更高。Apple 还会公布 upcoming requirements，这一数字封版与每次上传前都要复核。 |
| 056 | `chapters/056-archive-testflight-与-app-store-connect.md:97` | time-sensitive fact candidate | 测试通过以后，在 App Store Connect 的版本页面选择对应 build。补充描述、关键词、截图、支持网址、隐私政策、年龄分级和审核信息。Apple 当前提交流程要求先把版本 Add for Review，加入一个 draft submission，再在提交页面点击 Submit for Review。状态才会进入审核流程。只完成 Add for… |
| 056 | `chapters/056-archive-testflight-与-app-store-connect.md:118` | time-sensitive fact candidate | - **界面时效**　截至 2026 年 8 月 6 日，流程仍符合 Flutter 当前发布文档的主要阶段；Xcode 与 App Store Connect 界面标记为部分符合当前版本 |
| 056 | `chapters/056-archive-testflight-与-app-store-connect.md:138` | time-sensitive fact candidate | - **界面时效**　视频使用 2025 年界面，截至 2026 年 8 月 6 日可作为主要位置参考；Apple 会调整问卷、状态和审核要求，操作前仍需核对当前官方帮助 |
| 056 | `chapters/056-archive-testflight-与-app-store-connect.md:167` | time-sensitive fact candidate | 外部人数增加后，测试服务器可能收到接近公开流量。限额、监控、备份和滥用保护要先准备。测试账号使用合成数据。公开邀请链接可能扩散，不能授予查看所有用户的权限。测试版隐私政策仍然适用。收集反馈、设备数据和崩溃信息时，向测试者说明用途。 |
| 056 | `chapters/056-archive-testflight-与-app-store-connect.md:189` | time-sensitive fact candidate | 版本号显示给用户，build 用于内部区分。商店版本 `1.2.0` 可以经过多个 TestFlight build，最终只选择一个提交。 |
| 056 | `chapters/056-archive-testflight-与-app-store-connect.md:213` | time-sensitive fact candidate | 第一人核对二进制。Bundle ID、Version、Build、环境、签名、核心测试和符号资产正确。第二人核对商店。截图、描述、隐私、审核账号、联系信息、价格地区和发布方式正确。两人共同确认所选 build 与测试报告相同。保存提交时间和 submission 状态。 |
| 056 | `chapters/056-archive-testflight-与-app-store-connect.md:225` | time-sensitive fact candidate | 协议过期或资料待处理可能阻止销售或提交。发布计划提前检查，不在审核通过后才发现。费率、税务和结算政策会变化，本书不写固定比例。执行时使用 Apple 官方协议与合格财务意见。 |
| 056 | `chapters/056-archive-testflight-与-app-store-connect.md:233` | time-sensitive fact candidate | 审核人员可能在另一个国家、时区和网络使用应用。后端不能只允许办公室 IP，也不能在夜间自动关闭测试环境。测试账号、邮件验证码、地图、OCR、推送和支付沙箱都要可用。第三方配额不足会让审核看到空白页面。 |
| 056 | `chapters/056-archive-testflight-与-app-store-connect.md:241` | time-sensitive fact candidate | 需要解释政策时引用当前 App Review Guidelines 条目，描述应用事实。不要提交账户密码、私钥或无关用户数据。保存沟通与最终决定。后续版本涉及同一功能时，提前把曾经要求的说明加入审核资料。 |
| 057 | `chapters/057-商店素材-权限-隐私政策和审核反馈.md:1` | time-sensitive fact candidate | # 商店素材、权限、隐私政策和审核反馈 |
| 057 | `chapters/057-商店素材-权限-隐私政策和审核反馈.md:18` | time-sensitive fact candidate | - 隐私政策说明第三方处理者和删除办法 |
| 057 | `chapters/057-商店素材-权限-隐私政策和审核反馈.md:31` | time-sensitive fact candidate | 文字覆盖层保持短小，不能遮住核心界面。深色模式和小屏设备要检查可读性。Apple 的截图尺寸和设备系列会随硬件变化。截至 2026 年 8 月 5 日，官方规格页允许每类上传一到十张 JPEG 或 PNG，并明确不接受透明通道，具体尺寸应在制作当天查表。 |
| 057 | `chapters/057-商店素材-权限-隐私政策和审核反馈.md:43` | time-sensitive fact candidate | 相机只用于扫描时，不需要读取整个照片库。选择单张照片时，优先考虑平台提供的选择器，减少广泛存储权限。后台定位、通讯录、无障碍服务、VPN 和短信等高敏感能力会带来更严格政策。使用前先确认核心功能是否真正需要，并查当日平台规则。 |
| 057 | `chapters/057-商店素材-权限-隐私政策和审核反馈.md:47` | time-sensitive fact candidate | 隐私政策至少让普通用户知道收集什么、为什么、与谁共享、保存多久、怎样保护、如何请求访问或删除，以及如何联系开发者。政策页面必须可以公开访问，移动端可读，并在审核期间保持在线。只放一个需要登录的云文档链接，审核人员和用户可能打不开。 |
| 057 | `chapters/057-商店素材-权限-隐私政策和审核反馈.md:49` | time-sensitive fact candidate | 隐私政策不是免责声明。写“我们可能收集任何信息”不能替代具体说明，也不能让不必要收集变得合理。应用内要提供容易找到的隐私入口。Apple Review Guidelines 当前要求所有 App 在 App Store Connect 元数据和应用内提供可访问的隐私政策链接。 |
| 057 | `chapters/057-商店素材-权限-隐私政策和审核反馈.md:59` | time-sensitive fact candidate | “收集”不只指写入自己的数据库。数据由集成 SDK 发送给第三方，也可能需要披露。传输只为实时请求且不作更长保留的情况，按 Google 当前定义判断，不能自行简化。即使应用不收集用户数据，Google 当前帮助仍要求完成表单并提供隐私政策，内部测试单独存在特定豁免。进入其他轨道前重新核对。 |
| 057 | `chapters/057-商店素材-权限-隐私政策和审核反馈.md:61` | time-sensitive fact candidate | 填写后把商店预览与事实表逐项比较。版本新增 SDK 或数据用途时，更新表单和政策，不能等用户投诉。 |
| 057 | `chapters/057-商店素材-权限-隐私政策和审核反馈.md:65` | time-sensitive fact candidate | 回答以已经提交或准备提交的 App 版本为准。若同一 App 的不同 Apple 平台行为不同，按 Apple 当前规则完整回答。隐私政策 URL 为必填，用户隐私选择 URL 可按需要提供。数据实践变化时要更新答案。 |
| 057 | `chapters/057-商店素材-权限-隐私政策和审核反馈.md:73` | time-sensitive fact candidate | SDK 更新可能改变数据行为。依赖升级审查除了编译与功能，还要检查隐私说明和商店政策。Apple 的隐私清单与第三方 SDK 签名要求、Google 的 SDK 政策都会变化。封版与每次发布前查官方页面，不能依赖两年前的教程。 |
| 057 | `chapters/057-商店素材-权限-隐私政策和审核反馈.md:105` | time-sensitive fact candidate | 审核反馈可能指向应用行为、崩溃、元数据、隐私、账号访问、付款或政策。先分类，再决定改代码还是改资料。应用崩溃时，用反馈设备、系统、build 和步骤复现。保留日志与崩溃报告。元数据不准确时，更新说明和截图，并检查是否还有其他语言版本。 |
| 057 | `chapters/057-商店素材-权限-隐私政策和审核反馈.md:109` | time-sensitive fact candidate | 本章涉及的账号费用、测试人数、截图规格、目标 API、Data safety 和 App Privacy 均检索于 2026 年 8 月 5 日。在真正发布当天，至少重新检查 Google Play Policy status、目标 API 页面、Data safety 任务、Apple upcoming requirements、App Review Gu… |
| 057 | `chapters/057-商店素材-权限-隐私政策和审核反馈.md:111` | time-sensitive fact candidate | 把检查时间和链接写进发布记录。政策页更新后，可以知道旧版本依据的是哪一天的信息。AI 可以把事实表整理成隐私政策草稿和审核说明，也能扫描依赖清单找候选 SDK。你必须亲自核对网络流量、后台配置和正式商店表单。法律文本和高风险业务还需要合格专业人士审查。 |
| 057 | `chapters/057-商店素材-权限-隐私政策和审核反馈.md:119` | time-sensitive fact candidate | 隐私政策用于完整说明，特定敏感数据还可能需要在收集前提供醒目披露和同意。说明放在相关功能附近，写数据、用途、是否共享和继续操作的含义。默认勾选或把拒绝按钮藏在屏幕外，会削弱选择。用户撤回同意后，停止相应收集，并说明对历史数据的处理。关闭个性化广告不一定自动删除已收集资料，两件事分开写。 |
| 057 | `chapters/057-商店素材-权限-隐私政策和审核反馈.md:121` | time-sensitive fact candidate | Google 对不符合用户合理预期的敏感数据访问有 prominent disclosure 要求，实际使用时查当前 User Data 政策与具体权限页。 |
| 057 | `chapters/057-商店素材-权限-隐私政策和审核反馈.md:125` | time-sensitive fact candidate | 允许创建账号的应用通常要提供清楚的删除路径，并按平台当前政策提供网页入口或应用内入口。删除流程说明哪些数据立即删除、哪些进入恢复期、哪些因法律义务保留。用户取消订阅和删除账号可能是两个动作。 |
| 057 | `chapters/057-商店素材-权限-隐私政策和审核反馈.md:137` | time-sensitive fact candidate | 商店截图和说明要展示真实价格周期，订阅明确自动续费、试用与取消路径。不能把年度价格做大字，却把计费周期藏起来。审核使用沙箱或测试商品。不要向审核人员和测试者收真实款项。 |
| 057 | `chapters/057-商店素材-权限-隐私政策和审核反馈.md:139` | time-sensitive fact candidate | 为截图保存来源 build、设备画布、语言、文案和导出日期。设计文件进入受控目录，导出结果与商店版本关联。应用界面更新后，搜索截图中已经移除的按钮、旧品牌和旧价格。不同国家资料可能需要不同法律说明。 |
| 057 | `chapters/057-商店素材-权限-隐私政策和审核反馈.md:165` | time-sensitive fact candidate | 一款白噪声 App 宣称不收集数据。新版本加入崩溃分析 SDK，默认上传设备型号、系统、会话和崩溃堆栈。开发者只更新代码，没有改 Data safety、App Privacy 和隐私政策。审核或后续检查发现 SDK 流量与声明不符。 |
| 057 | `chapters/057-商店素材-权限-隐私政策和审核反馈.md:167` | time-sensitive fact candidate | 修复先决定是否真正需要该 SDK 与哪些字段。限制不必要收集，更新事实表、政策和商店问卷，再构建 Release 验证网络。只在说明中增加一句“可能收集任何数据”，没有解决最小化与准确披露。 |
| 057 | `chapters/057-商店素材-权限-隐私政策和审核反馈.md:179` | time-sensitive fact candidate | 支持 URL、隐私政策和营销网站要监控可用性。域名过期会让商店资料失效。应用删除功能后更新描述与截图。价格、免费额度和第三方服务变化时更新相关承诺。用户评价反映常见误解时，先检查商店文案和应用引导，不能只逐条回复。 |
| 057 | `chapters/057-商店素材-权限-隐私政策和审核反馈.md:185` | time-sensitive fact candidate | 保存候选 build、商店文案、每种语言截图、权限表、SDK 表、数据流图、隐私政策版本、Data safety 与 App Privacy 回答、内容分级和审核说明。每项带日期与负责人。敏感测试账号放密码管理器，证据包只保存引用。 |
| 057 | `chapters/057-商店素材-权限-隐私政策和审核反馈.md:197` | time-sensitive fact candidate | 隐私政策可以用普通语言概括，内部保留表写精确系统与负责人。 |
| 057 | `chapters/057-商店素材-权限-隐私政策和审核反馈.md:219` | time-sensitive fact candidate | ## 政策整改要覆盖仍在线版本 |
| 057 | `chapters/057-商店素材-权限-隐私政策和审核反馈.md:221` | time-sensitive fact candidate | 平台指出一个权限或 SDK 问题时，修复新版本还不一定足够。旧版本可能仍在用户设备收集数据。可以通过后端关闭相关接口或 SDK 配置止损，再发布修复。评估是否需要通知、删除历史数据和更新政策。 |
| 057 | `chapters/057-商店素材-权限-隐私政策和审核反馈.md:231` | time-sensitive fact candidate | 读者需要能从真实功能建立权限、SDK 和数据表，制作不误导的素材，填写当前平台隐私问卷，并给审核人员可复现路径。还要知道政策、尺寸、账号费与表单会变化，必须记录检索日期和官方链接。本书不代替法律意见，也不逐条解释所有行业政策。金融、医疗、儿童、VPN 和政府应用要做专项审查。 |
| 058 | `chapters/058-app-更新-崩溃日志和后端停机.md:11` | time-sensitive fact candidate | 假设 2.0 客户端把用户姓名字段从 `name` 改成 `displayName`，后端同一天删除旧字段。仍使用 1.9 的用户会突然无法读取资料；安全做法可以分阶段进行；后端先同时接受和返回新旧字段；2.0 客户端发布并逐步覆盖；观察旧版本使用比例下降，再让后端停止写旧字段；最后经过公告和期限才删除兼容代码。 |
| 058 | `chapters/058-app-更新-崩溃日志和后端停机.md:13` | time-sensitive fact candidate | 数据库变化也使用可兼容顺序。先新增可空字段或新表，让新旧程序都能运行。数据回填完成后再切读路径。直接重命名或删除旧字段，容易让旧客户端和回滚版本同时失效。兼容窗口有成本，因此要记录最低支持版本和结束时间。无限期支持所有旧版本也不现实。 |
| 058 | `chapters/058-app-更新-崩溃日志和后端停机.md:15` | time-sensitive fact candidate | App Version 用于商店和用户。API 版本用于客户端与后端约定请求格式。两者不必一一对应。一个 2.1 App 可能仍调用 `/v1` API，只增加本地界面。另一个 2.1.1 修复可能需要后端新增可选字段。 |
| 058 | `chapters/058-app-更新-崩溃日志和后端停机.md:23` | time-sensitive fact candidate | Apple phased release 会在七天内把自动更新逐步扩大。截至 2026 年 8 月 5 日，官方比例为第一天 1%、第二天 2%、第三天 5%、第四天 10%、第五天 20%、第六天 50%、第七天 100%。用户仍可手动下载新版本，因此它不是严格实验隔离。 |
| 058 | `chapters/058-app-更新-崩溃日志和后端停机.md:25` | time-sensitive fact candidate | 政策可能发生变化 |
| 058 | `chapters/058-app-更新-崩溃日志和后端停机.md:57` | time-sensitive fact candidate | 记账 App 2.0 修改本地 SQLite schema。开发者只测试了卸载后的干净安装，没有从 1.9 升级。旧用户首次启动时，迁移脚本按不存在的中间版本执行，读取缺失列并崩溃。新用户数据库直接创建为最新结构，因此团队设备都正常。 |
| 058 | `chapters/058-app-更新-崩溃日志和后端停机.md:59` | time-sensitive fact candidate | 逐步发布的第一批崩溃率上升。团队暂停扩大，保留后端兼容，修复迁移顺序并增加 2.0.1。测试使用 1.7、1.8、1.9 三个旧数据库副本逐级升级。这个事故说明干净安装和升级安装必须分别测试。本地数据 schema 也是发布接口。 |
| 058 | `chapters/058-app-更新-崩溃日志和后端停机.md:71` | time-sensitive fact candidate | 有时旧版本存在严重安全问题，或后端无法继续兼容；App 可以查询最低支持版本并提示升级；强制升级页面要保留商店入口、支持渠道和必要说明；若商店在某地区不可访问，用户需要替代方案；后端返回最低版本时，不能只比较版本名称字符串；`1.10` 按文字可能被错误认为小于 `1.9`；使用明确的整数 build 或规范版本比较。 |
| 058 | `chapters/058-app-更新-崩溃日志和后端停机.md:113` | time-sensitive fact candidate | 每季度做一次旧版本兼容、账号权限、签名资产、隐私表单和后端恢复检查。App 没有更新，证书、SDK 和商店政策仍会变化。AI 可以聚类崩溃、比较版本日志和生成演练清单。你必须确认符号是否匹配、指标是否真实、暂停或扩大范围的影响。任何自动发布系统都要把最终生产确认留给授权人员。 |
| 058 | `chapters/058-app-更新-崩溃日志和后端停机.md:133` | time-sensitive fact candidate | 服务端按客户端能力发送，或使用所有支持版本都理解的最小格式。敏感数据仍不放通知正文。发布新 App 以前先部署兼容后端，发布完成以后再逐步启用新通知类型。 |
| 058 | `chapters/058-app-更新-崩溃日志和后端停机.md:161` | time-sensitive fact candidate | 新支付页面只在 3.0 支持，远程配置却把开关发给所有版本。2.9 收到未知页面路径后停在空白页。团队关闭开关，修正服务端条件为 build 大于等于指定值，并让旧客户端对未知路径回首页。之后每个开关都记录最低版本、安全默认和回滚测试。控制台修改需要双人确认。 |
| 058 | `chapters/058-app-更新-崩溃日志和后端停机.md:179` | time-sensitive fact candidate | 商店下架、账号删除与后端关闭分别执行。只下架 App 不会停止服务器费用，也不会删除用户数据。 |
| 058 | `chapters/058-app-更新-崩溃日志和后端停机.md:231` | time-sensitive fact candidate | 每个版本保存兼容说明、数据库变更、最低支持版本、候选 build、测试轨道、逐步比例、监控基线和停止条件。异常时补时间线、影响、暂停动作、修复 build、数据补偿和用户沟通。恢复后加入复盘行动。 |
| 059 | `chapters/059-从现象到故障层级的统一判断方法.md:39` | time-sensitive fact candidate | 第四层是应用运行时，确认 systemd 服务、Docker 容器或平台实例是否运行，版本与配置是否正确，运行日志是否出现同一请求。第五层是数据库和外部服务，检查连接、认证、权限、容量、锁、超时与配额。第六层是主机，关注磁盘、内存、CPU、时间、文件权限和防火墙。所有服务同时异常时，主机或共同依赖更值得优先检查；只有一个接口异常时，则应先留在应用与数据边界。 |
| 059 | `chapters/059-从现象到故障层级的统一判断方法.md:64` | time-sensitive fact candidate | “网络有问题”太宽。更好的假设是“反向代理无法连接 127.0.0.1 的 3000 端口，所以返回 502”。这个假设预测三个可观察结果，代理能收到请求，应用端口连接失败，应用日志没有同一请求。检查结果不符时，假设就被削弱，维护者应更新判断，而不是寻找理由保住最初猜测。 |
| 059 | `chapters/059-从现象到故障层级的统一判断方法.md:84` | time-sensitive fact candidate | 用户访问 `https://notes.example.com` 看到 502。DNS 正常，TLS 有效，Caddy 访问日志记录请求并返回 502，这说明用户到代理的路径可以工作。检查上游配置发现目标是 `127.0.0.1:3000`，运行 `ss -lntp` 却没有进程监听 3000。此时问题范围已经从整条互联网链路缩到代理与应用之间。 |
| 061 | `chapters/061-服务器-docker-数据库和代理日志.md:143` | time-sensitive fact candidate | 集中平台方便跨主机搜索和保留，但网络中断、采集代理故障、字段解析错误与配额都可能让日志缺失。应用与代理仍应保留短期本地缓冲，并监控采集延迟、丢弃量和最后成功时间。平台搜索不到事件时，回到源主机和请求路径验证，不能立刻断言应用没有执行。 |
| 061 | `chapters/061-服务器-docker-数据库和代理日志.md:145` | time-sensitive fact candidate | 集中查询的访问权限往往覆盖多个服务与用户数据，应按环境和职责分开。导出、共享链接和 AI 集成都要经过脱敏与审批。索引保留过长会增加费用与隐私风险，过短又影响事故调查，期限应依据日志类型和真实调查需要，而不是所有内容使用一个永久保留策略。 |
| 062 | `chapters/062-flutter-logcat-xcode-与商店上传错误.md:72` | time-sensitive fact candidate | iOS 调试与发布需要真实 macOS、Xcode 和用户控制的 Apple 开发者配置。本工作环境是 Windows，因此下面内容依据截至 2026 年 8 月 6 日的 Apple 与 Flutter 官方资料整理，没有伪装成已经完成本机 Xcode 实测。最终出版前仍需在真实 Mac、测试设备与 App Store Connect 账号中核对界面和流程… |
| 062 | `chapters/062-flutter-logcat-xcode-与商店上传错误.md:84` | time-sensitive fact candidate | 常见处理顺序是先确认归档属于正确应用与 Team，再阅读第一条具体错误，修改后生成新的 Archive。若后台已接收过同一个 build number，通常需要增加构建号并重新归档，不能覆盖原构建。截至 2026 年 8 月 6 日，App Store Connect 官方状态参考区分处理中、处理失败和已完成等上传状态；界面文字与后台策略可能变化，封版前必须… |
| 062 | `chapters/062-flutter-logcat-xcode-与商店上传错误.md:90` | time-sensitive fact candidate | 收到反馈后先逐条拆成可验证项。记录原文、关联版本、需要修改二进制还是只改后台资料、负责人和复测方式。审核要求测试账号时，应提供专用账号、稳定数据和明确操作路径，不能提供个人真实账号。需要回复解释时，说明实际行为和验证步骤，不要承诺尚未实现的功能。 |
| 062 | `chapters/062-flutter-logcat-xcode-与商店上传错误.md:92` | time-sensitive fact candidate | 商店规则与界面属于高变化信息。账号费用、测试人数、处理时间、SDK 要求、隐私表单和审核政策都应写“截至检索日期”，并引用官方资料。社区帖子可以帮助理解某段错误，但最终操作要回到 Flutter、Android Developers、Apple Developer 和商店后台的当前说明。 |
| 063 | `chapters/063-复现-调用栈-最小复现-最近改动和回滚.md:19` | time-sensitive fact candidate | 复现指在已知前提下，通过明确步骤再次得到同一类结果。它至少应写环境、版本、账号状态、测试数据、操作顺序、预期结果、实际结果和发生频率。例如“保存失败”应展开成“Android 15 测试机上，应用 2.4.1 的 Release 构建，离线创建一条含图片的笔记，恢复网络后点击同步，十次中约有三次显示 409，服务器未生成重复记录”。 |
| 064 | `chapters/064-怎样向-ai-或开发者提交完整报错.md:15` | time-sensitive fact candidate | 一个清楚摘要可以这样写。“从 `2026-08-06T14:00:00+08:00` 起，生产站点所有登录请求返回 502，公开首页仍为 200。版本为 `web-2.8.4`，故障在部署 `abc1234` 后两分钟开始。已暂停继续发布并关闭登录写入，没有发现数据删除，旧会话仍可读取内容。”读者无需先翻日志，就能判断范围、时间关系与止损状态。 |
| 064 | `chapters/064-怎样向-ai-或开发者提交完整报错.md:95` | time-sensitive fact candidate | 附件使用稳定名称，例如 `build-log-web-2.8.4.txt`、`logcat-app-241-android15.txt` 和 `network-login-20260806.har`。HAR、崩溃报告、数据库日志和配置文件可能包含令牌与个人数据，不能因为扩展名普通就直接公开。压缩包内也要逐个检查，不能只给压缩包改名。给出附件清单和用途。接收者… |
| 064 | `chapters/064-怎样向-ai-或开发者提交完整报错.md:111` | time-sensitive fact candidate | 公开 Issue 适合可复现的产品缺陷、脱敏错误、环境和最小项目。安全漏洞、未修复的鉴权绕过、真实用户数据、生产内部地址与有效秘密不应先公开，应按项目安全政策或私有渠道报告。找不到安全入口时，可以先联系维护者询问受控方式，不在正文中披露可直接利用细节。 |
| 064 | `chapters/064-怎样向-ai-或开发者提交完整报错.md:164` | time-sensitive fact candidate | 修复发布后，使用原步骤和相邻场景复测，并在 Issue 中回报实际版本与结果。若问题消失但无法证明是某个修改导致，可以写“在版本 2.8.5 中连续验证 50 次未复现，原版本频率约为十次三次，继续观察”，不要把有限观察扩大成绝对结论。 |
| 064 | `chapters/064-怎样向-ai-或开发者提交完整报错.md:166` | time-sensitive fact candidate | 一条信息只有“登录坏了，重启也没用”，接收者不知道平台、版本、范围和错误。整理后可以写成以下事实。Windows 11 的 Chrome 生产网页从 14 时 05 分起，三个测试账号均在提交登录后收到 502，首页正常；应用版本 `web-2.8.4`，部署提交 `abc1234`；Network 显示 `POST /api/login` 等待十秒后 50… |
| 066 | `chapters/066-防火墙-数据库暴露-输入验证和文件上传.md:15` | time-sensitive fact candidate | 云平台安全组、供应商防火墙、Ubuntu UFW 和应用监听地址可能同时生效。外层拒绝会让流量根本到不了主机，主机防火墙拒绝会让应用日志为空，应用只监听 `127.0.0.1` 则外部即使到达主机也无法直连。排错时要辨认每层，不能一遇到超时就关闭所有防火墙。 |
| 066 | `chapters/066-防火墙-数据库暴露-输入验证和文件上传.md:54` | time-sensitive fact candidate | PostgreSQL 的 `listen_addresses` 决定服务器在哪些网络接口监听，`pg_hba.conf` 根据连接类型、数据库、用户与来源选择认证规则。应用和数据库在同一主机时，可以考虑只监听本机；在私有网络不同主机时，只允许应用子网或准确来源。具体设置要符合部署结构，不能机械复制 `0.0.0.0/0`。 |
| 066 | `chapters/066-防火墙-数据库暴露-输入验证和文件上传.md:130` | time-sensitive fact candidate | 若解码失败、像素过大、扫描超时或用户超额，上传保持隔离并返回安全错误编号。日志记录用户内部编号、文件大小、检测类型、结果和请求编号，不记录图片内容或签名链接。删除头像时同时删除当前对象和可控派生文件，备份按公开的数据保留政策到期清除。 |
| 066 | `chapters/066-防火墙-数据库暴露-输入验证和文件上传.md:138` | time-sensitive fact candidate | 防火墙启用、数据库规则变更、对象存储权限和删除隔离文件都会改变外部状态。执行前由维护者确认当前会话、恢复通道、准确地址、备份与验证步骤。AI 给出的 `0.0.0.0/0`、`chmod 777`、关闭 TLS 或关闭验证建议，应视为高风险信号并停止。 |
| 067 | `chapters/067-备份-恢复测试-监控-费用和安全下线.md:1` | time-sensitive fact candidate | # 备份、恢复测试、监控、费用和安全下线 |
| 067 | `chapters/067-备份-恢复测试-监控-费用和安全下线.md:3` | time-sensitive fact candidate | 一个项目上线后，需要回答三个容易被推迟的问题。数据丢失时能恢复到哪里，服务变坏时谁会先知道，项目停止时怎样关闭而不留下费用、域名、密钥和用户数据。备份、监控、费用与下线分别处理数据、运行、支出和终止，最终都在管理长期责任。 |
| 067 | `chapters/067-备份-恢复测试-监控-费用和安全下线.md:5` | time-sensitive fact candidate | 备份文件存在不等于能够恢复，监控页面绿色不等于用户核心路径正常，删除服务器也不等于项目已经下线。每项工作都需要明确对象、负责人、触发条件、验证证据和保留期限。本章使用一个小型笔记服务说明完整维护过程，具体命令仍要按真实数据库版本、平台和数据政策核对。 |
| 067 | `chapters/067-备份-恢复测试-监控-费用和安全下线.md:105` | time-sensitive fact candidate | 日志保留要设置总量与期限。systemd、Docker、代理和数据库各自会增长，任何一层无限保留都可能占满磁盘。事故日志可转存到受控位置，普通调试日志按政策到期删除。 |
| 067 | `chapters/067-备份-恢复测试-监控-费用和安全下线.md:107` | time-sensitive fact candidate | ## 费用监控从资源清单开始 |
| 067 | `chapters/067-备份-恢复测试-监控-费用和安全下线.md:109` | time-sensitive fact candidate | 费用不仅来自主服务器，还可能来自对象存储容量与请求、数据库、出站流量、日志、备份、域名、证书服务、CI 分钟、邮件、推送和商店账号。免费额度与价格会变化，所有数字应使用官方资料并注明检索日期。本书不把任何免费方案写成永久承诺。 |
| 067 | `chapters/067-备份-恢复测试-监控-费用和安全下线.md:111` | time-sensitive fact candidate | 建立资源清单，记录供应商、项目、区域、计费单位、负责人、付款方式、预算、续费时间和删除条件。设置平台预算告警只是提醒，通常不会自动阻止消费。异常费用出现时先找增长资源和时间，再判断流量、循环任务、日志爆炸、攻击或遗留测试环境，不能直接删除未知卷与数据库。 |
| 067 | `chapters/067-备份-恢复测试-监控-费用和安全下线.md:117` | time-sensitive fact candidate | 给用户合理导出期，并用可读格式说明内容、校验与导入限制。最终备份完成后进行恢复抽查，记录快照与保留到期。若承诺删除，应覆盖生产、缓存、搜索索引、派生图片和备份生命周期。无法立即从不可变备份删除时，要在政策中真实说明隔离与到期时间。 |
| 067 | `chapters/067-备份-恢复测试-监控-费用和安全下线.md:129` | time-sensitive fact candidate | 从外部网络确认域名与 API 按预期关闭或显示终止页面，从云平台确认计算、数据库、卷和对象状态，从账单页面确认不再产生新的可变费用，从身份系统确认成员、密钥和令牌已撤销。保留最终资源清单、导出校验、删除回执、账单截图的脱敏版本和仍需等待到期的项目。 |
| 067 | `chapters/067-备份-恢复测试-监控-费用和安全下线.md:131` | time-sensitive fact candidate | 下线后的一个或两个账单周期继续检查费用，防止快照、静态 IP、日志或域名遗留。监控与通知最后关闭，因为它们要覆盖下线过程。恢复材料按政策保留到期后，由授权人员删除并记录；如果项目可能重启，仍要明确哪些凭据必须重新生成，不能复用已经撤销的旧秘密。 |
| 067 | `chapters/067-备份-恢复测试-监控-费用和安全下线.md:147` | time-sensitive fact candidate | AI 可以根据资源清单生成备份矩阵、恢复演练步骤、监控项、费用分类和下线顺序，也能检查日志是否缺少退出码与时间。输入使用占位符和资源类别，不提供真实凭据与用户数据。让 AI 对每个动作标明读取、写入、停止服务或永久删除。 |
| 067 | `chapters/067-备份-恢复测试-监控-费用和安全下线.md:159` | time-sensitive fact candidate | - 费用清单包含资源、续费、预算与删除条件 |
| 067 | `chapters/067-备份-恢复测试-监控-费用和安全下线.md:164` | time-sensitive fact candidate | 备份解决可恢复性，监控缩短未知故障时间，费用清单防止资源失控，下线流程结束长期责任。它们共同要求同一种纪律，用真实恢复、外部检查和平台回执证明结果，而不是把“已经设置”写成“已经可靠”。 |
| 068 | `chapters/068-每周-每月和每季度维护清单.md:46` | time-sensitive fact candidate | 检查费用账单与资源清单，找出突然增长、闲置测试环境、未关联卷、静态 IP、旧快照和日志存储。任何删除先确认资源 ID、负责人、恢复价值和账单关系。Docker prune 会删除未使用对象，不能作为“每月自动清理全部”的命令；生产镜像可能是回滚材料。 |
| 068 | `chapters/068-每周-每月和每季度维护清单.md:52` | time-sensitive fact candidate | 域名、证书、支付方式、云额度、开发者账号与商店材料要查看未来九十天到期项。自动续费不能只看开关，还要确认付款方式、恢复邮箱、多因素认证和负责人仍可用。平台价格、免费额度与政策属于高变化信息，以当月官方页面为准并记录检索日期。 |
| 068 | `chapters/068-每周-每月和每季度维护清单.md:56` | time-sensitive fact candidate | - 容量和费用按最近三个月趋势比较，异常资源已归属 |
| 068 | `chapters/068-每周-每月和每季度维护清单.md:77` | time-sensitive fact candidate | 季度还要评估是否继续运行所有功能。无用户的测试环境、已替代 API、旧移动版本和无人维护的域名会增加费用与攻击面。能关闭的先制定迁移和下线计划，不能关闭的明确负责人、用户、恢复和更新责任。下线预案每季度核对一次，事故发生时才不会边找账号边决定数据去向。 |
| 068 | `chapters/068-每周-每月和每季度维护清单.md:88` | time-sensitive fact candidate | - 资源、费用、用户和维护能力支持继续运行决定 |
| 068 | `chapters/068-每周-每月和每季度维护清单.md:93` | time-sensitive fact candidate | 秘密泄露、正在利用的高风险漏洞、证书即将到期、备份连续失败、磁盘快速增长、异常费用、管理员离职、域名转移和商店政策截止，都应立即触发专项检查。日历频率是最低保养，不是延迟紧急响应的理由。告警应直接关联操作说明与负责人。 |
| 068 | `chapters/068-每周-每月和每季度维护清单.md:103` | time-sensitive fact candidate | “检查商店发布”应记录当前公开版本、测试构建、崩溃趋势、待处理反馈、证书与账号状态。截至 2026 年 8 月 6 日，App Store Connect 上传状态仍应按 Apple 官方参考核对，界面和政策封版前复查。Android 与 iOS 的检查分开，因为签名、后台和失败证据不同。 |
| 068 | `chapters/068-每周-每月和每季度维护清单.md:145` | time-sensitive fact candidate | - 资产表覆盖代码、域名、运行、数据、商店、监控和费用 |
| 068 | `chapters/068-每周-每月和每季度维护清单.md:148` | time-sensitive fact candidate | - 月检关注容量、费用、更新、账号和到期项 |
| 069 | `chapters/069-让-ai-先理解项目结构.md:107` | time-sensitive fact candidate | 定时任务还可能产生费用和外部副作用。确认它使用哪个时区、如何防止重复运行、错过一次后是否补跑。多个实例都启动同一 scheduler 时，锁或平台调度必须避免重复。找不到机制就列为风险，不直接在生产启动第二份 worker。 |
| 069 | `chapters/069-让-ai-先理解项目结构.md:115` | time-sensitive fact candidate | 不要为了“确认命令”立即触发远端工作流。先静态阅读，确实需要运行时获得仓库权限和费用授权。自托管 runner 可能接触生产网络，理解阶段不执行未知工作流。 |
| 069 | `chapters/069-让-ai-先理解项目结构.md:145` | time-sensitive fact candidate | 权威来源也可能过期。生产实际版本与声明不一致时，先记录漂移，不让 AI 直接覆盖任何一边。通过只读状态、部署记录与负责人确认，决定更新文档还是恢复生产。时间敏感事实写最后核对日期。平台界面、商店政策和 AI 产品功能尤其容易变化。源码内部稳定关系与外部政策分开记录，后者在每次操作前刷新。 |
| 070 | `chapters/070-计划-权限-diff-测试和验证证据.md:33` | time-sensitive fact candidate | 读取项目文件通常风险最低，但敏感目录、日志与用户数据仍要排除。写入文件会改变工作区，执行命令可能安装依赖、生成文件、启动服务或访问网络。外部状态包括推送仓库、部署、发邮件、修改 DNS、操作数据库、发布商店和产生费用，需要更明确授权。 |
| 070 | `chapters/070-计划-权限-diff-测试和验证证据.md:43` | time-sensitive fact candidate | GitHub Environments 可以把部署分支、环境秘密与人工审批组合起来。官方资料说明，启用审批时，作业在通过要求前不能访问环境秘密，也可以限制部署分支和防止自审。具体功能与套餐限制可能变化，截至 2026 年 8 月 6 日的规则应在封版前再次核对。 |
| 070 | `chapters/070-计划-权限-diff-测试和验证证据.md:144` | time-sensitive fact candidate | 证据索引记录文件、提交、环境、生成时间、用途和保留期限。哈希可以验证文件未变，不能证明内容正确。关键发布保留与组织政策相称的证据，普通开发日志按较短期限删除。NIST 关于来源与评估记录的建议支持可追溯性，仍需结合隐私与安全规则。项目手册说明证据在哪里、谁能看和何时清理，不把敏感附件散落在多个聊天。 |
| 070 | `chapters/070-计划-权限-diff-测试和验证证据.md:164` | time-sensitive fact candidate | AI 很擅长识别模式，却可能不了解“这个旧字段必须保留两年”“这个按钮需要财务批准”或“这个地区不能启用该服务”。代码所有者和业务负责人应检查权限、数据、费用、用户沟通与政策。高风险变更至少由未实施的人复核。 |
| 070 | `chapters/070-计划-权限-diff-测试和验证证据.md:204` | time-sensitive fact candidate | - 人工评审检查业务、权限、数据、费用和回滚 |
| 071 | `chapters/071-安全地生成配置-部署文档和回滚方案.md:5` | time-sensitive fact candidate | 安全做法是把 AI 输出当成待验证草案。配置从真实软件版本与项目结构生成，秘密在受控环境注入，部署文档逐步说明位置、权限、预期和失败入口，回滚方案在发布前验证关键步骤。任何涉及生产账号、数据迁移、域名、商店和费用的最终动作都保留人工确认。 |
| 071 | `chapters/071-安全地生成配置-部署文档和回滚方案.md:79` | time-sensitive fact candidate | 权限也按步骤分配。构建任务不需要生产数据库，部署任务不需要组织所有者，健康检查不需要删除权限。GitHub Environment 可以限制部署分支、环境秘密和人工批准。具体可用功能与套餐会变化，文档使用“截至 2026 年 8 月 6 日”并链接官方页面。 |
| 071 | `chapters/071-安全地生成配置-部署文档和回滚方案.md:81` | time-sensitive fact candidate | 准备阶段完成备份、配置验证、测试、容量和回滚检查。实施阶段上传产物、运行兼容迁移、切换少量流量或发布预览。观察阶段核对版本、健康、错误率、延迟、核心业务、数据和费用。每阶段有继续与停止条件。 |
| 071 | `chapters/071-安全地生成配置-部署文档和回滚方案.md:111` | time-sensitive fact candidate | AI 草案中的版本、路径、服务名、账号角色和阈值都要有来源。没有来源时使用 `[待确认]`，不要填入常见默认。要求它在文档末尾列出未验证命令、需要真实账号的步骤、仅适用于某平台的内容和时间敏感政策。 |
| 071 | `chapters/071-安全地生成配置-部署文档和回滚方案.md:125` | time-sensitive fact candidate | 计划输出要按创建、原地修改、替换和删除分类。替换数据库、负载均衡或静态 IP 的影响可能远大于改一个标签。AI 解释每项变化与费用，人核对资源 ID、区域、依赖、备份和恢复。plan 可能包含敏感属性，分享前脱敏。 |
| 071 | `chapters/071-安全地生成配置-部署文档和回滚方案.md:159` | time-sensitive fact candidate | 供应商恢复后验证积压任务、重复消息与费用。状态恢复不代表你的应用自动恢复，监控核心用户路径和队列。 |
| 072 | `chapters/072-ai-声称完成以后还要检查什么.md:75` | time-sensitive fact candidate | 删除功能尤其要检查软删除、对象、缓存、搜索、备份和审计。AI 删除了界面入口，不代表数据已按政策删除；AI 执行了数据库删除，也不代表外部文件消失。数据负责人决定保留与恢复责任。 |
| 072 | `chapters/072-ai-声称完成以后还要检查什么.md:89` | time-sensitive fact candidate | ## 检查性能、容量和费用 |
| 072 | `chapters/072-ai-声称完成以后还要检查什么.md:93` | time-sensitive fact candidate | 上传、AI API、对象存储、日志和第三方服务会产生费用。验证限额、超时、重试和预算告警，避免错误循环无限调用。免费额度与价格属于高变化信息，使用官方当前页面并注明检索日期。性能测试写数据量、并发、机器、缓存与时间。单次最快结果没有代表性，生产规模无法模拟时明确限制。发现退化后决定优化、回退或接受，不用“在我电脑上很快”覆盖用户环境。 |
| 072 | `chapters/072-ai-声称完成以后还要检查什么.md:131` | time-sensitive fact candidate | 性能与费用观察： |
| 072 | `chapters/072-ai-声称完成以后还要检查什么.md:150` | time-sensitive fact candidate | - 权限、秘密、依赖、性能、费用和可访问性经过检查 |
| 072 | `chapters/072-ai-声称完成以后还要检查什么.md:180` | time-sensitive fact candidate | 数据库内存替身与生产 PostgreSQL 在事务、类型、锁和 SQL 上可能不同。对象存储替身不会完全复制权限、签名链接和配额。支付与邮件必须使用供应商沙箱，不把真实交易用于自动测试，同时核对沙箱与生产差异。 |
| 072 | `chapters/072-ai-声称完成以后还要检查什么.md:184` | time-sensitive fact candidate | 真实路径验收会创建测试账号、订单、上传、邮件、数据库记录、对象和临时部署。开始前使用明确前缀、负责人和到期，结束后核对删除范围。测试数据若进入分析和备份，清理政策也要说明。删除前确认它们确属测试，不使用模糊通配符。无法安全自动删除时保留清单，由账号持有人逐项处理。清理动作本身可能不可逆，与生产数据同库时需要更谨慎。 |
| 072 | `chapters/072-ai-声称完成以后还要检查什么.md:186` | time-sensitive fact candidate | 测试环境长期保留也会产生费用和攻击面。验证报告列仍运行的实例、数据库、域名和秘密，设置自动到期或月度审查。不要为了让交付“看起来干净”立即删除唯一失败日志和回滚产物。 |
| 073 | `chapters/073-生产环境中的人工确认边界.md:3` | time-sensitive fact candidate | 生产环境是真实用户、真实数据、真实域名、真实费用和真实责任所在的系统。AI 可以准备代码、配置、测试、部署草案和观察清单，也可以在明确授权下执行部分自动化。到了会影响用户、数据、权限、费用或不可逆状态的边界，最终确认必须由能够理解并承担该结果的人作出。 |
| 073 | `chapters/073-生产环境中的人工确认边界.md:9` | time-sensitive fact candidate | *图 73-1　构建、测试和预览可高度自动化；涉及秘密、数据、费用、用户和永久删除时，由对应责任人确认准确版本与窗口，发布后按阈值扩大、停止或回滚。下文提供等价说明。* |
| 073 | `chapters/073-生产环境中的人工确认边界.md:19` | time-sensitive fact candidate | 代码合并通常由代码所有者确认，生产部署由服务负责人确认，数据库迁移与恢复由数据负责人确认，域名和证书由账号持有人确认，费用与合同由预算负责人确认，用户通知与政策由业务或合规负责人确认。一个人可能承担多个角色，责任仍要明确。 |
| 073 | `chapters/073-生产环境中的人工确认边界.md:37` | time-sensitive fact candidate | 审批提示中的命令要翻译成业务后果。`apply migration` 可能锁表和改变数据，`sync --delete` 可能删除远端文件，`terraform apply` 可能创建费用或销毁资源。确认人需要看到计划、准确目标、Diff 与回退，不能只看命令语法。网络访问也要限制。AI 搜索官方文档与向生产 API 发请求都使用网络，但风险完全不同。允许浏… |
| 073 | `chapters/073-生产环境中的人工确认边界.md:41` | time-sensitive fact candidate | 秘密轮换会影响所有使用者。先列应用、CI、备份、监控和人工客户端，创建新版本并小范围验证，再更新其余使用者，最后撤销旧值。批准应覆盖轮换顺序与失败恢复，不只批准“生成新密钥”。GitHub Environments 可以将环境秘密与人工审批结合。官方资料说明，在要求批准时，作业在通过保护规则前不能读取 Environment secrets。截至 2026 … |
| 073 | `chapters/073-生产环境中的人工确认边界.md:67` | time-sensitive fact candidate | ## 费用与配额属于生产确认 |
| 073 | `chapters/073-生产环境中的人工确认边界.md:69` | time-sensitive fact candidate | 创建更大服务器、开启日志、复制数据库、使用 AI API 和跨区域传输都会产生费用。批准前给出供应商、资源、区域、计费单位、预计持续时间、预算告警和删除条件。免费额度与价格随时间变化，使用官方当前信息并标注检索日期。 |
| 073 | `chapters/073-生产环境中的人工确认边界.md:71` | time-sensitive fact candidate | AI 生成基础设施计划后，先查看 dry run 或 plan，确认新增、修改与删除。资源数量异常、区域错误、保留无限或高价规格都要停下。预算告警通常只是通知，不一定自动停止费用。测试资源设置负责人和到期。任务完成后删除要再次核对数据与依赖，不让 AI 根据名称自动批量清理。下一个账单周期继续检查残留快照、卷、IP、日志和域名。 |
| 073 | `chapters/073-生产环境中的人工确认边界.md:73` | time-sensitive fact candidate | 删除数据库、对象、卷、备份、域名、商店应用和 Git 历史可能难以恢复。执行前列出准确资源 ID、内容、最后使用、依赖、备份、恢复测试、保留政策和批准人。不要使用宽泛通配符或从脚本输出动态拼接生产删除目标。 |
| 073 | `chapters/073-生产环境中的人工确认边界.md:105` | time-sensitive fact candidate | 为常见生产动作列执行者、技术审查者、业务批准者、知会对象与回滚负责人。代码部署、数据库迁移、DNS、商店发布、费用扩容和永久删除可以有不同角色。矩阵记录角色，不把每次流程绑死在某个姓名；值班表再映射当前人员。 |
| 073 | `chapters/073-生产环境中的人工确认边界.md:109` | time-sensitive fact candidate | 外部供应商也进入矩阵。托管数据库故障需要谁开工单，域名注册商账号由谁恢复，商店审核由谁回复。AI 可以整理联系人和状态，不能代表公司接受合同、费用或政策变更。 |
| 073 | `chapters/073-生产环境中的人工确认边界.md:119` | time-sensitive fact candidate | 批准评论不能只写“同意”。至少引用变更或部署 ID、目标环境和限制。执行发生在批准窗口之外、产物改变或目标不同，自动化应重新请求。审计用于复盘和交接，不用于制造大量无人阅读的表格。记录也有保留与访问期限。生产日志和用户数据按政策处理，审批元数据可以更久，具体由组织与法规决定。个人项目至少保存版本、日期、平台回执、回滚与费用结果，未来能解释发生过什么。 |
| 073 | `chapters/073-生产环境中的人工确认边界.md:125` | time-sensitive fact candidate | 控制面显示失败，数据面可能仍在运行；控制面显示成功，用户路径也可能失败。分别检查平台动作与外部服务。供应商状态页是线索，自己的监控和日志确认实际影响。无法确定状态时暂停后续依赖动作，保存请求与时间，联系官方支持。不要让 AI 尝试多个非官方绕过或把生产凭据搬到未知工具。恢复后对账资源、费用、队列与版本。 |
| 073 | `chapters/073-生产环境中的人工确认边界.md:133` | time-sensitive fact candidate | 短期观察覆盖启动、错误、延迟、核心路径和资源，通常以分钟或小时计算。长期观察覆盖内存增长、队列积压、费用、用户反馈、备份和低频任务，可能需要数天或一个完整业务周期。发布成功时间应说明观察窗口。 |
| 073 | `chapters/073-生产环境中的人工确认边界.md:147` | time-sensitive fact candidate | 隐私政策、数据跨境、支付、医疗健康、未成年人、内容审核、应用商店披露和备案可能有地区与行业要求。AI 可以整理官方资料和待办，不能给出永久有效的合规结论。记录检索日期，并由有资格的人确认高风险事项。 |
| 073 | `chapters/073-生产环境中的人工确认边界.md:149` | time-sensitive fact candidate | 技术上能收集的数据不等于业务可以收集。发布前核对最小必要、告知、同意、保留、删除与导出。监控和 AI 日志也可能包含个人信息，不能因调试目的自动豁免。政策变化应触发再评估。商店截止、供应商条款与地区规则不等待季度维护时，指定负责人及时处理。无法满足要求时暂停相关功能或地区发布，而不是让 AI生成一段免责声明绕过责任。 |
| 073 | `chapters/073-生产环境中的人工确认边界.md:153` | time-sensitive fact candidate | 定时备份、依赖更新、自动部署、内容处理和 AI agent 会在无人注视时改变状态。首次启用前审查触发频率、账号权限、数据范围、费用上限、失败告警、暂停开关和到期。批准的是明确自动化规则，不是未来所有自我修改。 |
| 073 | `chapters/073-生产环境中的人工确认边界.md:155` | time-sensitive fact candidate | 自动化账号使用最低权限，生产删除、数据库迁移和对外群发保留人工门。允许自动合并低风险依赖时，限定版本范围、必需测试与回滚；重大版本、权限变化和维护者异常转人工。任务连续失败后停止或退避，不能无限重试扩大费用。 |
| 073 | `chapters/073-生产环境中的人工确认边界.md:159` | time-sensitive fact candidate | 关闭任务前确认是否有正在运行的作业、队列、锁和半成品。先停止新触发，等待或安全终止当前作业，再核对数据与外部副作用。直接删除调度器可能留下无人处理的队列。撤销服务账号、令牌、Webhook、runner 和预算，删除资源前保留必要日志与回滚材料。下一个计划周期确认任务没有再次触发，下一个账单周期检查费用。停用记录写替代流程或功能终止，避免其他系统仍依赖它。 |
| 073 | `chapters/073-生产环境中的人工确认边界.md:175` | time-sensitive fact candidate | - 生产清单覆盖域名、数据、存储、消息、商店、监控和费用 |
| 073 | `chapters/073-生产环境中的人工确认边界.md:181` | time-sensitive fact candidate | - DNS、证书、商店、消息和费用分别核对 |
| 074 | `chapters/074-不懂代码时怎样保留最终判断能力.md:27` | time-sensitive fact candidate | 风险可以先分为数据、安全、可用性、费用、隐私、政策与不可逆操作。数据库迁移关心丢失和兼容，防火墙关心公网暴露，自动重试关心重复扣款，日志关心秘密和磁盘，商店提交关心账号、政策与用户版本。分类后就知道需要谁确认。 |
| 074 | `chapters/074-不懂代码时怎样保留最终判断能力.md:43` | time-sensitive fact candidate | 比较至少包含实现成本、维护成本、故障责任、平台依赖、数据迁移、费用与退出方式。最低初始价格不一定最低长期成本，技术最先进也不一定最适合非专业维护者。把方案写成并排表格，要求 AI 说明适用前提和不适用情况。 |
| 074 | `chapters/074-不懂代码时怎样保留最终判断能力.md:45` | time-sensitive fact candidate | 选择后记录为什么。半年后价格、用户量或能力变化，可以重新评估。没有记录时，团队只看到“用了 Docker”“选了 Firebase”，却不知道当时为了部署一致或减少自建责任，容易在错误条件下继续沿用。 |
| 074 | `chapters/074-不懂代码时怎样保留最终判断能力.md:77` | time-sensitive fact candidate | 软件版本、平台界面、价格、免费额度、商店政策、备案和安全配置会变化。AI 记忆中的答案可能过期。要求使用官方当前资料，记录检索日期、适用版本和链接。社区案例用于理解真实故障，最终规则回到官方来源。 |
| 074 | `chapters/074-不懂代码时怎样保留最终判断能力.md:79` | time-sensitive fact candidate | 涉及 Codex、ChatGPT 或 OpenAI API 的事实，应使用 OpenAI 官方资料。`AGENTS.md`、沙箱、审批与代码审查的产品行为都可能更新，本章依据截至 2026 年 8 月 6 日的官方页面。封版和实际操作前再次核对。 |
| 074 | `chapters/074-不懂代码时怎样保留最终判断能力.md:83` | time-sensitive fact candidate | 域名、云平台、数据库、GitHub 组织、商店和支付都需要真实账号。记录谁拥有、谁可恢复、如何多因素认证、付款方式与交接。凭据放受控密码或秘密系统，不放 AI 对话和项目文档。AI 可以导航和准备表单，最终提交由持有人核对账号、项目、地区、版本与费用。无法进入平台时，写“等待账号持有人确认”，不让 AI 模拟完成。外部状态需要平台回执和实际访问。 |
| 074 | `chapters/074-不懂代码时怎样保留最终判断能力.md:89` | time-sensitive fact candidate | 手册面向不会天天读代码的所有者，内容包括系统地图、生产资源、用户数据、域名、部署入口、备份恢复、监控、费用、账号持有人、应急停止和下线。它不复制秘密，只写安全存储和恢复责任。每个核心功能用一页说明输入、输出、数据位置、外部副作用、正常证据和故障入口。新增服务与平台时更新，删除后同步移除。OpenAI 的 `AGENTS.md` 适合保存给 Codex 的项目… |
| 074 | `chapters/074-不懂代码时怎样保留最终判断能力.md:95` | time-sensitive fact candidate | AI 可以列选项和初稿，人确认真实约束。不要把 AI 推荐当成独立证据，尤其是涉及花钱、政策和长期维护的选择。引用官方价格与限制，记录检索日期。决定以后，新信息可以修改记录，不必证明过去“永远正确”。重要的是让未来维护者知道当时条件，并在条件变化时重新选择，而不是被既有工具锁住。 |
| 074 | `chapters/074-不懂代码时怎样保留最终判断能力.md:101` | time-sensitive fact candidate | 第四种是给出一长串工具与命令，却不说明运行位置、预期和失败入口。第五种是界面或价格没有检索日期。第六种是 AI 同时实施、评审、批准生产并宣告成功，没有独立证据。遇到这些信号，停止并要求重写。 |
| 074 | `chapters/074-不懂代码时怎样保留最终判断能力.md:149` | time-sensitive fact candidate | 采用托管平台、BaaS、AI API、商店和专有工具时，问数据怎样导出、域名能否迁移、身份与权限怎样替换、离开后哪些功能消失、费用停止需要删除什么。考虑退出是为了避免未来完全没有选择，并不意味着现在就要离开。 |
| 074 | `chapters/074-不懂代码时怎样保留最终判断能力.md:159` | time-sensitive fact candidate | 个人维护时间、可接受停机、每月费用和最多可丢数据都有限。把这些约束写成数字或范围，例如每月预算、RPO、RTO、支持的平台和能够每周投入的时间。方案超过预算时，减少功能、选择托管或寻求协助，不能靠 AI 承诺“以后自动维护”。 |
| 074 | `chapters/074-不懂代码时怎样保留最终判断能力.md:161` | time-sensitive fact candidate | 风险预算也包括复杂度。一个人能可靠恢复的系统，比拥有十个服务却无人理解更适合长期运行。新增数据库、队列、对象存储和监控前，问它解决的具体问题、增加的月度任务和下线方式。预算不是永久不变。用户、收入与数据敏感性增长后，提高备份、监控和专业支持；项目不再使用时，按安全下线流程减少责任。每季度与费用和维护清单一起复评。 |
| 074 | `chapters/074-不懂代码时怎样保留最终判断能力.md:191` | time-sensitive fact candidate | AI 可以贯穿这些步骤，负责搜索、解释、生成草案、修改、测试和整理证据。你负责目标、凭据、外部账号、真实数据、费用、用户影响、生产批准和最终验收。两者分工清楚后，不懂代码不会变成放弃判断。 |
| 074 | `chapters/074-不懂代码时怎样保留最终判断能力.md:199` | time-sensitive fact candidate | - 能识别数据、安全、费用、隐私、政策和不可逆风险 |
| 074 | `chapters/074-不懂代码时怎样保留最终判断能力.md:202` | time-sensitive fact candidate | - 重要版本、价格和政策回到当前官方资料 |
| 077 | `chapters/077-领域边界-数据所有权与跨模块协作.md:39` | time-sensitive fact candidate | 订单保存购买时的商品名称和价格，通常属于历史快照。商品模块后来改名，旧订单仍要呈现当时交易内容。搜索服务保存商品标题与关键词，属于可重建的派生数据。账号模块的当前登录邮箱是权威身份属性，却不应自动覆盖发票已经确认的抬头。 |
| 077 | `chapters/077-领域边界-数据所有权与跨模块协作.md:47` | time-sensitive fact candidate | 删除请求会进一步检验所有权。账号模块可以撤销登录能力，订单模块可能仍需按法律和业务要求保存交易记录，分析与搜索副本则应按规则清理或去标识。删除不能由一个 `DELETE FROM users` 代替。每个责任模块要说明保留依据、删除动作、传播方式和验证结果。具体期限属于法律与业务政策，本书不替项目作统一决定。 |
| 080 | `chapters/080-微服务真正增加了哪些工程责任.md:43` | time-sensitive fact candidate | 补偿不等于时间倒流。退款可能产生费用，邮件无法从收件箱撤回，外部系统也可能已经读取事件。产品要定义可接受的后续动作，界面要向用户展示处理中、已失败或待人工确认。技术实现只能执行规则，不能自行决定商业后果。 |
| 081 | `chapters/081-架构异味与-ai-生成项目的复杂度增长.md:63` | time-sensitive fact candidate | 全局变量、单例缓存和自动注册机制能减少参数传递，也会隐藏代码实际依赖。一个看似只计算价格的函数顺手读取当前用户、修改缓存并发送分析事件，测试结果会受调用顺序影响。并行请求还可能互相覆盖状态。 |
| 081 | `chapters/081-架构异味与-ai-生成项目的复杂度增长.md:69` | time-sensitive fact candidate | 受控验证可以固定时间、随机数和外部适配器，重复运行同一测试。结果随顺序变化，说明存在未隔离状态。让邮件适配器返回错误，确认价格计算仍不受影响，则能说明两个责任在当前路径已被分开。测试只覆盖指定入口，不能据此断言全项目没有隐藏状态。 |
| 082 | `chapters/082-复杂度预算与什么时候不要增加新组件.md:7` | time-sensitive fact candidate | **新组件的收益应由当前证据支持，它的故障、升级、费用和退出方式也要有人承担。** |
| 082 | `chapters/082-复杂度预算与什么时候不要增加新组件.md:21` | time-sensitive fact candidate | 运维复杂度来自安装、升级、备份、监控、告警和恢复。一条 Docker 命令只能启动自建 Redis，长期运行还要考虑数据是否需要持久化、内存满了怎样淘汰、重启后影响什么、谁更新安全版本。托管服务减少一部分操作，仍有费用、配额、地区、权限和供应商变化。 |
| 082 | `chapters/082-复杂度预算与什么时候不要增加新组件.md:27` | time-sensitive fact candidate | 这五项不会等量出现。一个纯开发依赖可能几乎没有生产运行成本，却增加供应链更新。一个托管数据库代码接入简单，数据迁移和费用风险较高。预算的作用是强迫决策者把被宣传页面隐藏的成本重新列出来。 |
| 082 | `chapters/082-复杂度预算与什么时候不要增加新组件.md:43` | time-sensitive fact candidate | 比较方案时，至少保留“不改变架构，只修当前实现”这一项。它提供基线，防止讨论只在几个新工具之间进行。每个候选方案记录直接收益、引入内容、失败表现、数据影响、权限、月度费用、验证办法和退出步骤。 |
| 082 | `chapters/082-复杂度预算与什么时候不要增加新组件.md:105` | time-sensitive fact candidate | 要求 AI 推荐组件时，不只要安装命令。让它列出当前问题与证据、至少一个不增加组件的方案、预期收益、运行单元、数据身份、Secret、监控、失败表现、费用风险、迁移步骤和删除办法。事实不确定的项目用“待验证”标出，不允许用流行度补空白。 |
| 083 | `chapters/083-用-adr-保存选择-代价与重新评估条件.md:73` | time-sensitive fact candidate | 背景中的事实要标注来源和日期。平台价格、免费额度、商店政策与合规要求会变化，应链接官方页面并写检索日期。推测与已验证事实分开。预计明年有十万用户属于预测，当前峰值每分钟一百请求属于测量，两者不能混成同等依据。 |
| 083 | `chapters/083-用-adr-保存选择-代价与重新评估条件.md:79` | time-sensitive fact candidate | 商业合同、未公开费用和内部人员信息也可能不适合进入公共仓库。项目可以保留一份不含敏感值的 ADR，并链接到权限受控的补充记录。链接要说明访问责任和保留期限，不能用一句“详见内部文档”把全部依据移走。后来维护者至少应从仓库内记录理解决定边界、验证方式与重新评估条件。 |
| 083 | `chapters/083-用-adr-保存选择-代价与重新评估条件.md:83` | time-sensitive fact candidate | ADR 不要求写一篇长报告，至少应列出真正考虑过的可行方案，包括维持现状。每个方案使用相同维度比较，例如开发时间、运行责任、数据风险、费用、性能、可逆性和维护者熟悉程度。 |
| 083 | `chapters/083-用-adr-保存选择-代价与重新评估条件.md:93` | time-sensitive fact candidate | 决定带来的正面结果通常容易写，新增责任更容易遗漏。选择对象存储可以减少应用服务器磁盘管理，也要处理上传权限、失效链接、跨域设置、费用和数据迁移。选择托管身份服务可以缩短登录开发，同时增加供应商可用性与账号策略依赖。 |
| 083 | `chapters/083-用-adr-保存选择-代价与重新评估条件.md:131` | time-sensitive fact candidate | 若 AI 提议新数据库、队列、身份方式或模块边界，要求它起草候选 ADR。草稿要分开项目事实、外部资料和假设，列出维持现状，写明失败、费用、迁移与退出。人核对证据和产品后果以后才能接受。 |
| 083 | `chapters/083-用-adr-保存选择-代价与重新评估条件.md:139` | time-sensitive fact candidate | 选择项目中一个尚未定案的真实问题，例如文件放本地磁盘还是对象存储。先写当前规模、部署方式、备份要求与费用限制，再列出维持现状、托管对象存储和自建存储三项方案。没有数据时先标假设，不急着宣布答案。 |
| 083 | `chapters/083-用-adr-保存选择-代价与重新评估条件.md:141` | time-sensitive fact candidate | 挑选一个最小试验，上传文件、读取、删除，并模拟凭据失效。记录预期和实际结果。成功上传只能证明当前环境的基本路径，凭据失效时应用返回明确错误，可以证明这条权限失败得到处理。恢复、费用上限和批量迁移仍要另行验证。 |
| 084 | `chapters/084-怎样让两个工程方案真正对打.md:29` | time-sensitive fact candidate | 偏好允许权衡。本地开发更简单、费用更低、延迟更短、供应商依赖更少、团队更熟悉，都可能增加方案吸引力，却未必单独决定结果。把偏好伪装成硬约束，会让比较在开始前就结束。 |
| 084 | `chapters/084-怎样让两个工程方案真正对打.md:39` | time-sensitive fact candidate | 约束之间冲突时要明确优先顺序。极低费用、零运维、完全可控和无限扩展很难同时获得。个人项目可以先保护数据与恢复能力，再比较开发时间和费用。支付或医疗系统会有不同顺序，不能从一张通用评分表抄答案。 |
| 084 | `chapters/084-怎样让两个工程方案真正对打.md:88` | time-sensitive fact candidate | 估算应写范围和口径。每月消息量、请求次数、数据保留、出口流量和日志量都会影响费用。价格容易变化，正式决定前重新查看官方页面并写检索日期。不要把免费额度写进永久架构假设。 |
| 084 | `chapters/084-怎样让两个工程方案真正对打.md:96` | time-sensitive fact candidate | 评分表适合让结果并排出现，不适合制造数学权威。给数据安全五分、开发速度三分、费用两分，再算加权总分，权重稍微调整就可能换冠军。分数来自判断时，应保留原始观察和理由。 |
| 084 | `chapters/084-怎样让两个工程方案真正对打.md:104` | time-sensitive fact candidate | \| 当前月度费用 \| 使用现有数据库资源 \| 依据请求、保留和网络计费 \| 采用前核对官方价格 \| |
| 084 | `chapters/084-怎样让两个工程方案真正对打.md:113` | time-sensitive fact candidate | 支持方案的人通常最了解它，也最容易忽略熟悉带来的偏好。让每一方先列出自己方案最可能失败的三种方式，再提出验证。数据库方案要面对共享数据库过载、锁竞争和清理失控。队列方案要面对权限错误、重复消息、平台中断和费用变化。 |
| 084 | `chapters/084-怎样让两个工程方案真正对打.md:123` | time-sensitive fact candidate | 概念验证能测当前延迟和恢复过程，无法完整预测三年维护成本、供应商政策和团队变化。有些风险只能通过合同、官方承诺、真实运行和时间观察。把它们标为残余不确定性，并决定是否可以接受。 |
| 084 | `chapters/084-怎样让两个工程方案真正对打.md:135` | time-sensitive fact candidate | 决定实施后继续观察之前定义的指标。任务积压、最老任务年龄、重复发送、数据库负载和月度费用出现变化时，回到 ADR 的重新评估条件。方案比较完成以后，项目得到一项有条件、可复查的选择。某项技术是否赢得争论没有实际意义。 |
| 084 | `chapters/084-怎样让两个工程方案真正对打.md:146` | time-sensitive fact candidate | - 功能正确性、恢复、交付、费用和退出证据。 |
| 085 | `chapters/085-rest-graphql-polling-sse-与-websocket.md:119` | time-sensitive fact candidate | 手机 App 进入后台后，长期连接可能暂停或断开。需要系统级通知时，应评估 Apple Push Notification service 或 Firebase Cloud Messaging 等推送体系，不能期待网页 SSE 或 WebSocket 在后台长期保持。商店和系统政策会变化，具体流程需查当前官方资料。 |
| 086 | `chapters/086-sqlite-postgresql-sql-与文档数据库.md:19` | time-sensitive fact candidate | PostgreSQL 是一个独立运行的开源关系数据库服务。应用通过本地套接字或网络连接，数据库管理多个用户、连接和事务。它支持丰富 SQL、约束、索引、JSON、全文搜索与扩展。截至 2026 年 8 月 11 日，官方 current 文档指向 PostgreSQL 18。项目仍应以实际部署的小版本测试。 |
| 086 | `chapters/086-sqlite-postgresql-sql-与文档数据库.md:37` | time-sensitive fact candidate | Serverless 与边缘函数还要检查连接模型。大量短生命周期函数各自创建 PostgreSQL 连接，可能耗尽数据库连接数。平台连接池或数据库代理可以缓解，配置与费用也随之增加。SQLite 若运行在短暂文件系统中，实例销毁后本地数据可能消失。产品名字不变，部署平台会改变结论。 |
| 086 | `chapters/086-sqlite-postgresql-sql-与文档数据库.md:109` | time-sensitive fact candidate | PostgreSQL 提供 SQL dump、文件系统级备份和连续归档等路线。选择取决于数据量、恢复时间和恢复点要求。托管平台的自动备份需要核对保留时间、恢复粒度、地区与费用，不能把控制台显示“已备份”当成恢复完成。 |
| 086 | `chapters/086-sqlite-postgresql-sql-与文档数据库.md:115` | time-sensitive fact candidate | 恢复目标会反过来影响选型。只能接受一天数据丢失与必须恢复到几分钟前，需要的日志、归档、费用和操作完全不同。先写恢复点目标与恢复时间目标，再确认产品和维护能力能否做到。 |
| 087 | `chapters/087-baas-自建后端-托管平台-vps-与-serverless.md:25` | time-sensitive fact candidate | Serverless 通常指开发者按函数或请求模型运行代码，平台管理实例和扩缩。函数可能按请求、事件或计划任务触发。Vercel Functions 按调用运行，并由平台处理实例生命周期与扩展。项目仍要关心运行区域、数据库连接、执行限制、日志和费用。 |
| 087 | `chapters/087-baas-自建后端-托管平台-vps-与-serverless.md:39` | time-sensitive fact candidate | BaaS 还承担部分备份、扩展和可用性，但责任范围取决于产品与计划。保留时间、恢复粒度、地区、导出和费用都要查当前官方文档。控制台里存在备份选项，不代表项目已经完成恢复演练。 |
| 087 | `chapters/087-baas-自建后端-托管平台-vps-与-serverless.md:75` | time-sensitive fact candidate | 长任务要确认平台模型。视频转码、批量导入和持续爬取可能超过函数时限，或产生高额资源费用。可以把请求变成任务，交给专用 Worker、队列或容器服务。函数负责接收和查询状态，长任务在适合的运行环境执行。 |
| 087 | `chapters/087-baas-自建后端-托管平台-vps-与-serverless.md:91` | time-sensitive fact candidate | 一个常见网页可以部署在 Vercel，后端接口使用 Vercel Functions，数据和身份放在 Supabase。这里同时使用托管前端、Serverless 和 BaaS。项目要知道函数区域、数据库权限、两边日志和费用。 |
| 087 | `chapters/087-baas-自建后端-托管平台-vps-与-serverless.md:111` | time-sensitive fact candidate | 第五问是费用随什么增长。函数按调用与资源，BaaS 按数据库、存储、带宽或用户，托管服务按实例，VPS 按规格和流量。价格与免费额度变化快，应在 2026 年实际购买时重新查看官方页面。 |
| 087 | `chapters/087-baas-自建后端-托管平台-vps-与-serverless.md:119` | time-sensitive fact candidate | 小型会员 App 需要登录、用户资料、头像和少量实时状态，维护者只有一人。BaaS 可以缩短身份、数据库与存储接入。上线前要重点测试数据规则、管理员操作、导出和费用上限。 |
| 087 | `chapters/087-baas-自建后端-托管平台-vps-与-serverless.md:153` | time-sensitive fact candidate | 随后分别给出 BaaS、托管应用、Serverless 和 VPS 方案。每套方案都要覆盖权限、部署、备份、恢复、费用与退出，不能只比较首次上线步骤。要求保留一个组合方案，因为现实系统经常混合使用。 |
| 087 | `chapters/087-baas-自建后端-托管平台-vps-与-serverless.md:157` | time-sensitive fact candidate | 最终选择写进 ADR。记录当前规模、维护能力、数据地区、工作负载、平台责任、接受的限制和重新评估条件。平台功能、价格和计划会变化，封版与实际采用前重新核对官方资料。 |
| 088 | `chapters/088-直接进程-docker-compose-与-kubernetes.md:26` | time-sensitive fact candidate | python -m uvicorn app:app --host 127.0.0.1 --port 8000 |
| 088 | `chapters/088-直接进程-docker-compose-与-kubernetes.md:52` | time-sensitive fact candidate | ExecStart=/srv/course-api/.venv/bin/python -m uvicorn app:app --host 127.0.0.1 --port 8000 |
| 089 | `chapters/089-局部故障-超时-重试放大与退避.md:99` | time-sensitive fact candidate | 单次尝试上限      1.2 秒 |
| 090 | `chapters/090-背压-负载丢弃-隔离与队列语义.md:47` | time-sensitive fact candidate | 负载丢弃还要避免永远牺牲同一批用户。可以按优先级、租户配额、用户身份和请求成本分配容量。只按“谁先把连接占满”处理，单个脚本或大客户就可能挤走其他用户。策略越复杂，越需要记录被拒绝的原因与数量。 |
| 090 | `chapters/090-背压-负载丢弃-隔离与队列语义.md:55` | time-sensitive fact candidate | 隔离可以发生在多个位置。API 为导出报表设置独立并发上限，数据库给后台任务使用独立连接池，消息代理把邮件与支付事件放入不同队列，Kubernetes 为工作负载设置资源请求与上限，云账号为测试环境设置独立配额。边界应按故障传播方式选择，不能只按代码目录划分。 |
| 090 | `chapters/090-背压-负载丢弃-隔离与队列语义.md:83` | time-sensitive fact candidate | 增加消费者能提升并发，直到数据库、第三方 API、CPU 或磁盘成为新限制。十个 Worker 每个再开二十个并发，实际下游请求可能达到二百。扩容消费者之前，要核对下游配额、连接池和幂等设计。 |
| 091 | `chapters/091-sli-slo-sla-与-error-budget.md:46` | time-sensitive fact candidate | 至少 99.5% 的有效播放操作 |
| 091 | `chapters/091-sli-slo-sla-与-error-budget.md:71` | time-sensitive fact candidate | SLO            99.5% |
| 091 | `chapters/091-sli-slo-sla-与-error-budget.md:72` | time-sensitive fact candidate | 允许坏事件比例  0.5% |
| 091 | `chapters/091-sli-slo-sla-与-error-budget.md:81` | time-sensitive fact candidate | 误差预算必须配套政策。Google SRE 的示例政策会预先约定预算耗尽以后暂停哪些发布、优先处理哪些可靠性工作，以及分歧怎样升级。示例里的比例与组织角色不适合直接复制，个人项目可以写得很短。 |
| 091 | `chapters/091-sli-slo-sla-与-error-budget.md:99` | time-sensitive fact candidate | 这组阈值只是示例。项目应按发布频率、用户规模和故障后果调整。政策的价值来自提前同意行动，事故发生后才争论是否停止发布，数据很难改变各方原有立场。 |
| 091 | `chapters/091-sli-slo-sla-与-error-budget.md:145` | time-sensitive fact candidate | 第五步写一页误差预算政策。规定预算充足、快速消耗、接近耗尽和已经耗尽时分别采取什么行动。个人项目可以把“团队暂停发布”改成“本周不合并非必要大改动”。 |
| 091 | `chapters/091-sli-slo-sla-与-error-budget.md:169` | time-sensitive fact candidate | 误差预算政策由维护者最终确认。预算耗尽后暂停哪些变更、是否允许安全修复、谁能解除限制，都涉及项目风险偏好。AI 可以整理证据，不能替负责人向用户作出服务承诺。 |
| 092 | `chapters/092-日志-指标-追踪与-opentelemetry.md:23` | time-sensitive fact candidate | "time": "2026-08-11T09:42:18.372+08:00", |
| 092 | `chapters/092-日志-指标-追踪与-opentelemetry.md:103` | time-sensitive fact candidate | OpenTelemetry 也不负责存储与展示。项目仍需选择后端，设置保留期限、访问权限、费用上限、仪表盘和告警。Collector 停止或出口拥堵时，还要决定遥测可以丢多少，不能让监控流量拖垮业务请求。 |
| 093 | `chapters/093-性能基线-分位数-剖析-压测与成本.md:7` | time-sensitive fact candidate | 性能工作可以分成五步。先建立可重复基线，再用分布而非单个数字描述体验，通过剖析找到资源花在哪里，用受控负载验证容量与恢复，最后把速度改善和费用、复杂度、正确性一起计算。 |
| 093 | `chapters/093-性能基线-分位数-剖析-压测与成本.md:90` | time-sensitive fact candidate | 禁止对没有授权的第三方和生产服务随意压测。流量可能影响真实用户、触发防护或产生费用。优先使用隔离环境与脱敏数据，生产验证也应有明确窗口、限额、回退条件和负责人。 |
| 093 | `chapters/093-性能基线-分位数-剖析-压测与成本.md:100` | time-sensitive fact candidate | 数据库、队列和第三方 API 常先成为限制。应用增加副本后，数据库连接数成倍上升，吞吐反而下降。每次扩容都要重新核对共享依赖与费用，不能只看应用 CPU。 |
| 093 | `chapters/093-性能基线-分位数-剖析-压测与成本.md:108` | time-sensitive fact candidate | 优化还可能把成本转移。把图片全部预生成，读取变快，存储和构建时间增加。增加数据库索引，查询变快，写入与磁盘成本增加。使用全球 CDN 改善远端延迟，流量费用与缓存一致性会变化。 |
| 093 | `chapters/093-性能基线-分位数-剖析-压测与成本.md:115` | time-sensitive fact candidate | 搜索相关计算、数据库、缓存和网络费用 |
| 093 | `chapters/093-性能基线-分位数-剖析-压测与成本.md:120` | time-sensitive fact candidate | 成本还包括维护时间和复杂度。每月省十元服务器费用，却增加一种数据库、一个值班告警和四小时维护，未必划算。个人项目要把自己的时间放进判断，不能只比较云产品单价。 |
| 093 | `chapters/093-性能基线-分位数-剖析-压测与成本.md:122` | time-sensitive fact candidate | 价格、免费额度和计费维度会变化。书稿只说明计算方法，采用服务时必须按检索日查看官方价格，并用真实账单复核。压测本身也可能产生显著费用，开始前设置预算和停止条件。 |
| 093 | `chapters/093-性能基线-分位数-剖析-压测与成本.md:126` | time-sensitive fact candidate | 课程搜索变慢时，先保存基线。使用固定数据快照和二十种查询，分别测冷缓存与热缓存，在一、十、五十并发下记录成功率、p50、p95、p99、吞吐、CPU、内存、数据库时间与费用估算。 |
| 093 | `chapters/093-性能基线-分位数-剖析-压测与成本.md:136` | time-sensitive fact candidate | 错误率无变化，数据库存储增加 1.8 GB。 |
| 093 | `chapters/093-性能基线-分位数-剖析-压测与成本.md:149` | time-sensitive fact candidate | 性能工作最后要回答用户得到了什么，系统牺牲了什么，结论在哪些条件下成立。跑分只是证据的一部分，发布判断来自速度、正确性、容量、恢复、费用和维护责任的共同结果。 |
| 095 | `chapters/095-独立测试依据与可信的第二意见.md:17` | time-sensitive fact candidate | 一个税费函数返回 12.37，测试若直接复制同一段公式计算预期值，两边会一起犯错。更可靠的依据可以是法规给出的计算规则、人工核对的小样本、另一个经过验证的实现，或金额守恒等不变量。 |
| 095 | `chapters/095-独立测试依据与可信的第二意见.md:75` | time-sensitive fact candidate | 模型独立也不能替代资料独立。两个模型都依靠同一篇过时博客，输出仍然高度相关。时间敏感的平台政策、价格、界面和版本必须回到当前官方来源核对。 |
| 095 | `chapters/095-独立测试依据与可信的第二意见.md:98` | time-sensitive fact candidate | 测试依据要版本化。官方 API 版本、数据库版本、商店政策和业务规则变化后，旧测试可能继续通过却已经不适用。表中保存检索日期和适用版本，定期审查高风险项目。 |
| 096 | `chapters/096-怎样阅读事故复盘并提取可迁移经验.md:44` | time-sensitive fact candidate | 当时各类任务的连接配额 |
| 098 | `chapters/098-沿用户动作阅读测试-历史-issue-与-pr.md:28` | time-sensitive fact candidate | 前置状态  普通用户已登录，配额仍有空间 |
| 099 | `chapters/099-pocketbase-与-supabase-的边界选择.md:5` | time-sensitive fact candidate | 截至 2026 年 8 月 11 日，PocketBase 官方文档显示当前版本仍低于 1.0，并明确提醒完整向后兼容尚无保证，也不建议把它用于关键生产应用，除非使用者愿意持续阅读变更记录并完成必要的手工迁移。这个提示会随项目发展变化，实际选型前应重新核对。 |
| 099 | `chapters/099-pocketbase-与-supabase-的边界选择.md:17` | time-sensitive fact candidate | 第二个选项是使用 Supabase 托管平台。Supabase 以 Postgres 为核心，组合认证、自动接口、实时通信、存储和函数等服务。平台负责大量基础设施工作，用户仍要负责表结构、行级权限、密钥使用、数据生命周期和费用。 |
| 099 | `chapters/099-pocketbase-与-supabase-的边界选择.md:67` | time-sensitive fact candidate | 小型正式应用需要关系数据、登录、文件和稳定托管，团队没有数据库运维人员。托管 Supabase 往往更符合责任能力，但要测试行级权限、备份能力、地区可用性和费用。价格与免费额度会变化，必须按选型日期查询官方页面。 |
| 099 | `chapters/099-pocketbase-与-supabase-的边界选择.md:79` | time-sensitive fact candidate | 最终表格不要只填“支持”或“不支持”。填入谁负责、怎样验证、出错去哪里看、恢复需要多久。这样选型就从功能投票变成责任判断。AI 可以完成样例代码和对比表，账号权限、真实备份、费用与上线责任仍要由项目所有者确认。 |
| 099 | `chapters/099-pocketbase-与-supabase-的边界选择.md:105` | time-sensitive fact candidate | PocketBase 的单机边界使扩容路径更集中，要特别测试长事务、批量导入、备份和写入竞争。Supabase 托管版会替用户处理不少基础设施，但数据库连接、慢查询、索引、行级规则和费用仍会成为应用问题。自建 Supabase 还要管理多项服务的容量与升级。 |
| 099 | `chapters/099-pocketbase-与-supabase-的边界选择.md:113` | time-sensitive fact candidate | 选型记录中注明检索日期、官方价格与政策链接、支持渠道和重新评审条件。费用超过预算、数据量增长、需要多地区或兼容性承诺改变，都可以触发重新选择。 |
| 101 | `chapters/101-怎样正确使用技术社区中的争议与经验.md:19` | time-sensitive fact candidate | 普通论坛、Reddit、X 长帖和个人博客的上下文更分散。作者可能没有写版本，也可能只展示成功截图。它们适合发现关键词、特殊硬件、地区限制和用户感受。涉及安全、删除、费用、政策和数据恢复时，仍要查官方资料并自己验证。 |
| 102 | `chapters/102-repository-health-review-与长期清理.md:96` | time-sensitive fact candidate | 季度完整检查可以固定十项。生产版本可追溯，主分支检查有效，关键路径有责任人，安全报告入口可用，依赖风险已分类，备份恢复有近期证据，数据删除有批准边界，文档从空环境可执行，费用与账号有人负责，废弃资产已有处置日期。 |
| 104 | `chapters/104-把工程判断变成可持续的项目治理.md:3` | time-sensitive fact candidate | 一个人借助 AI 做出网页或 App，第一次上线只是工程工作的开始。域名要续费，依赖会更新，证书和密钥会轮换，平台政策会变，数据要备份，事故要有人处理。项目治理就是把谁能决定、什么证据足够、何时停止发布和怎样退出写成长期可执行的规则。 |
| 104 | `chapters/104-把工程判断变成可持续的项目治理.md:11` | time-sensitive fact candidate | 图中每项变化都经过分类、决定、实施、验证和发布，运行证据再进入维护。事故、成本、政策和人员变化会触发重新评审，项目也保留安全下线的出口。 |
| 104 | `chapters/104-把工程判断变成可持续的项目治理.md:21` | time-sensitive fact candidate | 文字和样式的小改动通常可以走轻量流程。认证、权限、付款、数据迁移、上传、安全配置和删除功能需要更严格门槛。平台切换、数据库升级和应用商店发布还涉及外部政策与恢复窗口。 |
| 104 | `chapters/104-把工程判断变成可持续的项目治理.md:42` | time-sensitive fact candidate | 维护节奏可以分成每周、每月和每季度。每周看可用性、错误、备份任务和异常费用。每月看依赖、安全告警、证书与域名、失败任务和恢复样本。每季度做一次完整恢复演练、权限复核、仓库健康检查和下线资产清点。 |
| 104 | `chapters/104-把工程判断变成可持续的项目治理.md:50` | time-sensitive fact candidate | 重要选择使用短 ADR。记录当时问题、可选方案、决定、后果、复查触发条件和相关提交。触发条件可以是用户量超过阈值、费用变化、平台停止某能力、恢复时间不达标或维护者离开。 |
| 104 | `chapters/104-把工程判断变成可持续的项目治理.md:56` | time-sensitive fact candidate | 记录域名注册商、DNS、托管平台、邮件、对象存储、数据库、分析、AI 接口和应用商店账号。每项写所有者、账单方式、免费额度检索日期、数据出口、替代方案和停用步骤。 |
| 104 | `chapters/104-把工程判断变成可持续的项目治理.md:58` | time-sensitive fact candidate | 价格、免费额度和平台政策会变化。预算不能只写当前月费，还要设置提醒与上限，检查流量增长、日志保留、出站流量和后台任务带来的费用。收到费用告警时，先限制非关键消耗，不能仓促删除数据。 |
| 104 | `chapters/104-把工程判断变成可持续的项目治理.md:76` | time-sensitive fact candidate | 项目可能因为费用、人员、法律要求或需求消失而结束。安全下线包括通知用户、提供数据导出、停止写入、撤销令牌、关闭公开入口、保留必要记录、删除不再需要的数据和终止账单。 |
| 104 | `chapters/104-把工程判断变成可持续的项目治理.md:80` | time-sensitive fact candidate | 仓库可以归档，文档要标明最后支持版本和安全状态。域名若不再保留，旧链接和回调可能被他人接管，需提前解除 OAuth、邮件和应用配置。 |
| 104 | `chapters/104-把工程判断变成可持续的项目治理.md:82` | time-sensitive fact candidate | 先完成五件事。记录生产提交和部署位置，确认备份能恢复，列出账号和费用所有者，为高风险改动写发布门槛，安排下次维护日期。随后每遇到一次真实问题，只增加一条确实能防止或缩小后果的规则。 |
| 104 | `chapters/104-把工程判断变成可持续的项目治理.md:110` | time-sensitive fact candidate | 检查项目还有哪些用户、产生什么价值、每年花费多少时间与费用、持有哪些数据和承诺。若维护成本已经超过价值，可以缩减功能、迁移到托管服务、只读归档或安全下线。 |
| 104 | `chapters/104-把工程判断变成可持续的项目治理.md:112` | time-sensitive fact candidate | 继续运营也要重新确认技术选择。原平台价格、地区、兼容性和维护者状态可能变化。重新评审不要求每年迁移，它防止团队因为已经投入很多而永久保留不合适方案。 |
| 104 | `chapters/104-把工程判断变成可持续的项目治理.md:114` | time-sensitive fact candidate | 把决定与下一次触发条件写进 ADR。用户量、费用、恢复结果或人员变化达到条件时提前复查，不必等到年度日期。 |

## Invalid chapter references

- None

## Repository and release baseline

- Canonical Markdown and build scripts were absent from the v2.2.0 branch before this recovery.
- Existing top-level v2.2.0 EPUB, TXT, DOCX, AZW3, FB2, HTMLZ, KEPUB and MOBI remain immutable inputs/artifacts.
- README and START-HERE positioning changes are deferred until the recovered baseline and pilot chapters are accepted.
- PDF page count/bookmarks and Release attachment correspondence remain deferred release checks.
