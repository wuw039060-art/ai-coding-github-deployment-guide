# 视频跟做索引

视频只辅助辨认动态界面，不替代正文。中文读者先看 B 站入口，遇到平台官方演示或 B 站没有合适中文材料时，再看 YouTube 备用入口。操作前先读对应章节，并以当前官方文档核对已经变化的按钮、政策和账号要求。

本索引只放完整入口。正文里会在最适合动手的位置嵌入短提示，提醒读者看到哪里可以暂停阅读、打开视频、用练习项目跟做。

## VID 001　GitHub Desktop 入门操作

- 主入口　B 站，尚硅谷《Git 全套教程》
- 推荐观看　P7 至 P16 中的 GitHub Desktop、远程仓库、README、Ignore 和文件比对部分
- 解决的问题　辨认 Changes、Commit、Push、Pull、分支、远程仓库和文件差异在 GitHub Desktop 中的位置
- 观看前需要完成　安装当前 GitHub Desktop，登录练习账号，准备一个只含 README 的练习仓库；不要使用生产仓库
- 观看时亲手完成　克隆练习仓库，修改 README，在 Changes 中核对 Diff，提交并 Push；再从网页修改一行并 Pull，最后创建练习分支
- 备用入口　YouTube，TECH GIANT 的 GitHub Desktop 入门视频
- 嵌入位置　第 7、8、9 章
- 检索日期　2026 年 8 月 31 日

[打开 B 站主入口](https://www.bilibili.com/video/BV1wm4y1z7Dg?p=7)

[打开 YouTube 备用入口](https://www.youtube.com/watch?v=AYJQi6TyPyU)

## VID 002　Chrome DevTools 入门演示

- 主入口　B 站，不懂就来学《30 分钟掌握 Chrome DevTools》
- 推荐观看　先看打开面板、Console、Network 和请求详情相关部分
- 解决的问题　演示打开 DevTools、查看 Console 错误、在 Network 中筛选请求，并分辨状态码、Headers、Payload 和 Response
- 观看前需要完成　使用当前稳定版 Chrome 打开本书的练习页面，先清空页面中的真实账号和个人数据
- 观看时亲手完成　亲手打开 DevTools，制造一条 Console 错误，刷新页面，在 Network 中选中请求并查看状态与响应，再切换网络限速
- 备用入口　YouTube，Chrome for Developers 的 DevTools 入门视频
- 嵌入位置　第 19、60 章
- 检索日期　2026 年 8 月 31 日

[打开 B 站主入口](https://www.bilibili.com/video/BV1TbVv67EiJ)

[打开 YouTube 备用入口](https://www.youtube.com/watch?v=t1c5tNPpXjs)

## VID 003　VPS 登录与基础加固

- 主入口　B 站，我不是咕咕鸽《如何有效保护你的 VPS 服务器》
- 推荐观看　P6、P8、P9，分别看 SSH、普通用户和 UFW 防火墙
- 解决的问题　展示云主机创建完成后的 SSH 设置、非 root 管理用户和基础防火墙操作
- 观看前需要完成　准备可随时重建的测试 VPS、云控制台救援入口与本地 SSH 密钥；记下实例 IP，不使用生产服务器跟做
- 观看时亲手完成　核对主机指纹后登录，创建管理用户并重新登录，运行只读状态检查；启用防火墙前确认 SSH 规则与云控制台仍可访问
- 备用入口　YouTube，Jilles 的 VPS 基础设置视频
- 嵌入位置　第 36、37、41 章
- 检索日期　2026 年 8 月 31 日

[打开 B 站主入口](https://www.bilibili.com/video/BV12L4y187Dy?p=6)

[打开 YouTube 备用入口](https://www.youtube.com/watch?v=E0tUio6ZgH8)

## VID 004　Linux 服务日志

- 主入口　B 站，大飞 1024 的 journalctl 命令讲解
- 推荐观看　整段，用来认识 systemd 日志筛选和时间范围
- 解决的问题　展示 journalctl 怎样按服务、时间和日志级别缩小范围
- 观看前需要完成　已能 SSH 登录一台使用 systemd 的练习 Linux 主机，并知道一个无业务风险的服务名称
- 观看时亲手完成　查看服务状态与最近日志，另开终端实时跟随日志；只在测试服务上练习 restart，并核对时间和退出状态
- 备用入口　YouTube，Akamai Developers 的 systemctl 与 journalctl 演示
- 嵌入位置　第 37、40、61 章
- 检索日期　2026 年 8 月 31 日

[打开 B 站主入口](https://www.bilibili.com/video/BV12P4y1u76e)

[打开 YouTube 备用入口](https://www.youtube.com/watch?v=3kl62YSU9XA)

## VID 005　Docker 与 Compose 入门演示

- 主入口　B 站，GeekHour《30 分钟 Docker 入门教程》
- 推荐观看　P6 至 P9，看 Dockerfile、实践环节、Docker Desktop 和 Compose 简介
- 解决的问题　把镜像、容器、Dockerfile、端口映射和 Compose 放进同一组可见操作
- 观看前需要完成　安装当前 Docker Desktop 或 Docker Engine 与 Compose 插件，准备作者示例或本书的无状态练习项目
- 观看时亲手完成　先运行 `docker compose config`，再执行 `build`、`up -d`、`ps` 与 `logs`；修改非秘密配置后用 `up -d` 重建，最后用不带 `-v` 的 `down` 停止
- 备用入口　YouTube，TechWorld with Nana 的 Docker Compose 视频
- 嵌入位置　第 44、45、47、48、49 章
- 检索日期　2026 年 8 月 31 日

[打开 B 站主入口](https://www.bilibili.com/video/BV14s4y1i7Vf?p=6)

[打开 YouTube 备用入口](https://www.youtube.com/watch?v=SXwC9fSwct8)

## VID 006　Vercel 控制台演示

- 主入口　B 站，一百个 Chocolate 的 Vercel 前端项目部署视频
- 推荐观看　整段，重点看导入项目、部署和打开生成地址
- 解决的问题　展示 Vercel 控制台导入 Git 仓库、创建部署和查看部署结果的基本路径
- 观看前需要完成　准备一个不含秘密的 GitHub 练习仓库，并在 Vercel 中只授权该仓库
- 观看时亲手完成　导入练习仓库，核对检测到的框架、项目名和目标分支；部署后打开生成的网址并保存部署记录，不照抄任何付费或安全配置
- 备用入口　YouTube，Vercel 官方产品演示
- 嵌入位置　第 24、25、26、27、28 章
- 检索日期　2026 年 8 月 31 日

[打开 B 站主入口](https://www.bilibili.com/video/BV11B4y1J7Rg)

[打开 YouTube 备用入口](https://www.youtube.com/watch?v=zFXscjUoDDA)

## VID 007　Google Play 发布界面

- 主入口　YouTube，King Rittik 的 Google Play 发布视频
- 推荐观看　50 秒到结尾
- 解决的问题　展示 Play Console 中登记包名、创建应用、填写商店信息、构建 AAB 和上传发布包的当前界面
- 观看前需要完成　使用完全独立的练习应用，确认唯一包名、版本号、隐私政策与测试签名材料；不要展示密钥口令
- 观看时亲手完成　在发布记录中写下包名、version、build 与签名证书指纹，生成 AAB，先上传到内部测试轨道并检查处理结果
- 备用说明　这一项暂时保留英文视频，因为公开可核的 B 站中文入口不够稳定。正式发布仍以 Play Console 当前帮助和自己的账号提示为准
- 嵌入位置　第 53、54、57 章
- 检索日期　2026 年 8 月 31 日

[打开 YouTube 入口](https://www.youtube.com/watch?v=adt9A8125S4)

## VID 008　iOS 上架全流程

- 主入口　B 站，ShiianAI 的 iOS App 开发上架全流程视频
- 推荐观看　重点看 Apple Developer、Xcode、App Store Connect 和上传步骤
- 解决的问题　从 Bundle ID、证书、Xcode 构建、App Store Connect 记录和上传动作建立一条可见路径
- 观看前需要完成　需要真实 Mac、当前 Xcode、受控 Apple Developer 账号和无真实用户数据的练习应用；没有这些条件只观看，不跟做
- 观看时亲手完成　逐项核对 Bundle ID、Team、Version、Build 与图标，Archive 后在 Organizer 核对签名身份，再由账号持有人决定是否上传
- 备用入口　YouTube，Flutter 官方 iOS 发布视频
- 嵌入位置　第 55、56 章
- 检索日期　2026 年 8 月 31 日

[打开 B 站主入口](https://www.bilibili.com/video/BV1U7j7zQEeQ)

[打开 YouTube 备用入口](https://www.youtube.com/watch?v=iE2bpP56QKc)

## VID 009　TestFlight 与测试分发

- 主入口　B 站，Winter 喵的 App Store 上架流程分享
- 推荐观看　重点看上传、审核前准备和 App Store Connect 相关部分
- 解决的问题　辅助辨认上传构建、测试分发和商店资料之间的关系
- 观看前需要完成　完成一次可验证的 Archive，准备受控测试账号、测试说明和可公开给测试者的数据；了解外部测试可能需要 Beta App Review
- 观看时亲手完成　只把已核对版本与 build 加入内部组，邀请一个测试账号，在真机安装并记录处理状态、设备、时间与核心功能结果
- 备用入口　YouTube，Noah Does Coding 的 TestFlight 操作视频
- 嵌入位置　第 56、57 章
- 检索日期　2026 年 8 月 31 日

[打开 B 站主入口](https://www.bilibili.com/video/BV1iPH9exEeW)

[打开 YouTube 备用入口](https://www.youtube.com/watch?v=x0d8Jx3HvdI)

## VID 010　微信小程序云开发与发布

- 主入口　B 站，编程小石头的小程序云开发合集
- 推荐观看　P5 至 P12 看云开发与开发者工具，P47 至 P59 看云函数，P62 看云存储
- 解决的问题　把小程序端、云开发环境、云数据库、云函数和云存储放进一组可见操作
- 观看前需要完成　准备练习小程序账号、微信开发者工具和不含真实用户数据的测试项目；不要把 AppSecret、云环境 ID 和生产数据库内容贴到公开页面
- 观看时亲手完成　创建练习项目，开通测试云环境，写一条测试数据，再用云函数读取它；发布前只走体验版或测试路径
- 备用入口　B 站，黑马程序员的小程序从基础到发布合集
- 嵌入位置　第 33、34、35、87 章
- 检索日期　2026 年 8 月 31 日

[打开 B 站主入口](https://www.bilibili.com/video/BV1x54y1s7pk?p=5)

[打开 B 站备用入口](https://www.bilibili.com/video/BV1834y1676P?p=15)
