# Token 统计、Token 活动与 Relay

## 统计入口

Token Switch 提供这些用量相关视图：

- Token 统计：查看整体 Token 用量、消耗概览和趋势。
- Token 活动：查看近期请求、Provider、模型、时间、输入输出和状态。
- Agent 会话统计：按 Codex、Claude、Claude Code 等本地 Agent 会话汇总请求与 Token。
- 菜单栏状态：快速查看近期活动、状态和跳转入口。
- 本地 Relay：统一请求入口，并记录经过 Relay 的请求状态。

## 统计来源

排查统计问题时区分两类来源：

- Relay 请求记录：来自 Token Switch 本地 Relay 经过的请求，适合看 Provider、模型、请求状态和用量事实。
- 本地 Agent 会话：来自本机 Agent 会话文件，适合看会话标题、时间线、应用维度和本地 token 汇总。

这两类数据可以在 Token 活动中汇总查看，但口径不同。用户问“为什么数字不一样”时，不要直接判定错误，先确认当前视图使用的是哪种口径。

## 常见任务

### 查看今日 Token

1. 打开 Token Switch。
2. 进入 Token 统计或 Token 活动。
3. 查看今日统计、请求数量、输入输出 Token 和费用或积分消耗。
4. 如果页面有刷新按钮，刷新后再读数。

### 查看某个 Agent 的会话统计

1. 打开 Token 活动或 Agent 会话统计。
2. 选择 Codex、Claude、Claude Code 等应用维度。
3. 查看会话列表、标题、最近活动时间和 Token 总量。
4. 如果某个会话缺失，检查该 Agent 是否在本机生成会话文件，且 Token Switch 是否有读取权限。

### 排查统计缺失

按顺序检查：

1. 请求是否经过 Token Switch Relay。
2. 目标 Agent 是否配置成使用 Token Switch 管理的 Provider。
3. 请求时间是否在当前筛选范围内。
4. 当前视图是 Relay 记录还是本地 Agent 会话统计。
5. Token Switch 是否需要刷新、重启或重新授权本地文件访问。

### 排查 Relay

检查项：

- Relay 是否启动。
- Agent 是否使用 Relay 地址或 Token Switch 写入的配置。
- Provider 是否有可用 API Key。
- 模型是否存在且兼容。
- Token 活动中是否出现请求记录。
- 配置变更后是否需要重启 Agent 或 Relay。

## 回答口径

用户问“Token 统计怎么用”时，给普通用户能理解的说明：

Token 统计看总量和趋势，Token 活动看每次请求明细，Agent 会话统计看不同工具和不同会话分别用了多少。

用户问“为什么没有记录”时，优先问或检查：

这次请求有没有经过 Token Switch。没有经过 Relay 或 Token Switch 写入的 Provider，就可能不会出现在 Relay 请求记录里。

用户问“为什么要重启”时，解释为：

很多 Agent 启动时会读取一次配置。Token Switch 保存新配置后，已经运行的 Agent 可能还在用旧配置，重启后才会读取新 Provider、API Key 或模型。
