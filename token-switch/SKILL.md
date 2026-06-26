---
name: token-switch
description: 帮助用户下载、安装、更新和使用 Token Switch。适用于用户想安装 Token Switch 桌面端、查看最新版、配置 Codex、Claude、Claude Code、OpenCode、OpenClaw 或 Hermes 的 Provider、API Key、模型和 Token，管理中转站或自定义 API 地址，查看 Token 用量统计、Token 活动、Agent 会话统计、本地 Relay 状态，或生成 Token Switch 自定义桌宠资源包的场景。
---

# Token Switch

## 概览

Token Switch 是面向 AI CLI 与 Agent 工具的 Provider、模型和 Token 管理工作台。使用本 Skill 帮用户完成下载安装、Agent 配置、中转站管理、连通测试、Token 统计查看和可选桌宠资源生成。

## 使用流程

1. 先判断用户目标：
   - 下载、安装、更新或查看版本：读取 `references/install-and-update.md`，必要时运行 `scripts/latest_release.py` 查询实时安装清单。
   - 配置 Agent、Provider、模型、API Key 或中转站：读取 `references/agent-provider-guide.md`。
   - 查看 Token 统计、Token 活动、会话统计或 Relay 状态：读取 `references/usage-and-relay.md`。
   - 生成或修复桌宠资源：读取 `references/pet-resource-spec.md`。
2. 如果用户要你执行安装，优先说明会运行的官方命令，再执行对应平台命令。不要要求用户手动保存脚本。
3. 如果用户要配置 API Key 或 Token，只在当前对话和当前机器操作中使用，不要写入持久说明、日志或记忆。
4. 如果用户描述“统计不准”“中转站不可用”“Agent 没生效”，按真实链路排查：配置值、选中 Provider、模型列表、连通测试、Relay 状态、是否需要重启目标 Agent。
5. 结束时给出用户下一步能直接操作的入口，例如打开 Token Switch 的具体页面、使用安装命令、或重启对应 Agent。

## 核心能力

- 下载和安装：支持 macOS 与 Windows，通过官方安装脚本或安装清单获取最新版。
- Agent 配置：帮助用户配置 Codex、Claude、Claude Code、OpenCode、OpenClaw 和 Hermes。
- Provider 管理：维护服务商、中转站、自定义 API 地址、模型列表和默认模型。
- Token 管理：选择 API Key、切换 Provider 和模型组合，测试接口连通性。
- Token 统计：查看 Token 活动、用量概览、Agent 会话统计、每日统计和本地 Relay 记录。
- 中转站排查：检查 Base URL、API Key、模型兼容、`/models` 获取和基础请求是否可用。
- 桌宠资源：按用户设定生成 Token Switch 可读取的自定义桌宠资源包。

## 重要原则

- 查询最新版时使用实时安装清单，不要依赖 Skill 编写时的版本号。
- 用户只问“怎么下载”时，给官网和命令行安装方式；用户明确要求执行时再运行安装命令。
- 配置 Agent 后，如果用户说没有生效，提醒并协助重启对应 Agent 或 Token Switch Relay。
- 处理中转站时避免假设它兼容所有模型；先确认 Base URL、API Key、模型名和接口类型。
- 统计相关问题要区分“Relay 请求记录”和“本地 Agent 会话统计”，二者来源不同但可以在 Token 活动中汇总查看。
