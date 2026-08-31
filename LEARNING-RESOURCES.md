# 配套学习资源

这份资源表只把视频用于界面辨认、连续操作和第一遍视觉理解。中文读者优先看 B 站入口。遇到官方演示、英文材料明显更新，或暂时没有合适中文视频时，再看 YouTube 备用入口。技术事实仍以当前官方文档、标准和经过验证的实际行为为准。检索日期为 2026 年 8 月 31 日。

观看时不要照搬账号、密钥、价格和生产配置。先准备练习仓库、测试服务器或独立应用，暂停视频亲手完成指定动作，再回到正文理解每一步改变了哪里。

## AI Coding 的工作方式

### V-AI-01　非程序员怎样完成一个 AI Coding 项目

- 主入口　YouTube，Riley Brown 的 Cursor 项目完整演示
- 推荐观看　23 分 59 秒至 33 分 54 秒看需求草图和首次提示，43 分 20 秒至 48 分 02 秒看浏览器检查，78 分 18 秒至 87 分 59 秒看 GitHub、Vercel 和域名
- 解决的问题　快速看到一个非传统编程背景的创作者怎样让 AI 修改项目，并把调试、仓库和部署接到同一条流程里
- 观看前准备　只需要浏览器和纸笔。第一次观看不必安装视频中的全部工具
- 亲手完成　画出自己项目从本地文件到公开地址的五个节点，并记下目前说不清楚的一处
- 链接　https://www.youtube.com/watch?v=faezjTHA5SU

这条资源用于建立整体印象，不是 Cursor、Firebase 或 Vercel 的事实来源，也不表示视频里的工具组合是唯一方案。

## Git 与 GitHub

### V-GIT-01　GitHub Desktop 第一次提交与同步

- 主入口　B 站，尚硅谷《Git 全套教程》
- 推荐观看　P7 至 P16 中的 GitHub Desktop、远程仓库、README、Ignore 和文件比对部分
- 解决的问题　辨认 Changes、Commit、Push、Pull、分支、远程仓库和文件差异在 GitHub Desktop 中的位置
- 观看前准备　安装当前 GitHub Desktop，登录练习账号，准备一个只含 README 的练习仓库
- 亲手完成　修改 README，在 Changes 中核对 Diff，提交并 Push；再从网页改一行并 Pull
- 备用入口　YouTube，TECH GIANT 的 GitHub Desktop 入门视频
- 链接　https://www.bilibili.com/video/BV1wm4y1z7Dg?p=7
- 备用链接　https://www.youtube.com/watch?v=AYJQi6TyPyU

### V-GIT-02　Git 命令行概念补充

- 主入口　B 站，尚硅谷《Git 全套教程》
- 推荐观看　命令行、远程仓库、分支、合并和冲突相关分集
- 解决的问题　把仓库、提交、推送和分支放入一条命令行工作流
- 观看前准备　准备可随时删除的练习仓库，不在生产项目上练习撤销和分支
- 亲手完成　创建一个文本文件，做两次小提交，并在 GitHub 网页确认提交顺序
- 备用入口　YouTube，freeCodeCamp 的 Git 与 GitHub 入门课
- 链接　https://www.bilibili.com/video/BV1wm4y1z7Dg
- 备用链接　https://www.youtube.com/watch?v=RGOj5yH7evk

第一遍只掌握 Repository、Commit、Push、Pull、Branch 和 Conflict。stash、cherry-pick 等操作可以在真实需求出现时再学。

## 浏览器开发者工具

### V-WEB-01　Chrome DevTools 快速入门

- 主入口　B 站，不懂就来学《30 分钟掌握 Chrome DevTools》
- 推荐观看　先看打开面板、Console、Network 和请求详情相关部分
- 解决的问题　展示如何打开 DevTools、查看 Console 错误、使用 Sources 断点并在 Network 中筛选请求
- 观看前准备　用当前稳定版 Chrome 打开无真实账号和个人数据的练习页面
- 亲手完成　制造一条 Console 错误，刷新页面，在 Network 中选择请求并查看状态码、Headers 和 Response
- 备用入口　YouTube，Chrome for Developers 的 DevTools 入门视频
- 链接　https://www.bilibili.com/video/BV1TbVv67EiJ
- 备用链接　https://www.youtube.com/watch?v=t1c5tNPpXjs

## 第一次 SSH 与服务日志

### V-LINUX-01　第一次登录测试 VPS

- 主入口　B 站，我不是咕咕鸽《如何有效保护你的 VPS 服务器》
- 推荐观看　P6、P8、P9，分别看 SSH、普通用户和 UFW 防火墙
- 解决的问题　观察 SSH 登录、普通用户、服务检查和防火墙设置的连续过程
- 观看前准备　准备可随时重建的测试 VPS、本地 SSH 密钥和云控制台救援入口
- 亲手完成　核对主机指纹后登录，创建练习用户并执行只读状态检查。启用防火墙前先确认 SSH 规则
- 备用入口　YouTube，Jilles 的 VPS 基础设置视频
- 链接　https://www.bilibili.com/video/BV12L4y187Dy?p=6
- 备用链接　https://www.youtube.com/watch?v=E0tUio6ZgH8

### V-LINUX-02　systemctl 与 journalctl

- 主入口　B 站，大飞 1024 的 journalctl 命令讲解
- 推荐观看　整段，用来认识日志筛选和时间范围
- 解决的问题　展示服务日志怎样按服务、时间和级别缩小范围
- 观看前准备　已经能登录使用 systemd 的练习 Linux 主机，并知道一个无业务风险的服务名
- 亲手完成　查看服务状态与最近日志，另开终端跟随日志；只在测试服务上练习 restart
- 备用入口　YouTube，Akamai Developers 的 systemctl 与 journalctl 演示
- 链接　https://www.bilibili.com/video/BV12P4y1u76e
- 备用链接　https://www.youtube.com/watch?v=3kl62YSU9XA

## Docker 与 Docker Compose

### V-DOCKER-01　Docker 与 Compose 主视频

- 主入口　B 站，GeekHour《30 分钟 Docker 入门教程》
- 推荐观看　P6 至 P9，看 Dockerfile、实践环节、Docker Desktop 和 Compose 简介
- 解决的问题　把镜像、容器、Dockerfile、端口映射和 Compose 放进同一组可见操作
- 观看前准备　安装当前 Docker Desktop 或 Docker Engine 与 Compose 插件，准备无生产数据的示例项目
- 亲手完成　先运行 `docker compose config`，再执行 `up -d`、`ps` 和 `logs`；最后用不带 `-v` 的 `down` 停止
- 备用入口　YouTube，TechWorld with Nana 的 Docker Compose 视频
- 链接　https://www.bilibili.com/video/BV14s4y1i7Vf?p=6
- 备用链接　https://www.youtube.com/watch?v=SXwC9fSwct8

## 部署平台控制台

### V-DEPLOY-01　Vercel 当前产品流程

- 主入口　B 站，一百个 Chocolate 的 Vercel 前端项目部署视频
- 推荐观看　整段，重点看导入项目、部署和打开生成地址
- 解决的问题　观察导入 Git 仓库、创建部署和查看部署结果的基本路径
- 观看前准备　准备不含秘密的 GitHub 练习仓库，并只授权该仓库
- 亲手完成　导入练习仓库，核对框架、项目名和目标分支，部署后打开生成地址并保存记录
- 备用入口　YouTube，Vercel 官方产品演示
- 链接　https://www.bilibili.com/video/BV11B4y1J7Rg
- 备用链接　https://www.youtube.com/watch?v=zFXscjUoDDA

## Flutter 与应用发布

### V-FLUTTER-01　Google Play 发布界面

- 主入口　YouTube，King Rittik 的 Google Play 发布视频
- 推荐观看　50 秒到结尾
- 解决的问题　展示登记包名、创建应用、构建 AAB 和上传发布包的连续过程
- 观看前准备　使用独立练习应用，确认包名、版本号、隐私政策和签名材料，不录入口令
- 亲手完成　记录 application ID、version、build 和签名证书指纹，生成 AAB 后先进入内部测试
- 说明　这一项暂时保留英文视频。公开可核的 B 站中文入口不够稳定，实践时以 Play Console 当前帮助为准
- 链接　https://www.youtube.com/watch?v=adt9A8125S4

### V-FLUTTER-02　iOS 上架全流程

- 主入口　B 站，ShiianAI 的 iOS App 开发上架全流程视频
- 推荐观看　重点看 Apple Developer、Xcode、App Store Connect 和上传步骤
- 解决的问题　从 Bundle ID、证书、Xcode 构建、App Store Connect 记录和上传动作建立一条可见路径
- 观看前准备　需要真实 Mac、当前 Xcode、受控 Apple Developer 账号和练习应用。没有这些条件时只观看
- 亲手完成　核对 Bundle ID、Team、Version、Build 与图标，Archive 后在 Organizer 检查签名身份
- 备用入口　YouTube，Flutter 官方 iOS 发布视频
- 链接　https://www.bilibili.com/video/BV1U7j7zQEeQ
- 备用链接　https://www.youtube.com/watch?v=iE2bpP56QKc

### V-FLUTTER-03　TestFlight 内部与外部测试

- 主入口　B 站，Winter 喵的 App Store 上架流程分享
- 推荐观看　重点看上传、审核前准备和 App Store Connect 相关部分
- 解决的问题　辅助辨认上传构建、测试分发和商店资料之间的关系
- 观看前准备　完成可验证的 Archive，准备受控测试账号和测试说明
- 亲手完成　先把已核对版本加入内部组，邀请一个测试账号，在真机记录安装和核心路径结果
- 备用入口　YouTube，Noah Does Coding 的 TestFlight 操作视频
- 链接　https://www.bilibili.com/video/BV1iPH9exEeW
- 备用链接　https://www.youtube.com/watch?v=x0d8Jx3HvdI

## 微信小程序

### V-WECHAT-01　小程序云开发与发布

- 主入口　B 站，编程小石头的小程序云开发合集
- 推荐观看　P5 至 P12 看云开发与开发者工具，P47 至 P59 看云函数，P62 看云存储
- 解决的问题　把小程序端、云开发环境、云数据库、云函数和云存储放进一组可见操作
- 观看前准备　准备练习小程序账号、微信开发者工具和不含真实用户数据的测试项目
- 亲手完成　创建练习项目，开通测试云环境，写一条测试数据，再用云函数读取它；发布前只走体验版或测试路径
- 备用入口　B 站，黑马程序员的小程序从基础到发布合集
- 链接　https://www.bilibili.com/video/BV1x54y1s7pk?p=5
- 备用链接　https://www.bilibili.com/video/BV1834y1676P?p=15
