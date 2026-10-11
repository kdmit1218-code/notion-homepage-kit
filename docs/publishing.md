# 发布到 GitHub 与 Plugin 目录

## GitHub

仓库根目录应为 `notion-homepage-kit/`。公共内容包括通用技能、默认布局、示例配置、脚本与说明；个人 profile、真实主页快照、运行记录和凭据不加入仓库。不要把上层个人工作区一起提交。

1. 运行验证与打包脚本，检查 ZIP 中的文件名及内容。
2. 确定仓库名、许可证和公开的作者信息，再初始化这个独立目录的 Git 仓库。
3. 在 GitHub 创建目标仓库并推送；已有仓库先检查远端变更，再更新已检查的公开文件，保留已有历史，不强制推送上层目录。
4. 以版本号发布 ZIP。记录已验证范围，保留使用者自己的配置，升级不覆盖 profile.local.json。

仓库发布后可让 Codex 的 skill-installer 从该仓库安装 `skills/notion-project-memory` 与 `skills/notion-homepage-setup`。不要把尚未存在的仓库地址写成可用安装源。

## Plugin

根目录 plugin.json 使用官方 portable manifest；onboardingSkill 指向同包设置技能。本包没有声明不存在的 MCP 或借用作者的注册连接 ID。[Plugin 包结构](https://developers.openai.com/plugins/build/plugins)

`dist/notion-homepage-kit-plugin.zip` 中 plugin.json 位于根目录。正式发布前需在官方平台验证导入并补齐发布身份、描述、截图和法律信息等实际要求。通过本地 JSON/资源验证不等于通过平台审核。

技能包目前依赖单独安装和授权的 Notion 连接器。若未来加入自有 MCP，需另设计用户授权、部署和平台审核；官方当前说明无法给已经发布的 skills-only Plugin 直接追加 MCP，因此先决定产品的发行路线再提交。[提交说明](https://developers.openai.com/plugins/deploy/submission)
