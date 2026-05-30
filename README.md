# Token Switch

Token Switch 是一个用于管理、切换和测试 CLI / Agent 工具 Provider、模型与 Token 配置的桌面应用。

这个公开仓库只用于发布说明、下载入口和自动更新清单。应用源码、构建脚本、签名密钥和私有配置不会放在这里。

## 下载

当前版本：`1.10.0`

- macOS Universal DMG：发布后放在 GitHub Releases
- Tauri 自动更新包：发布后放在 GitHub Releases
- 更新清单：[`update.json`](./update.json)

正式发布后，下载文件会作为 GitHub Release Assets 上传到对应版本，例如：

```text
https://github.com/<owner>/token-switch/releases/download/v1.10.0/Token%20Switch_1.10.0_universal.dmg
https://github.com/<owner>/token-switch/releases/download/v1.10.0/Token%20Switch_1.10.0_universal.tar.gz
```

## 自动更新

`update.json` 用于 Tauri updater。发布时需要把里面的占位 URL、签名和说明替换为真实值。

如果继续使用自有域名作为稳定入口，可以让服务端转发这个公开仓库中的 `update.json`。

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
