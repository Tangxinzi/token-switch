# Agent、Provider 与中转站配置

## 支持的 Agent

Token Switch 用来集中配置这些 AI CLI 与 Agent 工具：

- Codex：Provider、模型、Token、`auth.json` 与 TOML 配置管理。
- Claude：Claude Desktop 相关配置管理。
- Claude Code：Claude Code CLI 配置管理。
- OpenCode：Provider 与模型配置管理。
- OpenClaw：Provider 与模型配置管理。
- Hermes：YAML 配置管理。

## 配置前先收集

开始配置前，向用户确认或从上下文读取：

- 目标 Agent：Codex、Claude、Claude Code、OpenCode、OpenClaw 或 Hermes。
- Provider 类型：官方服务商、中转站、自定义 OpenAI-compatible API，或 Token Switch 登录密钥。
- Base URL：例如官方接口地址或中转站地址。
- API Key：只在当前操作中使用，不写入说明文档或持久记忆。
- 默认模型：例如用户希望 Agent 默认使用的模型名。
- 是否需要本地 Relay 统一入口。

## 配置流程

1. 打开 Token Switch。
2. 进入对应 Agent 页面。
3. 新建或编辑 Provider。
4. 填入 Base URL、API Key、模型列表和默认模型。
5. 使用“获取模型”或连通测试确认接口可用。
6. 保存配置，并按页面提示同步到目标 Agent。
7. 如果目标 Agent 已经运行，配置后重启目标 Agent；如果使用本地 Relay，必要时重启 Relay。

## 中转站管理

中转站配置重点检查：

- Base URL 是否包含正确的 API 根路径。
- API Key 是否属于该中转站。
- 模型名是否为中转站实际支持的模型名，不要只按官方模型名猜测。
- `/models` 是否可获取；如果获取失败，尝试手动填入模型名后做基础连通测试。
- 中转站是否兼容 OpenAI Chat Completions、Responses API 或目标 Agent 所需协议。
- 如果配置生效但请求失败，检查目标 Agent 是否仍在使用旧配置。

常见处理：

- 用户说“获取模型失败”：先检查 API Key 和 Base URL，再用连通测试或 curl 验证 `/models`。
- 用户说“保存了没生效”：确认是否同步到目标 Agent，之后重启目标 Agent。
- 用户说“模型不存在”：以中转站控制台或 `/models` 返回为准，更新 Token Switch 中的模型名。
- 用户说“某个 Provider 延迟高”：用 Token Switch 的连通测试和 Token 活动记录对比不同 Provider。

## Token Switch 登录密钥

如果页面支持从 Token Switch 获取或选择 API Key：

1. 确认用户已经登录 Token Switch。
2. 在 Provider 表单里选择 Token Switch 来源或已有密钥。
3. 没有密钥时，引导用户先在 Token Switch 控制台创建或获取密钥。
4. 获取模型前必须先选择 API Key，否则应先补齐密钥再测试。

## 配置后的验证

配置完成后，至少验证一项：

- Token Switch 页面连通测试成功。
- 模型列表能获取或手动模型能通过基础请求。
- 目标 Agent 发起一次简单请求成功。
- Token 活动或 Relay 日志出现对应请求记录。

## 安全要求

- 不把 API Key 写入 Skill、README、提交信息或长期记忆。
- 回答中需要展示时只显示前后少量字符，例如 `sk-...abcd`。
- 用户要求排查时，可以在当前终端临时使用 API Key，但不要保存到额外文件。
