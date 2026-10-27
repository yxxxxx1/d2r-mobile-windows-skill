# Windows 给 iPhone 安装 D2R Mobile：可复用的 Agent Skill

**我们只做流程整合、实测与 Skill 封装。** D2R Mobile 兼容层由 **jhaizhou 及原项目贡献者**开发，云端构建工具由 **jiayx 及其贡献者**提供。

## 原作者与项目来源

- **D2R Mobile：jhaizhou 及贡献者** — [jhaizhou-ops/d2r-mobile](https://github.com/jhaizhou-ops/d2r-mobile)。iPhone 上运行游戏所需的兼容层、触屏交互与相关能力来自这个原项目。
- **云端构建：jiayx 及贡献者** — [jiayx/d2r-mobile-build](https://github.com/jiayx/d2r-mobile-build)。本次使用的 GitHub Actions 构建与打包流程来自这个项目。
- **原项目使用的第三方工作与社区贡献** — 参见上游的 [Acknowledgements](https://github.com/jhaizhou-ops/d2r-mobile#acknowledgements) 与 [依赖和许可](https://github.com/jhaizhou-ops/d2r-mobile/blob/main/docs/DEPENDENCIES.md)。
- **原游戏** — 《Diablo II: Resurrected》及相关内容的权利归 Blizzard Entertainment 等相应权利人所有，使用者需自备有权使用的游戏文件。

本仓库新增的内容是 Windows 安装与更新步骤的整理、实测记录、供 AI 使用的 Skill，以及只读本地备份校验脚本。请优先关注和支持原作者；转载本流程或分享 Skill 时保留以上署名和原项目链接。

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
- 按用户选择导入社区离线角色，先备份、检查重名，导入后核对新旧存档。

## 可选：24 个社区角色存档

随 Skill 附带 [24 角色存档包](skills/d2r-mobile-windows/assets/community-characters-v105.zip)，涵盖七个传统职业，等级 81–93。原始角色由 **[P3N9U1N](https://github.com/P3N9U1N/diablo2-savegames)** 以 MIT 许可公开分享；格式转换使用 **[ResurrectedTrader/D2SSharp](https://github.com/ResurrectedTrader/D2SSharp)**。我们只做格式转换、校验和目录整理，原作者许可随包保留。

**完全可选。** 安装 Skill 或更新应用不会自动导入这批角色，也不会替换已有角色。完整角色列表、摘要、兼容范围和备份后追加导入步骤见 [可选存档说明](skills/d2r-mobile-windows/references/community-saves.md)。这些角色已完成本地格式校验和一次设备传输校验，尚未逐一实机进局验收。

可复制给 AI：

```text
使用 $d2r-mobile-windows，先列出 Skill 自带的 24 个可选社区角色，让我选择要导入的角色。导入前备份并校验手机最新存档，检查格式和同名冲突；只追加选中的角色目录，不覆盖现有角色或共享仓库，完成后读回核对。不要重新安装游戏，也不要改变自动续签设置。
```

## 先准备什么

1. 支持数据传输的 USB 线、已解锁并信任电脑的 iPhone。
2. 苹果设备支持组件与 [Sideloadly 官方安装程序](https://sideloadly.io/)。
3. 自己有权使用的游戏文件，以及匹配当前源码的构建输入／资源。使用免费签名时仍需要 Apple 账号；可以考虑单独账号并开启双重认证。
4. 足够的电脑与手机空间。手机空间应覆盖解压后的资源、应用和安装临时文件，不能只看下载包大小。

账号密码、验证码在本机软件界面输入。该 Skill 不提供游戏程序、密钥、证书、IPA 或游戏资源下载镜像；可选社区角色包单独保留原作者许可。

## 实测记录与边界

2026-10-26，Windows + iPhone 13 Pro Max（A15）+ iOS 26.6.2，完成源码 `195ae11dc70f1ba7735c6063e1ed81102e1dbf52` 的 `2.0.0 / build 2.1` 安装与数据恢复。共恢复 30 个存档文件并逐个核对 SHA-256，23 个资源文件合计 6,609,731,728 字节并核对远端大小；数据资源与 Legacy 文件在传输前做了本地摘要校验。该记录是经验基线，不代表其他机型、系统或后续版本已经实测。

本地技能瞄准测试 85/85、技能有效性测试 17/17 通过；另一个依赖生成文件的前端检查未在本地完成。iOS 编译与安装包校验在云端 macOS 完成，不能据此宣称全部游戏运行测试通过。

免费账号签名通常有效 7 天。自动续签依赖电脑和后台运行，并能连接手机；本次验证的是 USB 路径。续签会刷新缓存中的 IPA，不会自动追踪上游源码。详情以 [Sideloadly 官方说明](https://sideloadly.io/) 为准。

## 文件与本地验证

- [SKILL.md](skills/d2r-mobile-windows/SKILL.md)：AI 的任务入口。
- [Windows 流程](skills/d2r-mobile-windows/references/windows-workflow.md)：备份、安装、资源与续签细节。
- [备份校验脚本](skills/d2r-mobile-windows/scripts/verify_backup.py)：只读校验本地存档备份，不连接手机。
- [可选社区存档](skills/d2r-mobile-windows/references/community-saves.md)：24 个带装备的角色，按需选择后备份、校验并追加导入。
- [X 帖子草稿](docs/x-post.md)：主帖、回复与可复制命令。

```sh
python -m unittest discover -s tests -v
python skills/d2r-mobile-windows/scripts/verify_backup.py /path/to/backup-manifest.json
```

辅助脚本只依赖 Python 3.11+ 标准库；实际设备通信需要另外在隔离环境安装并验证 `pymobiledevice3`。它不会代替设备备份，也不会写入手机。

## 来源与许可

原作者和项目链接已在首页开头列明。D2R Mobile 与云端构建工具的代码及其贡献属于各自作者和贡献者；本仓库是独立的流程整合，与上述项目及 Apple、Blizzard、Sideloadly 均无隶属关系。

本仓库自行编写的整合说明与辅助脚本使用 [MIT License](LICENSE)。此许可只覆盖本仓库新增内容；社区角色包遵循随附的 [P3N9U1N MIT 许可](skills/d2r-mobile-windows/assets/community-characters-LICENSE.txt)，游戏、系统工具及原项目遵循各自许可与署名。
