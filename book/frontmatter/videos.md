# 视频跟做索引

视频只辅助辨认动态界面，不替代正文。操作前先阅读对应章节，并以当前官方文档核对已经变化的按钮、政策和账号要求。

## VID 001　GitHub Desktop 入门操作

**作者或机构**　TECH GIANT  
**平台**　YouTube  
**发布或更新**　2025-04-09  
**视频时长**　8 分 40 秒
**推荐观看区间**　2 分 15 秒到 6 分 30 秒
**解决的问题**　辨认创建或克隆仓库、Changes、Commit、Push、Pull、分支与合并在 GitHub Desktop 中的位置和先后关系。  
**观看前需要完成**　安装当前 GitHub Desktop，登录练习账号，准备一个只含 README 的练习仓库；不要使用生产仓库。  
**观看时亲手完成**　克隆练习仓库，修改 README，在 Changes 中核对 Diff，提交并 Push；再从网页修改一行并 Pull，最后创建练习分支。  
**界面时效**　current  
**对应章节**　[第7章](../chapters/007-用-github-desktop-管理本地项目.md)、[第8章](../chapters/008-commit-push-pull-clone-和-sync.md)、[第9章](../chapters/009-分支-合并-冲突-撤销与恢复.md)  
**检索日期**　2026-08-06

[打开视频](https://www.youtube.com/watch?v=AYJQi6TyPyU)

![GitHub Desktop 入门操作的公开链接二维码](../assets/qrcodes/vid-001.png)

## VID 002　Chrome DevTools 入门演示

**作者或机构**　Chrome for Developers  
**平台**　YouTube  
**发布或更新**　2024-02-22  
**视频时长**　5 分 34 秒
**推荐观看区间**　23 秒到 4 分 39 秒
**解决的问题**　演示打开 DevTools、查看 Console 错误、使用 Sources 断点和在 Network 中筛选请求。  
**观看前需要完成**　使用当前稳定版 Chrome 打开本书的练习页面，先清空页面中的真实账号和个人数据。  
**观看时亲手完成**　亲手打开 DevTools，制造一条 Console 错误，刷新页面，在 Network 中选中请求并查看状态与响应，再切换网络限速。  
**界面时效**　current  
**对应章节**　[第19章](../chapters/019-浏览器开发者工具-状态码和网络请求.md)、[第60章](../chapters/060-console-network-build-log-和-runtime-log.md)  
**检索日期**　2026-08-06

[打开视频](https://www.youtube.com/watch?v=t1c5tNPpXjs)

![Chrome DevTools 入门演示的公开链接二维码](../assets/qrcodes/vid-002.png)

## VID 003　VPS 基础设置演示

**作者或机构**　Jilles  
**平台**　YouTube  
**发布或更新**　2025-10-28  
**视频时长**　17 分 1 秒
**推荐观看区间**　6 分 16 秒到 13 分 10 秒
**解决的问题**　展示云主机创建完成后的 SSH 登录、建立非 root 管理用户、检查 Nginx 服务和启用 UFW 的可见过程。  
**观看前需要完成**　准备可随时重建的测试 VPS、云控制台救援入口与本地 SSH 密钥；记下实例 IP，不使用生产服务器跟做。  
**观看时亲手完成**　核对主机指纹后登录，创建管理用户并重新登录，运行只读状态检查；启用防火墙前确认 SSH 规则与云控制台仍可访问。  
**界面时效**　partly-current  
**对应章节**　[第36章](../chapters/036-vps-云服务器及购买时需要看的参数.md)、[第37章](../chapters/037-第一次使用-ssh-登录服务器.md)、[第41章](../chapters/041-防火墙-caddy-nginx-域名与-https.md)  
**检索日期**　2026-08-06

[打开视频](https://www.youtube.com/watch?v=E0tUio6ZgH8)

![VPS 基础设置演示的公开链接二维码](../assets/qrcodes/vid-003.png)

## VID 004　Linux 服务管理演示

**作者或机构**　Akamai Developers  
**平台**　YouTube  
**发布或更新**　2021-05-05  
**视频时长**　14 分
**推荐观看区间**　1 分到 12 分 1 秒
**解决的问题**　展示 systemctl 状态与启停、journalctl 按服务筛选日志以及实时跟随日志。  
**观看前需要完成**　已能 SSH 登录一台使用 systemd 的练习 Linux 主机，并知道一个无业务风险的服务名称。  
**观看时亲手完成**　查看服务状态与最近日志，另开终端实时跟随日志；只在测试服务上练习 restart，并核对时间和退出状态。  
**界面时效**　current  
**对应章节**　[第37章](../chapters/037-第一次使用-ssh-登录服务器.md)、[第40章](../chapters/040-systemd-systemctl-journalctl-和服务日志.md)、[第61章](../chapters/061-服务器-docker-数据库和代理日志.md)  
**检索日期**　2026-08-06

[打开视频](https://www.youtube.com/watch?v=3kl62YSU9XA)

![Linux 服务管理演示的公开链接二维码](../assets/qrcodes/vid-004.png)

## VID 005　Docker Compose 入门演示

**作者或机构**　TechWorld with Nana  
**平台**　YouTube  
**发布或更新**　2024-01-11  
**视频时长**　1 小时 3 分 14 秒
**推荐观看区间**　11 分 58 秒到 27 分 18 秒；40 分 36 秒到 46 分 41 秒
**解决的问题**　把多条 docker run 命令改写成 Compose 文件，演示创建服务、up、down、start、stop、依赖顺序、变量与秘密。  
**观看前需要完成**　安装当前 Docker Desktop 或 Docker Engine 与 Compose 插件，准备作者示例或本书的无状态练习项目。  
**观看时亲手完成**　先运行 docker compose config，再执行 build、up -d、ps 与 logs；修改非秘密配置后用 up -d 重建，最后用不带 -v 的 down 停止。  
**界面时效**　current  
**对应章节**　[第44章](../chapters/044-运行环境问题与-docker-的基本模型.md)、[第47章](../chapters/047-docker-compose-与多容器应用.md)、[第48章](../chapters/048-容器状态-日志-健康检查和重启策略.md)、[第49章](../chapters/049-更新-回滚-清理与数据丢失风险.md)  
**检索日期**　2026-08-06

[打开视频](https://www.youtube.com/watch?v=SXwC9fSwct8)

![Docker Compose 入门演示的公开链接二维码](../assets/qrcodes/vid-005.png)

## VID 006　Vercel 控制台演示

**作者或机构**　Vercel  
**平台**　YouTube  
**发布或更新**　2026-03-16  
**视频时长**　10 分 11 秒
**推荐观看区间**　1 分 17 秒到 3 分 34 秒；9 分 6 秒到 9 分 50 秒
**解决的问题**　展示当前 Vercel 控制台导入项目、创建部署、查看部署后的分析信息和安全入口。  
**观看前需要完成**　准备一个不含秘密的 GitHub 练习仓库，并在 Vercel 中只授权该仓库。  
**观看时亲手完成**　导入练习仓库，核对检测到的框架、项目名和目标分支；部署后打开生成的网址并保存部署记录，不照抄任何付费或安全配置。  
**界面时效**　current  
**对应章节**　[第25章](../chapters/025-vercel-render-等自动部署平台.md)、[第26章](../chapters/026-build-command-output-directory-和环境变量.md)、[第27章](../chapters/027-preview-production-部署日志和回滚.md)、[第28章](../chapters/028-自定义域名-dns-https-费用与地区差异.md)  
**检索日期**　2026-08-06

[打开视频](https://www.youtube.com/watch?v=zFXscjUoDDA)

![Vercel 控制台演示的公开链接二维码](../assets/qrcodes/vid-006.png)

## VID 007　Flutter 应用发布到 Google Play 演示

**作者或机构**　King Rittik  
**平台**　YouTube  
**发布或更新**　2026-05-03  
**视频时长**　10 分 10 秒
**推荐观看区间**　50 秒到 10 分 10 秒
**解决的问题**　展示 Play Console 中登记包名、创建应用、填写商店信息、构建 AAB 和上传发布包的当前界面。  
**观看前需要完成**　使用完全独立的练习应用，确认唯一包名、版本号、隐私政策与测试签名材料；不要展示密钥口令。  
**观看时亲手完成**　在发布记录中写下包名、version、build 与签名证书指纹，生成 AAB，先上传到内部测试轨道并检查处理结果。  
**界面时效**　current  
**对应章节**　[第53章](../chapters/053-apk-aab-包名-版本号和-android-签名.md)、[第54章](../chapters/054-google-play-内部测试与发布流程.md)、[第57章](../chapters/057-商店素材-权限-隐私政策和审核反馈.md)  
**检索日期**　2026-08-06

[打开视频](https://www.youtube.com/watch?v=adt9A8125S4)

![Flutter 应用发布到 Google Play 演示的公开链接二维码](../assets/qrcodes/vid-007.png)

## VID 008　Flutter iOS 发布演示

**作者或机构**　Flutter  
**平台**　YouTube  
**发布或更新**　2023-09-25  
**视频时长**　9 分 52 秒
**推荐观看区间**　58 秒到 9 分 52 秒
**解决的问题**　从 Bundle ID、App Store Connect 记录和 Xcode 设置一路演示到 Archive 与上传。  
**观看前需要完成**　需要真实 Mac、当前 Xcode、受控 Apple Developer 账号和无真实用户数据的练习应用；没有这些条件只观看，不跟做。  
**观看时亲手完成**　逐项核对 Bundle ID、Team、Version、Build 与图标，Archive 后在 Organizer 核对签名身份，再由账号持有人决定是否上传。  
**界面时效**　partly-current  
**对应章节**　[第55章](../chapters/055-ios-macos-xcode-证书和-provisioning-profile.md)、[第56章](../chapters/056-archive-testflight-与-app-store-connect.md)  
**检索日期**　2026-08-06

[打开视频](https://www.youtube.com/watch?v=iE2bpP56QKc)

![Flutter iOS 发布演示的公开链接二维码](../assets/qrcodes/vid-008.png)

## VID 009　TestFlight 与 Xcode 上传和测试演示

**作者或机构**　Noah Does Coding  
**平台**　YouTube  
**发布或更新**　2025-05-20  
**视频时长**　7 分 56 秒
**推荐观看区间**　1 分 35 秒到 7 分 50 秒
**解决的问题**　展示从 Xcode 向 App Store Connect 发送构建、建立 TestFlight 内部与外部测试组、启用测试并在设备安装。  
**观看前需要完成**　完成一次可验证的 Archive，准备受控测试账号、测试说明和可公开给测试者的数据；了解外部测试可能需要 Beta App Review。  
**观看时亲手完成**　只把已核对版本与 build 加入内部组，邀请一个测试账号，在真机安装并记录处理状态、设备、时间与核心功能结果。  
**界面时效**　current  
**对应章节**　[第56章](../chapters/056-archive-testflight-与-app-store-connect.md)、[第57章](../chapters/057-商店素材-权限-隐私政策和审核反馈.md)  
**检索日期**　2026-08-06

[打开视频](https://www.youtube.com/watch?v=x0d8Jx3HvdI)

![TestFlight 与 Xcode 上传和测试演示的公开链接二维码](../assets/qrcodes/vid-009.png)
