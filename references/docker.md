# Docker 与 Compose 操作参考

这份参考保存容器操作、Dockerfile、Compose、日志和排错清单。主章负责解释镜像、容器、宿主机与编排的关系。镜像标签、CLI 输出和平台限制会变化，执行时以当前 Docker 文档和项目文件为准。

## 容器身份卡

```text
服务用途：
源码提交：
镜像仓库 / 名称 / 摘要：
Dockerfile 路径：
构建上下文：
容器名：
端口：宿主 -> 容器
卷：宿主或命名卷 -> 容器
网络：
运行用户：
环境变量来源（不写秘密）：
健康检查：
重启策略：
数据备份：
```

镜像是只读模板，容器是一次运行实例，Registry 保存与分发镜像。删除容器通常不会删除镜像；删除容器内未挂载的数据却可能永久丢失。先画出代码、配置、秘密、数据库和上传文件分别在哪里。

## 最小观察命令

```bash
docker version
docker ps
docker ps -a
docker images
docker inspect CONTAINER
docker logs --tail 100 CONTAINER
docker stats --no-stream
```

`ps` 只说明进程状态，不说明业务可用。继续验证容器内监听、宿主端口映射、代理、健康接口和真实业务流程。日志可能包含个人数据或令牌，分享前缩小时间范围并脱敏。

## 构建与运行练习

```bash
docker build -t example-app:local .
docker run --rm -p 127.0.0.1:8080:8080 example-app:local
```

构建上下文的点决定哪些文件会发送给构建器；用 `.dockerignore` 排除 Git 历史、依赖缓存、秘密、本地数据库和无关产物。运行前阅读 Dockerfile 的基础镜像、下载、脚本、用户、入口命令和暴露端口。

生产部署不要只依赖可移动标签。记录镜像摘要、源码提交、构建系统和依赖锁文件。重新构建同名标签可能得到不同内容。

## Dockerfile 最小结构

```dockerfile
FROM runtime-image:version
WORKDIR /app
COPY dependency-files ./
RUN install-command
COPY . .
USER app
EXPOSE 8080
CMD ["start-command"]
```

这只是结构，不是可直接用于任何语言的模板。固定合适的基础镜像版本，减少层中的秘密和无关工具，使用非 root 用户，确保入口进程接收终止信号。多阶段构建可把编译工具留在构建阶段，但必须实际检查最终镜像内容和漏洞。

## Compose 最小工作流

```bash
docker compose config
docker compose pull
docker compose build
docker compose up -d
docker compose ps
docker compose logs --tail 100
docker compose down
```

先用 `docker compose config` 检查合并结果，输出中若包含秘密不要分享。`up -d` 返回不等于应用就绪；查看健康状态并执行业务验证。`down -v` 会删除命名卷，不能当普通停止命令使用。

示意关系：

```yaml
services:
  app:
    build: .
    ports:
      - "127.0.0.1:8080:8080"
    env_file: .env
    depends_on:
      db:
        condition: service_healthy
  db:
    image: postgres:VERSION
    volumes:
      - db-data:/var/lib/postgresql/data
volumes:
  db-data:
```

`depends_on` 描述启动关系，不替代应用的连接重试、迁移门禁和数据库恢复。版本、密码与健康命令按项目填写，`.env` 不进入仓库。

## 端口、网络和卷

- `8080:80` 表示宿主 8080 转到容器 80；左右不可混淆。
- 绑定 `127.0.0.1` 只给本机入口，绑定所有接口会扩大暴露范围；还要检查云和主机防火墙。
- 同一 Compose 网络内通常用服务名互访，不用 `localhost` 指向另一个容器。
- bind mount 直接映射宿主路径，权限和路径依赖更强；named volume 由 Docker 管理，仍需独立备份。
- 镜像层、容器可写层和卷是三类存储；空间满时分别检查，不能只删正在运行的容器。

## 健康、重启与优雅停止

健康检查只回答指定探针。检查进程存在很弱，检查依赖齐全的真实业务又可能放大故障；选择能说明服务是否可接流量、且没有破坏性的路径。

重启策略能恢复偶发退出，也可能把配置错误变成重启循环。记录退出码、最后日志、OOM 和健康历史后再重启。应用在停止信号后应停止接收新请求、完成或中止在途工作并在超时内退出。

## 常见故障定位

| 现象 | 先查 |
|---|---|
| 容器立即退出 | `docker ps -a`、退出码、入口命令、最后日志 |
| 端口访问失败 | 容器监听地址、映射、宿主防火墙、代理 |
| 容器间无法连接 | 服务名、网络、目标端口、启动与重试 |
| 改代码没有生效 | 镜像是否重建、容器使用的镜像摘要、挂载覆盖 |
| Permission denied | 运行用户、宿主 UID/GID、卷所有者与模式 |
| 数据重建后消失 | 数据是否只在容器可写层、卷是否被删 |
| 磁盘占满 | 镜像、停止容器、构建缓存、日志和卷分别统计 |
| 被 OOM 终止 | 宿主与容器限制、峰值任务、内核与平台事件 |

清理前先列对象和引用者。镜像、容器、缓存、网络和卷的删除影响不同；尤其不要在不清楚数据位置时使用带 `-v` 的删除或大范围 prune。

## 发布与回退证据

```text
源码提交：
构建命令 / 构建 ID：
基础镜像与依赖锁：
镜像标签 / 摘要：
漏洞与许可检查：
目标主机 / 服务：
配置版本：
迁移版本：
上线健康与业务验证：
旧镜像摘要 / 回退条件：
数据兼容边界：
```

回退镜像不能自动回退数据库。新旧版本短暂共存时，API、任务和数据格式必须兼容。Kubernetes 提供更高层的调度与编排，不会消除镜像、健康、秘密、数据和可观察性的这些责任。

