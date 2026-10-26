# X 发布草稿

以下主帖和回复分别发布；命令放在回复或仓库，便于复制。内容仅为草稿，不代表已发布到 X。

## 主帖

我让 AI 在 Windows 上，把《暗黑2重制版》装进了 iPhone。

云端编译 → Sideloadly 签名 → USB 导资源，连存档恢复和自动续签也跑通了。

现在把流程整理成开源 Skill，复制安装指令就能交给 AI 按步骤处理。

需要自备游戏文件，Apple 登录和手机确认仍由本人完成。

https://github.com/yxxxxx1/d2r-mobile-windows-skill

## 回复 1：安装 Skill

复制这条命令，按提示选你的 AI 工具：

```sh
npx skills add yxxxxx1/d2r-mobile-windows-skill --skill d2r-mobile-windows
```

装好后告诉 AI：用这个 Skill 帮我安装／更新 D2R Mobile，先备份存档，再校验资源和续签。

电脑需要 Node.js 22.20+，AI 需要本机文件与设备操作能力。

## 回复 2：实测与提醒

实测：Windows + iPhone 13 Pro Max，2.0.0 主分支修复版。

恢复了30个存档文件、约6.6GB资源，并校验安装结果和续签缓存。

更新时保留同一账号和应用标识，别先删游戏。自动续签仍需电脑后台运行并能连接手机，本次验证的是USB。

项目致谢与完整流程都在仓库；仓库不包含游戏文件。

## Codex 安装替代文案

可以把下面这句直接发给 Codex，无需先使用上面的 CLI：

```text
使用 $skill-installer 安装 https://github.com/yxxxxx1/d2r-mobile-windows-skill/tree/main/skills/d2r-mobile-windows 。安装后告诉我如何调用。
```
