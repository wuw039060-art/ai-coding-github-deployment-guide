# Archive、TestFlight 与 App Store Connect

Xcode 显示 Archive succeeded 时，应用还没有进入 TestFlight。Archive 是 Mac 上的发布归档。上传后，App Store Connect 还要接收、处理并把构建关联到正确应用。之后才能选择内部或外部测试，最后提交 App Review。

这条链上每个系统都有独立状态。把“上传完成”“处理完成”“可供测试”和“已经审核”混成一句话，会让等待和失败无法定位。

![从 Xcode Archive 到 TestFlight 和 App Store](../assets/diagrams/testflight-appstore-flow.png)

*图 56-1　Archive 经过上传与处理后进入 TestFlight，经过测试的构建再提交 App Review。等价说明见本章“一次发布候选构建的完整路径”。*

## App Store Connect 先要有应用记录

App Store Connect 管理应用资料、构建、TestFlight、审核、销售和角色。它不是 Xcode 项目本身。首次上传前创建 app record。至少选择平台、应用名称、主要语言、Bundle ID 和 SKU。Apple 当前工作流说明，应用记录必须在上传构建前存在。

Bundle ID 要与 Archive 完全一致。SKU 是开发者内部识别值，不会成为 Bundle ID，也不是商店版本号。创建记录需要相应角色。只有 Account Holder、Admin 或 App Manager 等授权角色能完成部分管理动作。不要为了解决按钮不可见而共享 Account Holder 密码，先检查角色。

第一步冻结候选代码。记录 Git 提交、Flutter 版本、依赖锁文件、Version 和 Build。完成 Release 功能测试。第二步在 Xcode 生成 Archive。Organizer 中核对应用名、Bundle ID、版本、build 和创建时间。把这次 archive 作为不可修改的发布证据保留。

第三步选择分发方法。Apple 当前 Xcode 文档中的常见选项包括 TestFlight & App Store 与 TestFlight Internal Only。前者可用于 TestFlight 并继续提交 App Store，后者限制为团队内部测试。

第四步让 Xcode 验证签名、entitlements 和包内容。警告需要理解，错误要修复并重新 Archive。不要用跳过验证隐藏问题。第五步上传。Xcode 完成传输后，保存 Delivery Log 或相关上传记录。网络上传成功只说明文件到达接收端。

第六步等待 App Store Connect 处理。在应用的构建或 TestFlight 页面查看状态。处理完成后，构建才会出现在可选择列表。第七步处理 Export Compliance、隐私或缺失资料等提示。状态为 Missing Compliance 时，需要回答加密出口合规问题，不是继续等待就会自动变绿。

第八步把构建加入内部测试组，完成核心测试。需要外部测试时，创建外部组并提交必要的 TestFlight Beta Review。第九步选择经过验证的 build，补齐商店版本资料与审核信息，加入 submission 并提交 App Review。

## 上传方式怎样选

Xcode Organizer 是个人项目最直观的入口。它把 Archive、签名验证和上传放在一条界面流程中。Flutter 也可以运行 `flutter build ipa` 生成 `.xcarchive` 与 `.ipa`。当前 Flutter iOS 发布文档给出的默认位置如下。

```
build/ios/archive/
build/ios/ipa/
```

Transporter 可以上传已经生成的包，适合由独立人员负责交付。App Store Connect API 和命令行适合受控自动化，需要专门的 API Key 与最小角色。第一次发布不必同时学习所有上传方式。选择 Xcode Organizer，先形成可复现记录。自动化应在手工路径稳定以后再建立。

上传后，Apple 会检查和处理构建。页面短时间显示 Processing 属于正常状态。Apple 当前 Build upload statuses 把状态分为 Processing、Failed 和 Complete。若处理超过 24 小时，官方建议通过 Feedback Assistant 或支持渠道处理。

Failed 时选择该 build 查看错误、警告和信息。官方说明上传处理失败时，可以在修复后重用相同 build number。成功上传并被系统接受后，下一次则使用更高 build number。

不要在 Processing 期间连续上传多个内容相同、build 不同的归档。这样会制造多个候选，测试人员更容易选错。

## App 现在到底走到了哪一步

iOS 发布会连续出现多个很像“完成”的状态。Archive 成功说明 Xcode 生成了归档，上传成功说明构建到达 Apple 的处理系统，Processing 完成说明平台能够读取构建，TestFlight 可测试说明指定测试者可以安装。审核通过以后，还要确认发布方式、商店地区、版本页面和真实用户更新。任何一步完成，都只代表流程走到了这里。

每道门留下的证据也不同。Archive 需要归档记录和准确 build number，上传需要 Organizer 或上传日志，处理状态与 TestFlight 需要 App Store Connect 中的构建页面，真机测试需要设备、系统版本和关键流程记录，正式发布需要商店页面与生产后端观察。若上传失败，商店截图不能解释 Xcode 本地问题；若审核通过但登录失败，应回到生产服务和测试账号，而不是重新签名。

第一次练习发布时，可以建立一张时间线，逐项记录版本、负责人、开始时间、状态变化和下一步。任何状态长时间不变，先确认当前停在哪道门，再查对应日志和官方状态。这样即使 AI 帮助生成命令、解释上传错误或整理材料，账号持有人仍能知道它解决的是哪一段，哪些外部状态尚未发生。

Invalid Binary 表示构建没有满足上传要求，修复后重新交付。Missing Compliance 表示缺少出口合规资料，需要操作。Ready to Submit 表示构建可以分配内部测试，或提交外部测试与审核。它不表示用户已经收到。

Testing 表示至少有组或测试者正在使用。Expired 表示 TestFlight 测试窗口结束。Apple 当前说明 TestFlight build 最长可测试 90 天。

状态用英文保留，是为了读者能直接对应控制台。中文解释用于理解，不另造一个界面上找不到的名称。

## 内部测试者属于 App Store Connect 团队

内部测试者是获得相应应用访问权的 App Store Connect 用户。Apple 当前 TestFlight 概览允许每个应用最多 100 名内部测试者。人数属于易变信息，执行时重新核对。

内部测试适合开发、测试和产品团队。测试者安装 TestFlight App，接受邀请并安装 build。给测试组添加构建时，写清 What to Test。说明本次变更、重点步骤、已知限制和反馈邮箱。测试者不能根据“新版本”三个字猜任务。

使用 TestFlight Internal Only 上传的 build 只能加入内部组，不能以后直接拿去做外部测试或 App Store 发布。选择分发方式前要明确目的。

外部测试适合客户、受邀用户和更大范围测试。Apple 当前帮助说明，每个应用可邀请最多 10000 名外部测试者，可以用邮箱或公开链接，具体条件会变化。外部测试需要建立组、添加 build、填写测试说明，并在需要时提交 TestFlight Beta App Review。第一份外部 build 通常需要较完整审核，后续 build 可能不需要完整审核。

公开链接可以设置设备或系统条件。它方便招募，也可能被转发。不要把含真实敏感数据的测试环境暴露给任何拿到链接的人。测试账号使用专门环境和最小权限。测试结束后撤销访问，清理产生的数据。

## TestFlight 反馈也要带版本

TestFlight 可以收集截图、文字反馈、会话和崩溃等信息。维护者仍要把反馈对应到 Version、Build、设备和系统。让测试者按固定格式提交。

```
版本与构建　1.2.0 (18)
设备与系统　iPhone 15，iOS 19.1
操作步骤　登录后打开共享清单并添加图片
实际结果　选择图片后回到首页
预期结果　显示裁剪页面
发生时间　2026-08-05 20:15 中国标准时间
```

截图不要包含密码、身份号码、真实订单和个人聊天。测试数据可以专门设计。崩溃需要保留对应 Archive 和符号文件。Apple 的崩溃诊断指南要求使用匹配构建的符号信息把地址转换成可读函数。

Xcode 可能只在顶部显示一个概括错误。打开交付日志，找到第一条具体问题和涉及的 bundle。常见问题包括 Bundle ID 不匹配、build number 已使用、图标缺失、entitlement 与 Profile 不一致、Framework 架构不合规和使用不受支持的 Xcode 构建。

截至 2026 年 8 月 5 日，Apple Upload builds 页面列出的 iOS 构建要求为 Xcode 16 或更高。Apple 还会公布 upcoming requirements，这一数字封版与每次上传前都要复核。

不要从论坛下载脚本直接删除签名或重写 archive。回到源项目修复，再产生新 Archive。交付物应能从源代码重复构建。

## 构建上传了却不出现

先确认 Xcode 最后显示上传成功，并查看交付历史。再确认打开了正确 App Store Connect 团队和应用。比较 Bundle ID、Version 和 Build。构建会根据这些值关联应用和版本。

检查 Build Uploads 或相关活动状态。Processing 时等待，Failed 时打开详情。邮件通知可能延迟或进入垃圾箱，控制台状态更直接。超过官方异常时间后再联系支持，提交 Delivery Log、时间、App ID 和 build，不提交私钥与账号密码。

测试通过以后，在 App Store Connect 的版本页面选择对应 build。补充描述、关键词、截图、支持网址、隐私政策、年龄分级和审核信息。Apple 当前提交流程要求先把版本 Add for Review，加入一个 draft submission，再在提交页面点击 Submit for Review。状态才会进入审核流程。只完成 Add for Review 还没有真正发送。

审核账号应能进入所有需要检查的功能。提供明确步骤、特殊硬件条件和后端环境说明。审核期间保持服务器和账号可用。如果某功能只在特定地区或设备出现，主动说明。让审核人员猜入口，可能被判定功能不完整。

## 审核反馈按事实回复

被拒绝不等于账号失败。先读取具体 guideline、截图、设备和复现步骤。能复现时修正应用，增加 build，重新 Archive、测试和提交。元数据问题可以修改说明或截图，但不能用元数据掩盖应用真实行为。

无法复现时提供版本、测试账号、操作视频或日志，并礼貌说明差异。不要只回复“在我的手机正常”。若认为审核误解，引用实际功能和相关指南，给出最短进入路径。回复越可验证，往返越少。

Flutter 官方视频把 Bundle ID、App Store Connect 记录、Xcode 设置、Archive 和上传连成一条路径。它发布于 2023 年，概念和主要步骤仍有效，局部按钮和表单会变化，因此必须与 Apple 和 Flutter 当前文档并排使用。

- **视频标题**　Release an iOS app with Flutter in 7 steps
- **作者或机构**　Flutter
- **平台**　YouTube
- **发布时间**　2023 年 9 月 25 日
- **视频时长**　9 分 52 秒
- **推荐观看区间**　0 分 58 秒至 9 分 52 秒
- **解决的问题**　登记 Bundle ID，创建 App Store Connect 记录，核对 Xcode 设置，生成 Archive 并上传构建
- **观看前需要完成**　准备真实 Mac、当前 Xcode、受控 Apple Developer 账号和无真实用户数据的练习应用；缺少这些条件时只观看，不跟做
- **观看时亲手完成**　逐项核对 Bundle ID、Team、Version、Build 与图标，Archive 后在 Organizer 核对签名身份，再由账号持有人决定是否上传
- **界面时效**　截至 2026 年 8 月 6 日，流程仍符合 Flutter 当前发布文档的主要阶段；Xcode 与 App Store Connect 界面标记为部分符合当前版本
- **可点击链接**　[打开视频并从 58 秒开始](https://www.youtube.com/watch?v=iE2bpP56QKc&t=58s)

![Flutter iOS 发布视频链接二维码](../assets/qrcodes/vid-008.png)

*二维码 56-1　扫码后打开 Flutter 官方视频。*

## 视频跟做卡　TestFlight 测试组与真机安装

完成 Archive 与上传以后，再观看这一段较新的 TestFlight 操作。它覆盖构建发送、内部与外部测试组、启用测试和设备安装，没有替代本章对处理失败、合规问卷和构建证据的说明。

- **视频标题**　TestFlight & Xcode  Upload, Distribute, and Beta Test Your iOS App In Under 10 Minutes! (2025)
- **作者或机构**　Noah Does Coding
- **平台**　YouTube
- **发布时间**　2025 年 5 月 20 日
- **视频时长**　7 分 56 秒
- **推荐观看区间**　1 分 35 秒至 7 分 50 秒
- **解决的问题**　把 Xcode 构建发送到 App Store Connect，建立内部与外部测试组，启用测试并在设备安装
- **观看前需要完成**　完成一份可验证的 Archive，准备受控测试账号、测试说明和可公开给测试者的数据，了解外部测试可能需要 Beta App Review
- **观看时亲手完成**　只把已核对版本与 build 加入内部组，邀请一个测试账号，在真机安装并记录处理状态、设备、时间和核心功能结果
- **界面时效**　视频使用 2025 年界面，截至 2026 年 8 月 6 日可作为主要位置参考；Apple 会调整问卷、状态和审核要求，操作前仍需核对当前官方帮助
- **可点击链接**　[打开视频并从 1 分 35 秒开始](https://www.youtube.com/watch?v=x0d8Jx3HvdI&t=95s)

![TestFlight 视频链接二维码](../assets/qrcodes/vid-009.png)

*二维码 56-2　扫码后打开 TestFlight 操作视频。*

## 保留一份发布记录

每个上传 build 记录 Git 提交、Archive 路径、Xcode 与 Flutter 版本、Bundle ID、Version、Build、上传时间、处理结果和测试组。每次测试记录设备、系统、安装来源、核心结果和未解决问题。提交审核时记录所选 build、元数据版本和审核说明。

修复后不要覆盖旧 Archive。旧用户反馈和崩溃报告仍需要对应旧符号。AI 可以帮助整理上传错误和审核反馈，不能替代账号持有人选择 build 和点击提交。上传日志、API Key、签名证书和测试账号在交给外部工具前要脱敏与限权。

App Store Connect 可以查看 build 的上传时间、SDK、设备要求、entitlements 和文件大小等元数据。信息范围以当前页面为准。测试组添加 build 前，比较版本、build、上传者和处理时间。多个候选名称相同，不能只选列表最上面一项。

文件大小经过 App Thinning 后会按设备形成不同变体，用户下载大小不一定等于上传包大小。记录本次测试所选 build。测试反馈只写版本名称，无法区分同一版本下的多个修复包。

## Export Compliance 先调查加密用途

应用使用 HTTPS、系统加密、VPN、自研密码或第三方加密库时，可能需要回答出口合规问题。要求取决于应用能力与适用规则。开发者先列出应用和 SDK 使用的加密功能，咨询组织合规人员或官方指南。不能看到 HTTPS 就随意选择，也不能为跳过提示隐藏加密。

符合特定条件的应用可能在 Info.plist 提供相应声明，减少每次构建重复询问。具体键和值以 Apple 当前文档和真实情况为准。回答与 build 一起记录。功能或加密库变化时重新评估。

开发组验证崩溃修复和日志，产品组验证流程与文案，运营组验证商店素材和通知。一个“大群”会让反馈目标模糊。每个组写 What to Test 与已知限制。需要全新安装的 build，不要让测试者直接覆盖后报告迁移通过。

内部用户拥有 App Store Connect 访问。只为测试而加入的人员使用最小角色，并在离开后移除。构建撤出组前保存反馈。测试者设备上的已安装包不会因为从列表移除就自动删除。

## 外部测试先保护测试环境

外部人数增加后，测试服务器可能收到接近公开流量。限额、监控、备份和滥用保护要先准备。测试账号使用合成数据。公开邀请链接可能扩散，不能授予查看所有用户的权限。测试版隐私政策仍然适用。收集反馈、设备数据和崩溃信息时，向测试者说明用途。

停止测试后让 build expire，撤销账号和 API 凭据，按保留规则清理测试数据。

Beta App Description 说明测试版用途，Feedback Email 必须有人接收。What to Test 写本 build 的重点。Contact Information 提供能回答技术和审核问题的人。电话号码与邮箱在审核期有效。

需要登录时提供测试账号。涉及后端地区限制、蓝牙硬件或订阅沙箱时，给出准备步骤。信息缺失会让外部 Beta Review 无法进入功能。第一份 build 的审核更需要完整上下文。

## 测试 90 天窗口怎样管理

TestFlight build 最多可测试 90 天，过期后测试者无法继续使用该 build。长期内测项目按节奏上传新 build，不能把 TestFlight 当永久企业分发。每个新 build 都重新检查版本和功能。

临近过期时通知测试者升级。后端保留旧 build 的兼容窗口，直到合理过渡完成。用户设备系统过旧或新 build 提高最低版本时，提前说明数据导出和替代方案。

TestFlight 反馈包含 build 和设备信息时，先找到对应 Xcode Archive。确认 dSYM 与 UUID 匹配，再符号化崩溃。顶部系统帧不一定是应用根因。查看触发线程、异常类型和第一个相关应用帧。

按相同设备、系统和操作复现。修复后创建更高 build，不能把本地修复口头当作原 build 已修好。关闭旧 build 测试前，保存崩溃数量、反馈和修复对应关系。

## App Store 版本资料与 build 分开

版本页面保存描述、关键词、截图、推广文本、支持 URL 和审核信息。Build 区域选择一个已上传二进制。修改描述不会改变二进制，选择新 build 也不会自动更新截图。提交前同时核对。本地化资料可能独立编辑。默认语言已修正，其他语言仍可能保留旧功能承诺。

版本号显示给用户，build 用于内部区分。商店版本 `1.2.0` 可以经过多个 TestFlight build，最终只选择一个提交。

App Store Connect 可以配置审核通过后自动发布、手动发布或分阶段发布等当前选项。选择要符合支持与监控值班时间。手动发布能让团队在准备完成后控制上线，但也要关注批准后的有效窗口和平台规则。

分阶段发布只控制自动更新比例，用户可以手动下载。它不能代替后端兼容。发布前记录选择。不要让默认选项在无人值守的凌晨把重大版本公开。

## App Store 没有传统二进制回滚

一个坏 build 已到用户设备后，无法把旧 build 直接重新标为更新，因为版本和 build 必须前进。可以暂停分阶段发布，阻止更多自动更新。可以让后端关闭有问题功能，前提是开关预先设计。真正客户端修复仍要提交更高版本。

从商店下架会影响新下载，已经安装的 App 和已有数据不会自动消失。它也可能带来业务和用户支持后果。因此每次 TestFlight 测试、逐步发布和后端兼容都在构成回滚能力。

专用账号使用可重复的测试数据，权限只覆盖审核功能。账号密码存入团队密码管理器，不进入代码和公开文档。审核期间不自动过期，不要求发送验证码到个人设备。必须使用二步验证时，提供可执行说明。

后端每天检查审核账号和依赖服务。一次数据库清理不应把它删掉。审核完成后按制度轮换。下一版本提交前重新验证登录和全部入口。

## 一次 Invalid Binary 的排查

团队从旧 Mac 上传 build，Xcode 显示传输结束，但 App Store Connect 标记 Invalid Binary。Build Uploads 提示某嵌入 Framework 含不支持架构。

开发者保留 Delivery Log，定位到旧 Flutter 插件。升级插件并在真机测试，生成 build 19 的新 Archive。验证通过后上传。旧失败 build 保留在记录中，新 build 完成 Processing 并进入内部 TestFlight。

团队没有直接修改 archive 里的 Framework，也没有删除全部签名资产。问题在源依赖层得到修复，可由以后构建重复。

第一人核对二进制。Bundle ID、Version、Build、环境、签名、核心测试和符号资产正确。第二人核对商店。截图、描述、隐私、审核账号、联系信息、价格地区和发布方式正确。两人共同确认所选 build 与测试报告相同。保存提交时间和 submission 状态。

这个核对不需要大型流程。它能防止开发者选错 build，也能防止运营提交旧截图。

## App Store Connect 角色影响按钮可见性

Account Holder 负责协议和最高级账号事项。Admin、App Manager、Developer、Marketing 等角色能执行的操作不同。页面缺少上传、测试组或提交按钮时，先查当前用户角色和 App access。不要把权限问题误判成浏览器故障。

只负责截图的人不需要证书权限。只负责上传的人也不必查看财务。按职责授权能减少账号被滥用的影响。人员离开或外包结束后，移除访问并审查 API Key。测试账号与 App Store Connect 用户不是同一类资产，分别处理。

免费应用与付费功能涉及的协议和财务设置不同。销售、订阅和付款需要 Account Holder 接受当前协议，并配置税务与银行资料。这些资料属于组织和财务责任，不能由开发者根据教程虚构。名称、地址和银行主体要与账号法律实体一致。

协议过期或资料待处理可能阻止销售或提交。发布计划提前检查，不在审核通过后才发现。费率、税务和结算政策会变化，本书不写固定比例。执行时使用 Apple 官方协议与合格财务意见。

## Build 与版本状态不要混淆

Build Upload Status 描述上传文件处理。TestFlight Build Status 描述测试资格。App Version Status 描述商店版本审核与发布。一个 build 为 Complete，版本仍可能是 Prepare for Submission。一个版本被 Rejected，其他 TestFlight build 仍可能继续测试。

报错时截图包含页面标题、状态和 build。只说“Apple 显示红色”无法判断层级。运行手册把每个状态链接到下一步。Processing 等待，Missing Compliance 补资料，Invalid Binary 回源项目修复。

审核人员可能在另一个国家、时区和网络使用应用。后端不能只允许办公室 IP，也不能在夜间自动关闭测试环境。测试账号、邮件验证码、地图、OCR、推送和支付沙箱都要可用。第三方配额不足会让审核看到空白页面。

用未连公司网络的设备按审核说明完整走一次。记录外部请求和预期时间。审核期监控专用账号与服务错误，发现故障及时在 Resolution Center 说明，不能让审核者反复猜。

## Resolution Center 沟通保留上下文

Apple 的审核沟通会关联具体 submission。回复时引用 build、功能入口和修正内容。若上传新 build，明确旧问题在哪个 build 修复，并确保新 build 已添加到版本。只在消息里说“已修复”不够。

需要解释政策时引用当前 App Review Guidelines 条目，描述应用事实。不要提交账户密码、私钥或无关用户数据。保存沟通与最终决定。后续版本涉及同一功能时，提前把曾经要求的说明加入审核资料。

第一层是邀请。测试者邮箱、组和公开链接条件正确。第二层是 Apple Account。TestFlight 登录账号与受邀账号一致，Managed Apple Account 等限制按当前文档核对。

第三层是设备兼容。系统版本、设备类型和地区满足 build 要求。第四层是 build 状态。没有过期、没有 Missing Compliance，也已真正加入组。按层检查比重复删除 TestFlight 有效。客户端重装不能修复服务端没有把 build 加入组。

## 一个外部测试审核退回案例

应用需要蓝牙设备才能进入主页面，外部 Beta Review 没有硬件和演示模式，审核者只能看到连接失败。团队增加受控演示模式，使用合成设备数据，审核说明写清入口和与真实硬件的差别。新 build 在内部组验证后再次提交外部测试。

真实发布仍要求硬件用户测试。演示模式帮助审核理解功能，不能用来伪造实际兼容性。这个案例的修复位于产品可访问性与审核说明，不在证书和上传层。

至少在该版本仍有活跃用户和崩溃调查需求期间，保留 Archive、dSYM、Git 提交、构建环境、测试报告和提交资料。存储策略写期限与访问人。Archive 可能体积大，不能因为磁盘紧张随意清理最近生产版本。

删除前确认商店仍能取得哪些符号、是否有未解决崩溃、是否完成迁移。备份校验后再清本地副本。只保存 IPA 不足以替代完整 archive 与符号。

## TestFlight 与提交专题的掌握边界

读者需要能区分 Archive、Upload、Processing、TestFlight 与 App Review，知道 build number 每次上传怎样变化。还要能建立内部组、写测试任务、从状态页找上传失败，并把经过验证的 build 加入 submission。

暂时不用自动化 App Store Connect API、Xcode Cloud 和复杂多平台 bundle。手工证据链稳定后再学习。真正完成的标准是测试者从 TestFlight 安装正确 build 并完成任务，控制台出现一个 build 只能算中间结果。
