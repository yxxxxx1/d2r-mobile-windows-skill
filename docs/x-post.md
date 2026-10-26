# X 发布草稿

以下主帖和回复分别发布；命令放在回复或仓库，便于复制。内容仅为草稿，不代表已发布到 X。

## 主帖

用 Windows + AI 跑通了《暗黑2重制版》的 iPhone 安装。

先谢原作者：D2R Mobile 来自 jhaizhou 及贡献者，云端构建来自 jiayx 及贡献者。

我们只把安装、备份、资源导入和续签流程整合成 Skill。

自备游戏文件，Apple 登录与手机确认仍需本人完成。

https://github.com/yxxxxx1/d2r-mobile-windows-skill

## 回复 1：原作者与原项目

核心能力来自原作者和社区，感谢：

D2R Mobile：jhaizhou 及贡献者
https://github.com/jhaizhou-ops/d2r-mobile

云端构建：jiayx 及贡献者
https://github.com/jiayx/d2r-mobile-build

我们做的是流程整合、实测和 Skill 封装。请优先关注和支持原项目。

## 回复 2：安装 Skill

复制这条命令，按提示选你的 AI 工具：

```sh
npx skills add yxxxxx1/d2r-mobile-windows-skill --skill d2r-mobile-windows
```

装好后告诉 AI：用这个 Skill 帮我安装／更新 D2R Mobile，先备份存档，再校验资源和续签。

电脑需要 Node.js 22.20+，AI 需要本机文件与设备操作能力。

## 回复 3：实测与提醒

实测：Windows + iPhone 13 Pro Max，2.0.0 主分支修复版。

恢复了30个存档文件、约6.6GB资源，并校验安装结果和续签缓存。

更新时保留同一账号和应用标识，别先删游戏。自动续签仍需电脑后台运行并能连接手机，本次验证的是USB。

项目致谢与完整流程都在仓库；仓库不包含游戏文件。

## Codex 安装替代文案

可以把下面这句直接发给 Codex，无需先使用上面的 CLI：

```text
使用 $skill-installer 安装 https://github.com/yxxxxx1/d2r-mobile-windows-skill/tree/main/skills/d2r-mobile-windows 。安装后告诉我如何调用。
```
