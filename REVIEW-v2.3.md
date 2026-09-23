# v2.3 从头复核记录

用户已要求停止压缩。后续以校对和问题核查为准，旧的卷内减重目标不再作为本轮修改依据。

## 覆盖范围

- 全部 104 章已运行 human-writing 规则扫描，上一轮硬性失败为 0。规则扫描不等于逐章精读或技术事实核验。
- 本轮第 001 至 043 章已连续精读；第 044 至 063、064 至 083、084 至 104 章分别逐章精读并形成 `docs/review-044-063.md`、`docs/review-064-083.md`、`docs/review-084-104.md`。三份报告记载各章的修改、图检、出处和未实测边界。
- 第 024、025 章重新查阅了 [Cloudflare GitHub 集成与仓库授权](https://developers.cloudflare.com/pages/configuration/git-integration/github-integration/)、[Pages 预览访问控制](https://developers.cloudflare.com/pages/configuration/preview-deployments/)及 [Render Web Service 端口要求](https://render.com/docs/web-services)。第 030 章微信登录的 UnionID 适用条件已收窄表述；微信原始文档本轮仍无法直接打开，发布前仍应核对当前接口页。
- 外部视频已按 B 站优先、YouTube 备用嵌入练习位置，但尚未逐条实际播放。全书 PDF 和 EPUB 已生成校样；最终页检和链接核验仍在进行。

## 已修正文句

- 第 001 章修正“交接越安静许多”的语病。
- 第 002 章把无来源的“真实故障”改为明确的假设示例。
- 第 003 章补齐 JavaScript 后的空格，修正跨设备登录能够证明远程状态的过强推断，区分账号、会话和本地草稿。
- 第 006 章区分个人私有仓库协作者与组织仓库的权限设置。
- 第 007 章区分本地合并与远程合并后的同步动作；第 008 章修正 Fetch 会下载提交和文件对象的说明。
- 第 008、009 章补入已有 B 站优先视频索引的正文入口；第 009 章修正中英文空格。
- 第 010 章区分公开 Release 的未登录验证与私有 Release 的授权访问验证。
- 第 011 章修正取消管理员授权的错句，区分目录、语言虚拟环境和安全隔离；修正删除快照与恢复快照混淆，并限制 Network 面板观察结论的范围。
- 第 012 章注明计划轮换图与泄露应急处置的差别，将无来源的事故叙述标为假设示例。
- 第 013 章澄清 DNS 不转发 HTTP 请求、数据库不直接返回网页，补充静态文件也可能需要授权和禁止共享缓存；请求追踪案例明确为假设。
- 第 014 章区分 URL 显式端口与协议默认端口，补充 DNS 缓存和定位图的含义。
- 第 015 章修正 202、304、403 的概括，避免将已接受处理写成已完成、将拒绝请求等同于已确认身份；补充复用请求图的阅读限制。
- 第 016 章区分跨源与同站，说明 API Cookie 不必扩大到父域，修正“来自 disk cache 就说明发布有问题”的错误推断。
- 第 017 章说明后端也可在本机运行，区分页面内存状态与本地持久化状态，并补充 JavaScript 示例的 DOM 加载前提。
- 第 018 章明确数据库事务不能回滚外部副作用，补上状态快照与实时订阅之间的事件衔接，以及 Webhook 可靠保存后再确认接收的要求。
- 第 019 章区分 Console 既有消息与 Network 捕获范围，修正“复制请求代码就会重发”的错误表述。已有 B 站优先视频入口位置合适，本轮未实际播放验证。
- 第 020 章统一 Webhook 可靠保存后确认的顺序，补充预约与邮件任务的事务衔接，并限定时段唯一约束的适用范围。
- 第 021 章明确构建图适用于静态站，补充服务端产物不能整体公开发布；菜单网站标为假设示例。
- 第 022 章补充锁文件的复现边界、严格安装与 npm ci 的目录影响，以及 0.x 版本范围的特殊规则；故障故事标为假设示例。
- 第 023 章补充 GitHub Pages 分支发布默认的 Jekyll 处理，并将本地验收移到可能触发自动部署的 Push 之前。
- 第 024 章区分仓库授权范围与权限级别，避免将“只授权该仓库”写成“只读”；明确公开练习场景和私有仓库不等于私有站点，补充 Jekyll 处理并标明假设案例。
- 第 025 章区分常驻 Web Service 与平台函数，说明前端和 API 分拆只是方案之一，同时补充跨源调用的认证配置。
- 第 026 章区分构建内嵌变量、运行时配置和进程环境，避免将每次读取环境理解成控制台热更新；明确变量名称示例不替代框架前缀规则。
- 第 027 章补充功能开关必须在后端控制危险操作，以及双写后回滚旧版本可能造成新字段过时的风险；迁移案例标为假设，不建议机械拆分真实姓名。
- 第 028 章统一域名下线顺序，避免先解绑却保留悬空 DNS；区分根域解析与 HTTP 跳转，补充验证记录保留边界，邮件故障案例标为假设。
- 第 029 章补充事务中的并发控制、幂等编号的原子登记与请求绑定，修正“按生产行为直接改文档”的过强结论，并澄清服务端秘密的使用范围。
- 第 030 章统一实时状态与订阅衔接的说明，区分 Cookie、Token、OAuth 与 OIDC，并补充小程序重新登录后写操作的查询或幂等重试要求。
- 第 031 章明确 SQLite 属于关系数据库，说明多连接、单写事务、WAL 和活跃数据库备份边界；NoSQL 迁移改为假设案例，避免将嵌套字段直接归因为非原子写入。
- 第 032 章区分计划轮换和泄露止损，提醒现有连接可能仍需终止；修正双写与回填顺序，明确失败迁移不能盲目重跑、已执行迁移不应直接改写。
- 第 033 章统一 Webhook 可靠保存后确认的顺序，补充上传授权重复使用与验证后覆盖风险，以及密钥轮换的适用条件。
- 第 034 章补充 Supabase 高权限 Key 绕过 RLS、Firestore 服务端库绕过 Security Rules，以及规则不是查询过滤器的边界；澄清模拟器不会自动阻止生产外部调用，案例标为假设。
- 第 035 章修正迁移时数据同步与读写切换顺序，区分小程序发布和 Web 静态托管，补充停服不等于停止计费；切换到已修连线的 reviewed 插图。
- 第 034、035 章运行 human-writing 检查，未报告翻案句或黑话等问题，仅各提示一处中文冒号。按当前技能入口允许自然标点的规定保留，未为旧版扫描规则机械改写。
- 两章 human-writing 扫描无硬性失败；第 024 章有句长接近提示，结合技术教程文体保留现有内容，不为通过统计指标压缩或扩写。
- 上一轮第 016、018、066 章的三处句式调整仍保留，未删去技术要点。

## 插图发现

| 章节 | 文件 | 结果 |
| --- | --- | --- |
| 001 | delivery-chain-reviewed.png | 已修并目视验收。网页与 App 分发路径分开，连线不再穿过应用商店文字；原图保留。 |
| 002 | five-locations.png | 原图未见明显文字遮挡或裁切。 |
| 003 | release-route-decision-reviewed.png | 已修并目视验收。决策主线与各结果框分开，标签和连线不再穿框；原图保留。 |
| 004 | file-path-terminal-ui.png | 原图未见明显文字遮挡或裁切。 |
| 005 | git-change-flow.png | 原图未见明显文字遮挡或裁切。 |
| 006 | github-web-repository-ui.png | 原图未见明显文字遮挡或裁切。 |
| 008 | git-change-flow.png | 复用第 005 章已检查图片。 |
| 009 | merge-conflict-tree-reviewed.png | 已修并目视验收。“暂停并询问负责人”为终止分支，文本与二进制处理分支分开；原图保留。 |
| 010 | project-maintenance-dashboard.png | 原图未见明显文字遮挡或裁切。 |
| 011 | safe-repo-run-checklist-reviewed.svg | 已重绘为“专用工作目录”，并明确目录不等于安全沙箱。 |
| 012 | secret-lifecycle.png | 未见明显遮挡。图注已补充新旧值重叠仅适用于平台允许的计划轮换。 |
| 013 | web-request-flow-reviewed.svg | 已重绘 DNS 查询与 HTTP 往返路径，未见压字。 |
| 014 | url-dns-anatomy.png | 未见明显遮挡或裁切，正文补充箭头表示定位顺序。 |
| 015 | web-request-flow-reviewed.svg | 复用第 013 章新图，A4 页面已目视。 |
| 016 | login-session-flow.png | 未见明显文字遮挡或裁切。 |
| 017 | dynamic-app-architecture.png | 未见明显文字遮挡或裁切。 |
| 018 | api-data-realtime.png | 未见明显文字遮挡或裁切。 |
| 020 | dynamic-app-architecture.png | 复用第 017 章已检查图片，正文澄清 DNS 与 HTTP 分工。 |
| 021、022 | build-pipeline.png | 未见明显文字遮挡或裁切，图注明确为静态站点示例。 |
| 023 | static-deploy-routes.png | 未见明显文字遮挡或裁切，正文补充 Pages 分支发布的构建行为。 |
| 024 | static-deploy-routes.png | 复用第 023 章已检查图片。 |
| 025 | deployment-lifecycle.png | 未见明显文字遮挡或裁切。 |
| 026 | deployment-settings-ui.png | 未见明显文字遮挡或裁切。 |
| 027 | deployment-lifecycle.png | 复用第 025 章已检查图片，应用回滚与数据恢复的区别仍适用。 |
| 028 | server-public-entry-reviewed.svg | 已重绘 DNS 独立往返与实际请求路径，并标出主机防火墙为可选层。 |
| 029 | api-data-realtime.png | 复用第 018 章已检查图片。 |
| 030 | login-session-flow.png | 复用第 016 章已检查图片。 |
| 031 | database-choice-reviewed.svg | 已将 SQLite 与 PostgreSQL 放在关系数据库分支之下。 |
| 032 | backup-monitor-shutdown.png | 未见明显文字遮挡或裁切。 |
| 033 | api-data-realtime.png | 复用第 018 章已检查图片。 |
| 034 | baas-control-plane.png | 未见明显文字遮挡或裁切。 |
| 035 | release-route-decision-reviewed.png | 原正文仍引用旧图，已改为第 003 章验收过的修正版。 |
| 036 | vps-responsibility.png | 原图及 A4 校样未见遮挡或裁切；图注对不存在的小节的引用已修正。 |

三张 reviewed 图片由原图编辑生成，保存为同目录新文件并更新正文引用。编辑要求分别是分开网页与 App 路线、决策线绕开结果框、让冲突不明分支在暂停处结束；均要求保留原有知识节点并检查文字。图片检查不等于 EPUB 或 PDF 页面渲染验收。

## 核验依据与限制

- Fetch 的对象与引用行为参照 [Git 官方文档](https://git-scm.com/docs/git-fetch)。
- 仓库权限参照 [GitHub 个人账户仓库权限](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/repository-access-and-collaboration/permission-levels-for-a-personal-account-repository)，Release 访问参照 [GitHub Release 说明](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)。
- Python 虚拟环境的依赖隔离范围参照 [Python venv 文档](https://docs.python.org/3.12/library/venv.html)；快照恢复和删除的区别参照 [VirtualBox 用户指南](https://docs.oracle.com/en/virtualization/virtualbox/7.2/user/working-with-vms.html)。
- 页面网络记录的观察范围参照 [Chrome DevTools Network 文档](https://developer.chrome.com/docs/devtools/network)。秘密泄露后的撤销优先级参照 [GitHub 敏感数据清理说明](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)。
- B 站 GitHub Desktop 系列标题和部分分集信息已用搜索结果交叉核对；直接抓取页面失败，尚未实际播放验证。不能据此宣布全部视频可用。
- HTTP 状态语义参照 [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html)，Cookie 的发送范围参照 [MDN Set-Cookie 文档](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Set-Cookie) 和 [会话管理文档](https://developer.mozilla.org/en-US/docs/Web/Security/Authentication/Session_management)。第 014 至 016 章修改后均运行 human-writing 检查。
- 第 019 章复制和重放行为参照 [Chrome Network 操作参考](https://developer.chrome.com/docs/devtools/network/reference)。Webhook 的验签、重复事件与异步处理参照 [Stripe Webhook 文档](https://docs.stripe.com/webhooks)；可靠入队后确认的说明是针对进程故障风险补充的工程要求。第 017 至 019 章修改后运行 human-writing 检查。

## 后续检查起点

第 020 至 023 章的补充核验依据包括 [npm 安装说明](https://docs.npmjs.com/cli/install/)、[semver 范围规则](https://github.com/npm/node-semver)、[GitHub Pages 发布来源](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)、[Pages 建站与 Jekyll 处理](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site) 和 [Cloudflare Direct Upload](https://developers.cloudflare.com/pages/get-started/direct-upload/)。四章均运行 human-writing 检查。

本轮第 024、025 章官方文档检索连续两次连接失败。Pages 当前访问控制适用范围、Cloudflare GitHub App 的具体权限与 Render 当前运行要求仍待联网核验，不把正文精读记为这些产品事实已全部验证。已修内容限于明确概念、表述边界及前轮核验过的 Jekyll 行为。

本轮网络检索恢复。第 028 章下线安全核对了 [GitHub 自定义域名管理](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site) 和 [域名验证记录保留要求](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages)。第 029 章并发边界参照 [PostgreSQL 事务隔离文档](https://www.postgresql.org/docs/17/transaction-iso.html)。这不等于第 024、025 章的平台待核项已经补完。

第 030、031 章参照 [OpenID Foundation 开发说明](https://openid.net/developers/) 与 [SQLite 隔离说明](https://www.sqlite.org/isolation.html)。微信 code2Session 官方页面打开失败，返回字段、unionid 获取条件与 session_key 的完整说明仍需专项复核，不记为已完成。

第 032、033 章核对了 [Flyway 迁移记录说明](https://documentation.red-gate.com/fd/migrations-271585107.html)、[已执行迁移的校验](https://documentation.red-gate.com/flyway/reference/commands/validate) 和 [S3 预签名 URL 说明](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html)。预签名能力以具体服务为准，正文不宣称所有服务都有相同限制手段。

第 034 章核对了 [Supabase API Key 说明](https://supabase.com/docs/guides/getting-started/api-keys) 与 [Firestore 规则条件说明](https://firebase.google.com/docs/firestore/security/rules-conditions)，分别用于高权限 Key 和服务端规则边界。

第 036 章补充关闭密码登录前的密钥与管理权限验证、恢复入口准备，明确端口监听地址与多层网络规则的关系。修正系统盘目录位置与数据持久性混淆，澄清后台任务也可由托管服务承载，报名示例标为假设。存储删除边界参照 [EC2 实例终止说明](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/how-ec2-instance-termination-works.html) 和 [实例存储生命周期](https://docs.aws.amazon.com/us_en/AWSEC2/latest/UserGuide/instance-store-lifetime.html)，不将 AWS 行为直接推广为所有云平台规则。human-writing 扫描未发现所覆盖的问题。

第 037 章按 human-writing 精读，修正首次主机验证不能仅凭 IP、完整指纹须由可信独立渠道核对的说明；区分终端应用与 Shell，补充密钥泄露后的撤权、sudo 的实际权限边界，以及改端口时云安全组和系统防火墙的共同验证。无来源事故标为假设，包索引更新不再混同只读检查。依据为 [OpenSSH 客户端手册](https://man.openbsd.org/ssh)、[OpenSSH 服务端手册](https://man.openbsd.org/sshd) 和 [Windows Terminal 官方概述](https://learn.microsoft.com/en-us/windows/terminal/)。规则扫描未发现所覆盖的问题；正文中的视频索引仍指向 B 站优先资源，本轮未验证播放。

第 038 至 043 章随后完成精读与 human-writing 检查；第 044 至 104 章的逐章结论见上述三份报告。第 011、013、015、028、031、085、088、090、103 章的图已经重绘；旧 PNG 保留但不再由正文引用。视频按 B 站优先、YouTube 备用直接放入多个练习位置，外部播放仍需抽样实测。没有继续执行篇幅压缩。

## 排版交付门槛

用户要求先审查排版，再输出成稿。正文规则扫描、源图片查看和实际页面验收分开记录；未完成全书排版复核前，不输出最终发布版。

第 034、035 章以 Pandoc 和本地 Chrome 制作临时排版校样。Calibre 渲染失败，未用失败结果验收。初次校样发现 Pandoc 默认隐式图注与正文图注重复，已在校样转换中使用 `-f markdown-implicit_figures`，保留原有图注；同时显式设置 A4，隐藏校样标题占用的独立页，并让图片与紧随的图注保持相邻。此设置仍需纳入正式导出流程，临时校样不等于正式 EPUB/PDF。

修正后的两章 A4 校样共 10 页，已逐页查看渲染图片。未见文字遮挡、裁切、乱码、表格横向溢出或孤立标题，两幅图各保留一条图注且与图片同页，决策表完整落在一页。章节末尾保留自然留白，没有为压页删改正文。临时证据位于 `/private/tmp/book-layout-sQwDuk/`，不作为交付文件；尚未加入正式页码、页眉与全书目录，EPUB 小屏重排和其余章节实际排版仍待检查。

第 036 章 A4 校样共 5 页，初次检查发现清单引导句与列表跨页分离。校样 CSS 增加 `p:has(+ ul), p:has(+ ol) { break-after:avoid; }` 后重新渲染，并逐页查看全部 5 页；引导句已跟随列表，图文无明显重叠、裁切或重复图注。文件前缀为同一临时目录中的 `ch036-final`。该规则仍需合入正式导出流程；本轮不交付校样、不宣称全书排版通过，未 commit、未 push。

第 037 章 A4 校样共 6 页，已逐页查看。未见文字重叠、裁切、孤立标题或英文命令溢出；跟做视频提示完整位于第 4 页，未跨页拆开。无正文插图。临时文件前缀为 `ch037`；本次只验页面外观，书内相对链接仍需在正式整书导出时映射并测试，不将临时校样里的链接当成已通过的成品导航。human-writing 与结构检查通过，未 commit、未 push。

## 2026-09-24 全书成品复核

- `scripts/build_release.py --epub` 按 manifest 顺序组合 10 卷、104 章、卷首、术语和参考资料；正文没有为页数目标删减。整书 PDF 为 A4、496 页，封面在第 1 页，目录在第 2 至 4 页，卷首另起页，章节自然接排，底部有页码。
- PDF 逐页生成 496 张低分辨率缩略图，分成 8 张接触表巡检；无异常空白页、明显大块裁切或整页乱码。另以较高分辨率查看封面、目录、孤页修复位置和第 011、013、015、028、031、085、088、090、103 章修订插图所在页。九处图文未见重叠或裁切。通过全文提取筛查长度小于 150 字的页面，最终只剩封面、书名页、献辞等正常短页。
- PDF 内部跳转 206 处、外部链接 74 处；206 处内部目标均能在 PDF 命名目的地中找到。EPUB 压缩包校验通过，含 133 个 XHTML、104 个不同章锚点、10 个卷锚点、8 张修订 SVG。对 EPUB 的 1735 处本地链接和资源引用逐项检查，未发现缺失文件或锚点。抽取 EPUB 正文的 132 个 XHTML，以精确 390 px 浏览器视口逐个检查横向滚动与图片加载，零溢出、零缺图；另对第 085 章截图目视。
- `make test` 的 31 项测试通过；`make verify` 报告 0 错误、0 警告；`make audit` 覆盖 104 章、重复段落 0。审读中发现的技术细节和未实测平台边界见逐章报告。B 站优先视频已直接链接到相应练习段落，但尚未逐条实播核验，故不宣称外部视频全部可用。
- 视频复核尝试直接读取 B 站视频页和官方视频信息接口，但页面返回 HTTP 412、接口无法由当前检索工具访问；搜索命中只能辅助识别标题，不能代替播放验证。故上述视频可播放性限制仍保留。
- 成品文件在被 Git 忽略的 `dist/v2.3/`，正文和审校记录仍是未提交的本地修改；本轮未 commit、未 push。
