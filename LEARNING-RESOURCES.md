# 配套学习资源

这份资源表只把视频用于界面辨认、连续操作和第一遍视觉理解。技术事实仍以当前官方文档、标准和经过验证的实际行为为准。检索日期为 2026 年 8 月 13 日。

观看时不要照搬账号、密钥、价格和生产配置。先准备练习仓库、测试服务器或独立应用，暂停视频亲手完成指定动作，再回到正文理解每一步改变了哪里。

## AI Coding 的工作方式

### V-AI-02　非程序员怎样完成一个 AI Coding 项目

- 视频标题　Complete Guide to Cursor For Non-Coders
- 作者　Riley Brown
- 平台　YouTube
- 发布时间　2025 年 2 月 11 日
- 视频时长　2 小时 28 分 17 秒
- 推荐观看　23 分 59 秒至 33 分 54 秒看模板、需求草图、首次提示和保存工作；43 分 20 秒至 48 分 02 秒看浏览器检查与 Console；78 分 18 秒至 87 分 59 秒看 GitHub、Vercel 和域名
- 解决的问题　快速看到一个非传统编程背景的创作者怎样让 AI 修改项目，并把调试、仓库和部署接到同一条流程里
- 观看前准备　只需要浏览器和纸笔。第一次观看不必安装视频中的全部工具
- 亲手完成　画出自己项目从本地文件到公开地址的五个节点，并记下目前说不清楚的一处
- 界面时效　部分界面已经变化，实践经验仍有参考价值，具体按钮与平台行为需核对官方文档
- 链接　https://www.youtube.com/watch?v=faezjTHA5SU

这条资源用于建立整体印象，不是 Cursor、Firebase 或 Vercel 的事实来源，也不表示视频里的工具组合是唯一方案。

## Git 与 GitHub

### V-GIT-01　GitHub Desktop 第一次提交与同步

- 视频标题　How to Use GitHub Desktop 2025
- 作者　TECH GIANT
- 平台　YouTube
- 发布时间　2025 年 4 月 9 日
- 视频时长　8 分 40 秒
- 推荐观看　2 分 15 秒至 6 分 30 秒
- 解决的问题　辨认创建或克隆仓库、Changes、Commit、Push、Pull、分支与合并在 GitHub Desktop 中的位置
- 观看前准备　安装当前 GitHub Desktop，登录练习账号，准备一个只含 README 的练习仓库
- 亲手完成　修改 README，在 Changes 中核对 Diff，提交并 Push；再从网页改一行并 Pull
- 界面时效　当前界面基本一致，GitHub Desktop 后续更新可能调整按钮位置
- 链接　https://www.youtube.com/watch?v=AYJQi6TyPyU

### V-GIT-02　英文 Git 与 GitHub 概念补充

- 视频标题　Git and GitHub for Beginners Crash Course
- 作者　freeCodeCamp.org
- 平台　YouTube
- 发布时间　2020 年 5 月 28 日
- 视频时长　1 小时 8 分 30 秒
- 推荐观看　1 分 10 秒至 5 分 20 秒理解 Git 与版本控制；17 分 30 秒至 31 分 40 秒跟随 add、commit、push；32 分 42 秒至 56 分 30 秒认识分支
- 解决的问题　把仓库、提交、推送和分支放入一条命令行工作流
- 观看前准备　准备可随时删除的练习仓库，不在生产项目上练习撤销和分支
- 亲手完成　创建一个文本文件，做两次小提交，并在 GitHub 网页确认提交顺序
- 界面时效　Git 原理仍适用，GitHub 注册和部分界面明显较旧
- 链接　https://www.youtube.com/watch?v=RGOj5yH7evk

第一遍只掌握 Repository、Commit、Push、Pull、Branch 和 Conflict。stash、cherry-pick 等操作可以在真实需求出现时再学。

## 浏览器开发者工具

### V-WEB-01　Chrome DevTools 快速入门

- 视频标题　Fun and powerful Intro to Chrome DevTools
- 作者　Chrome for Developers
- 平台　YouTube
- 发布时间　2024 年 2 月 22 日
- 视频时长　5 分 34 秒
- 推荐观看　0 分 23 秒至 4 分 39 秒
- 解决的问题　展示如何打开 DevTools、查看 Console 错误、使用 Sources 断点并在 Network 中筛选请求
- 观看前准备　用当前稳定版 Chrome 打开无真实账号和个人数据的练习页面
- 亲手完成　制造一条 Console 错误，刷新页面，在 Network 中选择请求并查看状态码、Headers 和 Response
- 界面时效　当前官方视频，主要面板仍适用
- 链接　https://www.youtube.com/watch?v=t1c5tNPpXjs

## 第一次 SSH 与服务日志

### V-LINUX-01　第一次登录测试 VPS

- 视频标题　You Need a VPS, The Foundational Setup Guide using Hetzner and Cloudflare DNS
- 作者　Jilles
- 平台　YouTube
- 发布时间　2025 年 10 月 28 日
- 视频时长　17 分 1 秒
- 推荐观看　6 分 16 秒至 13 分 10 秒
- 解决的问题　观察 SSH 登录、建立非 root 管理用户、检查服务和启用 UFW 的连续过程
- 观看前准备　准备可随时重建的测试 VPS、本地 SSH 密钥和云控制台救援入口
- 亲手完成　核对主机指纹后登录，创建练习用户并执行只读状态检查。启用防火墙前先确认 SSH 规则
- 界面时效　SSH 与 Linux 操作仍适用，云平台界面和价格不作为依据
- 链接　https://www.youtube.com/watch?v=E0tUio6ZgH8

### V-LINUX-02　systemctl 与 journalctl

- 视频标题　How To Manage Linux Services with systemctl and journalctl
- 作者　Akamai Developers
- 平台　YouTube
- 发布时间　2021 年 5 月 5 日
- 视频时长　14 分
- 推荐观看　1 分 00 秒至 12 分 01 秒
- 解决的问题　展示服务状态、启停和 journalctl 按服务筛选与实时跟随日志
- 观看前准备　已经能登录使用 systemd 的练习 Linux 主机，并知道一个无业务风险的服务名
- 亲手完成　查看服务状态与最近日志，另开终端跟随日志；只在测试服务上练习 restart
- 界面时效　命令行为仍适用，具体服务名称取决于系统和项目
- 链接　https://www.youtube.com/watch?v=3kl62YSU9XA

## Docker 与 Docker Compose

### V-DOCKER-01　Docker Compose 主视频

- 视频标题　Ultimate Docker Compose Tutorial
- 作者　TechWorld with Nana
- 平台　YouTube
- 发布时间　2024 年 1 月 11 日
- 视频时长　1 小时 3 分 14 秒
- 推荐观看　11 分 58 秒至 27 分 18 秒；40 分 36 秒至 46 分 41 秒
- 解决的问题　把多条 docker run 命令整理为 Compose 文件，并演示 up、down、依赖、变量与秘密
- 观看前准备　安装当前 Docker Desktop 或 Docker Engine 与 Compose 插件，准备无生产数据的示例项目
- 亲手完成　先运行 `docker compose config`，再执行 `up -d`、`ps` 和 `logs`；最后用不带 `-v` 的 `down` 停止
- 界面时效　当前 Compose 插件工作流仍适用，命令细节以 Docker Docs 为准
- 链接　https://www.youtube.com/watch?v=SXwC9fSwct8

### V-DOCKER-02　英文完整课程中的精选片段

- 视频标题　Docker Tutorial for Beginners, Full Course in 3 Hours
- 作者　TechWorld with Nana
- 平台　YouTube
- 发布时间　2020 年 10 月 21 日
- 视频时长　2 小时 46 分 15 秒
- 推荐观看　1 小时 29 分 49 秒至 1 小时 42 分 02 秒看 Compose；2 小时 27 分 26 秒至 2 小时 45 分 13 秒看 Volume 与持久化
- 解决的问题　建立多容器和持久数据的视觉模型
- 观看前准备　先读第 44 至 47 章，不需要完整观看三小时
- 亲手完成　指出自己项目中会随容器重建消失的数据，并确认是否使用命名 Volume 或 Bind Mount
- 界面时效　概念仍适用，安装界面和部分命令展示较旧
- 链接　https://www.youtube.com/watch?v=3c-iBn73dDE

## 部署平台控制台

### V-DEPLOY-01　Vercel 当前产品流程

- 视频标题　Vercel Product Walkthrough 2026
- 作者　Vercel
- 平台　YouTube
- 发布时间　2026 年 3 月 16 日
- 视频时长　10 分 11 秒
- 推荐观看　1 分 17 秒至 3 分 34 秒；9 分 06 秒至 9 分 50 秒
- 解决的问题　观察导入 Git 仓库、创建部署和查看部署结果的当前界面
- 观看前准备　准备不含秘密的 GitHub 练习仓库，并只授权该仓库
- 亲手完成　导入练习仓库，核对框架、项目名和目标分支，部署后打开生成地址并保存记录
- 界面时效　当前官方演示，套餐能力和界面仍可能变化
- 链接　https://www.youtube.com/watch?v=zFXscjUoDDA

## Flutter 与应用发布

### V-FLUTTER-01　Google Play 发布界面

- 视频标题　How to Publish Flutter App on Google Play Store 2026
- 作者　King Rittik
- 平台　YouTube
- 发布时间　2026 年 5 月 3 日
- 视频时长　10 分 10 秒
- 推荐观看　0 分 50 秒至 10 分 10 秒
- 解决的问题　展示登记包名、创建应用、构建 AAB 和上传发布包的连续过程
- 观看前准备　使用独立练习应用，确认包名、版本号、隐私政策和签名材料，不录入口令
- 亲手完成　记录 application ID、version、build 和签名证书指纹，生成 AAB 后先进入内部测试
- 界面时效　界面较新，账号测试门槛与政策必须重新核对 Play Console 帮助
- 链接　https://www.youtube.com/watch?v=adt9A8125S4

### V-FLUTTER-02　Flutter 官方 iOS 发布

- 视频标题　Release an iOS app with Flutter in 7 steps
- 作者　Flutter
- 平台　YouTube
- 发布时间　2023 年 9 月 25 日
- 视频时长　9 分 52 秒
- 推荐观看　0 分 58 秒至 9 分 52 秒
- 解决的问题　从 Bundle ID、App Store Connect 记录和 Xcode 设置一路演示到 Archive 与上传
- 观看前准备　需要真实 Mac、当前 Xcode、受控 Apple Developer 账号和练习应用。没有这些条件时只观看
- 亲手完成　核对 Bundle ID、Team、Version、Build 与图标，Archive 后在 Organizer 检查签名身份
- 界面时效　原理仍适用，App Store Connect 与 Xcode 界面可能变化
- 链接　https://www.youtube.com/watch?v=iE2bpP56QKc

### V-FLUTTER-03　TestFlight 内部与外部测试

- 视频标题　TestFlight and Xcode, Upload, Distribute, and Beta Test Your iOS App
- 作者　Noah Does Coding
- 平台　YouTube
- 发布时间　2025 年 5 月 20 日
- 视频时长　7 分 56 秒
- 推荐观看　1 分 35 秒至 7 分 50 秒
- 解决的问题　展示上传构建、建立测试组、启用测试并在设备安装
- 观看前准备　完成可验证的 Archive，准备受控测试账号和测试说明
- 亲手完成　先把已核对版本加入内部组，邀请一个测试账号，在真机记录安装和核心路径结果
- 界面时效　界面较新，外部测试审核要求以 Apple 当前帮助为准
- 链接　https://www.youtube.com/watch?v=x0d8Jx3HvdI

### V-FLUTTER-04　Flutter DevTools 定位性能与日志

- 视频标题　Dive into DevTools
- 作者　Flutter
- 平台　YouTube
- 发布时间　2023 年 10 月 2 日
- 视频时长　14 分 26 秒
- 推荐观看　0 分 42 秒至 9 分 35 秒看启动、Inspector、性能、CPU、内存、调试、网络和日志
- 解决的问题　认识 Flutter DevTools 各面板分别能观察什么
- 观看前准备　准备能够以 Debug 或 Profile 模式运行的练习 App
- 亲手完成　在自己的 App 中打开 Inspector 和 Network，记录一条日志并找到一次请求
- 界面时效　核心面板仍适用，当前入口和功能以 Flutter Docs 为准
- 链接　https://www.youtube.com/watch?v=_EYk-E29edo

## 待复核候选

任务书列出的部分 Bilibili 候选在本次检索环境中返回 412 或无法取得作者、日期、时长和分段信息。它们暂不作为正式推荐，也不进入 EPUB 的二维码索引。待能够逐项核对页面元数据、内容片段和当前界面后，再从这里升级到正式资源。这样可以避免只有标题和链接、没有观看说明的资源堆积。
