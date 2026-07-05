# 下载、安装与更新

## 官方入口

- 产品页：`https://token.ferer.net/switch`
- 官网：`https://token.ferer.net/`
- 支持能力：Agent 配置、Provider 管理、Token 统计、本地 Relay 与桌宠资源生成
- macOS 安装脚本：`https://token.ferer.net/install.sh`
- Windows 安装脚本：`https://token.ferer.net/install.ps1`
- 实时安装清单：`https://token.ferer.net/api/install.json?target=<target>&arch=<arch>&current_version=0.0.0`

## 查询最新版

优先运行 Skill 自带脚本：

```bash
python3 scripts/latest_release.py
```

可指定平台和架构：

```bash
python3 scripts/latest_release.py --target darwin --arch aarch64
python3 scripts/latest_release.py --target windows --arch x64
```

如果脚本不可用，用 `curl` 查询：

```bash
curl -fsSL 'https://token.ferer.net/api/install.json?target=darwin&arch=aarch64&current_version=0.0.0'
curl -fsSL 'https://token.ferer.net/api/install.json?target=windows&arch=x64&current_version=0.0.0'
```

## macOS 安装

向用户说明将运行官方安装脚本后再执行：

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

PowerShell 命令：

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

如果用户已经安装 Token Switch：

1. 先查询实时安装清单确认最新版。
2. 让用户在 Token Switch 内检查更新，或重新运行官方安装脚本覆盖安装。
3. 如果 Agent 配置或 Relay 状态更新后没有生效，重启 Token Switch 和目标 Agent。

## 回答模板

用户问“怎么下载”时，简洁给出：

- macOS：`curl -fsSL https://token.ferer.net/install.sh | sh`
- Windows PowerShell：`powershell -NoProfile -ExecutionPolicy Bypass -Command "irm https://token.ferer.net/install.ps1 | iex"`
- 产品页：`https://token.ferer.net/switch`

用户问“最新版是多少”时，实时查询安装清单后再回答具体版本、发布日期、更新说明和对应安装包链接。
