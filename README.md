# Token Switch

AI CLI / Agent Provider、模型与 Token 管理桌面应用。

[官网](https://token.ferer.net/) · [下载最新版](https://github.com/Tangxinzi/token-switch/releases/latest) · [更新清单](./update.json)

Token Switch 面向同时使用多个 AI CLI、Agent 工具和第三方中转服务的用户。它将 Provider、模型、Token、连通性测试、用量查询和本地 Relay 等能力集中到一个桌面应用中，减少反复修改配置文件、切换环境变量和手动排查接口状态的成本。

## 核心功能

- Provider 集中管理：统一维护不同服务商、中转站和自定义 API 地址。
- 模型与 Token 切换：在常用模型、Token 和配置组合之间快速切换。
- 连通性测试：检查 Provider 是否可用，并辅助拉取或验证模型列表。
- Codex 配置管理：管理 Codex Provider 配置与 `auth.json` 相关信息。
- Claude 配置管理：区分 Claude Desktop 与 Claude Code 的不同配置结构。
- 原始配置编辑：保留直接编辑配置文件的入口，适合高级用户精细调整。
- 用量查询模板：为不同服务商或中转站配置余额、用量、额度查询方式。
- 中转站监测：探测连通性、响应延迟、模型可用性和接口兼容情况。
- 本地 Relay：通过本地服务转发请求，便于统一管理 Provider 路由。
- 操作日志与数据库查询：方便回看配置变更、请求记录和本地数据状态。
- 内嵌 WebView：在应用内打开常用网页、控制台或服务商页面。
- 桌宠窗口：提供独立桌宠窗口与状态展示能力。

## 支持的工具

当前版本支持以下应用和 CLI 工具的配置管理：

| 工具 | 说明 |
| --- | --- |
| Codex | Provider、模型、Token、`auth.json` 与 TOML 配置管理 |
| Claude Desktop | Claude 桌面端配置库管理 |
| Claude Code | Claude Code CLI 配置管理 |
| OpenCode | Provider 与模型配置管理 |
| OpenClaw | Provider 与模型配置管理 |
| Hermes | YAML 配置管理 |

## 下载与安装

当前版本：`1.10.0`

- 官网：[https://token.ferer.net/](https://token.ferer.net/)
- GitHub Releases：[https://github.com/Tangxinzi/token-switch/releases/latest](https://github.com/Tangxinzi/token-switch/releases/latest)
- 自动更新清单：[update.json](./update.json)

macOS 用户优先下载 `Token Switch_<version>_universal.dmg`。自动更新使用同版本的 `.tar.gz` 更新包和 `.sig` 签名文件。

发布文件示例：

```text
Token Switch_1.10.0_universal.dmg
Token Switch_1.10.0_universal.tar.gz
Token Switch_1.10.0_universal.tar.gz.sig
```

## 使用场景

- 同时使用多个 AI Provider，需要频繁切换 API 地址、模型和 Token。
- 使用第三方中转站，需要检查接口连通性、延迟和模型支持情况。
- 需要在 Codex、Claude、OpenCode 等工具之间保持配置一致。
- 希望用桌面应用管理配置，同时保留原始配置文件的可控性。
- 需要本地 Relay 统一转发请求，并查看基础请求记录。

## 技术栈与开源项目

Token Switch 基于现代桌面应用和前端工程生态构建，并引用了以下公开项目：

- [Tauri](https://github.com/tauri-apps/tauri)：桌面应用框架与系统能力集成。
- [React](https://github.com/facebook/react)：前端界面框架。
- [Vite](https://github.com/vitejs/vite)：前端开发与构建工具。
- [TypeScript](https://github.com/microsoft/TypeScript)：类型系统与工程基础。
- [Tailwind CSS](https://github.com/tailwindlabs/tailwindcss)：界面样式工具。
- [Lucide](https://github.com/lucide-icons/lucide)：图标库。
- [Chart.js](https://github.com/chartjs/Chart.js)：图表展示。
- [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk)：桌宠相关引用。
- [js-yaml](https://github.com/nodeca/js-yaml)：YAML 配置解析。
- [toml-node](https://github.com/BinaryMuse/toml-node)：TOML 配置解析。
- [Babel Parser](https://github.com/babel/babel)：JavaScript / TypeScript 语法解析能力。
- [Playwright](https://github.com/microsoft/playwright)：界面自动化验证工具。

## 反馈

如需下载、查看更新或了解产品信息，请访问：

- 官网：[https://token.ferer.net/](https://token.ferer.net/)
- GitHub：[https://github.com/Tangxinzi/token-switch](https://github.com/Tangxinzi/token-switch)
