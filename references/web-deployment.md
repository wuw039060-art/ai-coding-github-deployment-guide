# Web 部署与浏览器排错参考

这份参考用于查操作，不代替主书中的判断模型。界面名称以 Chrome 当前版本为准；在别人的站点、账号或数据上调试前，先取得授权。

## Console 与 Network 快速路径

1. 打开 DevTools。Windows/Linux 常用 `F12` 或 `Ctrl+Shift+I`，macOS 常用 `Command+Option+I`；快捷键被占用时从浏览器菜单进入。
2. 打开 Console 和 Network，清空旧记录；需要观察跳转时才启用 Preserve log。
3. 刷新页面，先找 Console 第一条与本次操作相关的错误，再找 Network 第一个失败请求。
4. 记录页面地址、操作时间与时区、浏览器版本、复现步骤和页面版本。
5. 选择目标请求，依次检查 Request URL、Method、Status、Payload、Response、Initiator 和 Timing。

DevTools 只显示当前浏览器已经获得的信息，不会因此获得服务器权限。面板里没有记录，可能只是打开得太晚或筛选条件未清除。

## 请求详情字段

- **Headers / General** 记录请求地址、方法、状态码和远端地址。地址不应意外指向 `localhost` 或测试域名。
- **Request Headers** 记录认证、来源、内容类型和缓存上下文。截图前遮盖 `Authorization`、Cookie 和自定义令牌。
- **Payload** 包含 Query、Form、JSON 或文件元数据。表单字段为空通常先查前端收集；字段正确而返回校验错误，再查 API 规则。
- **Preview / Response** 中，Preview 是浏览器的友好展示，Response 更接近实际响应正文。声称返回 JSON 却收到 HTML 登录页时，应查认证和重定向。
- **Initiator** 说明谁触发了请求。可用于区分 HTML、应用脚本、第三方脚本、扩展和 Service Worker。
- **Timing** 记录排队、DNS、连接、TLS、等待服务器和下载阶段。单次数字不是性能结论，应重复测量并记录缓存与网络条件。

## 常见入口对照

| 现象 | 第一检查点 | 下一层证据 |
|---|---|---|
| 主文档 404 | 完整 URL、路由、文件大小写 | 平台路由或服务器访问日志 |
| API 401 | 凭据是否发送、是否过期 | 身份服务日志、测试账号状态 |
| API 403 | 已认证用户的权限与策略 | 服务端授权日志 |
| 429 | 限流响应与重试提示 | 服务端限流配置、请求频率 |
| 500 | Response 中的错误码或 Request ID | 应用日志 |
| 502 | 代理是否连到上游 | 代理日志、服务端口与状态 |
| 503 | 维护、容量、健康检查 | 平台事件与服务健康 |
| 504 | 哪一层超时 | 代理、应用与上游各自耗时 |
| `(blocked)` | CSP、混合内容、扩展、CORS、隐私功能 | Console 的具体策略消息 |
| `(canceled)` | 导航、代码取消、用户停止 | Initiator 与调用顺序 |
| `ERR_NAME_NOT_RESOLVED` | DNS | 解析记录与网络环境 |
| `ERR_CONNECTION_REFUSED` | 目标端口是否监听 | 主机服务状态与防火墙 |

CORS 错误要记录前端 Origin、API URL、方法、请求头、预检 OPTIONS 状态和响应头。上游先返回 500 时，也可能因为错误响应缺少 CORS 头而被浏览器表现成 CORS。不要用关闭浏览器保护的扩展当产品修复。

## 成功/失败对照实验

先保存一条成功请求，再只改变一个条件制造无害失败，例如在练习站点把图片路径改错一个字符，或用测试账号提交缺失必填字段。比较地址、方法、状态、请求头、Payload、Response 与 Timing。不要同时清缓存、换账号、切网络和改代码，否则无法判断是哪项变化产生结果。

修复后重新部署，确认旧的失败请求变成预期状态，并记录修复提交、实际页面版本和一次用户动作。浏览器里通过 Elements、Console 或 Local Overrides 做的临时修改不等于源码已经发布。

## 缓存、慢网和 Waterfall

Disable cache 通常只在 DevTools 打开时生效，适合做对照，不是用户长期设置。Waterfall 可观察 HTML、脚本、样式和 API 的发现顺序；横条很晚开始可能是前端初始化，早开始但等待很久更像后端或上游处理。仍应点开 Timing，不只凭列表排序判断。

Network/CPU Throttling 用于观察加载提示、重复提交和超时界面。模拟配置不代表某个真实地区、运营商或低端设备。记录配置，并在目标真机上检查输入、滚动、旋转、深色模式和字体缩放。

Request blocking 可以在本机模拟图片、脚本或第三方 API 不可用。规则只影响当前调试浏览器，结束后必须关闭；它不能证明服务器权限或其他用户的结果。

## WebSocket

在 WS 请求的 Messages/Frames 中查看收发消息。握手状态 101 通常只说明协议切换完成；连接成功但页面不更新时，继续检查订阅消息、服务端确认、频道和权限。刷新会创建新连接，不要把多个标签页或多次连接混为一条。聊天内容、令牌和二进制 Frame 都不应直接公开。

## HAR、截图和重放安全

HAR 可能包含完整 URL、Headers、Cookie、Payload 与 Response。优先分享脱敏截图或单个请求的最小结构。确需 HAR 时，按下面顺序处理。

1. 使用测试账号与测试数据。
2. 导出后用文本方式再次检查凭据和个人数据，不只依赖 Sanitized 选项。
3. 通过受控、限时渠道分享。
4. 问题解决后按项目的数据保留规则删除。

截图应保留地址的脱敏形式、面板名称、目标请求、关键列、时间与时区；模糊必须不可恢复，能重做干净截图时优先重做。

Copy as fetch、Copy as cURL 与 Replay XHR 可能再次创建订单、删除数据或消耗额度。默认只在练习环境和无害 GET 上使用。生产重放需要明确批准、测试账号、幂等键，并先确认第一次失败请求是否已经产生部分副作用。

## Application 与站点数据

Application 面板可观察 Cookie、Local Storage、IndexedDB、Cache Storage 和 Service Worker。数据按 Origin 隔离，子域或端口不同就是不同位置。删除站点数据会退出登录并可能清除草稿；先在测试账号和可恢复数据上操作。登录循环先看 Cookie 是否存在及其属性，不复制值；旧 PWA 再查 Service Worker 和缓存版本。

## 证据模板

```text
页面地址（脱敏）：
页面版本或提交：
浏览器与设备：
复现时间及时区：
最短复现步骤：
Console 第一条相关错误：
请求方法与地址（脱敏）：
状态 / Content-Type / Request ID：
Payload 与 Response 的最小非敏感字段：
Timing 主要阶段：
成功对照：
已经尝试及结果：
仍未验证：
```

## 视频入口

- Chrome Console 与 Network 入门见[全书视频索引里的 Chrome DevTools 入门演示](../book/frontmatter/videos.md)。中文主入口使用 B 站 DevTools 完整指南，YouTube 官方视频作为备用入口；面板位置和筛选语法应按当前浏览器复核。
