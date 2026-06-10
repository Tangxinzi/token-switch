# Token Switch

Token Switch 是一个配置 Agent 的工作台，Provider、模型接口和 Token 配置。选择客户端，切换供应商，测试连通性。支持 macOS、Windows 使用，下载访问 [产品页 https://token.ferer.net/switch](https://token.ferer.net/switch)。

![Token Switch 桌面端产品界面](https://token.ferer.net/images/token-switch-light.png)

## 命令行安装 Token Switch

[Token Switch](https://token.ferer.net/switch) 官网访问下载外，也支持提供命令行快捷安装方式，用于通过终端快速下载、安装或更新桌面端。

macOS：

```sh
curl -fsSL https://token.ferer.net/install.sh | sh
```

Windows PowerShell：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -Command "irm https://token.ferer.net/install.ps1 | iex"
```

## 产品能力

- Agent 管理：Codex、Claude、Claude Code、OpenCode、OpenClaw 与 Hermes 的模型接口配置。
- Token 供应商管理：把常用 Provider、中转站、自定义 API 地址和模型配置收进一个工作台。
- Token 用量统计：查看 Token 相关统计与用量概览，便于了解本地配置使用情况。
- 桌宠陪伴：按自己的使用场景调整桌宠的角色、语气、行为边界和任务偏好。

## Agent 支持


| Agent       | 说明                                        |
| ----------- | ----------------------------------------- |
| Codex       | Provider、模型、Token、`auth.json` 与 TOML 配置管理 |
| Claude Code | Claude Code CLI 配置管理                      |
| OpenCode    | Provider 与模型配置管理                          |
| OpenClaw    | Provider 与模型配置管理                          |
| Hermes      | YAML 配置管理                                 |


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

## 自定义桌宠 Prompt

用户只要调整下面的 Prompt 提示词，目录结构、桌宠角色、名称、描述和 SVG 主题都会跟着动态生成。可以把下面整段作为生成或适配自定义桌宠的 Prompt。

这份 Prompt 分成两层资源：基础资源是应用一定会使用的常规状态；增强资源用于贴边极简模式、悬停探出和点击彩蛋，不提供也能运行，提供后桌宠会更完整。

```text
请根据下面的用户设定，为 Token Switch 生成一个完整可测试的自定义桌宠资源包。

用户设定：
「在这里填写桌宠描述，例如：一只赛博风的「小狐狸」，性格机灵，主色是青绿色和橙色，适合陪我写代码」

任务目标：
1. 先从用户设定中提炼桌宠的角色关键词，包括：
   - 角色名称 name
   - 英文/拼音风格角色 ID characterId
   - 一句话描述 description
   - 视觉风格 style
   - 主色 palette
   - 性格 personality
2. characterId 必须根据用户设定生成，不能使用 test、demo、sample 等占位词。
3. characterId 只能包含字母、数字、点、横线、下划线或冒号，长度不超过 64。
4. 目标目录必须使用该 characterId：
   ~/.token-switch/pets/<characterId>/

请创建这些基础文件：
- ~/.token-switch/pets/<characterId>/manifest.json
- ~/.token-switch/pets/<characterId>/default.svg
- ~/.token-switch/pets/<characterId>/idle.svg
- ~/.token-switch/pets/<characterId>/thinking.svg
- ~/.token-switch/pets/<characterId>/typing.svg
- ~/.token-switch/pets/<characterId>/completed.svg
- ~/.token-switch/pets/<characterId>/failed.svg
- ~/.token-switch/pets/<characterId>/sleeping.svg
- ~/.token-switch/pets/<characterId>/building.svg
- ~/.token-switch/pets/<characterId>/notification.svg
- ~/.token-switch/pets/<characterId>/hover.svg

建议额外创建这些增强文件：
- ~/.token-switch/pets/<characterId>/drag.svg
- ~/.token-switch/pets/<characterId>/mini-idle.svg
- ~/.token-switch/pets/<characterId>/mini-peek.svg
- ~/.token-switch/pets/<characterId>/mini-typing.svg
- ~/.token-switch/pets/<characterId>/mini-alert.svg
- ~/.token-switch/pets/<characterId>/mini-happy.svg
- ~/.token-switch/pets/<characterId>/mini-sleep.svg
- ~/.token-switch/pets/<characterId>/mini-enter.svg
- ~/.token-switch/pets/<characterId>/mini-enter-sleep.svg
- ~/.token-switch/pets/<characterId>/mini-crabwalk.svg
- ~/.token-switch/pets/<characterId>/poke-double.svg
- ~/.token-switch/pets/<characterId>/poke-burst.svg
- ~/.token-switch/pets/<characterId>/poke-annoyed.svg

硬性限制：
1. manifest.json 文件大小必须小于 2MB。
2. 每个 SVG 建议小于 80KB，全部资源尽量控制在 1MB 内。
3. SVG 必须是独立文件，不引用外部图片、字体、CSS、脚本或网络资源。
4. 动画 SVG 使用统一画布，例如 viewBox="0 0 128 128"，width="128"，height="128"。
5. default.svg 必须单独适配为设置页预览图标，不要直接复用完整画布的 idle.svg。
6. default.svg 建议使用 height="1em"、width="1em"、style="flex:none;line-height:1"，并通过更紧的 viewBox 裁切主体，让角色在小图标里视觉大小饱满。
7. default.svg 的 viewBox 应围绕主体有效像素裁切，保留少量安全边距；如果原始画布是 24x24 但主体偏小，可以使用类似 viewBox="3 4 18 18" 的方式放大主体，而不是给主体额外套 scale。
8. 背景必须透明。
9. 主体完整落在画布内，动画 SVG 建议视觉范围在 x=18..110、y=12..118 之间。
10. 底部留 8-12px 空白，避免贴边。
11. 不要放文字，避免小尺寸不可读。
12. 所有资源路径必须相对 manifest.json 所在目录，不能使用绝对路径，不能包含 ..。
13. JSON 必须可被标准 JSON.parse 解析，不能有注释或尾随逗号。

视觉设计要求：
1. 所有 SVG 必须围绕用户设定生成，不要使用通用测试角色。
2. 角色外形、颜色、道具、表情都要体现用户设定里的主题。
3. 风格统一，适合桌面悬浮小窗，64px 到 180px 缩放都能看清。
4. 使用简洁几何形状和少量颜色，建议 4-7 个主色。
5. 每个状态的角色外形要一致，只改变表情、姿态、道具或局部动作暗示。
6. 不要做复杂背景、卡片、说明文字或 UI 面板。
7. 极简模式资源需要在更小可见区域里仍能识别角色，例如半身、侧身、探头或贴边姿态。
8. 点击彩蛋资源可以更夸张一点，但仍应保持角色一致性，不要突然换成另一个角色。

基础状态设计：
- default.svg：中性站立姿态，用于设置页预览；必须是静态图标版，主体居中、轮廓清楚、viewBox 单独裁切到合适视觉大小，不能显得比其他内置桌宠预览图小一圈。
- idle.svg：自然待机，体现角色性格。
- thinking.svg：思考状态，结合角色主题设计思考符号或姿态。
- typing.svg：工作/输入状态，可以加入键盘、小屏幕、代码感或节奏线。
- completed.svg：完成状态，开心、确认、闪光或小勾号。
- failed.svg：失败状态，困惑、沮丧或警告感，但保持可爱、非攻击性。
- sleeping.svg：休息状态，闭眼、蜷缩、睡眠气泡或主题化睡姿。
- building.svg：构建状态，可以有工具、零件、积木、进度暗示。
- notification.svg：提醒状态，可以有铃铛、感叹符号图标或抬头动作。
- hover.svg：鼠标悬停状态，友好回应，比如挥手、眨眼、靠近或展示主题小道具。

增强状态设计：
- drag.svg：拖拽状态，表现被移动、抓住、滑行或小幅慌张的姿态。
- mini-idle.svg：贴靠屏幕右边缘的极简空闲状态；建议只露出半身、侧脸或小爪子，轮廓要清楚。
- mini-peek.svg：极简模式下鼠标悬停时探出来；可以比 mini-idle 更外探、更好奇。
- mini-typing.svg：极简模式下正在思考、输入或构建；建议保留小屏幕、节奏线或工作道具。
- mini-alert.svg：极简模式下通知或失败；可以用抬头、感叹符号、警觉表情。
- mini-happy.svg：极简模式下完成任务；可以用开心、闪光、小勾号。
- mini-sleep.svg：极简模式下休眠；可以趴在边缘、闭眼、睡眠气泡。
- mini-enter.svg：从正常模式切换到极简模式时短暂展示；可以设计成角色钻向屏幕边缘。
- mini-enter-sleep.svg：休眠状态下进入极简模式时短暂展示；可以设计成抱着睡意慢慢缩进边缘。
- mini-crabwalk.svg：反复点击彩蛋之一；可以设计成贴边横移、侧步或躲避。
- poke-double.svg：双击桌宠时短暂展示；可以是惊讶、跳一下、眨眼或回头。
- poke-burst.svg：短时间连续点击 4 下时短暂展示；可以更兴奋、闪光、弹跳或冒出主题粒子。
- poke-annoyed.svg：反复戳很多次时短暂展示；可以有点被打扰、护住道具或小小抗议，但不要攻击性过强。

manifest.json 必须使用动态生成的 characterId、name、description 和 ariaLabel。基础结构如下：

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

如果已经生成增强资源，manifest.json 建议补全为：

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
        "hover": "hover.svg",
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
      },
      "audio": {}
    }
  }
}

完成后请执行校验：
1. 确认目标目录为 ~/.token-switch/pets/<characterId>/。
2. 用 JSON.parse 或等效方式校验 manifest.json。
3. 确认 manifest.json 小于 2MB。
4. 确认 manifest 中引用的所有 SVG 文件都存在。
5. 确认动画 SVG 都包含统一 viewBox，例如 viewBox="0 0 128 128"。
6. 单独检查 default.svg：在 20px、32px、64px 三种尺寸预览时主体都清晰、居中、不裁切，视觉大小接近内置桌宠 default 图。
7. 如果生成了增强资源，确认 manifest 中的 miniIdle、miniPeek、miniTyping、miniAlert、miniHappy、miniSleep、miniEnter、miniEnterSleep、miniCrabwalk、pokeDouble、pokeBurst、pokeAnnoyed 都能找到对应文件。
8. 列出最终创建的文件、文件大小、生成的 characterId、name、description。

最后提醒我：
打开 Token Switch 设置页，展开“桌宠”，查看是否出现新角色 <name>。如果没有出现，重启应用后再检查；如果设置页显示配置警告，优先检查 JSON 格式、角色 ID 和资源相对路径。
```

## 反馈

如需下载、查看更新或了解产品信息，请访问：

- 产品页：[https://token.ferer.net/switch](https://token.ferer.net/switch)
- 官网：[https://token.ferer.net/](https://token.ferer.net/)
- GitHub：[https://github.com/Tangxinzi/token-switch](https://github.com/Tangxinzi/token-switch)
