# Token Switch 桌宠资源规范

## 必需文件

在 `~/.token-switch/pets/<characterId>/` 中创建这些文件：

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

完整资源包建议额外创建：

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

## Manifest 结构

基础 manifest：

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

## 硬性限制

- `manifest.json` 必须是标准 JSON，不能有注释或尾随逗号。
- `manifest.json` 必须小于 2 MB。
- 每个 SVG 建议小于 80 KB；完整资源包整体尽量控制在 1 MB 左右或以内。
- SVG 必须是独立文件，并使用透明背景。
- 不要引用外部图片、字体、CSS、脚本或网络资源。
- manifest 中的每个资源路径都必须相对 `manifest.json`，不能使用绝对路径或 `..`。
- 动画 SVG 建议统一使用 `viewBox="0 0 128 128"`、`width="128"` 和 `height="128"`。
- 角色主体必须完整落在画布内；建议视觉范围在 x=18..110、y=12..118，并在底部保留 8 到 12 px 空白。
- SVG 内不要出现可见文字。

## `default.svg`

`default.svg` 是设置页预览图标，不是完整动画帧。

- 使用 `width="1em"` 和 `height="1em"`。
- 条件允许时加入 `style="flex:none;line-height:1"`。
- `viewBox` 需要围绕主体有效像素紧裁切，让图标在 20 px、32 px 和 64 px 下都显得饱满。
- 主体需要居中且不能被裁切。
- 不要直接复用 `idle.svg`；单独制作一个小尺寸轮廓更清楚的静态图标版。

## 状态设计

- `idle`：自然待机，体现角色性格。
- `thinking`：思考姿态，加入贴合主题的思考暗示。
- `typing`：工作或输入状态，可加入键盘、屏幕、代码感或节奏线。
- `completed`：开心、勾选、闪光或成功姿态。
- `failed`：困惑、沮丧或警告暗示，保持友好。
- `sleeping`：闭眼、蜷缩、睡眠气泡或主题化睡姿。
- `building`：工具、零件、积木或进度暗示。
- `notification`：铃铛、感叹号、抬头或提醒姿态。
- `hover`：挥手、眨眼、靠近或展示道具等友好回应。
- `drag`：被移动、抓住、滑行或轻微慌张的姿态。
- `mini-idle`：贴边极简空闲状态，只露出半身、侧脸或小手。
- `mini-peek`：贴边悬停状态，比 `mini-idle` 更外探。
- `mini-typing`：贴边工作状态。
- `mini-alert`：贴边通知或失败状态。
- `mini-happy`：贴边完成状态。
- `mini-sleep`：贴边休眠状态。
- `mini-enter`：进入贴边极简模式的过渡。
- `mini-enter-sleep`：休眠时进入贴边极简模式的过渡。
- `mini-crabwalk`：反复点击后的贴边彩蛋，可表现为侧移或躲避。
- `poke-double`：双击反馈。
- `poke-burst`：短时间连续点击 4 下后的更兴奋反馈。
- `poke-annoyed`：反复戳很多次后的轻微抗议反馈，避免攻击性。

## 最终提醒

告诉用户：

`打开 Token Switch 设置页，展开“桌宠”，查看是否出现新角色 <name>。如果没有出现，重启应用后再检查；如果设置页显示配置警告，优先检查 JSON 格式、角色 ID 和资源相对路径。`
