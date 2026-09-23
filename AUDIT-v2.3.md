# 《AI 写代码之后》v2.3.0 Editorial Audit

**Status:** FROZEN — recovered v2.2.0 baseline; no chapter prose compressed yet.

- Manifest SHA256: `1ae83bb863eb42bf75c8d2afda44b6d1f814125009b1a8f5a3482d803c5fe918`
- Chapters audited: 104
- Recovered visible characters: 422025
- v2.3 target: 380000–420000 visible characters
- Reduction required to 400000-character midpoint: 5.22%
- Exact duplicate paragraphs over 80 characters: 0
- Risk-command candidates: 30
- Volatile-fact candidates: 303
- Invalid chapter references: 0

## Volume baseline

| Volume | Visible characters | v2.3 page target |
|---:|---:|---:|
| 1 | 21220 | 22–25 |
| 2 | 36913 | 36–40 |
| 3 | 36452 | 38–42 |
| 4 | 32068 | 34–38 |
| 5 | 28287 | 30–34 |
| 6 | 40711 | 42–48 |
| 7 | 31963 | 32–36 |
| 8 | 37769 | 40–46 |
| 9 | 39109 | 40–44 |
| 10 | 117533 | 90–100 |

## Six-chapter pilot baseline

| Chapter | Current chars | 40% reduction | 45% reduction | Source |
|---:|---:|---:|---:|---|
| 001 | 4611 | 2767 | 2536 | `chapters/001-从本地文件到公开可用的产品.md` |
| 019 | 5096 | 3058 | 2803 | `chapters/019-浏览器开发者工具-状态码和网络请求.md` |
| 040 | 6578 | 3947 | 3618 | `chapters/040-systemd-systemctl-journalctl-和服务日志.md` |
| 054 | 5312 | 3187 | 2922 | `chapters/054-google-play-内部测试与发布流程.md` |
| 070 | 4906 | 2944 | 2698 | `chapters/070-计划-权限-diff-测试和验证证据.md` |
| 091 | 2903 | 1742 | 1597 | `chapters/091-sli-slo-sla-与-error-budget.md` |

## Chapter baseline

| ID | Volume | Level | Visible chars | Paragraphs | Code blocks | Images | Links | Title |
|---:|---:|---|---:|---:|---:|---:|---:|---|
| 001 | 1 | core | 4611 | 51 | 0 | 1 | 0 | 从本地文件到公开可用的产品 |
| 002 | 1 | core | 4001 | 49 | 0 | 1 | 4 | 本地电脑、GitHub、部署平台、服务器和用户设备 |
| 003 | 1 | core | 6233 | 66 | 0 | 1 | 1 | 静态网站、动态网站、服务器程序和手机 App |
| 004 | 1 | core | 6375 | 72 | 7 | 1 | 1 | 文件、路径、终端和图形界面的最低限度知识 |
| 005 | 2 | core | 3004 | 41 | 1 | 1 | 2 | Git、GitHub、项目文件夹和仓库 |
| 006 | 2 | core | 3056 | 42 | 0 | 1 | 1 | GitHub 账号、公开仓库、私有仓库和网页上传 |
| 007 | 2 | core | 5490 | 58 | 0 | 0 | 2 | 用 GitHub Desktop 管理本地项目 |
| 008 | 2 | core | 5702 | 61 | 0 | 1 | 2 | Commit、Push、Pull、Clone 和 Sync |
| 009 | 2 | core | 5411 | 65 | 1 | 1 | 2 | 分支、合并、冲突、撤销与恢复 |
| 010 | 2 | core | 5381 | 69 | 1 | 1 | 0 | README、Releases、Issues、Actions、许可证和项目维护状态 |
| 011 | 2 | core | 5293 | 57 | 0 | 1 | 0 | 下载、检查并运行别人的项目 |
| 012 | 2 | core | 3576 | 48 | 2 | 1 | 1 | .gitignore、秘密泄露和历史中的敏感信息 |
| 013 | 3 | core | 4201 | 44 | 0 | 1 | 0 | 浏览器、客户端和服务器 |
| 014 | 3 | core | 4125 | 46 | 1 | 1 | 0 | IP、域名、DNS、端口和 URL |
| 015 | 3 | core | 4437 | 46 | 0 | 1 | 0 | HTTP、HTTPS、TLS、请求与响应 |
| 016 | 3 | core | 4798 | 47 | 0 | 1 | 0 | Cookie、Session、Token、缓存和 CDN |
| 017 | 3 | core | 4251 | 50 | 3 | 1 | 0 | HTML、CSS、JavaScript、前端和后端 |
| 018 | 3 | core | 4467 | 50 | 1 | 1 | 1 | API、数据库、文件存储和实时通信 |
| 019 | 3 | core | 5096 | 53 | 1 | 0 | 3 | 浏览器开发者工具、状态码和网络请求 |
| 020 | 3 | core | 5077 | 53 | 0 | 1 | 0 | 动态应用的完整架构图 |
| 021 | 4 | core | 3440 | 41 | 0 | 1 | 0 | 源代码、依赖、运行时、构建和构建产物 |
| 022 | 4 | core | 4007 | 45 | 0 | 1 | 0 | 包管理器、锁文件、版本号和环境差异 |
| 023 | 4 | core | 3281 | 38 | 0 | 1 | 0 | 本地预览与静态网站发布 |
| 024 | 4 | core | 4446 | 47 | 0 | 1 | 0 | GitHub Pages 与 Cloudflare Pages |
| 025 | 4 | core | 3974 | 42 | 0 | 1 | 2 | Vercel、Render 等自动部署平台 |
| 026 | 4 | core | 4065 | 46 | 1 | 1 | 0 | Build Command、Output Directory 和环境变量 |
| 027 | 4 | core | 3861 | 44 | 0 | 1 | 0 | Preview、Production、部署日志和回滚 |
| 028 | 4 | core | 4994 | 56 | 0 | 1 | 0 | 自定义域名、DNS、HTTPS、费用与地区差异 |
| 029 | 5 | core | 3767 | 49 | 2 | 1 | 0 | 后端为什么存在以及 API 怎样工作 |
| 030 | 5 | core | 4188 | 50 | 0 | 1 | 0 | REST、WebSocket、身份认证和权限控制 |
| 031 | 5 | core | 3766 | 47 | 1 | 1 | 0 | SQL、NoSQL、PostgreSQL 与 SQLite |
| 032 | 5 | core | 3735 | 50 | 0 | 1 | 0 | 数据库迁移、连接、备份和恢复 |
| 033 | 5 | core | 4261 | 51 | 0 | 1 | 2 | 文件上传、对象存储、邮件、推送和 AI API |
| 034 | 5 | core | 4813 | 53 | 0 | 1 | 0 | Supabase、Firebase 与后端即服务 |
| 035 | 5 | core | 3757 | 50 | 0 | 1 | 0 | 托管方案、自建方案和平台依赖 |
| 036 | 6 | core | 4515 | 56 | 0 | 1 | 0 | VPS、云服务器及购买时需要看的参数 |
| 037 | 6 | core | 5559 | 66 | 0 | 0 | 2 | 第一次使用 SSH 登录服务器 |
| 038 | 6 | core | 5058 | 66 | 0 | 0 | 0 | Linux 文件、目录、用户、root、sudo 和权限 |
| 039 | 6 | core | 4449 | 62 | 0 | 0 | 0 | 软件包、进程、端口、磁盘和内存 |
| 040 | 6 | core | 6578 | 87 | 0 | 0 | 2 | systemd、systemctl、journalctl 和服务日志 |
| 041 | 6 | core | 4446 | 61 | 0 | 0 | 0 | 防火墙、Caddy、Nginx、域名与 HTTPS |
| 042 | 6 | core | 4517 | 66 | 0 | 0 | 0 | 部署、更新、回滚、备份和恢复 |
| 043 | 6 | core | 5589 | 84 | 0 | 0 | 0 | 自建服务器增加了哪些长期责任 |
| 044 | 7 | core | 4327 | 64 | 0 | 1 | 0 | 运行环境问题与 Docker 的基本模型 |
| 045 | 7 | core | 4243 | 64 | 0 | 1 | 0 | 镜像、容器、Dockerfile 和 Registry |
| 046 | 7 | core | 3873 | 60 | 0 | 1 | 0 | 端口映射、Volume、Bind Mount 和数据持久化 |
| 047 | 7 | core | 4612 | 66 | 0 | 1 | 2 | Docker Compose 与多容器应用 |
| 048 | 7 | core | 4423 | 68 | 0 | 1 | 0 | 容器状态、日志、健康检查和重启策略 |
| 049 | 7 | core | 4805 | 73 | 0 | 1 | 0 | 更新、回滚、清理与数据丢失风险 |
| 050 | 7 | core | 5680 | 74 | 0 | 1 | 0 | Docker、虚拟机和 Kubernetes 的边界 |
| 051 | 8 | core | 4464 | 47 | 0 | 1 | 1 | App 客户端、后端和本地数据 |
| 052 | 8 | core | 4715 | 55 | 3 | 1 | 0 | Flutter 项目、依赖、Debug、Profile 和 Release |
| 053 | 8 | core | 4223 | 50 | 3 | 1 | 0 | APK、AAB、包名、版本号和 Android 签名 |
| 054 | 8 | core | 5312 | 58 | 1 | 1 | 4 | Google Play 内部测试与发布流程 |
| 055 | 8 | core | 4646 | 51 | 1 | 1 | 0 | iOS、macOS、Xcode、证书和 Provisioning Profile |
| 056 | 8 | core | 5258 | 58 | 3 | 1 | 4 | Archive、TestFlight 与 App Store Connect |
| 057 | 8 | core | 4583 | 62 | 2 | 1 | 0 | 商店素材、权限、隐私政策和审核反馈 |
| 058 | 8 | core | 4568 | 52 | 0 | 1 | 0 | App 更新、崩溃日志和后端停机 |
| 059 | 9 | core | 3404 | 50 | 3 | 1 | 0 | 从现象到故障层级的统一判断方法 |
| 060 | 9 | core | 4471 | 54 | 0 | 1 | 1 | Console、Network、Build Log 和 Runtime Log |
| 061 | 9 | core | 4055 | 53 | 2 | 1 | 2 | 服务器、Docker、数据库和代理日志 |
| 062 | 9 | core | 4553 | 54 | 0 | 1 | 0 | Flutter、Logcat、Xcode 与商店上传错误 |
| 063 | 9 | core | 3617 | 53 | 0 | 1 | 0 | 复现、调用栈、最小复现、最近改动和回滚 |
| 064 | 9 | core | 3791 | 55 | 4 | 1 | 0 | 怎样向 AI 或开发者提交完整报错 |
| 065 | 9 | core | 3759 | 51 | 1 | 1 | 1 | Secret、.env、SSH 密钥和最小权限 |
| 066 | 9 | core | 3817 | 51 | 1 | 1 | 1 | 防火墙、数据库暴露、输入验证和文件上传 |
| 067 | 9 | core | 3444 | 50 | 0 | 1 | 0 | 备份、恢复测试、监控、费用和安全下线 |
| 068 | 9 | core | 4198 | 59 | 0 | 1 | 0 | 每周、每月和每季度维护清单 |
| 069 | 10 | core | 3271 | 39 | 0 | 1 | 1 | 让 AI 先理解项目结构 |
| 070 | 10 | core | 4906 | 59 | 1 | 1 | 1 | 计划、权限、Diff、测试和验证证据 |
| 071 | 10 | core | 3440 | 40 | 0 | 1 | 0 | 安全地生成配置、部署文档和回滚方案 |
| 072 | 10 | core | 3720 | 43 | 1 | 1 | 1 | AI 声称完成以后还要检查什么 |
| 073 | 10 | core | 3539 | 44 | 0 | 1 | 0 | 生产环境中的人工确认边界 |
| 074 | 10 | core | 3396 | 43 | 0 | 1 | 0 | 不懂代码时怎样保留最终判断能力 |
| 075 | 10 | optional | 2763 | 35 | 2 | 1 | 3 | 代码能运行以后，架构问题才开始出现 |
| 076 | 10 | optional | 2386 | 27 | 0 | 0 | 0 | 模块、内聚、耦合、依赖方向与公开接口 |
| 077 | 10 | optional | 3625 | 46 | 0 | 1 | 0 | 领域边界、数据所有权与跨模块协作 |
| 078 | 10 | optional | 3411 | 37 | 0 | 1 | 0 | 分层架构、按功能组织与 Vertical Slice |
| 079 | 10 | optional | 3516 | 44 | 0 | 1 | 0 | 模块化单体怎样控制变化范围 |
| 080 | 10 | optional | 3516 | 46 | 0 | 1 | 0 | 微服务真正增加了哪些工程责任 |
| 081 | 10 | optional | 3571 | 48 | 0 | 1 | 0 | 架构异味与 AI 生成项目的复杂度增长 |
| 082 | 10 | optional | 3300 | 44 | 0 | 1 | 0 | 复杂度预算与什么时候不要增加新组件 |
| 083 | 10 | optional | 3717 | 63 | 1 | 1 | 0 | 用 ADR 保存选择、代价与重新评估条件 |
| 084 | 10 | optional | 3382 | 48 | 0 | 1 | 0 | 怎样让两个工程方案真正对打 |
| 085 | 10 | advanced | 3443 | 40 | 0 | 1 | 1 | REST、GraphQL、Polling、SSE 与 WebSocket |
| 086 | 10 | advanced | 3829 | 47 | 0 | 1 | 1 | SQLite、PostgreSQL、SQL 与文档数据库 |
| 087 | 10 | advanced | 3794 | 40 | 0 | 1 | 2 | BaaS、自建后端、托管平台、VPS 与 Serverless |
| 088 | 10 | advanced | 3586 | 39 | 1 | 1 | 2 | 直接进程、Docker、Compose 与 Kubernetes |
| 089 | 10 | advanced | 3589 | 48 | 2 | 1 | 1 | 局部故障、超时、重试放大与退避 |
| 090 | 10 | advanced | 3787 | 44 | 0 | 1 | 1 | 背压、负载丢弃、隔离与队列语义 |
| 091 | 10 | advanced | 2903 | 42 | 3 | 1 | 2 | SLI、SLO、SLA 与 Error Budget |
| 092 | 10 | advanced | 3643 | 46 | 2 | 1 | 1 | 日志、指标、追踪与 OpenTelemetry |
| 093 | 10 | advanced | 3547 | 50 | 3 | 1 | 0 | 性能基线、分位数、剖析、压测与成本 |
| 094 | 10 | advanced | 2044 | 28 | 1 | 1 | 0 | 契约、性质、模糊、变异与回归测试 |
| 095 | 10 | advanced | 2068 | 29 | 0 | 1 | 0 | 独立测试依据与可信的第二意见 |
| 096 | 10 | advanced | 3462 | 53 | 3 | 1 | 1 | 怎样阅读事故复盘并提取可迁移经验 |
| 097 | 10 | reference | 3309 | 39 | 2 | 1 | 1 | 先画成熟开源仓库的 Repository Map |
| 098 | 10 | reference | 1869 | 27 | 1 | 1 | 0 | 沿用户动作阅读测试、历史、Issue 与 PR |
| 099 | 10 | reference | 2019 | 26 | 0 | 1 | 2 | PocketBase 与 Supabase 的边界选择 |
| 100 | 10 | reference | 2126 | 27 | 0 | 1 | 3 | Immich 与 PostHog 中的后台任务和工程组织 |
| 101 | 10 | reference | 3274 | 43 | 2 | 1 | 1 | 怎样正确使用技术社区中的争议与经验 |
| 102 | 10 | reference | 3261 | 44 | 1 | 1 | 0 | Repository Health Review 与长期清理 |
| 103 | 10 | reference | 3213 | 45 | 2 | 1 | 0 | 审查 AI 的范围扩张、依赖与架构漂移 |
| 104 | 10 | reference | 3308 | 50 | 1 | 1 | 0 | 把工程判断变成可持续的项目治理 |

## Exact duplicate paragraphs (>80 chars)

- None

## Risk-command candidates

| Chapter | Location | Reason | Candidate |
|---:|---|---|---|
| 027 | `chapters/027-preview-production-部署日志和回滚.md:51` | database migration | 数据库迁移、用户写入、发送的邮件、支付事件、对象存储文件、DNS 修改和第三方配置通常不随应用版本回滚。假设新版本把数据库列改名，旧代码回滚后仍面对新结构，可能继续故障。用户在故障期间创建的订单不能简单用旧备份覆盖，否则会丢失真实写入。 |
| 027 | `chapters/027-preview-production-部署日志和回滚.md:55` | database migration | 数据库迁移分为兼容添加、数据转换和破坏性删除。新增可空列通常与旧代码兼容；把整列数据转换成新格式后，旧代码能否读取要实测；删除列或合并数据可能无法自动恢复。应用回滚前查看本次部署是否执行迁移、迁移成功到哪一步、是否已有新写入。没有这些证据时，不要直接运行所谓 down migration。 |
| 032 | `chapters/032-数据库迁移-连接-备份和恢复.md:1` | database migration | # 数据库迁移、连接、备份和恢复 |
| 032 | `chapters/032-数据库迁移-连接-备份和恢复.md:49` | database migration | 有些迁移可以重试，例如创建缺失索引前先检查是否已存在。有些迁移需要人工补偿，例如数据转换完成一半。所谓 down migration 也不总安全。列已删除、数据已合并、外部事件已发送后，逆向脚本可能恢复不了真实状态。 |
| 038 | `chapters/038-linux-文件-目录-用户-root-sudo-和权限.md:13` | privileged or destructive shell command | ## root 和 sudo |
| 043 | `chapters/043-自建服务器增加了哪些长期责任.md:27` | privileged or destructive shell command | 不要共享 root 密码来协作。给每个人独立账号和权限，必要操作通过 sudo 或云平台权限完成。出了问题能追踪是谁、什么时候、做了什么。共享账号看似省事，事故时会让所有人一起失明。 |
| 059 | `chapters/059-从现象到故障层级的统一判断方法.md:78` | database migration | 最近改动是重要线索，也只是线索。代码提交、依赖升级、环境变量、证书、DNS、数据库迁移、云平台策略、流量突增和外部 API 都可能改变系统。没有部署代码，证书到期也能让应用失效。 |
| 061 | `chapters/061-服务器-docker-数据库和代理日志.md:57` | privileged or destructive shell command | sudo nginx -T |
| 061 | `chapters/061-服务器-docker-数据库和代理日志.md:58` | privileged or destructive shell command | sudo tail -n 200 /var/log/nginx/access.log |
| 061 | `chapters/061-服务器-docker-数据库和代理日志.md:59` | privileged or destructive shell command | sudo tail -n 200 /var/log/nginx/error.log |
| 063 | `chapters/063-复现-调用栈-最小复现-最近改动和回滚.md:53` | database migration | 二分定位需要稳定复现。若问题偶发，先建立能稳定观察的指标或脚本。否则一次成功可能只是运气。数据库迁移、外部 API 和生产数据变化也会干扰结果，测试前要固定环境。 |
| 063 | `chapters/063-复现-调用栈-最小复现-最近改动和回滚.md:59` | database migration | 故障发生在一次发布后，最近提交值得优先看。完整变更面还包括依赖解析、环境变量、证书、DNS、数据库迁移、平台策略、流量、数据规模、系统更新和外部 API。没有人主动部署，证书到期或云平台规则调整也能改变结果。 |
| 063 | `chapters/063-复现-调用栈-最小复现-最近改动和回滚.md:66` | database migration | \| 13 点 40 分 \| 数据库迁移 \| 小周 \| 订单字段 \| 迁移日志 \| |
| 063 | `chapters/063-复现-调用栈-最小复现-最近改动和回滚.md:73` | database migration | 回滚的目标是恢复服务，修复的目标是消除原因。两者经常不同。网页代码可以回滚，数据库迁移、外部邮件、付款、对象存储写入和用户操作不一定能回滚。App 已安装到用户设备后，也不能像网页那样瞬间换回旧包。 |
| 063 | `chapters/063-复现-调用栈-最小复现-最近改动和回滚.md:75` | database migration | 回滚前先看有没有状态变化。新版本是否写入了旧版本不能读取的数据。是否发送了外部通知。是否产生了订单和付款。是否执行了破坏性迁移。若答案不清楚，不要直接运行所谓 down migration。 |
| 064 | `chapters/064-怎样向-ai-或开发者提交完整报错.md:56` | database migration | 最近改动不要写成猜测。写部署记录、提交号、配置变化、依赖升级、证书轮换、DNS 修改、数据库迁移、商店 build、后端开关和第三方服务状态。能附链接或编号就附，不能附时写时间和负责人。 |
| 064 | `chapters/064-怎样向-ai-或开发者提交完整报错.md:58` | database migration | 不要把无关改动都塞进去。过去一个月所有提交没人看得完。先列和现象时间接近、影响层级相关的变化。保存订单失败，就优先列订单 API、数据库迁移、权限、部署和依赖。页面字体调整可以先放后。 |
| 064 | `chapters/064-怎样向-ai-或开发者提交完整报错.md:89` | database migration | 如果让 AI 改代码，先给范围。允许改哪些文件，不能碰哪些文件，是否允许改依赖、数据库迁移、CI、环境变量和部署配置。很多风险来自范围外修改。一个按钮报错任务，AI 顺手升级框架、改鉴权、重写路由，看起来勤快，排查会变难。 |
| 065 | `chapters/065-secret-env-ssh-密钥和最小权限.md:68` | privileged or destructive shell command | 服务器日常操作不要共享 root 密码。每个人使用独立账号，必要时通过 sudo 执行授权命令。这样出了问题能知道谁在什么时候做了什么。共享账号会让审计失明。 |
| 066 | `chapters/066-防火墙-数据库暴露-输入验证和文件上传.md:16` | privileged or destructive shell command | sudo ss -lntp |
| 066 | `chapters/066-防火墙-数据库暴露-输入验证和文件上传.md:17` | privileged or destructive shell command | sudo ufw status verbose |
| 068 | `chapters/068-每周-每月和每季度维护清单.md:69` | privileged or destructive shell command | 季度检查也适合做一次权限瘦身。很多权限是在赶项目时临时给出的。三个月后，上传权限、管理员权限、生产数据库访问、商店发布角色、服务器 sudo 和第三方 API 管理权，可能已经超过实际需要。收回权限比等事故后追责有效。 |
| 068 | `chapters/068-每周-每月和每季度维护清单.md:75` | database migration | 某些变化发生时，不要等到下周或下季度。发布重大版本、数据库迁移、接入支付、开放文件上传、上线 AI 功能、换云平台、改域名、升级目标 API、提交 App 或小程序审核，都应临时执行相关检查。 |
| 072 | `chapters/072-ai-声称完成以后还要检查什么.md:23` | database migration | Diff 展示版本控制文件的真实变化。先看文件列表、增删规模和二进制，再逐块审查。任务是改一处按钮，却出现锁文件、数据库迁移、CI、格式化数百行或删除测试，就需要解释。未跟踪文件不会总出现在普通 Diff 中，还要结合 `git status`。 |
| 073 | `chapters/073-生产环境中的人工确认边界.md:35` | database migration | 审批提示中的命令要翻译成业务后果。`apply migration` 可能锁表和改变数据，`sync --delete` 会让远端文件按规则消失，`terraform apply` 可能创建费用或销毁资源。确认人需要看到计划、准确目标、Diff 与回退。 |
| 087 | `chapters/087-baas-自建后端-托管平台-vps-与-serverless.md:19` | database migration | 自建后端表示项目自己拥有并维护业务服务代码。它可以部署在 VPS，也可以部署到 Render、Vercel 或其他应用平台。托管应用平台接收仓库或容器，负责构建、启动、域名、证书、日志入口和部分扩缩容。项目仍要提供启动命令、环境变量、数据库迁移、健康检查和应用监控。 |
| 103 | `chapters/103-审查-ai-的范围扩张-依赖与架构漂移.md:20` | database migration | 允许修改  表单、用户接口、数据库迁移、相关测试 |
| 103 | `chapters/103-审查-ai-的范围扩张-依赖与架构漂移.md:30` | database migration | 先看新增、修改、删除文件和总差异，不急着逐行读。按功能代码、测试、依赖清单、锁文件、数据库迁移、部署配置、工作流、权限和文档分类。任何超出约定的类别先标记。 |
| 103 | `chapters/103-审查-ai-的范围扩张-依赖与架构漂移.md:44` | database migration | 数据库迁移、对象存储、环境变量、缓存键和队列消息会跨版本存在。代码回滚不一定撤销数据变化。审查迁移前向和回退方向，确认旧版本能否读取新数据，部署顺序是否允许新旧进程短暂共存。 |
| 104 | `chapters/104-把工程判断变成可持续的项目治理.md:40` | database migration | 发布记录应包含提交、制品校验、数据库迁移、配置变化、部署时间、操作者、验证和回滚点。几个月后出现故障时，这些信息比“当时应该测过”可靠。 |

## Volatile-fact candidates

| Chapter | Location | Reason | Candidate |
|---:|---|---|---|
| 001 | `chapters/001-从本地文件到公开可用的产品.md:59` | time-sensitive fact candidate | 数据位置要单独决定。网页在静态托管，不妨碍账号与数据库由另一服务承担；后端在 VPS，也不要求数据库必须同机。拆分可以降低单机故障，也会增加账户、网络、权限和费用关系。选择时要看每个组件的负责人、入口和恢复方式是否说得清楚。 |
| 001 | `chapters/001-从本地文件到公开可用的产品.md:82` | time-sensitive fact candidate | \| 费用 \| 哪些资源会持续收费 \| 账单入口、预算与告警 \| |
| 001 | `chapters/001-从本地文件到公开可用的产品.md:89` | time-sensitive fact candidate | App 同理。商店拒绝上传时查包名、版本、签名和政策；安装后立即崩溃时查客户端构建；只有登录或同步失败时再追踪网络与后端。先定位对象，能避免为数据库故障反复重装 App，或为构建失败修改 DNS。 |
| 003 | `chapters/003-静态网站-动态网站-服务器程序和手机-app.md:51` | time-sensitive fact candidate | 前端是用户设备上直接呈现和交互的部分。网页前端在浏览器中运行，App 前端在移动操作系统中运行。后端在用户设备之外处理需要集中管理或保密的工作。这条边界最重要的判断是信任。用户能够查看、修改或伪造客户端发出的请求；前端隐藏一个按钮，不能阻止用户直接调用接口。价格、账户归属、管理员权限和付费状态等关键规则必须由后端重新检查。 |
| 003 | `chapters/003-静态网站-动态网站-服务器程序和手机-app.md:98` | time-sensitive fact candidate | 表格计算、图片预览和界面筛选可以留在浏览器。价格、权限和私密 API 调用必须由后端判断。若前端把 100 元改成 1 元，服务器仍应按商品和优惠重新计算；若把 AI 供应商密钥写进前端，任何用户都可能提取并消耗额度。“能运行”只描述技术可能性。“应该放哪里”还要考虑秘密、权限、费用、延迟、离线需求和维护责任。 |
| 003 | `chapters/003-静态网站-动态网站-服务器程序和手机-app.md:123` | time-sensitive fact candidate | 学习项目容易过早加入账号和数据库。一个计算器、作品集、活动说明页或只在本机使用的表格工具，可能靠静态文件和浏览器本地数据就能完成目标。暂时不建后端，可以减少账户安全、数据库备份、服务器费用和隐私政策等责任。等到确实需要跨设备同步、多人共享、集中权限或私密凭据时，再增加远程服务。 |
| 004 | `chapters/004-文件-路径-终端和图形界面的最低限度知识.md:66` | time-sensitive fact candidate | 从 GitHub 下载 ZIP 后，通常得到项目文件快照。解压只把文件放到某个目录，不会自动安装编程语言、数据库或依赖。先把压缩包解压到明确的普通目录，再阅读 README。项目要求 Node.js、Python、Flutter 或 Docker 时，要分别安装对应工具，并核对支持版本。安装完成后，旧终端未必自动取得新的环境变量。关闭终端并重新打开，再运行官… |
| 004 | `chapters/004-文件-路径-终端和图形界面的最低限度知识.md:171` | time-sensitive fact candidate | 同一台电脑可以同时运行许多网络程序。端口号帮助系统把请求交给正确程序。本地开发地址 `http://localhost:5173` 中，`5173` 就是端口。浏览器能打开，说明这个端口上有程序响应；关闭终端进程后再刷新，页面可能无法连接。文件仍在电脑里，负责响应的程序已经停止。“端口被占用”表示另一个进程已经监听同一入口。先查看占用者，再决定停止旧进程或使… |
| 006 | `chapters/006-github-账号-公开仓库-私有仓库和网页上传.md:15` | time-sensitive fact candidate | 个人练习和个人作品可以由个人账号拥有；公司、社团或长期多人项目更适合组织。判断标准是成员离开后谁继续拥有项目、支付费用和处理安全事件。组织资源不应为了绕过规则复制到个人账号。 |
| 008 | `chapters/008-commit-push-pull-clone-和-sync.md:79` | time-sensitive fact candidate | 视频、数据集和构建包进入普通 Git 历史后，每次 Clone 可能都要传输历史版本。删除当前文件也不能自动缩小旧历史。Git LFS 可以把大文件内容放到专门存储，并在 Git 中保留指针。它有配额、费用和平台支持要求，使用前查当前官方文档。已经进入历史的大文件迁移仍会影响协作者。 |
| 009 | `chapters/009-分支-合并-冲突-撤销与恢复.md:144` | time-sensitive fact candidate | AI 可以解释冲突两边来自哪些提交，提出候选合并内容，列出撤销方案的影响。它也能检查文件是否还残留冲突标记。让 AI 修改前，要求它保留两边原文、说明业务依据，并在独立分支工作。没有业务信息时，它不能替你决定活动时间、价格、权限和生产数据。 |
| 010 | `chapters/010-readme-releases-issues-actions-许可证和项目维护状态.md:15` | time-sensitive fact candidate | README 不应把所有技术细节塞在一页。复杂项目可以链接到 `docs` 目录、贡献指南、安全政策和变更记录。入口页保留读者第一次运行所需的最短路径。例如，一个项目只写“运行 `npm start`”，却没说明需要哪个 Node.js 版本、在哪个目录运行、成功后打开什么地址。读者无法判断命令报错来自环境还是项目。 |
| 010 | `chapters/010-readme-releases-issues-actions-许可证和项目维护状态.md:43` | time-sensitive fact candidate | GitHub Release 建立在标签之上，可以包含版本说明、二进制文件与其他下载资产。GitHub 也会提供对应源码压缩包。Tag 译为标签，用一个稳定名称指向某个提交，例如 `v1.2.0`。Release 在这个版本上增加面向使用者的说明。仓库最新提交可能正在开发，最新稳定 Release 可能更适合普通用户。 |
| 010 | `chapters/010-readme-releases-issues-actions-许可证和项目维护状态.md:85` | time-sensitive fact candidate | 仓库 Tag 指向源码提交，Release 围绕 Tag 提供说明和资产，部署平台又有自己的部署编号。三者要能互相追溯。例如 Release `v1.2.0` 对应提交 `abc123`，Windows 安装包由同一提交的 Actions 构建，生产部署也记录 `abc123`。用户报错时提供版本号，维护者能找到源码和日志。 |
| 010 | `chapters/010-readme-releases-issues-actions-许可证和项目维护状态.md:87` | time-sensitive fact candidate | 如果安装包由另一个未记录目录手工构建，版本名相同也可能内容不同。可重复构建、签名和哈希能减少这种不确定。紧急修复发布 `v1.2.1` 后，说明受影响版本与升级建议。不要悄悄替换旧资产，让已经下载的人无法确认内容。 |
| 010 | `chapters/010-readme-releases-issues-actions-许可证和项目维护状态.md:101` | time-sensitive fact candidate | 许多项目使用类似 `1.4.2` 的版本号，通常分别表示主要版本、次要版本和修复版本。是否严格遵守语义化版本由项目决定，不能仅凭数字断言兼容。Pre-release 常用于测试版本，可能包含新功能，也可能有未解决问题。生产环境应按项目说明选择稳定版本，并在升级前查看变更与迁移要求。 |
| 010 | `chapters/010-readme-releases-issues-actions-许可证和项目维护状态.md:103` | time-sensitive fact candidate | Latest 标签是 GitHub 界面或维护者设置的一种提示。自动工具选择版本时，还要结合是否为预发布、系统架构和项目自己的发布政策。Issue 用于缺陷、任务和可执行反馈。提交前搜索版本与日期相近的开放和关闭结果；提供最小示例时排除秘密、个人信息与受限内容。 |
| 010 | `chapters/010-readme-releases-issues-actions-许可证和项目维护状态.md:123` | time-sensitive fact candidate | 第一分钟确认所有者、官方链接与仓库是否归档；接着读 README 的用途、系统要求和支持版本；查看最新稳定 Release 与发布日期；打开 Actions 看最近默认分支结果。搜索与你系统和目标功能相关的 Issue，例如 Windows、Apple Silicon、Docker 或具体错误。打开许可证，确认使用范围。最后查看安装命令会执行哪些脚本，是否需… |
| 011 | `chapters/011-下载-检查并运行别人的项目.md:53` | time-sensitive fact candidate | 查看 Compose 文件和 `docker run` 参数。挂载 `C:\`、`/`、用户主目录或 Docker socket 都会给容器很大访问范围。`privileged` 模式与添加系统能力也要有明确原因。端口映射 `127.0.0.1:8080:8080` 通常只从本机访问，绑定所有网络接口会扩大范围。语法因工具与平台而异，最终用 Docker 实… |
| 012 | `chapters/012-gitignore-秘密泄露和历史中的敏感信息.md:98` | time-sensitive fact candidate | 调试代码打印 Authorization Header，会把令牌复制到本地、部署或第三方日志。先轮换，再按保留政策限制日志访问；调查完成前不盲目删除所有证据。以后省略令牌和敏感正文，或只记录不可逆的短识别值。错误监控与 AI 分析服务也是数据接收方，要过滤并核对地区与保留政策。 |
| 013 | `chapters/013-浏览器-客户端和服务器.md:19` | time-sensitive fact candidate | 浏览器运行在用户设备上，用户可以查看页面代码、修改请求、安装扩展，甚至不用浏览器而改用别的工具直接调用 API。因此价格、权限、所有权、支付状态和管理员操作不能只由浏览器决定。前端可以帮助用户输入和展示结果，服务端必须重新验证关键规则。 |
| 014 | `chapters/014-ip-域名-dns-端口和-url.md:17` | time-sensitive fact candidate | `127.0.0.1` 是回环地址，通常指当前设备自身。`localhost` 常解析到回环地址。开发服务器只监听 `127.0.0.1` 时，其他设备不能直接访问。`0.0.0.0` 在监听配置中常表示所有 IPv4 接口，不是普通用户该输入浏览器的目标地址。把服务监听到所有接口会扩大暴露面，需要防火墙、认证和日志。 |
| 014 | `chapters/014-ip-域名-dns-端口和-url.md:49` | time-sensitive fact candidate | 监听地址要和端口一起看。`127.0.0.1:3000` 表示只监听当前机器；同机反向代理可以访问，远程用户不能直接连。`0.0.0.0:3000` 表示监听所有 IPv4 接口，是否能从公网访问还要看网络边界和认证。 |
| 014 | `chapters/014-ip-域名-dns-端口和-url.md:58` | time-sensitive fact candidate | https://api.example.com:8443/v1/orders?status=open#recent |
| 014 | `chapters/014-ip-域名-dns-端口和-url.md:61` | time-sensitive fact candidate | `https` 是 Scheme，决定访问方式；`api.example.com` 是 Host；`8443` 是显式端口；`/v1/orders` 是路径；`status=open` 是查询参数；`recent` 是片段标识。片段通常由浏览器本地使用，不会作为普通 HTTP 请求目标发给服务器。 |
| 014 | `chapters/014-ip-域名-dns-端口和-url.md:77` | time-sensitive fact candidate | 面向中国大陆提供公开网站时，域名、服务器位置、备案和内容要求可能涉及法规与服务商政策。这些规则会变化，部署前查当时官方主管部门和服务商说明，并记录日期。不要把旧博客里的结论写成永久规则。 |
| 014 | `chapters/014-ip-域名-dns-端口和-url.md:83` | time-sensitive fact candidate | 另一个例子来自 502。用户访问域名得到 502。后端启动日志显示监听 `127.0.0.1:3000`，Caddy 配置却转发到 `localhost:3001`。应用没坏，代理连错端口。修复上游端口并验证公开域名即可，不需要把应用改成公网监听，也不应为了“试一下”开放 3000 防火墙。 |
| 018 | `chapters/018-api-数据库-文件存储和实时通信.md:89` | time-sensitive fact candidate | API 限流保护稳定和费用。可以按用户、IP、令牌或资源限制一定时间内请求。登录、上传和 AI 调用需要不同策略。超过限制返回 429，并给出可理解提示。客户端指数退避，不每毫秒重试。IP 可能多人共享，不能作为唯一账户限制。 |
| 018 | `chapters/018-api-数据库-文件存储和实时通信.md:95` | time-sensitive fact candidate | 恢复到测试环境后，API 使用测试域名，禁用真实外部通知，避免向真实用户发邮件。校验记录数、关键查询、文件引用和权限。备份完成提示不能替代恢复成功证据。删除账号、软删除和保留政策也要覆盖数据库、对象、索引、缓存和备份。 |
| 018 | `chapters/018-api-数据库-文件存储和实时通信.md:97` | time-sensitive fact candidate | 一个完整头像上传流程可以作为练习。客户端预览图片，向 API 请求上传授权；API 验证身份和配额，生成特定 Key 的短期上传 URL；客户端上传对象存储；API 验证对象存在并更新数据库头像 Key；后台生成缩略图；展示时用公开 URL 或短期读取 URL。任何一步失败，都有状态和清理方式。 |
| 019 | `chapters/019-浏览器开发者工具-状态码和网络请求.md:113` | time-sensitive fact candidate | 截图只保留需要的面板、目标请求和关键列，同时保留时间与面板名。HAR 会包含大量 URL、Headers、Cookie、Payload 和 Response，风险远高于普通截图。确需导出时使用测试账号，导出后再次检查文本内容，通过受控渠道限时分享，并按数据政策删除。 |
| 020 | `chapters/020-动态应用的完整架构图.md:29` | time-sensitive fact candidate | 文件上传跨过存储边界。客户端预览不代表服务器接受。后端验证身份、配额和元数据，生成安全对象 Key 与临时授权。客户端直接上传可以减少后端带宽。上传完成后，后端验证对象并创建记录。后台任务扫描、转码或生成缩略图。对象、数据库、缓存和备份都要进入删除和恢复流程。 |
| 020 | `chapters/020-动态应用的完整架构图.md:59` | time-sensitive fact candidate | 成本同样沿组件产生。CDN 按流量或请求，应用按运行时间与资源，数据库按实例、存储和备份，对象存储按容量和传输，外部 API 按调用。价格、免费额度和政策会变化，具体数值以上线当日官方控制台为准。图旁记录账单所有者、预算提醒和关闭入口。 |
| 020 | `chapters/020-动态应用的完整架构图.md:65` | time-sensitive fact candidate | 个人作品页允许短暂停机，支付、医疗和企业协作系统要求更高。先定义用户可接受的中断和数据丢失，再决定冗余与恢复。RTO 表示期望恢复时间，RPO 表示可接受的数据时间损失。数值由业务承担者批准，并通过演练验证。高目标会增加费用和复杂度。 |
| 020 | `chapters/020-动态应用的完整架构图.md:99` | time-sensitive fact candidate | 能从一个用户动作画出设备、入口、应用、数据和外部服务。每条箭头有协议、权限和日志。能从“打不开”“操作失败”“任务卡住”进入不同故障树。知道静态首页正常不能证明后端正常。图有日期、环境、来源和待验证项。责任表覆盖账号、备份、费用和下线。 |
| 022 | `chapters/022-包管理器-锁文件-版本号和环境差异.md:27` | time-sensitive fact candidate | 常见语义化版本写成 `3.7.2`。三个数字通常依次代表主版本、次版本和修订版本。兼容性承诺由维护者给出，不能只凭数字保证。项目清单还会使用范围符号。`1.2.3` 倾向锁定一个版本，`^1.2.3` 通常允许同一主版本内更新，`~1.2.3` 通常允许同一次版本内修订更新。实际规则以当前包管理器文档为准。 |
| 022 | `chapters/022-包管理器-锁文件-版本号和环境差异.md:29` | time-sensitive fact candidate | 上面的范围示例不能直接套到所有 `0.x` 版本。按 npm 使用的 semver 规则，`^0.2.3` 允许兼容的 `0.2.x` 更新，不包括 `0.3.0`；`^0.0.3` 则不会接受 `0.0.4`。预发布版本还有额外匹配规则。 |
| 022 | `chapters/022-包管理器-锁文件-版本号和环境差异.md:45` | time-sensitive fact candidate | 本机记录版本时保留完整输出。`v20` 太宽泛，`v20.19.4` 才能用于复现。npm、pnpm 或 Yarn 也各自有版本。不要把 npm 版本号误填到 Node.js Runtime 选项，也不要因为 npm 有新版本就立即全局升级正式构建机。先看项目支持范围，在练习分支验证，再统一团队和平台设置。 |
| 023 | `chapters/023-本地预览与静态网站发布.md:43` | time-sensitive fact candidate | 静态托管只描述文件提供方式，不限制浏览器脚本发请求。天气页面可以托管成静态文件，再从浏览器调用天气 API。这会遇到跨域、密钥暴露、配额和第三方停机。需要秘密的 API 不应由浏览器直接持有私钥。公开 API 也要处理超时、空数据和错误状态。 |
| 024 | `chapters/024-github-pages-与-cloudflare-pages.md:47` | time-sensitive fact candidate | 若项目依赖服务端长进程、私有网络、本地磁盘或数据库写入，这两个静态发布入口都不是完整答案。先画清后端需求，再选择动态托管或服务器。选择还要考虑账号权限、地区网络、域名管理、构建限制和费用。所有额度和价格都可能变化，本书不把当前免费层写成永久承诺。 |
| 024 | `chapters/024-github-pages-与-cloudflare-pages.md:59` | time-sensitive fact candidate | 每个分支都自动部署很方便，也可能消耗构建额度并暴露大量预览地址。根据项目隐私和费用设置预览分支规则。Pull Request 关闭后，旧预览地址可能仍存在一段时间。不要把地址难猜当作清理机制。 |
| 025 | `chapters/025-vercel-render-等自动部署平台.md:33` | time-sensitive fact candidate | 托管平台通常承担构建机器、发布入口、TLS 证书、部署历史和基础运行设施。动态服务还可能提供健康检查、日志和伸缩选项。你仍负责源代码、依赖、配置、数据、权限、秘密、业务监控和费用。平台显示绿色，只说明它的部署检查通过，不代表注册、支付、备份和数据恢复可用。 |
| 025 | `chapters/025-vercel-render-等自动部署平台.md:37` | time-sensitive fact candidate | 价格、免费额度和休眠规则变化频繁。正式决策时打开官方定价与限制页，写明查询日期和预计用量，不沿用本书截稿时数字。面向中国大陆公众提供服务时，还要根据服务器位置、域名接入、网络质量和现行规则核对官方渠道，本书不会把全球平台的默认流程写成完整合规答案。 |
| 025 | `chapters/025-vercel-render-等自动部署平台.md:41` | time-sensitive fact candidate | 云平台通常通过环境变量提供端口。后端应读取该值，不能固定只监听本机开发端口。监听 `127.0.0.1` 只接受容器内部本机连接，平台代理可能无法访问。许多平台要求绑定对外可接入的地址，具体按当前运行时示例配置。不要为了测试随意开放云服务器防火墙端口；托管服务的公网入口通常由平台代理提供。 |
| 025 | `chapters/025-vercel-render-等自动部署平台.md:45` | time-sensitive fact candidate | 某些计划会在空闲时暂停服务，下一次请求需要等待启动。是否存在、等待多久和适用计划会变化。访问慢不一定是代码性能问题。对照平台事件和实例启动日志，判断是否冷启动。需要稳定响应的业务应按当前官方计划评估资源和费用，不把免费层当生产保证。 |
| 025 | `chapters/025-vercel-render-等自动部署平台.md:67` | time-sensitive fact candidate | 等价表至少写七项。仓库来源和生产分支是否相同；Root、Build、Output 或 Start 字段怎样对应；运行时版本与包管理器是否一致；环境变量名称、作用环境和秘密范围是否迁移；自定义域名、重定向和 HTTPS 谁负责；日志、监控和告警入口在哪里；费用、团队权限和停用旧平台的步骤由谁批准。 |
| 025 | `chapters/025-vercel-render-等自动部署平台.md:83` | time-sensitive fact candidate | 能根据产物选择 Static Site 或 Web Service，正确区分 Build Command 与 Start Command。动态服务读取平台端口并通过健康检查。用户数据不写入无保障临时盘，后台任务和定时任务有明确去处。部署平台的仓库权限、秘密范围、Hook 和费用告警经过确认。 |
| 025 | `chapters/025-vercel-render-等自动部署平台.md:85` | time-sensitive fact candidate | AI 可以从项目结构推断候选服务类型，比较平台需要的字段，解释部署日志，并生成上线验收表。它不能根据“这是 React 项目”就确定静态或服务端路线。让它引用构建配置、脚本和产物证据。亲自检查仓库授权、生产分支、环境变量、持久数据位置和费用告警。下一章逐项解释 Build Command、Output Directory 和环境变量。 |
| 027 | `chapters/027-preview-production-部署日志和回滚.md:63` | time-sensitive fact candidate | 功能开关能减少回滚压力。新功能通过开关逐步开放，故障时可切回已保留并验证过的旧代码路径，不一定需要回滚整个部署。涉及写入或费用的功能，要在后端停用相应操作；只隐藏前端入口，不能阻止旧客户端或直接 API 请求。开关本身也是生产配置，要记录默认值、作用环境、负责人和清理日期。临时开关长期遗留，会让代码路径越来越难测试。发布记录中写明本次依赖哪些开关，故障时才能… |
| 027 | `chapters/027-preview-production-部署日志和回滚.md:87` | time-sensitive fact candidate | AI 可以把部署、提交和日志排成时间线，找出故障首次出现的版本，生成回滚前检查表，并比较旧版与数据库变更。它不能替你判断真实订单是否可以丢弃，也不能仅凭应用代码保证数据库兼容。亲自选择回滚目标，确认正式域名实际指向，检查核心流程和外部数据。下一章把平台自带网址连接到自己的域名，并说明 DNS、HTTPS、费用和地区差异为什么需要单独核对。 |
| 028 | `chapters/028-自定义域名-dns-https-费用与地区差异.md:1` | time-sensitive fact candidate | # 自定义域名、DNS、HTTPS、费用与地区差异 |
| 028 | `chapters/028-自定义域名-dns-https-费用与地区差异.md:68` | time-sensitive fact candidate | ## 费用、续费和地区差异 |
| 028 | `chapters/028-自定义域名-dns-https-费用与地区差异.md:70` | time-sensitive fact candidate | 域名通常按周期续费，首年促销价与续费价可能不同。隐私保护、溢价域名、转移和赎回也可能产生费用。托管平台可能按构建分钟、带宽、请求、函数执行、团队席位或额外功能收费。免费额度、超额价格和休眠规则会调整。 |
| 028 | `chapters/028-自定义域名-dns-https-费用与地区差异.md:72` | time-sensitive fact candidate | 真正购买前打开注册商和平台官方定价页，记录币种、税费、续费价、配额与超额处理，并写明查询日期。为域名开启自动续费和到期提醒，保留可用支付方式。域名过期会同时影响网站、邮件、API 和登录回调。 |
| 028 | `chapters/028-自定义域名-dns-https-费用与地区差异.md:86` | time-sensitive fact candidate | 面向中国大陆公众提供网站时，服务器位置、接入服务商、域名实名、备案与具体业务许可可能影响上线流程。办理材料、地区受理流程和政策要求会变化，实际项目应在上线前查询工信部门、域名注册商、云服务商和业务主管部门的当前官方说明。涉及经营、内容许可或个人信息处理时，寻求合格专业意见。本书不把某次查询结果写成永久规则。 |
| 029 | `chapters/029-后端为什么存在以及-api-怎样工作.md:50` | time-sensitive fact candidate | 价格、折扣、用户 ID、角色和库存同理。请求里带了 `role: admin`，后端不能相信。请求里带了 `price: 1`，后端也不能照收。后端应从已验证身份、数据库状态和服务端配置中重新计算。 |
| 029 | `chapters/029-后端为什么存在以及-api-怎样工作.md:78` | time-sensitive fact candidate | 版本管理不一定从 `/v1` 开始，也可以通过兼容字段、响应扩展和发布窗口完成。关键是别让旧客户端突然读不到必需字段。新增字段通常安全，删除字段和改变含义风险更高。错误结构也要稳定。前端、小程序和 App 都要能根据错误码给用户明确提示。 |
| 030 | `chapters/030-rest-websocket-身份认证和权限控制.md:35` | time-sensitive fact candidate | OAuth 2.0 主要处理委托授权，OpenID Connect 在其上提供身份认证。做第三方登录时，要按身份提供商的登录协议验证身份结果，不能把拿到任意访问令牌当作已经证明用户身份。业务资料仍要在本系统里建模。第三方返回的邮箱、头像和昵称不能自动变成业务权限。账号合并、重复邮箱和撤销授权都要有流程。 |
| 032 | `chapters/032-数据库迁移-连接-备份和恢复.md:39` | time-sensitive fact candidate | RPO 表示最多能接受丢失多久的数据。RTO 表示希望多久恢复服务。个人作品页可以容忍较长时间，支付、订单和企业协作系统通常不能。目标越高，费用和流程越复杂。不要只买一个备份功能就以为满足业务要求。 |
| 033 | `chapters/033-文件上传-对象存储-邮件-推送和-ai-api.md:3` | time-sensitive fact candidate | 现代应用的数据不只在数据库。用户上传图片，对象存储保存文件；邮件服务发送确认信；推送服务把通知送到设备；AI API 接收任务并返回生成结果。每增加一个外部服务，就增加权限、费用、失败和恢复边界。 |
| 033 | `chapters/033-文件上传-对象存储-邮件-推送和-ai-api.md:21` | time-sensitive fact candidate | 客户端先向后端请求上传。后端验证登录、用途、大小上限和配额，生成对象 Key 与临时上传授权。客户端把文件直接上传对象存储，减少后端转发大文件的负担。上传完成后通知后端。后端确认对象存在、大小和类型，必要时进入病毒扫描、图片解码和转码队列。验证完成前状态为待处理，不对其他用户公开。 |
| 033 | `chapters/033-文件上传-对象存储-邮件-推送和-ai-api.md:41` | time-sensitive fact candidate | AI API 和邮件、支付一样，是外部服务调用。请求会消耗费用，响应可能慢，结果需要验证。不要把服务端密钥放进浏览器、App 或小程序前端。客户端请求自己的后端，后端检查身份、配额、内容范围和费用，再调用 AI 服务。 |
| 033 | `chapters/033-文件上传-对象存储-邮件-推送和-ai-api.md:47` | time-sensitive fact candidate | 长任务不要压在一次请求里。用户提交文件总结，后端创建任务并返回 ID。工作进程调用 AI API，记录状态、费用、模型名称和错误。前端轮询或订阅任务状态。超时、重试和取消都要有规则。重复调用可能重复扣费，所以任务 ID 和幂等键很重要。 |
| 033 | `chapters/033-文件上传-对象存储-邮件-推送和-ai-api.md:53` | time-sensitive fact candidate | 每个外部服务至少记录服务名、用途、密钥位置、调用方、费用指标、日志入口、失败提示、重试规则和负责人。表中不写明文密钥。供应商状态页只能说明供应商自报状态，不能替代自己的请求日志。 |
| 033 | `chapters/033-文件上传-对象存储-邮件-推送和-ai-api.md:57` | time-sensitive fact candidate | 费用也要进入设计。上传文件按容量和流量收费，邮件按发送量和信誉影响成本，推送可能有平台限制，AI API 按输入输出和工具调用计费。上线前设置预算或用量告警。账单突然增长时，按用户、接口、任务和供应商拆分，不先删除生产资源。 |
| 033 | `chapters/033-文件上传-对象存储-邮件-推送和-ai-api.md:71` | time-sensitive fact candidate | 文件保留期限要和业务一致。用户删除头像后，公开 URL 应失效，数据库记录应更新，对象存储和缩略图应进入删除流程。备份中的残留要按政策处理。临时上传失败的文件可以更快清理，审计材料可能需要保留更久。不要让所有对象都永久保存。 |
| 033 | `chapters/033-文件上传-对象存储-邮件-推送和-ai-api.md:101` | time-sensitive fact candidate | 能画出文件从客户端到对象存储、数据库记录和访问 URL 的路径。知道文件名、类型、大小、扫描和孤立对象清理都要处理。能区分事务邮件、营销邮件和推送提醒。AI API 调用有服务端密钥、任务状态、费用记录和输出验证。每个外部服务都有负责人、日志、重试和下线办法。 |
| 033 | `chapters/033-文件上传-对象存储-邮件-推送和-ai-api.md:103` | time-sensitive fact candidate | AI 可以帮你设计上传状态机、通知清单和 AI 任务表。不要把真实文件、用户资料、邮件密钥、推送证书和 AI API Key 交给它。正式接入前，用测试账号、测试文件和供应商沙盒验证成功、失败、重试和费用。下一章讨论 Supabase、Firebase 与后端即服务。 |
| 034 | `chapters/034-supabase-firebase-与后端即服务.md:3` | time-sensitive fact candidate | 后端即服务常缩写为 BaaS。供应商把数据库、身份认证、文件存储、实时通信和函数等能力组合起来，通过控制台、SDK 和 API 提供。个人项目可以更快得到可用后端，仍要设计数据、权限、费用和恢复。 |
| 034 | `chapters/034-supabase-firebase-与后端即服务.md:15` | time-sensitive fact candidate | 控制台让初学者直观看表、用户和文件。生产维护仍需要迁移文件、权限规则、备份验证和变更记录。BaaS 缩短起步时间，也把更多组件放到同一供应商。账号、区域、规则和费用配置出错时，影响会集中。 |
| 034 | `chapters/034-supabase-firebase-与后端即服务.md:45` | time-sensitive fact candidate | ## 费用和生命周期 |
| 034 | `chapters/034-supabase-firebase-与后端即服务.md:47` | time-sensitive fact candidate | BaaS 的免费额度适合试验，不适合当作长期承诺。数据库读写、实时监听、函数调用、存储容量、下载流量、认证短信、推送和日志都可能计费。价格和额度会变化，正式项目按当前官方控制台确认。 |
| 034 | `chapters/034-supabase-firebase-与后端即服务.md:49` | time-sensitive fact candidate | 实时监听尤其容易失控。一个列表页面若给每个卡片都开监听，用户一多就会产生大量连接和读取。页面离开后要取消订阅。后台标签页、移动端重连和小程序生命周期也会影响连接数量。费用排查时，按页面、用户动作、监听数量和读取次数拆分。 |
| 034 | `chapters/034-supabase-firebase-与后端即服务.md:89` | time-sensitive fact candidate | 反过来，若团队只有一两个人，功能是登录、资料、少量文件和实时状态，BaaS 可能比自建后端安全。前提是权限规则认真写，备份和费用认真看。工具替你省掉机器维护，省不掉权限设计。 |
| 034 | `chapters/034-supabase-firebase-与后端即服务.md:103` | time-sensitive fact candidate | 能说清 BaaS 替你运行了哪些组件，哪些责任仍在项目方。能区分 Supabase 的 PostgreSQL 与 RLS、Firebase 的文档模型与 Security Rules。认证和数据权限分别测试。实时监听、函数重试、存储、短信和 AI 调用都有费用边界。备份、恢复、导出和退出计划按组件列出。 |
| 034 | `chapters/034-supabase-firebase-与后端即服务.md:105` | time-sensitive fact candidate | AI 可以帮你整理数据模型、规则测试矩阵和费用风险表。不要把服务角色 Key、Firebase Admin 凭据、真实用户导出和生产规则控制权交给它。上线前用多个测试账号、目标客户端和真实规则跑权限测试。下一章比较托管方案、自建方案和平台依赖。 |
| 035 | `chapters/035-托管方案-自建方案和平台依赖.md:11` | time-sensitive fact candidate | 应用至少包含计算、数据库、文件存储、域名、TLS、身份、日志、备份、监控和费用。托管平台可能处理服务器硬件、操作系统、数据库进程和自动备份。你仍处理数据模型、权限、密钥、业务监控和恢复验证。 |
| 035 | `chapters/035-托管方案-自建方案和平台依赖.md:19` | time-sensitive fact candidate | 自建数据库或服务器意味着你要安装受支持版本、配置存储与内存、限制网络、创建受限用户、监控连接与查询、安排备份和升级。磁盘满会让写入失败，证书过期会断开连接，系统补丁需要维护窗口。单台服务器故障时，应用和数据库可能一起离线。 |
| 035 | `chapters/035-托管方案-自建方案和平台依赖.md:33` | time-sensitive fact candidate | ## 免费额度和服务等级怎样看 |
| 035 | `chapters/035-托管方案-自建方案和平台依赖.md:35` | time-sensitive fact candidate | 免费额度适合试验和早期验证。正式项目要看当前官方价格、超额处理、休眠规则、限制项、团队席位、日志保留、备份保留和支持方式。价格会变，本书不写永久数字。创建项目时记录查询日期、预计用量和告警入口。 |
| 035 | `chapters/035-托管方案-自建方案和平台依赖.md:60` | time-sensitive fact candidate | 供应商停服、账号被锁、价格大涨、地区不可用和产品能力改变，都属于平台风险。预案可以很朴素。谁接收通知，数据如何导出，临时公告放哪里，关键服务能否降级，费用上限到哪里必须人工确认。 |
| 035 | `chapters/035-托管方案-自建方案和平台依赖.md:74` | time-sensitive fact candidate | 托管服务也会变化。数据库版本升级、运行时弃用、免费额度调整、证书策略变化和区域维护都可能影响项目。把这些变化放进日历。收到供应商邮件后，记录影响组件、截止日期、测试环境和负责人。不要等到旧运行时停止支持当天再改。 |
| 035 | `chapters/035-托管方案-自建方案和平台依赖.md:90` | time-sensitive fact candidate | 退出清单至少包含三类验收：新服务能读旧数据，用户能继续登录，旧平台的收费资源和订阅已逐项处理。停止应用不一定停止计费，保留的磁盘、快照、存储和套餐仍可能产生费用；应核对最终账单，并确认没有非预期的新费用。若登录供应商改变，还要处理用户标识映射和会话失效。若文件域名改变，还要处理旧链接、缓存和搜索引擎引用。 |
| 035 | `chapters/035-托管方案-自建方案和平台依赖.md:104` | time-sensitive fact candidate | 能列出计算、数据库、文件、域名、身份、日志、备份、监控和费用的负责人。知道托管减少操作量，不取消数据模型、权限和恢复责任。自建前能说明补丁、备份、监控和故障处理怎样做。平台依赖有分层和出口。删除或迁移前有清单。 |
| 035 | `chapters/035-托管方案-自建方案和平台依赖.md:106` | time-sensitive fact candidate | AI 可以帮你把方案拆成责任表、费用表和退出清单。不要把生产账号、账单权限、密钥和客户数据交给它。真正选择平台前，由负责人确认价格、地区、备份、支持、合规和下线办法。下一章进入 VPS 和云服务器购买参数。 |
| 036 | `chapters/036-vps-云服务器及购买时需要看的参数.md:26` | time-sensitive fact candidate | - 监控进程、磁盘、内存和费用 |
| 036 | `chapters/036-vps-云服务器及购买时需要看的参数.md:81` | time-sensitive fact candidate | ## 采购记录和费用 |
| 036 | `chapters/036-vps-云服务器及购买时需要看的参数.md:83` | time-sensitive fact candidate | 购买决策要留下记录。项目名称、服务商、地区、规格、镜像、磁盘、网络、价格、付款账户、负责人、用途、备份方式和到期或删除条件都写清。价格、免费权益和活动条款会变化，记录查询日期。 |
| 036 | `chapters/036-vps-云服务器及购买时需要看的参数.md:109` | time-sensitive fact candidate | 删除 VPS 前同样要走清单。确认数据已备份并可恢复，域名不再指向它，计划任务已迁移，日志已导出，账单不会继续产生磁盘或快照费用。删除机器可能不删除云盘、快照和公网 IP，费用入口要逐项检查。 |
| 036 | `chapters/036-vps-云服务器及购买时需要看的参数.md:113` | time-sensitive fact candidate | 服务器不是买完就静止。Ubuntu、Debian、Node.js、Python、PostgreSQL、Nginx 和 OpenSSL 都有支持周期。选择镜像时先看长期支持版本，记录当前系统、运行时和数据库版本。上线后每月看一次安全更新，重大漏洞单独处理。 |
| 036 | `chapters/036-vps-云服务器及购买时需要看的参数.md:123` | time-sensitive fact candidate | AI 可以帮你比较参数、整理采购记录和生成验收清单。不要把云账号登录、SSH 私钥、Root 密码、账单权限和生产备份交给它。真正购买前，由负责人确认价格、地区、合规、备份、告警和删除条件。第五卷到这里结束。下一卷进入 Linux 与服务器运行，开始处理已经买到的机器。 |
| 039 | `chapters/039-软件包-进程-端口-磁盘和内存.md:17` | time-sensitive fact candidate | 端口是服务等待连接的位置。在常见 Linux 系统上，`ss -lntp` 可以看 TCP 监听，部分进程信息需要相应权限才能显示。监听 `127.0.0.1` 表示只接受本机 IPv4 连接。监听 `0.0.0.0` 表示所有 IPv4 网卡都有可能接入，最终能否从公网到达还取决于安全组、系统防火墙和路由。应用只给同机反向代理访问时，通常监听本机地址即可。… |
| 039 | `chapters/039-软件包-进程-端口-磁盘和内存.md:59` | time-sensitive fact candidate | 带宽满时，用户会觉得页面慢、上传失败、SSH 卡顿。查看流量方向也很重要。出站流量可能来自文件下载、备份、镜像拉取或异常请求。入站流量可能来自上传、攻击或爬虫。费用按流量计费的平台，还要把带宽和账单一起看。 |
| 039 | `chapters/039-软件包-进程-端口-磁盘和内存.md:71` | time-sensitive fact candidate | 假设用户访问域名看到 502。维护者登录服务器，发现应用进程在，日志也没有明显错误。继续查端口，应用监听在 `127.0.0.1:3001`。Nginx 配置却转发到 `127.0.0.1:3000`。代理连接不到预期后端，于是返回 502。 |
| 041 | `chapters/041-防火墙-caddy-nginx-域名与-https.md:91` | time-sensitive fact candidate | 代理配置可以给 AI 看，但要去掉真实域名、内网地址和证书路径中的敏感部分。把域名改成 `example.com`，把后端地址改成 `127.0.0.1:3000` 这类示例。保留结构，删掉秘密。 |
| 042 | `chapters/042-部署-更新-回滚-备份和恢复.md:35` | time-sensitive fact candidate | 备份任务也会失败。磁盘满、权限变更、密钥失效、费用欠费和网络中断都会影响备份。备份任务要有日志和告警。只在事故后打开备份目录，才发现最近一次成功是几个月前，这种痛最好提前避免。 |
| 042 | `chapters/042-部署-更新-回滚-备份和恢复.md:63` | time-sensitive fact candidate | 备份保留时间要有规则。保留太短，事故时找不到需要的时间点。保留太长，会增加费用和隐私风险。按业务要求、合规要求和恢复需求制定。删除备份前确认没有正在调查的事故或审计需求。 |
| 042 | `chapters/042-部署-更新-回滚-备份和恢复.md:65` | time-sensitive fact candidate | 跨账号备份能防一类事故。生产账号被锁、账单异常或权限误删时，同账号备份可能也拿不到。重要项目可以把备份复制到独立账号或独立区域。这样做会增加费用和管理工作，需要写入责任清单。 |
| 042 | `chapters/042-部署-更新-回滚-备份和恢复.md:73` | time-sensitive fact candidate | 练习还要包含删除。停止服务，清理产物，保留备份，删除临时域名或测试记录。很多人会部署，不会干净下线。下线不完整会留下费用、端口、证书、旧数据和安全入口。 |
| 043 | `chapters/043-自建服务器增加了哪些长期责任.md:7` | time-sensitive fact candidate | 管理从清单开始。至少记录服务器、域名、证书、数据库、对象存储、邮件服务、监控、备份位置、云账号、账单联系人和负责人。每项写明在哪里登录，谁有权限，费用怎样产生，故障时看哪里。 |
| 043 | `chapters/043-自建服务器增加了哪些长期责任.md:41` | time-sensitive fact candidate | 迁回托管平台前，要看数据出口、停机窗口、费用、权限模型和回滚路径。不能只看到“更省心”。托管会减少机器维护，也会带来供应商限制。选择哪边，取决于团队能力、合规要求、预算和业务风险。 |
| 043 | `chapters/043-自建服务器增加了哪些长期责任.md:55` | time-sensitive fact candidate | 供应商邮件要有人看。价格调整、接口弃用、证书策略变化和区域维护，通常会提前通知。若通知发到离职同事邮箱，项目会在截止当天才知道。团队邮箱、工单系统或共享收件规则，比个人邮箱更稳。 |
| 043 | `chapters/043-自建服务器增加了哪些长期责任.md:75` | time-sensitive fact candidate | 自建服务器的费用不只是一台机器。公网流量、云盘、快照、备份、对象存储、日志、监控、短信和邮件都可能单独计费。账单里某项突然上涨，通常说明系统行为变了。可能是下载变多，日志变多，也可能是备份没有清理。 |
| 045 | `chapters/045-镜像-容器-dockerfile-和-registry.md:27` | time-sensitive fact candidate | 镜像标签方便人读，比如 `app:1.4.2`、`app:staging`。标签可以被覆盖。摘要指向具体镜像内容，更稳定。生产发布记录最好写清镜像完整名称、标签和摘要。只写 `latest`，以后很难知道当时跑的是哪一份。 |
| 049 | `chapters/049-更新-回滚-清理与数据丢失风险.md:35` | time-sensitive fact candidate | 删除之后也要验收。确认应用能启动，数据库能读写，上传文件仍在，回滚所需镜像还在，备份没有被删。云盘、快照、对象存储和 Registry 费用也要看。删了容器，不一定删了卷。删了机器，也不一定删了快照。 |
| 050 | `chapters/050-docker-虚拟机和-kubernetes-的边界.md:101` | time-sensitive fact candidate | Kubernetes 能按 CPU 或自定义指标调整副本。应用必须支持多副本，状态不能只放本地容器。数据库连接、会话、队列和第三方配额会随副本增加。扩容 Web 可能把数据库先压垮。错误指标会来回扩缩，造成启动风暴和费用。单机项目可以先手工扩规格，复杂度更低。 |
| 050 | `chapters/050-docker-虚拟机和-kubernetes-的边界.md:121` | time-sensitive fact candidate | 托管 Kubernetes 可能对控制面、节点、负载均衡、公网 IP、磁盘、快照、出站和日志分别计费。为了高可用常需多节点和多区域资源，空闲容量也产生费用。价格与免费权益按采购日官方资料核对，本书不提供永久数字。 |
| 050 | `chapters/050-docker-虚拟机和-kubernetes-的边界.md:125` | time-sensitive fact candidate | 一些平台接受 Dockerfile 或镜像，替你管理主机、证书、扩缩和日志入口。它位于 Compose 与自管 Kubernetes 之间。平台限制端口、持久磁盘、后台任务和区域，需要核对。费用可能按实例或使用量。 |
| 051 | `chapters/051-app-客户端-后端和本地数据.md:102` | time-sensitive fact candidate | - 删除账号与删除 App 的结果在界面和隐私政策中一致。 |
| 052 | `chapters/052-flutter-项目-依赖-debug-profile-和-release.md:32` | time-sensitive fact candidate | version: 1.2.0+17 |
| 052 | `chapters/052-flutter-项目-依赖-debug-profile-和-release.md:35` | time-sensitive fact candidate | sdk: ^3.5.0 |
| 052 | `chapters/052-flutter-项目-依赖-debug-profile-和-release.md:40` | time-sensitive fact candidate | http: ^1.2.0 |
| 052 | `chapters/052-flutter-项目-依赖-debug-profile-和-release.md:85` | time-sensitive fact candidate | `flutter clean` 删除构建产物和部分缓存，适合解决旧产物干扰、原生构建状态错乱或依赖变更后仍引用旧文件的问题。它不会修复包名填错、签名密钥丢失、权限说明缺失、后端地址错误和商店政策问题。 |
| 052 | `chapters/052-flutter-项目-依赖-debug-profile-和-release.md:97` | time-sensitive fact candidate | 环境名称也要谨慎。`prod`、`production`、`release`、`online` 混用时，人会选错。发布说明里直接写后端域名、数据库项目名的脱敏标识、支付模式和推送项目，比只写“正式环境”更可靠。审核和内部测试使用测试环境时，要确认测试数据、隐私政策和审核说明也指向这套环境。 |
| 053 | `chapters/053-apk-aab-包名-版本号和-android-签名.md:3` | time-sensitive fact candidate | Android 发布最容易被一个词骗住。很多人说“打个包”，像是把项目压缩一下就能交给用户。真实发布至少包含应用身份、构建产物、版本递增、签名连续性、目标系统要求和商店政策。任何一项混乱，都会让上传、安装或后续更新失败。 |
| 053 | `chapters/053-apk-aab-包名-版本号和-android-签名.md:21` | time-sensitive fact candidate | `versionName` 通常展示给用户，例如 `1.2.0`。`versionCode` 是 Android 用于判断升级顺序的整数。每个要上传到商店的新构建都应使用更高 versionCode。重命名 AAB 文件、改 Release notes、重新压缩，都不能让已用过的 versionCode 再次可用。 |
| 053 | `chapters/053-apk-aab-包名-版本号和-android-签名.md:64` | time-sensitive fact candidate | APK 适合本地安装、企业内部分发或特定侧载场景。AAB 适合交给 Google Play 处理设备拆分、优化和商店分发。面向普通公众时，商店分发能提供更新通道、签名托管、崩溃入口和政策流程。侧载 APK 会把版本传播、更新提醒、来源可信和安全支持责任更多放回发布者身上。 |
| 053 | `chapters/053-apk-aab-包名-版本号和-android-签名.md:88` | time-sensitive fact candidate | minSdk、compileSdk 和 targetSdk 经常被混在一起。minSdk 表示应用声称支持的最低 Android 版本。compileSdk 是编译时使用的平台 API。targetSdk 告诉系统应用按哪个行为级别适配，也会受到商店政策要求影响。 |
| 053 | `chapters/053-apk-aab-包名-版本号和-android-签名.md:96` | time-sensitive fact candidate | Android 上传错误通常落在四层。第一层是应用身份，例如包名不匹配、应用记录选错、versionCode 已使用。第二层是签名，例如上传证书与控制台记录不一致，或第三方服务只登记了调试证书。第三层是构建内容，例如缺少图标、Manifest 权限冲突、原生库格式不符合要求。第四层是政策任务，例如目标 API、数据安全、广告声明和内容分级。 |
| 053 | `chapters/053-apk-aab-包名-版本号和-android-签名.md:98` | time-sensitive fact candidate | 先把错误放到层里，再决定动作。versionCode 已使用时，提高版本代码并重新构建。包名不匹配时，核对打开的是不是正确应用，不要修改已发布应用身份来迁就一次上传。签名不匹配时，查 keystore、上传证书和 Play 应用签名设置。政策任务缺失时，回到真实功能和表单，不要删除代码里仍在使用的权限来让提示消失。 |
| 053 | `chapters/053-apk-aab-包名-版本号和-android-签名.md:102` | time-sensitive fact candidate | 如果从 AAB 生成的 APK 在本地能安装，商店仍拒绝，不要急着怀疑商店。商店检查的是另一组条件，包括应用记录、签名、目标 API、设备目录、政策表单和分发轨道。本地安装只证明设备接受了这组安装包，不能代替 Play 分发测试。 |
| 054 | `chapters/054-google-play-内部测试与发布流程.md:5` | time-sensitive fact candidate | ## 一个模型，身份、制品、轨道、用户与政策 |
| 054 | `chapters/054-google-play-内部测试与发布流程.md:7` | time-sensitive fact candidate | Play Console 开发者账号代表发布主体，其中可以管理多个应用。应用由包名长期识别；AAB 还带 versionName、versionCode 和签名关系。轨道决定谁可以取得版本，测试者的 Google 账号、国家/地区和设备条件决定他是否在范围内。政策与内容表单再决定某个版本能否向更广人群推进。 |
| 054 | `chapters/054-google-play-内部测试与发布流程.md:15` | time-sensitive fact candidate | 5. **政策边界**　账号资格、目标 API、数据披露、内容、地区和审核要求。 |
| 054 | `chapters/054-google-play-内部测试与发布流程.md:27` | time-sensitive fact candidate | 账号权限按职责分配。上传 AAB 的人不一定需要管理付款、用户或删除应用；不要共享同一个 Google 密码。AI 可以整理字段、检查项目配置和准备草稿，不能替账号持有人决定法律主体、市场、价格，也不能替授权人员执行最终公开发布。 |
| 054 | `chapters/054-google-play-内部测试与发布流程.md:57` | time-sensitive fact candidate | 它不能证明应用符合所有生产政策，不能覆盖所有设备、语言和网络，也不会自动满足某类账号的生产准入条件。内部测试者都是熟悉项目的人时，还可能绕过新用户才会遇到的说明和权限问题。 |
| 054 | `chapters/054-google-play-内部测试与发布流程.md:61` | time-sensitive fact candidate | > “Release 已发布到内部测试”证明平台接受了这次轨道变更；“测试者安装成功”只证明该账号、设备和时刻的分发与安装成立；“核心流程通过”也只覆盖实际执行的步骤。生产发布仍需政策、商店资料、后端容量、支持与授权人的独立确认。 |
| 054 | `chapters/054-google-play-内部测试与发布流程.md:77` | time-sensitive fact candidate | Release notes 不写“修复若干问题”，而要告诉测试者该触碰什么。例如从 1.1.0 升级到 1.2.0，确认旧记录仍在；离线新增一条练习记录后恢复网络；拒绝一次通知权限，核心功能仍可使用。已知限制也应写出，避免把预期未完成误报成新回归。 |
| 054 | `chapters/054-google-play-内部测试与发布流程.md:103` | time-sensitive fact candidate | - **权限或政策警告**　回到真实功能、SDK 和数据流；删除披露文字不能改变应用实际收集。 |
| 054 | `chapters/054-google-play-内部测试与发布流程.md:111` | time-sensitive fact candidate | > **政策时效** |
| 054 | `chapters/054-google-play-内部测试与发布流程.md:123` | time-sensitive fact candidate | 商店名称、说明、图标、截图、联系邮箱和隐私政策应与当前 Release 一致，不含真实用户数据。审核需要登录时提供受限测试账号与进入步骤，不能交出生产管理员账号。选择国家、价格、订阅和购买还会带来支付、税务、退款和支持责任，不应默认首日全球开放。 |
| 054 | `chapters/054-google-play-内部测试与发布流程.md:143` | time-sensitive fact candidate | 如果只需要验证第一条分发链，现在可以跳过开放测试、定价、managed publishing、Android vitals 深入分析和完整生产申请；先把包名、签名、versionCode、测试账号与一次真机升级做对。准备扩大范围时，再按当日控制台逐项补齐政策和内容责任。 |
| 054 | `chapters/054-google-play-内部测试与发布流程.md:149` | time-sensitive fact candidate | > Google Play 这一项暂用[YouTube 操作演示](https://www.youtube.com/watch?v=adt9A8125S4)，原因及备用说明见[视频索引](../frontmatter/videos.md)。跟做时只使用独立练习应用，目标停在内部测试轨道，不把视频里的商店说明、政策答案和生产范围照搬到自己的账号里。 |
| 055 | `chapters/055-ios-macos-xcode-证书和-provisioning-profile.md:48` | time-sensitive fact candidate | 版本号和构建号也要对应。用户看到的版本号可以是 `1.2.0`。构建号用于区分同一版本下多次上传。App Store Connect 对构建号有递增要求。每次重新上传修复包，都要提高构建号，并保存源码提交和 Archive。 |
| 055 | `chapters/055-ios-macos-xcode-证书和-provisioning-profile.md:72` | time-sensitive fact candidate | 相机、相册、定位、麦克风和蓝牙等敏感访问，通常需要在 Info.plist 中填写对应的用途说明；推送通知走用户授权请求与相应能力配置，不能笼统当作一条 Info.plist 用途说明。文案要解释具体功能，不要写“需要权限以正常使用”。审核人员会把文案、实际调用和隐私政策一起看。 |
| 055 | `chapters/055-ios-macos-xcode-证书和-provisioning-profile.md:90` | time-sensitive fact candidate | 测试时至少用一台不连公司网络的真机走完整流程。登录、验证码、图片上传、支付沙箱、推送、隐私政策和客服入口都要能访问。若应用同时提供微信登录、小程序入口或公众号服务，后端账号绑定和注销路径要一致。不要让 iOS 账号、微信账号和自有账号各自删除一半数据。 |
| 055 | `chapters/055-ios-macos-xcode-证书和-provisioning-profile.md:100` | time-sensitive fact candidate | 站外分发时，下载页本身也成为发布面。用户需要知道版本、发布日期、校验值、最低系统、安装方法和隐私政策。自动更新器要签名并保护更新源，不能让任何人替换下载包。崩溃符号和发布记录同样要保存。 |
| 056 | `chapters/056-archive-testflight-与-app-store-connect.md:69` | time-sensitive fact candidate | 版本与构建　1.2.0 (18) |
| 056 | `chapters/056-archive-testflight-与-app-store-connect.md:70` | time-sensitive fact candidate | 设备与系统　iPhone 15，iOS 19.1 |
| 056 | `chapters/056-archive-testflight-与-app-store-connect.md:79` | time-sensitive fact candidate | 同一版本号下可能上传多个 build。测试反馈只写 `1.2.0`，无法判断问题属于 build 17 还是 build 18。发布记录要把每个 build 的上传时间、处理结果、测试组、设备、核心结果和未解决问题分开写。 |
| 056 | `chapters/056-archive-testflight-与-app-store-connect.md:91` | time-sensitive fact candidate | 版本页面保存描述、关键词、截图、推广文本、支持 URL、隐私政策和审核信息。Build 区域选择一个已上传二进制。修改描述不会改变二进制，选择新 build 也不会自动更新截图。提交前同时核对。默认语言修好了，其他本地化语言仍可能保留旧承诺。 |
| 056 | `chapters/056-archive-testflight-与-app-store-connect.md:97` | time-sensitive fact candidate | 地区和价格也会影响发布判断。某些功能只在特定国家可用，审核人员却可能从另一地区进入。订阅、付费下载和应用内购买涉及协议、税务和退款。免费应用先公开，后续再加付费功能，也要提前考虑账号主体和用户承诺。发布按钮不是技术按钮，背后还有支持和经营责任。 |
| 056 | `chapters/056-archive-testflight-与-app-store-connect.md:103` | time-sensitive fact candidate | 提交审核前，最好让两个人按不同角度看同一个候选。第一人看二进制。Bundle ID、Version、Build、签名、后端环境、核心流程、升级测试、符号文件和 Archive 是否一致。第二人看商店资料。截图、描述、隐私政策、审核账号、联系信息、价格地区、发布方式和测试说明是否对应当前 build。 |
| 057 | `chapters/057-商店素材-权限-隐私政策和审核反馈.md:1` | time-sensitive fact candidate | # 商店素材、权限、隐私政策和审核反馈 |
| 057 | `chapters/057-商店素材-权限-隐私政策和审核反馈.md:3` | time-sensitive fact candidate | 应用商店审核会同时看用户会看到什么、应用会做什么、数据怎样流动、开发者怎样承担责任。代码质量很重要，提交材料还要让截图、描述、权限弹窗、隐私政策、SDK 行为和审核账号彼此一致。 |
| 057 | `chapters/057-商店素材-权限-隐私政策和审核反馈.md:36` | time-sensitive fact candidate | 商店文案尽量写可验证的能力。少写“安全可靠、智能高效”，多写用户能做什么、数据在哪里处理、失败时有什么退路。涉及健康、金融、法律、儿童、VPN、新闻或用户生成内容时，截图和描述还可能触发额外资质与政策要求。 |
| 057 | `chapters/057-商店素材-权限-隐私政策和审核反馈.md:46` | time-sensitive fact candidate | ## 隐私政策不能替代码撒谎 |
| 057 | `chapters/057-商店素材-权限-隐私政策和审核反馈.md:48` | time-sensitive fact candidate | 隐私政策至少让普通用户知道收集什么、为什么收集、与谁共享、保存多久、怎样保护、如何访问或删除，以及如何联系开发者。政策页面要公开可访问，移动端可读，审核期间保持在线。只放一个需要登录的云文档链接，审核人员和用户都可能打不开。 |
| 057 | `chapters/057-商店素材-权限-隐私政策和审核反馈.md:50` | time-sensitive fact candidate | 政策不是免责声明。写“可能收集任何信息”不能替代具体说明，也不能让不必要收集变得合理。应用内应有容易找到的隐私入口。账号删除、导出、撤回同意和联系渠道要能从界面或说明中走到。 |
| 057 | `chapters/057-商店素材-权限-隐私政策和审核反馈.md:60` | time-sensitive fact candidate | App Store Connect 的 App Privacy 问卷也要覆盖自有代码和第三方合作方代码的数据实践。数据类型、用途、是否关联用户、是否用于跟踪，都应来自事实表。应用版本、SDK 或远程配置改变后，问卷和隐私政策要一起复核。 |
| 057 | `chapters/057-商店素材-权限-隐私政策和审核反馈.md:68` | time-sensitive fact candidate | SDK 更新可能改变数据行为。依赖升级审查不能只看编译是否通过，还要看权限、隐私说明、目标系统要求和商店政策。封版前查官方页面，不依赖两年前教程。 |
| 057 | `chapters/057-商店素材-权限-隐私政策和审核反馈.md:78` | time-sensitive fact candidate | 素材也要做版本管理。图标、截图、商店描述、隐私政策、审核说明和客服模板，都应对应一个源码提交或构建号。运营单独改了描述，开发者单独换了 build，最终很容易出现“资料说有，包里没有”的情况。每次提交前，把素材版本和所选 build 放在同一张清单里。 |
| 057 | `chapters/057-商店素材-权限-隐私政策和审核反馈.md:108` | time-sensitive fact candidate | 涉及付款和订阅时，商店会关心用户在哪里购买、如何恢复、如何取消、价格怎样展示、试用怎样结束。应用内说明要与真实结算一致。外部购买链接与引导方式受平台、地区、应用类型和当前政策约束；上线前按目标商店的当日规则核对。测试价格、沙箱环境和正式价格也不能混在同一份截图里。 |
| 057 | `chapters/057-商店素材-权限-隐私政策和审核反馈.md:118` | time-sensitive fact candidate | 审核反馈可能指向应用行为、崩溃、元数据、隐私、账号访问、付款、内容或政策。先保存原文和截图，再确认对应版本。应用崩溃时，用反馈设备、系统、build 和步骤复现。元数据不准确时，更新说明、截图和所有语言版本。隐私披露不一致时，回到数据流和 SDK。 |
| 057 | `chapters/057-商店素材-权限-隐私政策和审核反馈.md:128` | time-sensitive fact candidate | 建立一个小规则。每次版本评审问四件事。有没有新增系统权限。有没有新增数据接收者。有没有改变用户承诺。有没有改变审核进入路径。四个问题任何一个答案为是，就回到事实表、隐私政策、商店表单和审核说明。 |
| 057 | `chapters/057-商店素材-权限-隐私政策和审核反馈.md:130` | time-sensitive fact candidate | 政策本身也会变化。平台更新 SDK 要求、目标 API、儿童保护、账号删除、隐私标签和内容分级时，旧版本也可能需要处理。把核对日期写进发布记录，能说明当时依据。真正执行时仍以当前平台页面为准。 |
| 057 | `chapters/057-商店素材-权限-隐私政策和审核反馈.md:143` | time-sensitive fact candidate | 隐私政策或隐私保护指引： |
| 057 | `chapters/057-商店素材-权限-隐私政策和审核反馈.md:148` | time-sensitive fact candidate | 发布当天政策核对日期： |
| 057 | `chapters/057-商店素材-权限-隐私政策和审核反馈.md:153` | time-sensitive fact candidate | 商店与隐私专题的边界也很清楚。你不需要背下所有政策条款，但要能证明截图、描述、权限、SDK、数据披露、审核账号和实际代码说的是同一个产品。每次新增 SDK、支付、广告、推送、用户内容、小程序能力或敏感权限，都要回到事实表重查。 |
| 058 | `chapters/058-app-更新-崩溃日志和后端停机.md:13` | time-sensitive fact candidate | 假设 2.0 客户端把用户姓名字段从 `name` 改成 `displayName`，后端同一天删除旧字段。仍使用 1.9 的用户会突然无法读取资料。安全顺序是后端先同时接受和返回新旧字段，再发布 2.0 客户端并逐步覆盖。观察旧版本比例下降后，后端停止写旧字段。最后经过公告和期限，才删除兼容代码。 |
| 058 | `chapters/058-app-更新-崩溃日志和后端停机.md:15` | time-sensitive fact candidate | 数据库变化也要按可兼容顺序处理。先新增可空字段或新表，让新旧程序都能运行。数据回填完成后再切读路径。直接重命名或删除旧字段，可能让旧客户端和回滚版本一起失效。兼容窗口有成本，因此要记录最低支持版本和结束时间。无限期支持所有旧版本也不现实。 |
| 058 | `chapters/058-app-更新-崩溃日志和后端停机.md:17` | time-sensitive fact candidate | App Version 面向商店和用户。API 版本面向客户端与后端约定。两者不必一一对应。一个 2.1 App 可能仍调用 `/v1` API，只增加本地界面。另一个 2.1.1 修复可能需要后端新增可选字段。后端日志应同时记录平台、App Version、Build 和 API 版本，便于判断错误是否集中在某次构建。 |
| 058 | `chapters/058-app-更新-崩溃日志和后端停机.md:39` | time-sensitive fact candidate | 假设记账 App 2.0 修改本地 SQLite schema，开发者只测试了卸载后的干净安装，没有从 1.9 升级。旧用户首次启动时，迁移脚本按错误顺序执行，读取缺失列并崩溃；新用户数据库直接创建为最新结构，测试设备都正常。 |
| 058 | `chapters/058-app-更新-崩溃日志和后端停机.md:41` | time-sensitive fact candidate | 在这个演练里，第一批用户的启动崩溃率上升。团队暂停扩大，保持后端兼容，修复迁移顺序并准备 2.0.1。再用 1.7、1.8、1.9 的测试数据库副本分别验证升级。干净安装和升级安装必须分开测试，本地数据 schema 也是发布接口。 |
| 058 | `chapters/058-app-更新-崩溃日志和后端停机.md:73` | time-sensitive fact candidate | 最低支持版本也要由后端和客服知道。客户端弹出强制升级页时，后端最好返回明确的最低 build、升级原因和可继续访问的安全功能。客服要知道哪些系统版本已经不能更新，用户如何导出数据，是否有网页或小程序临时入口。否则用户只会看到一个无法关闭的页面，支持团队也不知道怎样解释。 |
| 058 | `chapters/058-app-更新-崩溃日志和后端停机.md:75` | time-sensitive fact candidate | 强制升级不能只比较版本字符串。`1.10` 和 `1.9` 用普通文字排序可能得出错误结果。使用整数 build 或规范版本比较。不同平台的版本号也不要混算。Android versionCode、iOS build、小程序代码版本和后端 API 版本要各自清楚，再在发布记录中说明对应关系。 |
| 058 | `chapters/058-app-更新-崩溃日志和后端停机.md:103` | time-sensitive fact candidate | 版本下线也要给数据出口。有些旧设备可能无法升级到新最低系统版本。强制升级页面要保留商店入口、支持渠道和必要说明。若某地区商店不可访问，用户需要替代方案。后端返回最低版本时，使用明确 build 或规范版本比较，不要把 `1.10` 按字符串排在 `1.9` 前面或后面。 |
| 059 | `chapters/059-从现象到故障层级的统一判断方法.md:46` | time-sensitive fact candidate | 静态网站打不开，先看域名、DNS、CDN 和构建产物。按钮点击无反应，先看浏览器 Console 和前端状态。请求发出但 401，先看登录态和权限。请求 500，先看后端日志。后端说数据库连接失败，再看数据库和网络边界。App 商店上传失败，先看包名、版本号、签名和政策任务。 |
| 059 | `chapters/059-从现象到故障层级的统一判断方法.md:68` | time-sensitive fact candidate | 再问是否稳定复现。每次都失败，适合按步骤拆。偶尔失败，要记录频率、时间、数据量和外部依赖。只在晚上失败，可能和定时任务、配额、备份或网络有关。只在移动网络失败，可能和证书、DNS、IPv6 或运营商链路有关。 |
| 059 | `chapters/059-从现象到故障层级的统一判断方法.md:82` | time-sensitive fact candidate | 假设用户访问网站得到 502。先确认影响范围。所有用户访问公开域名都失败，本地开发环境正常。再看代理日志，发现请求已到 NGINX，但连接上游失败。应用进程在运行，却监听 `127.0.0.1:3001`；NGINX 配置仍转发到 `127.0.0.1:3000`。 |
| 060 | `chapters/060-console-network-build-log-和-runtime-log.md:63` | time-sensitive fact candidate | 日志级别不是情绪词。Debug 用于开发或短期诊断，Info 记录正常关键事件，Warn 表示可恢复异常，Error 表示请求或任务失败。生产环境长期开 Debug，可能带来费用、隐私和性能问题。事故临时提高日志级别后，要记录撤销时间。 |
| 060 | `chapters/060-console-network-build-log-和-runtime-log.md:89` | time-sensitive fact candidate | 日志要有保留期。保留太短，事故调查找不到证据。保留太长，费用和隐私风险增加。登录、付款、删除、上传和管理员操作日志通常比普通访问日志更重要。保留策略要写清时间、访问人、脱敏方式和删除办法。 |
| 061 | `chapters/061-服务器-docker-数据库和代理日志.md:44` | time-sensitive fact candidate | 这些命令用于读取和观察。不要在不了解影响时运行批量清理。容器日志中若只有应用启动信息，没有用户请求，先看端口映射、代理上游和应用监听地址。应用监听 `127.0.0.1`、容器暴露端口和代理转发地址不一致，常会造成 502。 |
| 061 | `chapters/061-服务器-docker-数据库和代理日志.md:82` | time-sensitive fact candidate | 队列排查先看任务是否入队，再看是否被消费。随后看重试次数、失败原因、死信队列和任务参数。不要只看 Web 进程日志。任务失败如果不断重试，可能消耗外部 API 费用，也可能给用户重复发邮件。 |
| 062 | `chapters/062-flutter-logcat-xcode-与商店上传错误.md:71` | time-sensitive fact candidate | Google Play 上传错误先看包名、versionCode、签名、目标 API、权限和政策任务。App Store 上传错误先看 Bundle ID、build number、签名、entitlements、Framework 和缺失资料。两个平台都要求版本递增，也都讨厌你临时改应用身份。 |
| 062 | `chapters/062-flutter-logcat-xcode-与商店上传错误.md:75` | time-sensitive fact candidate | AI 可以解释报错字段，帮你列核对清单。涉及开发者账号、签名资产、生产发布和政策表单时，仍由授权人员确认。商店账号和密钥不要交给 AI。 |
| 062 | `chapters/062-flutter-logcat-xcode-与商店上传错误.md:87` | time-sensitive fact candidate | 审核反馈是一种外部证据。它可能不够完整，却包含设备、系统、build、截图、政策条款和操作路径。收到反馈后，先保存原文，再确认对应版本。不要把审核意见直接翻译成“代码错了”。它可能指向测试账号、后端环境、隐私资料、权限文案或页面入口。 |
| 063 | `chapters/063-复现-调用栈-最小复现-最近改动和回滚.md:15` | time-sensitive fact candidate | 复现失败也有价值。它说明条件还不完整，或问题已经变化。记录“在 iPhone 15 iOS 19.1 build 18 未复现”，比沉默有用。 |
| 063 | `chapters/063-复现-调用栈-最小复现-最近改动和回滚.md:27` | time-sensitive fact candidate | 范围变化也要记录时间。今天只影响测试账号，明天影响生产用户，说明故障在扩大或条件改变。发布后前十分钟正常，半小时后失败，可能与缓存、队列、定时任务、配额或流量有关。 |
| 064 | `chapters/064-怎样向-ai-或开发者提交完整报错.md:22` | time-sensitive fact candidate | 标题也要具体。“系统坏了”不如“普通用户保存订单返回 500”。“App 闪退”不如“Android build 42 从 1.9 升级后启动闪退”。标题先给层级，正文再给证据。 |
| 065 | `chapters/065-secret-env-ssh-密钥和最小权限.md:42` | time-sensitive fact candidate | 4. 检查异常访问和费用。 |
| 066 | `chapters/066-防火墙-数据库暴露-输入验证和文件上传.md:38` | time-sensitive fact candidate | 前端表单校验是用户体验，服务端校验是安全边界。价格、角色、所有者 ID、库存、折扣、文件类型、数量和状态流转，都不能只相信客户端。攻击者可以绕过页面直接发请求。 |
| 066 | `chapters/066-防火墙-数据库暴露-输入验证和文件上传.md:102` | time-sensitive fact candidate | - 服务端是否重新验证价格、角色、所有者和状态。 |
| 067 | `chapters/067-备份-恢复测试-监控-费用和安全下线.md:1` | time-sensitive fact candidate | # 备份、恢复测试、监控、费用和安全下线 |
| 067 | `chapters/067-备份-恢复测试-监控-费用和安全下线.md:3` | time-sensitive fact candidate | 项目能上线，只说明它现在能工作。能不能承受误删、数据库坏掉、费用暴涨、服务商故障和安全下线，要看另一套维护能力。很多团队直到出事才发现，备份从没恢复过，监控只看 CPU，云账单没人管，旧服务器还在扣费。 |
| 067 | `chapters/067-备份-恢复测试-监控-费用和安全下线.md:7` | time-sensitive fact candidate | *图 67-1　备份、恢复测试、监控、费用和下线共同构成长期维护。等价说明见本章“先确定能承受丢多少和停多久”。* |
| 067 | `chapters/067-备份-恢复测试-监控-费用和安全下线.md:33` | time-sensitive fact candidate | 对象存储也要有版本、生命周期和删除保护。用户删除文件后，是否立即永久删除，还是进入延迟清理，要与隐私政策一致。恢复时要避免把用户已删除的数据重新公开。 |
| 067 | `chapters/067-备份-恢复测试-监控-费用和安全下线.md:49` | time-sensitive fact candidate | ## 费用监控从资源清单开始 |
| 067 | `chapters/067-备份-恢复测试-监控-费用和安全下线.md:51` | time-sensitive fact candidate | 云费用失控常来自忘记关的测试服务器、日志暴涨、对象存储外发、数据库规格过高、AI API 调用和备份保留太久。先列资源，再设预算和告警。资源清单包括云账号、项目、服务器、数据库、存储桶、CDN、队列、域名、监控、第三方 API 和商店账号费用。 |
| 067 | `chapters/067-备份-恢复测试-监控-费用和安全下线.md:53` | time-sensitive fact candidate | 账单要有负责人。个人项目也要知道每月固定成本和可能暴涨的项目。AI 功能尤其要有限额、超时、重试控制和按用户或任务的费用记录。不要让一个错误循环不断调用付费 API。 |
| 067 | `chapters/067-备份-恢复测试-监控-费用和安全下线.md:55` | time-sensitive fact candidate | 费用优化不能破坏恢复能力。删除备份、关监控、缩小数据库前，先确认影响。省下一点钱，换来无法恢复，通常不划算。 |
| 067 | `chapters/067-备份-恢复测试-监控-费用和安全下线.md:57` | time-sensitive fact candidate | 费用异常也可能是安全信号。对象存储外发突然变高，可能是公开文件被爬取。AI API 调用暴涨，可能是循环重试或密钥泄露。数据库读写量异常，可能是坏查询或恶意访问。账单告警同时服务财务、稳定性和安全。 |
| 067 | `chapters/067-备份-恢复测试-监控-费用和安全下线.md:59` | time-sensitive fact candidate | 给每个高费用资源写停止办法。队列可以暂停到什么程度，API key 怎样限额，哪些任务可以降频，哪些存储桶不能删除。事故时先限流和止血，再做长期优化。 |
| 067 | `chapters/067-备份-恢复测试-监控-费用和安全下线.md:61` | time-sensitive fact candidate | 费用预算也要分环境。测试环境不应无限调用付费 AI、短信、地图和邮件。预发布压测要设置上限和结束时间。生产环境要有每日和每月告警。免费额度用完后的价格、限速和停服方式，要在上线前知道。 |
| 067 | `chapters/067-备份-恢复测试-监控-费用和安全下线.md:63` | time-sensitive fact candidate | 如果费用突然归零，也值得看。监控、备份或支付服务可能已经停了。账单正常不是越低越好，关键是符合预期。 |
| 068 | `chapters/068-每周-每月和每季度维护清单.md:44` | time-sensitive fact candidate | - 检查预算、固定费用、闲置资源和第三方配额。 |
| 068 | `chapters/068-每周-每月和每季度维护清单.md:45` | time-sensitive fact candidate | - 检查隐私政策、商店资料和小程序隐私保护指引是否仍对应实际功能。 |
| 068 | `chapters/068-每周-每月和每季度维护清单.md:51` | time-sensitive fact candidate | 每月还适合整理文档。README、部署步骤、恢复手册、商店发布记录、隐私政策链接和客服模板，都会随着项目变化变旧。文档过期比没有文档更危险，因为它会让新人按旧步骤做错。 |
| 068 | `chapters/068-每周-每月和每季度维护清单.md:53` | time-sensitive fact candidate | 如果项目使用 AI 生成功能，每月看配额、失败率、平均费用、敏感数据过滤和模型版本变化。模型供应商、价格、上下文限制和安全策略都可能调整。记录当前使用的模型和关键参数，避免一次升级改变生产行为却无人知道。 |
| 068 | `chapters/068-每周-每月和每季度维护清单.md:77` | time-sensitive fact candidate | 安全事件、费用异常、用户投诉集中、依赖曝出漏洞、成员离职、密钥疑似泄露，也要立刻触发清单。日历是最低频率，不是最高频率。 |
| 068 | `chapters/068-每周-每月和每季度维护清单.md:132` | time-sensitive fact candidate | - 每周是否看部署、告警、费用、容量和临时变更。 |
| 070 | `chapters/070-计划-权限-diff-测试和验证证据.md:35` | time-sensitive fact candidate | 权限要分类型。读取仓库、写工作区、执行命令、访问网络、推送、部署、发邮件、改 DNS、操作数据库和产生费用不是同一授权。“可以操作项目”不能覆盖全部。一个清楚范围可以写成允许读取仓库、修改当前测试分支、运行现有测试；不允许安装依赖、联网、推送或访问生产。 |
| 070 | `chapters/070-计划-权限-diff-测试和验证证据.md:103` | time-sensitive fact candidate | 人审与自动检查关注点不同。机器擅长重复规则，人知道“这个旧字段要兼容两年”“这个地区不能启用服务”“这次费用需要财务批准”。高风险变更至少让未实施的人检查验收、Diff、证据、未验证项和回滚。旧截图、旧测试报告和只允许 Preview 的批准不能混进当前交付。 |
| 070 | `chapters/070-计划-权限-diff-测试和验证证据.md:123` | time-sensitive fact candidate | 自动检查完成后，人重点看业务规则、权限、数据、费用、用户沟通和不可逆影响。高风险变更最好由未实施的人复核。一个人维护的项目也可以把实现与评审分时进行，从原始目标重新读 Diff 和证据。 |
| 071 | `chapters/071-安全地生成配置-部署文档和回滚方案.md:5` | time-sensitive fact candidate | 安全做法是把 AI 输出当成待验证草案。配置从真实软件版本与项目结构生成，秘密在受控环境注入，部署文档说明位置、权限、预期和失败入口，回滚方案在发布前验证关键步骤。涉及生产账号、数据迁移、域名、商店和费用的最终动作都保留人工确认。 |
| 071 | `chapters/071-安全地生成配置-部署文档和回滚方案.md:41` | time-sensitive fact candidate | 权限也按步骤分配。构建任务不需要生产数据库，部署任务不需要组织所有者，健康检查不需要删除权限。准备阶段完成备份、配置验证、测试、容量和回滚检查。实施阶段上传产物、运行兼容迁移、切换少量流量或发布预览。观察阶段核对版本、健康、错误率、延迟、业务、数据和费用。 |
| 071 | `chapters/071-安全地生成配置-部署文档和回滚方案.md:59` | time-sensitive fact candidate | AI 草案中的版本、路径、服务名、账号角色和阈值都要有来源。没有来源时使用 `[待确认]`，不要填入常见默认。要求它在文档末尾列出未验证命令、需要真实账号的步骤、仅适用于某平台的内容和时间敏感政策。 |
| 072 | `chapters/072-ai-声称完成以后还要检查什么.md:55` | time-sensitive fact candidate | 功能正确却把页面从一秒变成十秒，或每次请求执行百次数据库查询，仍然没有完成。与修改前基线比较响应时间、CPU、内存、查询、包体、日志和网络。上传、AI API、对象存储、日志和第三方服务会产生费用，要验证限额、超时、重试和预算告警。免费额度与价格属于高变化信息，使用官方当前页面并注明检索日期。 |
| 072 | `chapters/072-ai-声称完成以后还要检查什么.md:79` | time-sensitive fact candidate | 性能与费用观察： |
| 072 | `chapters/072-ai-声称完成以后还要检查什么.md:106` | time-sensitive fact candidate | - 权限、秘密、依赖、性能、费用和可访问性经过检查 |
| 073 | `chapters/073-生产环境中的人工确认边界.md:3` | time-sensitive fact candidate | 生产环境承载真实用户和真实数据，也连着域名、账单和责任。AI 可以准备代码、配置、测试、部署草案和观察清单，也可以在明确授权下执行部分自动化。到了会影响用户、数据、权限、费用或不可逆状态的边界，确认必须由能够承担结果的人作出。 |
| 073 | `chapters/073-生产环境中的人工确认边界.md:9` | time-sensitive fact candidate | *图 73-1　构建、测试和预览可高度自动化；涉及秘密、数据、费用、用户和永久删除时，由对应责任人确认准确版本与窗口，发布后按阈值扩大、停止或回滚。下文提供等价说明。* |
| 073 | `chapters/073-生产环境中的人工确认边界.md:19` | time-sensitive fact candidate | 代码合并通常由代码所有者确认，生产部署由服务负责人确认，数据库迁移与恢复由数据负责人确认，域名和证书由账号持有人确认，费用与合同由预算负责人确认，用户通知与政策由业务或合规负责人确认。一个人可能承担多个角色，责任仍要明确。 |
| 073 | `chapters/073-生产环境中的人工确认边界.md:35` | time-sensitive fact candidate | 审批提示中的命令要翻译成业务后果。`apply migration` 可能锁表和改变数据，`sync --delete` 会让远端文件按规则消失，`terraform apply` 可能创建费用或销毁资源。确认人需要看到计划、准确目标、Diff 与回退。 |
| 073 | `chapters/073-生产环境中的人工确认边界.md:41` | time-sensitive fact candidate | ## 数据、域名、商店和费用各有门禁 |
| 073 | `chapters/073-生产环境中的人工确认边界.md:49` | time-sensitive fact candidate | 创建更大服务器、开启日志、复制数据库、使用 AI API 和跨区域传输都会产生费用。批准前给出供应商、资源、区域、计费单位、预计持续时间、预算告警和删除条件。免费额度与价格随时间变化，使用官方当前信息并标注检索日期。 |
| 073 | `chapters/073-生产环境中的人工确认边界.md:51` | time-sensitive fact candidate | 删除数据库、对象、卷、备份、域名、商店应用和 Git 历史可能难以恢复。执行前列出准确资源 ID、内容、最后使用、依赖、备份、恢复测试、保留政策和批准人。若资源可以先停用或移入回收站，优先使用可恢复方式。历史重写无法让泄露秘密重新安全，必须先轮换。 |
| 073 | `chapters/073-生产环境中的人工确认边界.md:77` | time-sensitive fact candidate | 发布后观察分短期和长期。短期看启动、错误、延迟、关键用户路径和资源，长期看内存增长、队列积压、费用、用户反馈、备份和低频任务。可能停机、改变数据、要求重新登录或影响旧客户端的发布，应提前准备通知。 |
| 073 | `chapters/073-生产环境中的人工确认边界.md:79` | time-sensitive fact candidate | 定时备份、依赖更新、自动部署、内容处理和 AI agent 会在无人注视时改变状态。首次启用前审查触发频率、账号权限、数据范围、费用上限、失败告警、暂停开关和到期。关闭自动化前先停止新触发，再撤销服务账号、令牌、Webhook、runner 和预算。 |
| 073 | `chapters/073-生产环境中的人工确认边界.md:85` | time-sensitive fact candidate | - 生产清单覆盖域名、数据、存储、消息、商店、监控和费用 |
| 073 | `chapters/073-生产环境中的人工确认边界.md:91` | time-sensitive fact candidate | - DNS、证书、商店、消息和费用分别核对 |
| 074 | `chapters/074-不懂代码时怎样保留最终判断能力.md:23` | time-sensitive fact candidate | 风险可以先分为数据、安全、可用性、费用、隐私、政策与不可逆操作。数据库迁移关心丢失和兼容，防火墙关心公网暴露，自动重试关心重复扣款，日志关心秘密和磁盘，商店提交关心账号、政策与用户版本。分类后就知道需要谁确认。 |
| 074 | `chapters/074-不懂代码时怎样保留最终判断能力.md:35` | time-sensitive fact candidate | 比较至少包含实现成本、维护成本、故障责任、平台依赖、数据迁移、费用与退出方式。最低初始价格不一定最低长期成本，技术最先进也不一定最适合非专业维护者。把方案写成并排表格，要求 AI 说明适用前提和不适用情况。 |
| 074 | `chapters/074-不懂代码时怎样保留最终判断能力.md:37` | time-sensitive fact candidate | 选择后记录原因。半年后价格、用户量或能力变化，可以重新评估。没有记录时，团队只看到用了 Docker、选了 Firebase，不知道当时的约束。 |
| 074 | `chapters/074-不懂代码时怎样保留最终判断能力.md:59` | time-sensitive fact candidate | 软件版本、平台界面、价格、免费额度、商店政策、备案和安全配置会变化。AI 记忆中的答案可能过期。要求使用官方当前资料，记录检索日期、适用版本和链接。社区案例可以理解真实故障，规则要回到官方来源。 |
| 074 | `chapters/074-不懂代码时怎样保留最终判断能力.md:67` | time-sensitive fact candidate | 手册面向不会天天读代码的所有者，内容包括系统地图、生产资源、用户数据、域名、部署入口、备份恢复、监控、费用、账号持有人、应急停止和下线。它不复制秘密，只写安全存储和恢复责任。每个核心功能用一页说明输入、输出、数据位置、外部副作用和故障入口。 |
| 074 | `chapters/074-不懂代码时怎样保留最终判断能力.md:85` | time-sensitive fact candidate | - 识别数据、安全、费用、隐私、政策和不可逆风险 |
| 074 | `chapters/074-不懂代码时怎样保留最终判断能力.md:88` | time-sensitive fact candidate | - 重要版本、价格和政策回到当前官方资料 |
| 077 | `chapters/077-领域边界-数据所有权与跨模块协作.md:39` | time-sensitive fact candidate | 订单保存购买时的商品名称和价格，通常属于历史快照。商品模块后来改名，旧订单仍要呈现当时交易内容。搜索服务保存商品标题与关键词，属于可重建的派生数据。账号模块的当前登录邮箱是权威身份属性，却不应自动覆盖发票已经确认的抬头。 |
| 080 | `chapters/080-微服务真正增加了哪些工程责任.md:39` | time-sensitive fact candidate | 补偿不等于时间倒流。退款可能产生费用，邮件无法从收件箱撤回，外部系统也可能已经读取事件。产品要定义可接受的后续动作。 |
| 081 | `chapters/081-架构异味与-ai-生成项目的复杂度增长.md:59` | time-sensitive fact candidate | 全局变量、单例缓存和自动注册机制能减少参数传递，也会隐藏代码实际依赖。一个名为计算价格的函数顺手读取当前用户、修改缓存并发送分析事件，测试结果会受调用顺序影响。 |
| 081 | `chapters/081-架构异味与-ai-生成项目的复杂度增长.md:65` | time-sensitive fact candidate | 受控验证可以固定时间、随机数和外部适配器，重复运行同一测试。结果随顺序变化，说明存在未隔离状态。让邮件适配器返回错误，确认价格计算仍不受影响。 |
| 082 | `chapters/082-复杂度预算与什么时候不要增加新组件.md:7` | time-sensitive fact candidate | **新组件的收益应由当前证据支持，它的故障、升级、费用和退出方式也要有人承担。** |
| 082 | `chapters/082-复杂度预算与什么时候不要增加新组件.md:27` | time-sensitive fact candidate | 这五项不会等量出现。一个纯开发依赖可能几乎没有生产运行成本，却增加供应链更新。一个托管数据库代码接入简单，数据迁移和费用风险较高。预算也需要回收。功能下线后关闭 Worker、告警和云资源，迁移完成后删除旧 SDK、兼容层与 Secret。 |
| 082 | `chapters/082-复杂度预算与什么时候不要增加新组件.md:41` | time-sensitive fact candidate | 比较方案时，至少保留“不改变架构，只修当前实现”这一项。它提供基线，防止讨论只在几个新工具之间进行。每个候选方案记录直接收益、引入内容、失败表现、数据影响、权限、月度费用、验证办法和退出步骤。 |
| 082 | `chapters/082-复杂度预算与什么时候不要增加新组件.md:89` | time-sensitive fact candidate | 要求 AI 推荐组件时，不只要安装命令。让它列出当前问题与证据、至少一个不增加组件的方案、预期收益、运行单元、数据身份、Secret、监控、失败表现、费用风险、迁移步骤和删除办法。 |
| 083 | `chapters/083-用-adr-保存选择-代价与重新评估条件.md:79` | time-sensitive fact candidate | 背景中的事实要标注来源和日期。平台价格、免费额度、商店政策与合规要求会变化，应链接官方页面并写检索日期。推测与已验证事实分开。预计明年有十万用户属于预测，当前峰值每分钟一百请求属于测量。 |
| 083 | `chapters/083-用-adr-保存选择-代价与重新评估条件.md:85` | time-sensitive fact candidate | ADR 不要求写一篇长报告，至少应列出实际考虑过的可行方案，包括维持现状。每个方案使用相同维度比较，例如开发时间、运行责任、数据风险、费用、性能、可逆性和维护者熟悉程度。 |
| 083 | `chapters/083-用-adr-保存选择-代价与重新评估条件.md:93` | time-sensitive fact candidate | 决定带来的正面结果通常容易写，新增责任更容易遗漏。选择对象存储可以减少应用服务器磁盘管理，也要处理上传权限、失效链接、跨域设置、费用和数据迁移。选择托管身份服务可以缩短登录开发，同时增加供应商可用性与账号策略依赖。 |
| 083 | `chapters/083-用-adr-保存选择-代价与重新评估条件.md:125` | time-sensitive fact candidate | 若 AI 提议新数据库、队列、身份方式或模块边界，要求它起草候选 ADR。草稿要分开项目事实、外部资料和假设，列出维持现状，写明失败、费用、迁移与退出。人核对证据和产品后果以后才能接受。 |
| 083 | `chapters/083-用-adr-保存选择-代价与重新评估条件.md:133` | time-sensitive fact candidate | 选择项目中一个尚未定案的真实问题，例如文件放本地磁盘还是对象存储。先写当前规模、部署方式、备份要求与费用限制，再列出维持现状、托管对象存储和自建存储三项方案。没有数据时先标假设，不急着宣布答案。 |
| 083 | `chapters/083-用-adr-保存选择-代价与重新评估条件.md:135` | time-sensitive fact candidate | 挑选一个最小试验，上传文件、读取、删除，并模拟凭据失效。记录预期和实际结果。成功上传只能证明当前环境的基本路径，凭据失效时应用返回明确错误，可以证明这条权限失败得到处理。恢复、费用上限和批量迁移仍要另行验证。 |
| 084 | `chapters/084-怎样让两个工程方案真正对打.md:27` | time-sensitive fact candidate | 偏好允许权衡。本地开发更简单、费用更低、延迟更短、供应商依赖更少、团队更熟悉，都可能增加方案吸引力，却未必单独决定结果。 |
| 084 | `chapters/084-怎样让两个工程方案真正对打.md:31` | time-sensitive fact candidate | 约束之间冲突时要明确优先顺序。极低费用、零运维、完全可控和无限扩展很难同时获得。个人项目可以先保护数据与恢复能力。 |
| 084 | `chapters/084-怎样让两个工程方案真正对打.md:59` | time-sensitive fact candidate | 估算应写范围和口径。每月消息量、请求次数、数据保留、出口流量和日志量都会影响费用。价格容易变化，正式决定前重新查看官方页面并写检索日期。数据库方案看起来熟悉，正确实现并发领取也需要数据库锁和事务知识。 |
| 084 | `chapters/084-怎样让两个工程方案真正对打.md:65` | time-sensitive fact candidate | 评分表适合让结果并排出现，不适合制造数学权威。给数据安全五分、开发速度三分、费用两分，再算加权总分，权重稍微调整就可能换冠军。分数来自判断时，应保留原始观察和理由。 |
| 084 | `chapters/084-怎样让两个工程方案真正对打.md:67` | time-sensitive fact candidate | 硬约束先单独判断。任一方案无法满足数据地区、恢复目标或权限要求，就标为不合格。剩余方案再比较偏好。评分表只保留原始观察和理由，例如注册是否解耦、Worker 中断怎样恢复、月度费用如何计算、退出路径是否可走。 |
| 084 | `chapters/084-怎样让两个工程方案真正对打.md:71` | time-sensitive fact candidate | 支持方案的人通常最了解它，也最容易忽略熟悉带来的偏好。让每一方先列出自己方案最可能失败的三种方式，再提出验证。数据库方案要面对共享数据库过载、锁竞争和清理失控。队列方案要面对权限错误、重复消息、平台中断和费用变化。 |
| 084 | `chapters/084-怎样让两个工程方案真正对打.md:79` | time-sensitive fact candidate | 概念验证能测当前延迟和恢复过程，无法完整预测三年维护成本、供应商政策和团队变化。有些风险只能通过合同、官方承诺、真实运行和时间观察。把它们标为残余不确定性。 |
| 084 | `chapters/084-怎样让两个工程方案真正对打.md:87` | time-sensitive fact candidate | 决定实施后继续观察之前定义的指标。任务积压、最老任务年龄、重复发送、数据库负载和月度费用出现变化时，回到 ADR 的重新评估条件。 |
| 084 | `chapters/084-怎样让两个工程方案真正对打.md:98` | time-sensitive fact candidate | - 功能正确性、恢复、交付、费用和退出证据。 |
| 085 | `chapters/085-rest-graphql-polling-sse-与-websocket.md:63` | time-sensitive fact candidate | 手机 App 进入后台后，长期连接可能暂停或断开。需要系统级通知时，应评估 Apple Push Notification service 或 Firebase Cloud Messaging 等推送体系，不能期待网页 SSE 或 WebSocket 在后台长期保持。商店和系统政策会变化，采用前要查当前官方资料。 |
| 086 | `chapters/086-sqlite-postgresql-sql-与文档数据库.md:29` | time-sensitive fact candidate | Serverless 与边缘函数还要检查连接模型。大量短生命周期函数各自创建 PostgreSQL 连接，可能耗尽数据库连接数。平台连接池或数据库代理可以缓解，配置与费用也随之增加。SQLite 若运行在短暂文件系统中，实例销毁后本地数据可能消失。 |
| 086 | `chapters/086-sqlite-postgresql-sql-与文档数据库.md:73` | time-sensitive fact candidate | PostgreSQL 提供 SQL dump、文件系统级备份和连续归档等路线。选择取决于数据量、恢复时间和恢复点要求。托管平台的自动备份需要核对保留时间、恢复粒度、地区与费用，不能把控制台显示已备份当成恢复完成。文档数据库同样需要与部署拓扑匹配的备份，恢复后检查记录数量、关键约束、索引和应用行为。 |
| 086 | `chapters/086-sqlite-postgresql-sql-与文档数据库.md:75` | time-sensitive fact candidate | 恢复目标会反过来影响选型。只能接受一天数据丢失，与必须恢复到几分钟前，需要的日志、归档、费用和操作完全不同。先写恢复点目标与恢复时间目标，再确认产品和维护能力能否做到。 |
| 087 | `chapters/087-baas-自建后端-托管平台-vps-与-serverless.md:21` | time-sensitive fact candidate | Serverless 是一类由平台管理服务器容量的运行方式，也包括无服务器容器与数据服务。本章主要比较其中的函数形态，函数可能按请求、事件或计划任务触发。项目仍要关心运行区域、数据库连接、执行限制、日志和费用。VPS 是 Virtual Private Server 的缩写，可以译为虚拟专用服务器。用户维护操作系统、软件包、防火墙、SSH、反向代理、应用进程… |
| 087 | `chapters/087-baas-自建后端-托管平台-vps-与-serverless.md:31` | time-sensitive fact candidate | BaaS 会承担部分备份、扩展和可用性，但责任范围取决于产品与计划。保留时间、恢复粒度、地区、导出和费用都要查当前官方文档。控制台里有备份选项，也要做恢复演练。 |
| 087 | `chapters/087-baas-自建后端-托管平台-vps-与-serverless.md:37` | time-sensitive fact candidate | 云开发适合早期验证登录、数据、文件和简单函数。它减少服务器维护，也会让数据模型、权限规则、日志、费用和迁移方式与平台绑定。以后要同时支持网页、App、后台和其他渠道时，应提前记录接口边界，别把业务规则全部散在小程序页面里。 |
| 087 | `chapters/087-baas-自建后端-托管平台-vps-与-serverless.md:61` | time-sensitive fact candidate | 冷启动、执行时间、资源限制和地区距离都会影响体验。视频转码、批量导入和持续爬取可能超过函数时限，或产生高额资源费用。可以把请求变成任务，交给专用 Worker、队列或容器服务。 |
| 087 | `chapters/087-baas-自建后端-托管平台-vps-与-serverless.md:79` | time-sensitive fact candidate | 给 AI 一个项目需求时，要求它先画客户端、计算、身份、数据库、文件、消息和外部 API。每个节点写明谁管理、数据是否持久、Secret 在哪里、失败看哪份日志。随后让它分别给出 BaaS、托管应用、Serverless、VPS 和组合方案。每套方案都要覆盖权限、部署、备份、恢复、费用与退出。 |
| 087 | `chapters/087-baas-自建后端-托管平台-vps-与-serverless.md:81` | time-sensitive fact candidate | AI 生成配置后，检查它是否默认开放数据库、把服务密钥放入前端、依赖临时文件、忽略函数时限或让所有服务共用管理员权限。最终选择写进 ADR，记录当前规模、维护能力、数据地区、工作负载、平台责任、接受的限制和重新评估条件。平台功能、价格和计划会变化，封版与采用前重新核对官方资料。 |
| 088 | `chapters/088-直接进程-docker-compose-与-kubernetes.md:22` | time-sensitive fact candidate | python -m uvicorn app:app --host 127.0.0.1 --port 8000 |
| 090 | `chapters/090-背压-负载丢弃-隔离与队列语义.md:37` | time-sensitive fact candidate | 负载丢弃还要避免永远牺牲同一批用户。可以按优先级、租户配额、用户身份和请求成本分配容量。客户端收到过载响应后，应显示明确状态并限制手动连点。后台自动重试必须有退避、抖动与总次数。 |
| 091 | `chapters/091-sli-slo-sla-与-error-budget.md:35` | time-sensitive fact candidate | > 在 28 天滚动窗口内，有效视频播放操作中至少 99.5% 应在点击后 2 秒内开始播放。 |
| 091 | `chapters/091-sli-slo-sla-与-error-budget.md:37` | time-sensitive fact candidate | 99.5% 不是越高越专业。更高目标可能需要更多冗余、更慢发布和更强值班，仍可能测错用户结果。目标来自用户容忍度、业务后果、历史数据与团队能力。100% 通常不是默认答案，它会消灭任何试验空间，也无法区分普通波动和紧急工作。 |
| 091 | `chapters/091-sli-slo-sla-与-error-budget.md:39` | time-sensitive fact candidate | “几个九”还要说明按请求还是按时间。30 天内 99.9% 的时间型目标约允许 43.2 分钟不符合；请求型目标按事件计算，高峰一分钟与深夜一分钟消耗不同。滚动 28 天关注最近状态，日历月便于结算，两者不能在报告时临时挑更好看的。 |
| 091 | `chapters/091-sli-slo-sla-与-error-budget.md:52` | time-sensitive fact candidate | 仍用课程视频举例。28 天内有 200,000 次有效播放，SLO 为 99.5%，允许坏事件如下。 |
| 091 | `chapters/091-sli-slo-sla-与-error-budget.md:55` | time-sensitive fact candidate | 200000 × (1 - 0.995) = 1000 |
| 091 | `chapters/091-sli-slo-sla-与-error-budget.md:58` | time-sensitive fact candidate | 若这 200,000 次事件中已有 650 次坏事件，剩余 350 次，使用了 65% 预算。若另一份同样有 200,000 次有效事件的样本中，某次发布贡献了 100 次失败，它就消耗了该窗口预算的 10%，不能用“只影响了 0.05% 请求”忽略。这是固定分母的示例；实际滚动窗口的新事件进入、旧事件退出都会改变允许量和已用量，预算要随窗口重算。 |
| 091 | `chapters/091-sli-slo-sla-与-error-budget.md:60` | time-sensitive fact candidate | 预算要配预先同意的政策。充足时正常发布；消耗加快时缩小变更并加强观察；接近耗尽时暂停非必要高风险发布；耗尽后只做安全修复与恢复工作。具体阈值由项目后果与发布频率决定，事故发生后才临时发明规则，数字很难改变立场。 |
| 091 | `chapters/091-sli-slo-sla-与-error-budget.md:62` | time-sensitive fact candidate | Burn Rate 观察“烧得多快”。简化理解为当前坏事件比例除以 SLO 允许的坏比例。允许坏比例是 0.5%，若某窗口实际坏比例为 5%，burn rate 为 10；按同样速度会比预算允许快十倍。短窗口发现突发，长窗口过滤小波动。 |
| 091 | `chapters/091-sli-slo-sla-与-error-budget.md:72` | time-sensitive fact candidate | 内部 SLO 应为对外承诺留余量。产品承诺 99.9%，唯一数据库的供应商 SLA 也写着 99.9%，并不能推出用户路径能达到同样水平。SLA 是约定口径，不是依赖实际故障率；还要核对测量范围、冗余和降级。多个串行依赖会共同影响用户结果，不能挑最高数字作为系统承诺。 |
| 091 | `chapters/091-sli-slo-sla-与-error-budget.md:91` | time-sensitive fact candidate | AI 可以生成查询和仪表盘，但必须同时交付分子、分母、阈值、窗口、时区、去重、缺失数据处理，以及几条人工判定样本。只给一条百分比曲线，不能用于发布决策。SLA 和预算政策涉及风险偏好与客户责任，由人最终确认。 |
| 091 | `chapters/091-sli-slo-sla-与-error-budget.md:97` | time-sensitive fact candidate | 个人低风险项目可以先只记录一个诚实 SLI 和五条样本，不必立刻建立正式 SLA、值班和多窗口告警。出现付费承诺、多人协作、频繁发布或明显用户损失时，再引入完整 SLO、预算政策和 burn-rate 告警。 |
| 092 | `chapters/092-日志-指标-追踪与-opentelemetry.md:23` | time-sensitive fact candidate | "time": "2026-08-11T09:42:18.372+08:00", |
| 092 | `chapters/092-日志-指标-追踪与-opentelemetry.md:89` | time-sensitive fact candidate | 开放标准不保证完全无迁移成本。不同后端支持的字段、查询、采样和告警能力不同，各语言 SDK 的成熟度也会变化。自动插桩适合先获得 HTTP、数据库与运行时信息，业务动作仍需手工描述。OpenTelemetry 也不负责存储与展示，项目仍需设置保留期限、访问权限、费用上限、仪表盘和告警。 |
| 093 | `chapters/093-性能基线-分位数-剖析-压测与成本.md:7` | time-sensitive fact candidate | 性能工作可以分成五步。先建立可重复基线，再用分布描述体验，通过剖析找到资源花在哪里，用受控负载验证容量与恢复，最后把速度、费用、复杂度和正确性一起计算。 |
| 093 | `chapters/093-性能基线-分位数-剖析-压测与成本.md:74` | time-sensitive fact candidate | 容量上限不应定义成机器崩溃前最后一个成功数字。安全容量需要留出流量波动、后台任务、单机故障和发布重启余量。压测停止后还要观察连接池、队列、重试、内存和错误率怎样恢复。数据库、队列和第三方 API 常先成为限制，每次扩容都要重新核对共享依赖与费用。 |
| 093 | `chapters/093-性能基线-分位数-剖析-压测与成本.md:82` | time-sensitive fact candidate | 优化还可能把成本转移。把图片全部预生成，读取变快，存储和构建时间增加。增加数据库索引，查询变快，写入与磁盘成本增加。使用全球 CDN 改善远端延迟，流量费用与缓存一致性会变化。 |
| 093 | `chapters/093-性能基线-分位数-剖析-压测与成本.md:89` | time-sensitive fact candidate | 搜索相关计算、数据库、缓存和网络费用 |
| 093 | `chapters/093-性能基线-分位数-剖析-压测与成本.md:94` | time-sensitive fact candidate | 成本还包括维护时间和复杂度。每月省十元服务器费用，却增加一种数据库、一个值班告警和四小时维护，未必划算。价格、免费额度和计费维度会变化，采用服务时必须按检索日查看官方价格，并用真实账单复核。压测本身也可能产生显著费用，开始前设置预算和停止条件。 |
| 093 | `chapters/093-性能基线-分位数-剖析-压测与成本.md:98` | time-sensitive fact candidate | 课程搜索变慢时，先保存基线。使用固定数据快照和二十种查询，分别测冷缓存与热缓存，在一、十、五十并发下记录成功率、p50、p95、p99、吞吐、CPU、内存、数据库时间与费用估算。 |
| 093 | `chapters/093-性能基线-分位数-剖析-压测与成本.md:106` | time-sensitive fact candidate | 错误率无变化，数据库存储增加 1.8 GB。 |
| 095 | `chapters/095-独立测试依据与可信的第二意见.md:15` | time-sensitive fact candidate | 税费函数返回 12.37，测试若复制同一公式计算预期值，两边会一起犯错。更可靠的依据可能来自法规、人工核对样本、验证过的参考实现，或金额守恒等不变量。 |
| 095 | `chapters/095-独立测试依据与可信的第二意见.md:31` | time-sensitive fact candidate | 复核任务应提供原始目标、仓库与变更范围，要求寻找能推翻方案的输入、版本冲突、权限绕过、恢复失败和未测试假设。两个模型依赖同一篇过时文章时，来源仍不独立。平台政策、价格、界面与版本需要回到当前官方资料核对。 |
| 095 | `chapters/095-独立测试依据与可信的第二意见.md:37` | time-sensitive fact candidate | 依据也要版本化。官方 API、数据库版本、商店政策和业务规则变化后，旧测试可能继续通过。只有 `PASS`，没有输入、预期和比较过程，复核者无法判断脚本本身。 |
| 096 | `chapters/096-怎样阅读事故复盘并提取可迁移经验.md:36` | time-sensitive fact candidate | 当时各类任务的连接配额 |
| 099 | `chapters/099-pocketbase-与-supabase-的边界选择.md:13` | time-sensitive fact candidate | PocketBase 把嵌入式 SQLite、实时订阅、认证、管理界面和接口放在一个可独立运行的程序里，也支持用 Go 扩展。它适合先用原型、局域网工具和边界清楚的小项目评估，部署与本地复现路径较短。截至 2026 年 9 月 23 日，[官方文档](https://pocketbase.io/docs/)仍提示 1.0 之前不保证完整向后兼容，不建议用于生… |
| 099 | `chapters/099-pocketbase-与-supabase-的边界选择.md:15` | time-sensitive fact candidate | Supabase 托管平台以 Postgres 为中心，组合认证、接口、实时通信、存储与函数。平台承担不少基础设施工作，项目仍要设计表结构、行级权限、密钥使用、数据生命周期和费用控制。 |
| 099 | `chapters/099-pocketbase-与-supabase-的边界选择.md:51` | time-sensitive fact candidate | 选型记录要注明检索日期、价格与政策来源、支持渠道和重新评审条件。费用、数据量、地区要求或兼容承诺发生变化时，重新运行关键试验。 |
| 101 | `chapters/101-怎样正确使用技术社区中的争议与经验.md:19` | time-sensitive fact candidate | 普通论坛、Reddit、X 长帖和个人博客的上下文更分散。作者可能没有写版本，也可能只展示成功截图。它们适合发现关键词、特殊硬件、地区限制和用户感受。涉及安全、删除、费用、政策和数据恢复时，仍要查官方资料并自己验证。 |
| 102 | `chapters/102-repository-health-review-与长期清理.md:92` | time-sensitive fact candidate | 季度完整检查可以固定十项。生产版本可追溯，主分支检查有效，关键路径有责任人，安全报告入口可用，依赖风险已分类，备份恢复有近期证据，数据删除有批准边界，文档从空环境可执行，费用与账号有人负责，废弃资产已有处置日期。 |
| 104 | `chapters/104-把工程判断变成可持续的项目治理.md:3` | time-sensitive fact candidate | 一个人借助 AI 做出网页或 App，第一次上线只是工程工作的开始。域名要续费，依赖会更新，证书和密钥会轮换，平台政策会变，数据要备份，事故要有人处理。项目治理把谁能决定、什么证据足够、何时停止发布和怎样退出写成可执行的规则。 |
| 104 | `chapters/104-把工程判断变成可持续的项目治理.md:11` | time-sensitive fact candidate | 图中每项变化都经过分类、决定、实施、验证和发布，运行证据再进入维护。事故、成本、政策和人员变化会触发重新评审，项目也保留安全下线的出口。 |
| 104 | `chapters/104-把工程判断变成可持续的项目治理.md:21` | time-sensitive fact candidate | 文字和样式的小改动通常可以走轻量流程。认证、权限、付款、数据迁移、上传、安全配置和删除功能需要更严格门槛。平台切换、数据库升级和应用商店发布还涉及外部政策。 |
| 104 | `chapters/104-把工程判断变成可持续的项目治理.md:42` | time-sensitive fact candidate | 维护节奏可以分成每周、每月和每季度。每周看可用性、错误、备份任务和异常费用。每月看依赖、安全告警、证书与域名、失败任务和恢复样本。每季度做恢复演练、权限复核、仓库健康检查和下线资产清点。 |
| 104 | `chapters/104-把工程判断变成可持续的项目治理.md:50` | time-sensitive fact candidate | 重要选择使用短 ADR。记录当时问题、可选方案、决定、后果、复查触发条件和相关提交。触发条件可以是用户量超过阈值、费用变化、平台停止某能力、恢复时间不达标或维护者离开。 |
| 104 | `chapters/104-把工程判断变成可持续的项目治理.md:58` | time-sensitive fact candidate | 价格、免费额度和平台政策会变化。预算不能只写当前月费，还要设置提醒与上限，检查流量增长、日志保留、出站流量和后台任务带来的费用。收到费用告警时，先限制非关键消耗。 |
| 104 | `chapters/104-把工程判断变成可持续的项目治理.md:76` | time-sensitive fact candidate | 项目可能因为费用、人员、法律要求或需求消失而结束。安全下线包括通知用户、提供数据导出、停止写入、撤销令牌、关闭公开入口、保留必要记录、删除不再需要的数据和终止账单。具体顺序必须照顾依赖关系，例如先完成用户导出，再撤销导出所需的访问；暂停写入后还要核对未完成任务、付款与回调。 |
| 104 | `chapters/104-把工程判断变成可持续的项目治理.md:80` | time-sensitive fact candidate | 仓库可以归档，文档要标明最后支持版本和安全状态。域名若不再保留，旧链接和回调可能被他人接管，需提前解除 OAuth、邮件和应用配置。 |
| 104 | `chapters/104-把工程判断变成可持续的项目治理.md:82` | time-sensitive fact candidate | 先完成五件事。记录生产提交和部署位置，确认备份能恢复，列出账号和费用所有者，为高风险改动写发布门槛，安排下次维护日期。随后每遇到一次真实问题，只增加一条确实能缩小后果的规则。 |
| 104 | `chapters/104-把工程判断变成可持续的项目治理.md:102` | time-sensitive fact candidate | 检查项目还有哪些用户、产生什么价值、每年花费多少时间与费用、持有哪些数据和承诺。若维护成本已经超过价值，可以缩减功能、迁移到托管服务、只读归档或安全下线。继续运营也要重新确认技术选择。 |
| 104 | `chapters/104-把工程判断变成可持续的项目治理.md:104` | time-sensitive fact candidate | 把决定与下一次触发条件写进 ADR。用户量、费用、恢复结果或人员变化达到条件时提前复查，不必等到年度日期。 |

## Invalid chapter references

- None

## Repository and release baseline

- Canonical Markdown and build scripts were absent from the v2.2.0 branch before this recovery.
- Existing top-level v2.2.0 EPUB, TXT, DOCX, AZW3, FB2, HTMLZ, KEPUB and MOBI remain immutable inputs/artifacts.
- README and START-HERE positioning changes are deferred until the recovered baseline and pilot chapters are accepted.
- PDF page count/bookmarks and Release attachment correspondence remain deferred release checks.
