# Token Switch

Token Switch 是一个用于管理、切换和测试 CLI / Agent 工具 Provider、模型与 Token 配置的桌面应用。

这个公开仓库只用于发布说明、下载入口和自动更新清单。应用源码、构建脚本、签名密钥和私有配置不会放在这里。

## 功能介绍

- 统一管理不同 CLI / Agent 工具的 Provider、模型和 Token 配置。
- 在多个 Provider 之间快速切换，减少手动编辑配置文件的重复操作。
- 测试 Provider 连通性、模型列表与常见 API 调用状态。
- 管理 Codex `auth.json` 相关配置，支持保留登录态字段。
- 支持原始配置编辑，适合需要精细调整配置文件的场景。
- 提供 Provider 用量查询模板，便于对接不同中转站或服务商的余额、用量接口。
- 内置第三方中转站监测，用于检查连通性、延迟与模型可用性。
- 提供本地 Relay、操作日志、数据库查询、内嵌 WebView 与独立桌宠窗口等辅助能力。

## 支持的工具

当前版本面向以下应用和 CLI 工具的配置管理：

- Codex
- Claude Desktop
- Claude Code
- OpenCode
- OpenClaw
- Hermes

## 下载

当前版本：`1.10.0`

- macOS Universal DMG：发布后放在 GitHub Releases
- Tauri 自动更新包：发布后放在 GitHub Releases
- 更新清单：[`update.json`](./update.json)

正式发布后，下载文件会作为 GitHub Release Assets 上传到对应版本，例如：

```text
https://github.com/Tangxinzi/token-switch/releases/download/v1.10.0/Token%20Switch_1.10.0_universal.dmg
https://github.com/Tangxinzi/token-switch/releases/download/v1.10.0/Token%20Switch_1.10.0_universal.tar.gz
```

## 自动更新

`update.json` 用于 Tauri updater。发布时需要把里面的占位 URL、签名和说明替换为真实值。

如果继续使用自有域名作为稳定入口，可以让服务端转发这个公开仓库中的 `update.json`。

## 技术栈与开源项目

Token Switch 的应用实现基于以下公开开源项目和生态工具构建：

- [Tauri](https://github.com/tauri-apps/tauri)：桌面应用框架与系统能力集成。
- [React](https://github.com/facebook/react)：前端界面框架。
- [Vite](https://github.com/vitejs/vite)：前端开发与构建工具。
- [TypeScript](https://github.com/microsoft/TypeScript)：类型系统与前端工程基础。
- [Tailwind CSS](https://github.com/tailwindlabs/tailwindcss)：界面样式工具。
- [Lucide](https://github.com/lucide-icons/lucide)：图标库。
- [Chart.js](https://github.com/chartjs/Chart.js)：图表展示。
- [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk)：桌宠。
- [js-yaml](https://github.com/nodeca/js-yaml)：YAML 配置解析。
- [toml-node](https://github.com/BinaryMuse/toml-node)：TOML 配置解析。
- [Babel Parser](https://github.com/babel/babel)：JavaScript / TypeScript 语法解析能力。
- [Playwright](https://github.com/microsoft/playwright)：界面自动化验证工具。

## 仓库边界

这个仓库可以公开包含：

- 项目介绍
- 下载页
- `update.json`
- GitHub Releases 中的 `.dmg`、`.tar.gz`、`.sig` 附件

这个仓库不应包含：

- 应用源码
- 构建脚本
- `updater.key`、证书、密码、Token
- 用户配置、数据库、日志或备份
- `dist/`、`target/` 等构建产物目录
