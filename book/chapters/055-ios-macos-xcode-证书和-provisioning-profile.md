# iOS、macOS、Xcode、证书和 Provisioning Profile

iOS 应用可以用 Flutter 编写大部分界面和逻辑，最终仍要由 macOS 上的 Xcode 构建、签名和分发。Windows 可以写 Dart 代码、完成 Android 构建，也可以研究 Apple 文档，但不能在本机完成可信的 iOS Archive 和 App Store 上传验收。

Apple 签名看起来复杂，是因为它同时回答应用是谁、签名者属于哪个团队、允许使用哪些系统能力以及准备怎样分发。把证书、标识和 Provisioning Profile 分开以后，错误信息会清楚很多。

macOS 与 Windows 差异

> 本章涉及 Xcode、钥匙串、Archive 和 iOS 真机签名的步骤必须在 Mac 上完成。当前书稿工作环境是 Windows，没有真实 Apple Developer Program 账号，因此本章只依据截至 2026 年 8 月 5 日的 Apple 与 Flutter 官方资料核验。最终需要在用户控制的 Mac 和账号中实测。

## Apple Account 与开发者会员不同

普通 Apple Account 可以下载 Xcode、阅读文档，并在一定限制下做设备开发测试。要通过 TestFlight、App Store 或其他受支持分发方式向用户提供应用，通常需要加入 Apple Developer Program。Apple 的分发文档说明，加入后会建立 App Store Connect 访问，并提供相应分发能力。

截至 2026 年 8 月 5 日，Apple 官方会员比较页写明，Apple Developer Program 为每会员年 99 美元，支持当地货币的地区按当地货币收取。符合条件的非营利、教育或政府实体可能申请费用减免。

成本可能发生变化

> 费用、税费、支付方式、地区可用性和减免资格都要在付款当天核对官方页面。本书不把 99 美元写成永久价格。

个人加入时，商店通常显示个人法定姓名。组织加入时，需要合法实体和 D-U-N-S Number 等资料，应用可显示组织名称。不要为了显示品牌名，把尚未准备好的个人账号误当组织注册。

## Xcode 是 Apple 平台的构建与签名中心

Xcode 是 Apple 的集成开发环境。Flutter 命令最终调用 Xcode 工具链来编译 iOS 原生部分、链接 Framework、处理资源和签名。Flutter 项目中的 `ios/Runner.xcworkspace` 是常用打开入口。使用 CocoaPods 的项目应打开 workspace，直接打开 `Runner.xcodeproj` 可能看不到 Pods 依赖。

在项目根目录先运行下面的检查。

```
flutter doctor -v
flutter pub get
cd ios
pod install
cd ..
```

运行位置

> macOS Terminal。需要已安装兼容的 Flutter、Xcode、Xcode Command Line Tools 和 CocoaPods。`pod install` 只在项目使用 CocoaPods 且需要更新依赖时运行。

预期 `flutter doctor -v` 的 Xcode 项没有阻止构建的错误，Pods 安装完成，并生成或更新 workspace 依赖。若 Xcode 许可未接受或命令行工具路径错误，先修工具链，不修改应用代码。

## Bundle ID 是 Apple 侧的应用标识

Bundle ID 例如 `com.example.pocketlist`，用于连接 Xcode Target、Apple Developer 账号中的 Identifier 和 App Store Connect 应用记录。它与 Android Application ID 形式相似，可以设计成相同文字，但两边是独立平台记录。修改一边不会自动修改另一边。

首次发布前确认 Bundle ID 属于自己的命名空间，能长期保持。推送、Sign in with Apple、Associated Domains 等能力会附着到标识上。发布后换标识会形成另一款应用，旧用户不能按普通更新迁移。

在 Xcode 选择 Runner Target 后，可以在 Signing & Capabilities 与 General 区域看到团队、Bundle Identifier、版本和构建号。具体界面随 Xcode 变化，封版时要按当前版本复核。

Apple 开发证书用于设备开发和测试，分发证书用于分发或上传。Apple 当前证书概览说明，Xcode 11 及以后可使用 Apple Development 和 Apple Distribution 等统一证书类型。

证书包含公开部分，私钥通常保存在创建它的 Mac 钥匙串中。只下载 `.cer` 文件，不一定拥有能完成签名的私钥。组织中的分发证书属于团队资产。不要把个人 Apple 账号密码和整个钥匙串导出给外包人员。使用 App Store Connect 角色与 Xcode 的团队签名管理，按需要授权。

证书到期不一定让商店中已经安装的 App 立即停止，但会影响继续上传新版本。企业内部分发等场景的影响不同，必须按证书类型查官方说明。

## Provisioning Profile 连接多项条件

Provisioning Profile 常译为描述文件。它把 App ID、团队、签名证书、应用能力以及某些分发方式中的设备集合连接起来。开发 Profile 允许指定团队在注册设备上运行开发构建。App Store 分发 Profile 对应商店提交。Ad Hoc Profile 会包含允许安装的已注册设备。

![Apple 签名资产的关系](../assets/diagrams/apple-signing-assets.png)

*图 55-1　证书、Bundle ID、Capabilities 与分发方式通过 Provisioning Profile 形成可签名组合。等价说明见本章“Provisioning Profile 连接多项条件”。*

错误提示说 Profile 不包含某项 entitlement，通常表示项目启用了某个能力，但开发者账号或 Profile 中没有一致授权。反复重新下载证书不能修复 Bundle ID 或能力不匹配。

## 先让 Xcode 自动管理签名

对个人项目和小团队，优先使用 Xcode 的 Automatically manage signing。选择正确 Team，Xcode 会创建或更新必要 Identifier、证书和 Profile。

自动签名减少手工匹配，不等于可以忽略结果。仍要确认团队、Bundle ID、能力和分发方式正确。手动签名适合受控 CI、大型团队或特殊权限制度。它要求明确管理每个证书和 Profile 的生成、安装、到期与轮换。本书不要求初学者为展示专业程度改成手动模式。

Push Notifications、Associated Domains、Sign in with Apple、iCloud 和 In-App Purchase 等属于应用能力。它们可能同时要求开发者账号配置、Xcode entitlement、后端配置和商店资料。

例如启用推送时，客户端需要正确 entitlement，服务器还要使用 APNs 密钥或证书发送。只在 Xcode 点开开关，推送不会自动工作。每添加一个第三方 Flutter 插件，检查它是否要求新的 capability、Info.plist 使用说明或最低 iOS 版本。插件编译成功不能证明商店审核允许其行为。

## 权限说明写在 Info.plist

iOS 在访问相机、麦克风、照片和定位等敏感能力前，会显示应用提供的用途说明。缺少某些说明可能导致运行时退出或审核问题。说明要具体，例如“扫描纸质收据并添加到本次记账”。写“需要权限以提供更好体验”没有告诉用户数据用于什么。

请求权限的时机仍由应用代码控制。把用途字符串加入 Info.plist 只是准备系统弹窗，不会自动获得权限。多语言应用要核对本地化说明。审核截图和商店描述也要与实际权限用途一致。

在 Mac 上用 Xcode 打开 `ios/Runner.xcworkspace`，选择 Runner Target 与正确 Team。连接一台由你控制的 iPhone，按 Xcode 和设备提示建立信任。选择真机作为运行目标，执行 Run。预期 Xcode 完成编译、签名、安装并启动 App。设备可能要求启用 Developer Mode，按当前系统提示操作。

若出现 Signing for Runner requires a development team，说明尚未选择 Team。若 Bundle Identifier 无法注册，检查它是否已被占用或账号没有权限。若设备不在开发 Profile 中，让自动签名更新，或由账号管理员注册设备。

运行成功后，测试需要权限和系统能力的功能。模拟器不能完整替代相机、推送、性能和真实签名环境。

## 版本与构建号必须对应

Flutter 的 `version: 1.2.0+17` 会映射到 iOS 的用户版本和 build number，也可以在构建命令中覆盖。Flutter iOS 发布文档说明，每次上传需要唯一 build number。

Xcode General 页也能显示和编辑 Version 与 Build。团队要确定唯一事实来源，避免 `pubspec.yaml`、CI 参数和 Xcode 手工值互相覆盖。商店同一版本可以上传多个 build，例如 `1.2.0 (17)` 和 `1.2.0 (18)`。版本给用户看，build 用于区分同一版本的不同候选构建。

收到问题时同时记录两者。只有“1.2.0 崩溃”无法知道用户拿到哪个 build。

Run 面向开发设备，Archive 生成供分发的 Release 归档。Archive 保存应用、签名信息和符号等发布证据，后续可从 Organizer 验证和分发。在 Xcode 中选择合适的通用或真实设备目标，再使用 Product 菜单的 Archive。构建完成后 Organizer 应显示新归档，版本、build、时间和 Bundle ID 正确。

若 Archive 菜单不可用，常见原因是选择了模拟器。若 Release 编译失败，保存第一条有效错误。不要仅因为 Debug Run 成功，就认为 Xcode 有问题。Apple 的 Release 测试指南建议保留 archive，以便测试、提交和后来分析匹配版本的崩溃。

## 常见签名错误按关系排查

No profiles for 某 Bundle ID were found，先核对当前 Team、Bundle ID、账号网络和自动签名权限。Profile doesn't include 某 entitlement，核对 Signing & Capabilities、开发者网站 Identifier 和目标分发方式。

Signing certificate not found，检查当前 Mac 钥匙串是否同时有证书和私钥，团队角色是否允许获取或创建证书。Bundle ID mismatch，比较 Flutter 项目、Xcode Target、Developer Identifier 和 App Store Connect app record。不要在四个页面轮流改成不同值。

Archive 验证时报版本已使用，增加 build number 后重新 Archive。归档内部信息在创建时已经确定，给文件夹改名无效。

源代码、依赖锁文件和项目设置进入受控版本库。证书私钥、API Key 和密码放在专门秘密管理中。使用自动签名时，新 Mac 登录获授权的 Apple Account，由 Xcode 获取团队签名资产。组织可限制谁能访问云管理证书。

需要迁移本地私钥时，使用钥匙串的受保护导出流程，设置强密码并通过独立安全通道传递。迁移后验证目标 Mac 能 Archive，再删除临时副本。不要把 `.p12`、Profile、密码和账号恢复码放进同一个网盘目录。团队离职流程要撤销不再需要的账号权限和本地资产。

## 中国大陆使用注意

Apple Developer Program 注册、付款、组织验证、双重认证和服务访问会受到地区、网络与支付条件影响。预留审核资料和 D-U-N-S 处理时间。开发者账号、App Store Connect 和证书属于长期资产。不要通过来源不明的代上架服务交出账号控制权。若必须与服务商合作，使用最小角色和书面交接。

应用还可能涉及中国大陆的隐私、网络服务和内容合规。商店通过不等于自动满足当地法律要求。需要时咨询合格专业人士。

在真实 Mac 和账号中，本章应完成 Xcode 工具链检查、自动签名真机运行、权限功能测试和一次 Archive。记录 Xcode、macOS、Flutter、设备系统、Team、Bundle ID、Version 与 Build。

当前项目尚不能完成这项实机验收。书稿只会把步骤标为待 Mac 验证，不用“根据文档应该成功”替代实际证据。AI 可以解释 Xcode 错误并比较签名配置。你必须亲自确认 Team、Bundle ID、证书私钥、Capabilities 和 Archive。不要把 Apple Account 密码、恢复码或分发私钥交给 AI。

## Runner、Target、Scheme 和 Configuration

Runner 是 Flutter 默认 iOS 应用名称，也常是 Xcode Target。Target 定义要构建的产品和设置。Scheme 选择构建哪些 Target、使用什么动作和配置。Configuration 常见 Debug、Profile 与 Release。Archive 使用 Release 配置，普通 Run 常使用 Debug。

一个项目加入开发、预发布和生产环境后，可能有多个 Scheme 与 Configuration。构建前在 Xcode 顶部确认当前选择，不能只看窗口标题。环境错配会生成签名正确却连接测试服务器的生产包。关于页面显示环境，Archive 记录 Scheme 和配置。

Build Settings 可以来自项目、Target、Configuration、`.xcconfig` 和依赖。界面中显示的最终值可能覆盖源文件中的设置。修改前查看该值来自哪一层。直接在 Target 页面写死，可能让 CI 和本地配置分叉。

Flutter 生成的配置文件连接 Dart 构建和 Xcode。删除或手工重写后，`flutter build` 与 Xcode Archive 可能表现不同。遇到值不符，先导出或查看最终 Build Settings，再比较 Configuration。不要在每个层级都加一份相同变量。

## CocoaPods 故障先看依赖关系

许多 Flutter iOS 插件通过 CocoaPods 集成。`Podfile` 声明平台和安装规则，`Podfile.lock` 记录解析版本，Pods 目录保存下载与生成内容。`pod install` 遵循锁文件安装，`pod update` 可能改变依赖版本。排错时不要把两者混用。出现 deployment target 过低时，查看插件支持和项目最低 iOS 版本。提高版本会让旧设备失去支持，要记录产品决定。

出现找不到模块或 Framework 时，确认打开 workspace、Pods 安装成功、架构支持当前设备。清缓存以前保存第一条错误。

Apple Silicon Mac 使用 ARM 架构。旧原生库可能只有 Intel 模拟器或真机架构，导致链接失败。为了临时成功而全局排除某架构，可能让某类设备无法构建。先检查插件是否有支持当前 Xcode 的新版本。

真机 iPhone、Apple Silicon 模拟器和 Archive 的架构需求不同。错误发生在哪个目标，要从构建命令和日志确认。使用 Rosetta 运行旧工具只能作为过渡。把依赖升级与原生库替换写入维护计划。

## 注册设备的数量和用途

开发和 Ad Hoc 分发会涉及设备注册。设备由 UDID 唯一识别，加入开发者账号后进入相应 Profile。团队不要收集无关个人设备。记录设备所有者、用途和移除日期。Apple 对年度设备数量和重置有当前规则，执行时查账号帮助。

TestFlight 不要求逐台登记外部测试设备，因此面向较大测试组更合适。设备更换后，旧 Profile 可能仍包含旧 UDID。自动签名会处理很多更新，团队资产清单仍要维护。

Keychain Access 中的证书展开后，应能看到对应 private key。只有证书而没有私钥，Xcode 无法用它签名。从另一台 Mac 只下载 `.cer`，不会把原私钥带来。需要受控导出包含证书与私钥的 `.p12`，或通过团队云管理签名重新获取授权资产。

私钥导出设置强密码。传输文件与传输密码使用不同渠道，并在目标 Mac 导入后删除临时副本。发现不认识的分发证书时，先查团队成员和 CI。随意撤销可能让别人的发布任务中断。

## 证书到期前做什么

每月检查 Apple Developer Program 会员、分发证书、APNs 凭据和相关 Profile 的到期时间。提前创建或更新资产，在测试环境完成 Archive、上传和推送验证。不能等发布当天才轮换。

证书到期对已上架 App 与新上传的影响不同。Apple 证书概览说明，会员有效时，App Store 中已有应用通常不受已过期 App Store 分发证书影响，但不能再用它上传新应用或更新。

APNs 证书到期会影响推送。使用 Token Key 的生命周期和撤销方式不同，单独记录。

Entitlements 文件可以包含推送环境、关联域、钥匙串组和应用组等声明。最终签名把这些能力纳入应用。源文件写了某 entitlement，不代表 Profile 允许。Profile 允许，也不代表后端与平台服务已经配置。

使用 Xcode archive 验证和签名检查查看最终能力。开发与生产推送环境不要混淆。删除功能时，同时清代码、capability、entitlement、后台配置和隐私披露。只隐藏入口仍可能保留权限。

## Archive 前的真机清单

- 从系统结束 App 后冷启动
- 拒绝每项非核心权限并继续使用
- 登录、退出和令牌过期路径通过
- 深层链接在未开 App 与后台状态都通过
- 推送在开发或测试分发环境到达
- 弱网、超时和后端 5xx 有准确提示
- 本地数据库从上个商店版本升级
- Version、Build、环境和支持链接正确

一项依赖真实生产服务时，使用受控预发布环境模拟。不能因为开发服务器暂时可用就跳过错误路径。

Dart 编译失败看源码文件和行。CocoaPods 或 Swift 编译失败看具体插件与平台版本。Linker 错误看重复符号、缺失架构和 Framework。CodeSign 错误看 Team、证书私钥、Profile、Bundle ID 和 entitlement。Validate 错误看商店要求、图标、版本和包内容。

每次只改一层并重新执行相同 Archive。换 Xcode、删 Pods、改 Bundle ID 和重建证书同时进行，会失去因果关系。修复后保存成功 archive 和失败日志。下次相同错误可以比较。

## Mac 本身也要可恢复

源代码保存在远程受控仓库。依赖和工具版本有记录。签名私钥与 API Key 依照组织制度备份或由云管理。新 Mac 恢复演练从克隆项目开始，安装固定 Flutter 与 Xcode，获取最小签名权限，完成 Archive。若只能在原 Mac 构建，项目有单点故障。

不要备份整个 DerivedData 当恢复方案。它是可重建缓存，不能替代源码和签名资产。Mac 报废或人员离开时，撤销账号会话和不再需要的证书访问，轮换本地保存的 API Key。

Flutter 可以构建 macOS 应用，签名与分发路径却不同。Mac App Store、Developer ID、notarization 和 sandbox 有自己的要求。本章标题提到 macOS，是为了说明 Xcode 与 Apple 账号同时服务多个平台。后续 Archive 和 TestFlight 重点仍是 iOS。

把 iOS 的 Provisioning Profile 或分发选择原样套到直接分发 macOS App 会出错。真正发布 macOS 时查当前 Apple 专门文档。书中不为篇幅同时展开两个完整商店流程，避免读者在第一次 iOS 发布中混入 Developer ID 和 notarization。

## 一次团队交接案例

原开发者离开后，新成员能打开源码，却无法 Archive。钥匙串里没有分发私钥，App Store Connect 角色也只有 Marketing。团队先由 Account Holder 审查账号，授予完成构建所需角色。使用 Xcode 管理的团队证书获取签名能力，而不是索要前员工 Apple 密码。

然后在新 Mac 选择同一 Team 和 Bundle ID，核对 capabilities，生成新 build 并上传内部 TestFlight。交接完成后补上签名资产清单、角色表、构建版本和离职流程。这种修复保护了账号控制，也恢复了发布能力。

Archive 完成后不要只看绿色成功。Organizer 中核对应用名、Bundle ID、Team、Version、Build 和创建时间。导出的签名摘要与 entitlements 应对应目标分发方式。开发环境推送、错误应用组或测试 Bundle ID 都要在上传前发现。

把 archive 与 Git 提交、Xcode 版本和测试报告关联。后来收到崩溃时，可以从 build 找回完全匹配的符号。若记录与界面不一致，停止上传并回到配置来源。给 archive 文件夹改名不会改变归档内部身份。

## 签名专题的掌握边界

第一次发布需要理解 Bundle ID 是应用身份，证书证明签名者，Profile 连接团队、能力与分发方式，Xcode 自动签名负责大部分匹配。还要能在钥匙串确认私钥、处理 Team 选择、保留 Archive，并知道 Windows 无法完成 iOS 最终构建。

暂时不用研究代码签名文件格式、证书链数学和手工 Profile 自动化。组织 CI 或特殊企业分发出现真实需求时再深入。能根据错误指出是哪一项不匹配，比背下证书页面的所有按钮更重要。
