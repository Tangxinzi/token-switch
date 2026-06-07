# Token Switch

本地 AI Token 供应商切换工具，支持 macOS、Windows 使用，下载访问[产品页 https://token.ferer.net/switch](https://token.ferer.net/switch)。

![Token Switch 桌面端产品界面](https://token.ferer.net/images/token-switch-light.png)

Token Switch 是一个桌面端本地配置工作台，用来集中管理常用 AI 编程客户端的 Provider、模型接口和 Token 配置。选择客户端，切换供应商，测试连通性，然后安全写入本机配置，减少反复编辑配置文件、切换环境变量和手动排查接口状态的成本。

## 核心能力

- 一键切换本地 Token 供应商：把常用 Provider、中转站、自定义 API 地址和模型配置收进一个工作台。
- 客户端配置管理：管理 Codex、Claude Code、OpenCode、OpenClaw 与 Hermes 的模型接口配置。
- 模型与 Token 管理：维护多个 Token、模型和 Provider 组合，并在需要时快速切换。
- 连通性测试：测试 Provider 可用性、响应状态、延迟和基础接口兼容情况。
- 模型列表辅助：辅助拉取、验证和维护不同供应商下的模型列表。
- Token 统计：查看 Token 相关统计与用量概览，便于了解本地配置使用情况。
- 控制台：集中查看配置、状态和操作入口，减少在多个工具页面之间来回切换。
- Provider 列表：优化展示常用供应商、最近使用信息和配置状态。
- 本地 Relay：通过本地服务统一转发请求，并按当前活动供应商动态路由。
- 高级配置入口：保留原始配置编辑、日志、数据库查询、中转站监测和内嵌 WebView 等能力。

## 支持的客户端

| 客户端 | 说明 |
| --- | --- |
| Codex | Provider、模型、Token、`auth.json` 与 TOML 配置管理 |
| Claude Code | Claude Code CLI 配置管理 |
| OpenCode | Provider 与模型配置管理 |
| OpenClaw | Provider 与模型配置管理 |
| Hermes | YAML 配置管理 |

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

- 产品页：[https://token.ferer.net/switch](https://token.ferer.net/switch)
- 官网：[https://token.ferer.net/](https://token.ferer.net/)
- GitHub：[https://github.com/Tangxinzi/token-switch](https://github.com/Tangxinzi/token-switch)
