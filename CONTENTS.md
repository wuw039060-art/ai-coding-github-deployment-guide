# 《从 GitHub 到上线》完整目录

本目录对应 EPUB 2.1.0，共十卷、104 章。总目录只收录分卷和章，不把章内小标题全部展开，方便在手机阅读器中快速定位。

## 第一卷　先看懂软件怎样来到用户面前

1. 从本地文件到公开可用的产品
2. 本地电脑、GitHub、部署平台、服务器和用户设备
3. 静态网站、动态网站、服务器程序和手机 App
4. 文件、路径、终端和图形界面的最低限度知识

## 第二卷　GitHub 与项目版本

5. Git、GitHub、项目文件夹和仓库
6. GitHub 账号、公开仓库、私有仓库和网页上传
7. 用 GitHub Desktop 管理本地项目
8. Commit、Push、Pull、Clone 和 Sync
9. 分支、合并、冲突、撤销与恢复
10. README、Releases、Issues、Actions、许可证和项目维护状态
11. 下载、检查并运行别人的项目
12. `.gitignore`、秘密泄露和历史中的敏感信息

## 第三卷　浏览器、网络与 Web 系统

13. 浏览器、客户端和服务器
14. IP、域名、DNS、端口和 URL
15. HTTP、HTTPS、TLS、请求与响应
16. Cookie、Session、Token、缓存和 CDN
17. HTML、CSS、JavaScript、前端和后端
18. API、数据库、文件存储和实时通信
19. 浏览器开发者工具、状态码和网络请求
20. 动态应用的完整架构图

## 第四卷　构建项目与发布网页

21. 源代码、依赖、运行时、构建和构建产物
22. 包管理器、锁文件、版本号和环境差异
23. 本地预览与静态网站发布
24. GitHub Pages 与 Cloudflare Pages
25. Vercel、Render 等自动部署平台
26. Build Command、Output Directory 和环境变量
27. Preview、Production、部署日志和回滚
28. 自定义域名、DNS、HTTPS、费用与地区差异

## 第五卷　后端、数据库与托管服务

29. 后端为什么存在以及 API 怎样工作
30. REST、WebSocket、身份认证和权限控制
31. SQL、NoSQL、PostgreSQL 与 SQLite
32. 数据库迁移、连接、备份和恢复
33. 文件上传、对象存储、邮件、推送和 AI API
34. Supabase、Firebase 与后端即服务
35. 托管方案、自建方案和平台依赖

## 第六卷　Linux、VPS 与远程服务器

36. VPS、云服务器及购买时需要看的参数
37. 第一次使用 SSH 登录服务器
38. Linux 文件、目录、用户、root、sudo 和权限
39. 软件包、进程、端口、磁盘和内存
40. systemd、systemctl、journalctl 和服务日志
41. 防火墙、Caddy、Nginx、域名与 HTTPS
42. 部署、更新、回滚、备份和恢复
43. 自建服务器增加了哪些长期责任

## 第七卷　Docker 与个人项目部署

44. 运行环境问题与 Docker 的基本模型
45. 镜像、容器、Dockerfile 和 Registry
46. 端口映射、Volume、Bind Mount 和数据持久化
47. Docker Compose 与多容器应用
48. 容器状态、日志、健康检查和重启策略
49. 更新、回滚、清理与数据丢失风险
50. Docker、虚拟机和 Kubernetes 的边界

## 第八卷　Flutter、App 打包与应用商店

51. App 客户端、后端和本地数据
52. Flutter 项目、依赖、Debug、Profile 和 Release
53. APK、AAB、包名、版本号和 Android 签名
54. Google Play 内部测试与发布流程
55. iOS、macOS、Xcode、证书和 Provisioning Profile
56. Archive、TestFlight 与 App Store Connect
57. 商店素材、权限、隐私政策和审核反馈
58. App 更新、崩溃日志和后端停机

## 第九卷　日志、排错、安全与维护

59. 从现象到故障层级的统一判断方法
60. Console、Network、Build Log 和 Runtime Log
61. 服务器、Docker、数据库和代理日志
62. Flutter、Logcat、Xcode 与商店上传错误
63. 复现、调用栈、最小复现、最近改动和回滚
64. 怎样向 AI 或开发者提交完整报错
65. Secret、`.env`、SSH 密钥和最小权限
66. 防火墙、数据库暴露、输入验证和文件上传
67. 备份、恢复测试、监控、费用和安全下线
68. 每周、每月和每季度维护清单

## 第十卷　与 AI 一起完成工程工作

69. 让 AI 先理解项目结构
70. 计划、权限、Diff、测试和验证证据
71. 安全地生成配置、部署文档和回滚方案
72. AI 声称完成以后还要检查什么
73. 生产环境中的人工确认边界
74. 不懂代码时怎样保留最终判断能力
75. 代码能运行以后，架构问题才开始出现
76. 模块、内聚、耦合、依赖方向与公开接口
77. 领域边界、数据所有权与跨模块协作
78. 分层架构、按功能组织与 Vertical Slice
79. 模块化单体怎样控制变化范围
80. 微服务真正增加了哪些工程责任
81. 架构异味与 AI 生成项目的复杂度增长
82. 复杂度预算与什么时候不要增加新组件
83. 用 ADR 保存选择、代价与重新评估条件
84. 怎样让两个工程方案真正对打
85. REST、GraphQL、Polling、SSE 与 WebSocket
86. SQLite、PostgreSQL、SQL 与文档数据库
87. BaaS、自建后端、托管平台、VPS 与 Serverless
88. 直接进程、Docker、Compose 与 Kubernetes
89. 局部故障、超时、重试放大与退避
90. 背压、负载丢弃、隔离与队列语义
91. SLI、SLO、SLA 与 Error Budget
92. 日志、指标、追踪与 OpenTelemetry
93. 性能基线、分位数、剖析、压测与成本
94. 契约、性质、模糊、变异与回归测试
95. 独立测试依据与真正独立的第二意见
96. 怎样阅读事故复盘并提取可迁移经验
97. 先画成熟开源仓库的 Repository Map
98. 沿用户动作阅读测试、历史、Issue 与 PR
99. PocketBase 与 Supabase 的边界选择
100. Immich 与 PostHog 中的后台任务和工程组织
101. 怎样正确使用技术社区中的争议与经验
102. Repository Health Review 与长期清理
103. 审查 AI 的范围扩张、依赖与架构漂移
104. 把工程判断变成可持续的项目治理

[返回项目介绍](README.md)

