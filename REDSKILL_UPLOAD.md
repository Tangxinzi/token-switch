# REDSkill 上传说明

本仓库目前保留两种 Token Switch Skill 形态：

- 正式目录包：[token-switch](token-switch/)
- 单文件 Markdown：[SKILL.md](SKILL.md)

如果 REDSkill 网页端支持多格式上传，可以优先上传 `SKILL.md`。它是完整的单文件版，不依赖 `references/` 或 `scripts/`。

如果使用本机 `skillhub-upload` CLI，当前已验证的 0.1.0 版本仍只接受 Skill 目录，需上传 `token-switch/` 目录，不能直接上传 `SKILL.md` 或手动 zip。

## 推荐参数

- source：原创
- tag：编程开发
- Skill ID：token-switch
- name：token-switch

## CLI dry-run

```bash
node /Users/mac/.local/skillhub-upload-cli/node_modules/@xhs/skillhub-upload/cli/index.mjs publish /Users/mac/Projects/token-switch/token-switch --dry-run --agent --source original --tag 编程开发
```

已验证目录包 dry-run 可通过，`bundle_size_bytes` 约 10102。

## 注意

- 不要上传用户自己压缩的 zip。
- 不要把 API Key、Token、账号凭证写入 Skill 文档。
- 如果平台提示 `Skill ID 已被占用`，需要在平台侧换一个新的 Skill ID；本地文件本身仍是合法 Skill。
