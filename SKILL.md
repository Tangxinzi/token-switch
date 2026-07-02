---
name: token-switch
description: 帮助用户下载、安装、更新和使用 Token Switch。适用于用户想安装 Token Switch 桌面端、查看最新版、配置 Codex、Claude、Claude Code、OpenCode、OpenClaw 或 Hermes 的 Provider、API Key、模型和 Token，管理中转站或自定义 API 地址，查看 Token 用量统计、Token 活动、Agent 会话统计、本地 Relay 状态，或生成 Token Switch 自定义桌宠资源包的场景。
---

# Token Switch 单文件 Skill

把这份 Markdown 整段发给 Agent 后，Agent 应按本文完成 Token Switch 的下载、安装、配置、统计排查、中转站排查和桌宠资源生成。本文是可互传的单文件版，不依赖额外 `references/`、`scripts/` 或二进制资源。

## 工作原则

1. 先判断用户目标：安装更新、Agent 配置、Provider/API Key/模型配置、中转站排查、Token 统计、Relay 状态、桌宠资源生成。
2. 用户只问“怎么下载”时，给官网和安装命令；用户明确要求执行时，再运行安装命令。
3. 查询最新版必须实时访问官方安装清单，不要依赖本文写入时的版本号。
4. API Key 只在当前对话和当前机器操作中使用，不写入文档、提交信息、日志或长期记忆。
5. 配置保存后如果没有生效，优先检查是否已同步到目标 Agent，并重启目标 Agent 或 Token Switch Relay。
6. 排查“统计不准”时，区分 Relay 请求记录和本地 Agent 会话统计，这两类来源不同。

## 官方入口

- 产品页：`https://token.ferer.net/switch`
- 官网：`https://token.ferer.net/`
- GitHub：`https://github.com/Tangxinzi/token-switch`
- macOS 安装脚本：`https://token.ferer.net/install.sh`
- Windows 安装脚本：`https://token.ferer.net/install.ps1`
- 实时安装清单：`https://token.ferer.net/api/install.json?target=<target>&arch=<arch>&current_version=0.0.0`

## 查询最新版

根据用户平台选择 target 和 arch：

- macOS Apple Silicon：`target=darwin&arch=aarch64`
- macOS Intel：`target=darwin&arch=x64`
- Windows x64：`target=windows&arch=x64`
- Windows arm64：`target=windows&arch=arm64`

使用 `curl` 查询：

```bash
curl -fsSL 'https://token.ferer.net/api/install.json?target=darwin&arch=aarch64&current_version=0.0.0'
curl -fsSL 'https://token.ferer.net/api/install.json?target=windows&arch=x64&current_version=0.0.0'
```

回答“最新版是多少”时，读取清单里的版本号、发布日期、更新说明和安装包链接后再回答。

## macOS 安装

用户要求安装时，先说明将运行官方安装脚本，然后执行：

```bash
curl -fsSL https://token.ferer.net/install.sh | sh
```

常用参数：

```bash
curl -fsSL https://token.ferer.net/install.sh -o /tmp/token-switch-install.sh
sh /tmp/token-switch-install.sh --dry-run
sh /tmp/token-switch-install.sh --no-launch
sh /tmp/token-switch-install.sh --version <version>
sh /tmp/token-switch-install.sh --arch aarch64
sh /tmp/token-switch-install.sh --arch x64
```

说明：

- 默认安装到 `/Applications`。
- Apple Silicon 使用 `aarch64`，Intel 使用 `x64`。
- 安装脚本会解析官方清单，下载安装包，并在条件允许时校验签名。

## Windows 安装

PowerShell 安装命令：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -Command "irm https://token.ferer.net/install.ps1 | iex"
```

常用参数：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -DryRun
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -NoLaunch
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Version <version>
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Arch x64
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Arch arm64
```

## 更新

1. 查询实时安装清单确认最新版。
2. 让用户在 Token Switch 内检查更新，或重新运行官方安装脚本覆盖安装。
3. 如果 Agent 配置或 Relay 状态更新后没有生效，重启 Token Switch 和目标 Agent。

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
- API Key：只在当前操作中使用。
- 默认模型：用户希望 Agent 默认使用的模型名。
- 是否需要本地 Relay 统一入口。

## Agent、Provider 与模型配置流程

1. 打开 Token Switch。
2. 进入对应 Agent 页面。
3. 新建或编辑 Provider。
4. 填入 Base URL、API Key、模型列表和默认模型。
5. 使用“获取模型”或连通测试确认接口可用。
6. 保存配置，并按页面提示同步到目标 Agent。
7. 如果目标 Agent 已经运行，配置后重启目标 Agent；如果使用本地 Relay，必要时重启 Relay。

配置完成后，至少验证一项：

- Token Switch 页面连通测试成功。
- 模型列表能获取，或手动模型能通过基础请求。
- 目标 Agent 发起一次简单请求成功。
- Token 活动或 Relay 日志出现对应请求记录。

## 中转站排查

重点检查：

- Base URL 是否包含正确的 API 根路径。
- API Key 是否属于该中转站。
- 模型名是否为中转站实际支持的模型名，不要只按官方模型名猜测。
- `/models` 是否可获取；如果获取失败，尝试手动填入模型名后做基础连通测试。
- 中转站是否兼容 OpenAI Chat Completions、Responses API 或目标 Agent 所需协议。
- 如果配置生效但请求失败，检查目标 Agent 是否仍在使用旧配置。

常见处理：

- “获取模型失败”：先检查 API Key 和 Base URL，再用连通测试或 curl 验证 `/models`。
- “保存了没生效”：确认是否同步到目标 Agent，之后重启目标 Agent。
- “模型不存在”：以中转站控制台或 `/models` 返回为准，更新 Token Switch 中的模型名。
- “某个 Provider 延迟高”：用 Token Switch 的连通测试和 Token 活动记录对比不同 Provider。

## Token Switch 登录密钥

如果页面支持从 Token Switch 获取或选择 API Key：

1. 确认用户已经登录 Token Switch。
2. 在 Provider 表单里选择 Token Switch 来源或已有密钥。
3. 没有密钥时，引导用户先在 Token Switch 控制台创建或获取密钥。
4. 获取模型前必须先选择 API Key，否则先补齐密钥再测试。

## Token 统计、Token 活动与 Relay

统计入口：

- Token 统计：查看整体 Token 用量、消耗概览和趋势。
- Token 活动：查看近期请求、Provider、模型、时间、输入输出和状态。
- Agent 会话统计：按 Codex、Claude、Claude Code 等本地 Agent 会话汇总请求与 Token。
- 菜单栏状态：快速查看近期活动、状态和跳转入口。
- 本地 Relay：统一请求入口，并记录经过 Relay 的请求状态。

统计来源：

- Relay 请求记录：来自 Token Switch 本地 Relay 经过的请求，适合看 Provider、模型、请求状态和用量事实。
- 本地 Agent 会话：来自本机 Agent 会话文件，适合看会话标题、时间线、应用维度和本地 token 汇总。

用户问“Token 统计怎么用”时，给普通用户能理解的说明：

Token 统计看总量和趋势，Token 活动看每次请求明细，Agent 会话统计看不同工具和不同会话分别用了多少。

用户问“为什么没有记录”时，优先问或检查：

这次请求有没有经过 Token Switch。没有经过 Relay 或 Token Switch 写入的 Provider，就可能不会出现在 Relay 请求记录里。

排查统计缺失时按顺序检查：

1. 请求是否经过 Token Switch Relay。
2. 目标 Agent 是否配置成使用 Token Switch 管理的 Provider。
3. 请求时间是否在当前筛选范围内。
4. 当前视图是 Relay 记录还是本地 Agent 会话统计。
5. Token Switch 是否需要刷新、重启或重新授权本地文件访问。

排查 Relay 时检查：

- Relay 是否启动。
- Agent 是否使用 Relay 地址或 Token Switch 写入的配置。
- Provider 是否有可用 API Key。
- 模型是否存在且兼容。
- Token 活动中是否出现请求记录。
- 配置变更后是否需要重启 Agent 或 Relay。

## 桌宠资源生成

当用户要生成 Token Switch 自定义桌宠资源时，在 `~/.token-switch/pets/<characterId>/` 中创建资源包。

必需文件：

- `manifest.json`
- `default.svg`
- `idle.svg`
- `thinking.svg`
- `typing.svg`
- `completed.svg`
- `failed.svg`
- `sleeping.svg`
- `building.svg`
- `notification.svg`
- `hover.svg`

完整资源包可额外创建：

- `drag.svg`
- `mini-idle.svg`
- `mini-peek.svg`
- `mini-typing.svg`
- `mini-alert.svg`
- `mini-happy.svg`
- `mini-sleep.svg`
- `mini-enter.svg`
- `mini-enter-sleep.svg`
- `mini-crabwalk.svg`
- `poke-double.svg`
- `poke-burst.svg`
- `poke-annoyed.svg`

基础 `manifest.json`：

```json
{
  "characters": {
    "<characterId>": {
      "name": "<name>",
      "description": "<description>",
      "ariaLabel": "<name> 桌宠",
      "default": "default.svg",
      "animations": {
        "idle": "idle.svg",
        "thinking": "thinking.svg",
        "typing": "typing.svg",
        "completed": "completed.svg",
        "failed": "failed.svg",
        "sleeping": "sleeping.svg",
        "building": "building.svg",
        "notification": "notification.svg",
        "hover": "hover.svg"
      },
      "audio": {}
    }
  }
}
```

完整资源包额外加入这些 animation key：

```json
{
  "drag": "drag.svg",
  "miniIdle": "mini-idle.svg",
  "miniPeek": "mini-peek.svg",
  "miniTyping": "mini-typing.svg",
  "miniAlert": "mini-alert.svg",
  "miniHappy": "mini-happy.svg",
  "miniSleep": "mini-sleep.svg",
  "miniEnter": "mini-enter.svg",
  "miniEnterSleep": "mini-enter-sleep.svg",
  "miniCrabwalk": "mini-crabwalk.svg",
  "pokeDouble": "poke-double.svg",
  "pokeBurst": "poke-burst.svg",
  "pokeAnnoyed": "poke-annoyed.svg"
}
```

硬性限制：

- `manifest.json` 必须是标准 JSON，不能有注释或尾随逗号。
- `manifest.json` 必须小于 2 MB。
- 每个 SVG 建议小于 80 KB；完整资源包整体尽量控制在 1 MB 左右或以内。
- SVG 必须是独立文件，并使用透明背景。
- 不要引用外部图片、字体、CSS、脚本或网络资源。
- manifest 中的每个资源路径都必须相对 `manifest.json`，不能使用绝对路径或 `..`。
- 动画 SVG 建议统一使用 `viewBox="0 0 128 128"`、`width="128"` 和 `height="128"`。
- 角色主体必须完整落在画布内；建议视觉范围在 x=18..110、y=12..118，并在底部保留 8 到 12 px 空白。
- SVG 内不要出现可见文字。

`default.svg` 要作为设置页预览图标单独制作：

- 使用 `width="1em"` 和 `height="1em"`。
- 条件允许时加入 `style="flex:none;line-height:1"`。
- `viewBox` 需要围绕主体有效像素紧裁切。
- 主体需要居中且不能被裁切。
- 不要直接复用 `idle.svg`。

完成后告诉用户：

`打开 Token Switch 设置页，展开“桌宠”，查看是否出现新角色 <name>。如果没有出现，重启应用后再检查；如果设置页显示配置警告，优先检查 JSON 格式、角色 ID 和资源相对路径。`

## 常用回答模板

用户问“怎么下载”：

```text
macOS:
curl -fsSL https://token.ferer.net/install.sh | sh

Windows PowerShell:
powershell -NoProfile -ExecutionPolicy Bypass -Command "irm https://token.ferer.net/install.ps1 | iex"

产品页:
https://token.ferer.net/switch
```

用户问“为什么要重启”：

```text
很多 Agent 启动时会读取一次配置。Token Switch 保存新配置后，已经运行的 Agent 可能还在用旧配置，重启后才会读取新 Provider、API Key 或模型。
```

用户问“为什么数字不一样”：

```text
先看当前页面的数据来源。Relay 请求记录统计的是经过 Token Switch Relay 的请求；Agent 会话统计读取的是本机 Agent 会话文件。两者都能帮助看用量，但口径不同。
```
