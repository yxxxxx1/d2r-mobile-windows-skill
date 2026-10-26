# Windows 给 iPhone 安装 D2R Mobile：可复用的 Agent Skill

把一次实际跑通的 Windows → iPhone 安装、更新、存档恢复与自动续签流程，整理成 AI 可以执行的 Skill。

适合有 Windows 电脑、iPhone 和自己游戏文件的玩家。AI 需要有访问本机文件、运行终端及使用安装工具的能力；纯网页聊天不能直接操作 USB 手机。

## 复制安装指令

在有 Node.js 22.20+ 的电脑终端运行，按提示选择你的 AI 工具：

```sh
npx skills add yxxxxx1/d2r-mobile-windows-skill --skill d2r-mobile-windows
```

这是安装 **Skill** 的命令。Apple 登录、双重认证、手机解锁、信任开发者和开启开发者模式仍需本人完成。

Codex 用户也可以复制下面这句，发给 Codex：

```text
使用 $skill-installer 安装 https://github.com/yxxxxx1/d2r-mobile-windows-skill/tree/main/skills/d2r-mobile-windows 。安装后告诉我如何调用。
```

然后复制任务：

```text
使用 $d2r-mobile-windows，帮我在 Windows 上给连接的 iPhone 安装或更新 D2R Mobile。先检查设备与当前版本；更新前备份并校验存档，保持原签名账号和应用标识，保留资源，并核对自动续签缓存。Apple 密码和验证码由我在软件窗口输入。缺少材料时明确告诉我，不要把下载构建原料当成可安装 IPA。
```

如果使用其他支持 Agent Skills 的工具，通过其 Skill 安装功能导入 [skills/d2r-mobile-windows](skills/d2r-mobile-windows)。命令格式与支持范围见 [skills CLI](https://github.com/vercel-labs/skills)；Codex 机制见 [官方文档](https://developers.openai.com/codex/skills/)。

## 它会处理哪些事情

- 检查苹果 USB 通信、手机系统和现有安装情况。
- 区分可安装 IPA 与构建原料；需要时使用云端 macOS 编译。
- 通过 Sideloadly 签名安装，指导完成手机端信任和开发者模式。
- 经 House Arrest／AFC 备份存档、校验文件、导入匹配的 Data 与 Legacy 资源。
- 更新时保持签名账号和最终 bundle ID；安装后校验存档及资源。
- 核对 Sideloadly 自动续签及新版缓存；无线连接单独验证。

## 先准备什么

1. 支持数据传输的 USB 线、已解锁并信任电脑的 iPhone。
2. 苹果设备支持组件与 [Sideloadly 官方安装程序](https://sideloadly.io/)。
3. 自己有权使用的游戏文件，以及匹配当前源码的构建输入／资源。使用免费签名时仍需要 Apple 账号；可以考虑单独账号并开启双重认证。
4. 足够的电脑与手机空间。手机空间应覆盖解压后的资源、应用和安装临时文件，不能只看下载包大小。

账号密码、验证码在本机软件界面输入。该 Skill 不提供游戏文件、密钥、证书、IPA 或游戏资源下载镜像。

## 实测记录与边界

2026-10-26，Windows + iPhone 13 Pro Max（A15）+ iOS 26.6.2，完成源码 `195ae11dc70f1ba7735c6063e1ed81102e1dbf52` 的 `2.0.0 / build 2.1` 安装与数据恢复。共恢复 30 个存档文件并逐个核对 SHA-256，23 个资源文件合计 6,609,731,728 字节并核对远端大小；数据资源与 Legacy 文件在传输前做了本地摘要校验。该记录是经验基线，不代表其他机型、系统或后续版本已经实测。

本地技能瞄准测试 85/85、技能有效性测试 17/17 通过；另一个依赖生成文件的前端检查未在本地完成。iOS 编译与安装包校验在云端 macOS 完成，不能据此宣称全部游戏运行测试通过。

免费账号签名通常有效 7 天。自动续签依赖电脑和后台运行，并能连接手机；本次验证的是 USB 路径。续签会刷新缓存中的 IPA，不会自动追踪上游源码。详情以 [Sideloadly 官方说明](https://sideloadly.io/) 为准。

## 文件与本地验证

- [SKILL.md](skills/d2r-mobile-windows/SKILL.md)：AI 的任务入口。
- [Windows 流程](skills/d2r-mobile-windows/references/windows-workflow.md)：备份、安装、资源与续签细节。
- [备份校验脚本](skills/d2r-mobile-windows/scripts/verify_backup.py)：只读校验本地存档备份，不连接手机。
- [X 帖子草稿](docs/x-post.md)：主帖、回复与可复制命令。

```sh
python -m unittest discover -s tests -v
python skills/d2r-mobile-windows/scripts/verify_backup.py /path/to/backup-manifest.json
```

辅助脚本只依赖 Python 3.11+ 标准库；实际设备通信需要另外在隔离环境安装并验证 `pymobiledevice3`。它不会代替设备备份，也不会写入手机。

## 来源与许可

游戏兼容层：[jhaizhou-ops/d2r-mobile](https://github.com/jhaizhou-ops/d2r-mobile)。云端打包流程参考：[jiayx/d2r-mobile-build](https://github.com/jiayx/d2r-mobile-build)。本仓库是独立的使用流程整理，与上述项目及 Apple、Blizzard、Sideloadly 均无隶属关系。

本仓库原创说明与辅助脚本使用 [MIT License](LICENSE)。游戏、系统工具及其他项目遵循各自许可。

