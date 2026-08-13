<p align="center">
  <img src="assets/cover-v2.2.0-preview.jpg" alt="《AI 写代码之后》中文封面" width="420">
</p>

<h1 align="center">AI 写代码之后</h1>

<p align="center">给非专业开发者的 AI Coding 工程手册</p>

<p align="center"><strong>作者 Stellan</strong></p>

<p align="center">AI Coding · Vibe Coding · GitHub · Web 部署 · Linux · Docker · 数据库 · Flutter · App 发布</p>

<p align="center">
  <img src="https://img.shields.io/badge/版本-2.2.0-176875" alt="当前版本 2.2.0">
  <img src="https://img.shields.io/badge/正文-10%20卷%20·%20104%20章-284b63" alt="全书十卷 104 章">
  <img src="https://img.shields.io/badge/核心格式-EPUB%203.3%20·%20PDF-9c6644" alt="核心格式 EPUB 3.3 和 PDF">
  <img src="https://img.shields.io/badge/语言-简体中文-b23a48" alt="语言 简体中文">
</p>

<p align="center">
  <a href="START-HERE.md"><strong>从这里开始</strong></a> ·
  <a href="https://github.com/wuw039060-art/ai-coding-github-deployment-guide/releases/download/V2.2.0/AI.-v2.2.0.epub">EPUB</a> ·
  <a href="https://github.com/wuw039060-art/ai-coding-github-deployment-guide/releases/download/V2.2.0/AI.-v2.2.0.pdf">PDF</a> ·
  <a href="https://github.com/wuw039060-art/ai-coding-github-deployment-guide/releases/tag/V2.2.0">全部格式</a> ·
  <a href="FORMATS.md">格式说明</a> ·
  <a href="CONTENTS.md">完整目录</a>
</p>

<p align="center"><strong>如果这本书正好补上了你在 AI Coding 之后不知道怎样真正交付产品的知识空白，欢迎 ⭐ Star 收藏，方便以后回来查。</strong></p>

这是一套为非科班 AI Coding 使用者重新组织的软件工程学习与参考体系。它从一个直接的问题展开。AI 已经把代码写出来了，然后呢？你怎样看懂它修改了什么，怎样把项目交给真实用户，怎样定位错误，又怎样判断一句“已经完成”究竟有多少证据。

## 这本书写给谁

你可能已经借助 ChatGPT、Codex、Claude Code、Cursor、GitHub Copilot、Replit、Lovable、Bolt 或其他 AI Coding 工具做出了网站、App、自动化工具和个人软件。你能描述想法，也能让 AI 快速执行，但没有经过系统的计算机专业训练。仓库、接口、环境变量、服务器、数据库、容器、签名和日志已经出现在项目里，它们之间的关系仍然不够清楚。

本书也适合需要直接参与软件交付的产品经理、设计师、内容创作者、独立开发者和创业者。你不必先会写复杂代码，但需要愿意亲手完成少量关键操作，并用实际结果判断项目状态。

## 你可能正卡在两种学习方式之间

传统计算机专业路线完整而有价值，学习周期和理论深度却未必匹配眼前问题。你今天也许只想弄清楚 `.env` 为什么让部署失败，暂时没有条件先学完操作系统、网络、数据库和算法。

完全依赖 AI 的路线起步很快。项目变复杂以后，你会发现 AI 可以一次修改几十个文件，也可以引入数据库、缓存、队列和容器，却无法替你承担所有判断。构建成功不等于产品正常，容器运行不等于用户可用，测试通过也不等于不存在其他缺陷。

## 本书提供的第三条路

《AI 写代码之后》按照 AI Coding 的真实工作顺序筛选知识。它不会把传统教材简单缩短，也不会只教按钮位置。每个专题会解释技术在系统中的位置、AI 为什么可能修改它、故障会留下什么迹象、当前需要理解到哪一层，以及什么证据可以支持下一步判断。

目标并非让一本书替代计算机专业训练。更准确的目标是，在常见 AI Coding 场景中，尽量缩小由基础工程认知造成的使用能力差距。你会逐渐更准确地描述问题、阅读主要 Diff、检查日志、限制修改范围、识别明显风险，并知道什么时候需要继续查官方资料或请专业人士加入。

## 我需要读完整本书吗

不需要。全书有十卷、104 章，适合系统学习，也适合作为工作中的参考手册。第一次阅读可以从约 8.7 万中文字符的十五章核心路线开始。正在做网站、App 或服务器项目的读者，可以沿对应项目路线阅读。遇到具体问题时，也可以直接按 `CORS`、`502`、`Volume`、`journalctl`、`AAB` 或 `TestFlight` 等术语查询。

具体路线见 [START-HERE.md](START-HERE.md)。完整章节名称见 [CONTENTS.md](CONTENTS.md)。

## 视频、AI 和本书怎样配合

界面操作第一次跟着视频做，通常更快。配套视频会帮助你辨认 GitHub Desktop、DevTools、SSH、Docker Compose、部署平台和 App 发布界面。本书负责连接概念、解释原因、划清成功状态的证明范围。AI 则可以结合你的真实项目继续解释、执行和反馈。

视频用于帮助看懂，官方文档和经过验证的实际行为负责确认事实。视频内容与当前官方资料冲突时，以后者为准。已核验的观看区间、前置准备和跟做任务见 [LEARNING-RESOURCES.md](LEARNING-RESOURCES.md)。

## 全书覆盖范围

| 分卷 | 核心内容 | 建立的能力 |
| --- | --- | --- |
| 第一卷 | 软件从本地来到用户面前 | 看懂交付链路和故障层级 |
| 第二卷 | Git、GitHub 与项目版本 | 审查变化、保留版本并保护秘密 |
| 第三卷 | 浏览器、DNS、HTTP 与 API | 看懂请求并使用 DevTools 收集证据 |
| 第四卷 | 构建、网页部署、域名与回滚 | 把网站交付到互联网并核对环境 |
| 第五卷 | 后端、认证、数据库与托管服务 | 理解动态产品的数据流和权限边界 |
| 第六卷 | VPS、SSH、Linux 与反向代理 | 查看服务与日志，理解自建责任 |
| 第七卷 | Docker、Compose 与数据持久化 | 管理容器并避免误删持久数据 |
| 第八卷 | Flutter、签名、测试与应用商店 | 理解 Android 和 iOS 发布流程 |
| 第九卷 | 排错、安全、备份与维护 | 从现象寻找证据并准备恢复 |
| 第十卷 | AI 协作、测试、架构与治理 | 检查 AI 的完成声明并控制复杂度 |

## 阅读格式

核心格式为可重排 EPUB 和可搜索 PDF。另提供 AZW3、KEPUB、FB2、DOCX、RTF、TXT、HTMLZ 和 Legacy MOBI。现代 Kindle 用户优先把 EPUB 发送到 Send to Kindle，MOBI 只用于旧设备兼容。

不知道选什么时，优先使用 EPUB。iPhone、iPad 和 Apple Books 适合 EPUB。Windows 与 macOS 适合 PDF 或 EPUB。详细选择说明见 [FORMATS.md](FORMATS.md)。

## 为什么开源

这本书希望让更多人借助 AI 获得解决真实问题的能力。开放阅读、多格式发布和公开修正记录，可以降低学习门槛，也让过时界面、事实错误和遗漏更容易被发现。

## 反馈与联系

发现事实错误、工具界面变化、失效链接或阅读器兼容问题时，欢迎提交 Issue。请尽量附上章节、设备、软件版本、实际现象和已经尝试的步骤。也可以发邮件至 [wuw039060@gmail.com](mailto:wuw039060@gmail.com)。

如果希望接收仓库活动通知，请使用 GitHub 的 Watch。Star 适合收藏和表达兴趣，不会自动订阅仓库通知。

## ⭐ 如果这本书对你有帮助

如果这本书帮你解决过一个实际问题，或者让你第一次看懂 GitHub、部署、服务器、Docker、数据库或 App 发布中的某个环节，欢迎给这个仓库一个 Star。

Star 对我最重要的意义，是让我知道这套内容确实有人在使用，也让我更有依据决定哪些章节值得继续更新和完善。更具体的错误和改进建议，欢迎通过 Issue 或邮件告诉我。

## 书籍信息

- 书名　《AI 写代码之后》
- 副标题　给非专业开发者的 AI Coding 工程手册
- 作者　Stellan
- 当前版本　2.2.0
- 规模　十卷、104 章、约 67.8 万中文字符
