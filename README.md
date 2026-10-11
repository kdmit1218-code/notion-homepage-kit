# Notion Homepage Kit

把项目聊天中的决策和知识沉淀到自己的 Notion，并从个人 Homepage 找到每个项目。版本 0.5.0。

本套包含主页初始化、项目开始时查找/建页、每个确定决策后记录、知识整理、导航更新及按要求归档。它复用一种个人工作方式；每位使用者连接自己的 Notion、设置自己的主页名称和 URL。

## 首次使用

1. 在运行平台连接你自己的 Notion，并完成 OAuth 授权。不要把账号密码或令牌填写到 Skill。
2. Codex 安装 `skills/` 内两个技能；网页自定义 GPT 按下面的两文件方法配置。本套尚未在网页 Plugin 目录发布。
3. Codex 使用 `$notion-homepage-setup`。提供显示名称、主页链接（或请求新建）、语言、时区，以及按决策自动保存还是手动保存。
4. 新开项目聊天，选择 `notion-project-memory`；网页端直接打开配置好的 GPT。例如：“开始库存分析项目，每确定一个决策就记到我的主页下。”

一个完整的新用户例子：

> 我的显示名称是 Alex。使用我已连接的 Notion，在我指定的父页面下创建 Alex’s Homepage，使用中文和 UTC（首次设置时可改为自己的时区）。启用按决策同步，允许自动创建新项目并补主页入口。保留现有内容。

## 网页自定义 GPT 配置

网页只需两个文件：[轻量指令](docs/gpt-instructions.md) 全文粘到“指令”栏，[统一知识文件](docs/gpt-skill.md) 上传到“知识”。它已合并原七份参考，不再要求逐个上传。按 [五步配置说明](docs/chatgpt.md) 检查 Notion 写入工具；保存后进入你创建的 GPT 直接发请求。仅上传文件不等于安装 Plugin，也不会在其他 GPT 聊天中自动启用。

Codex 的两个技能已允许隐式选择；网页自定义 GPT 则在你选择该 GPT 后按指令处理相关任务。自动选择不保证每次触发，自动写入仍遵循用户已确认的记录范围。

也可把同一份轻量指令放到 ChatGPT 的“项目指令”，只上传统一知识文件，供该项目内聊天使用。实际写入仍需可用的 Notion 工具。

学习结论、具体日程或活动安排、项目启动及阶段成果均可提供一次记录选择：仅此次、本主题持续记录、暂不记录。已有授权范围直接沿用；未回复不写入，同主题拒绝后不反复提示。日程活动按现有主页栏目记录，不自动创建日历事件或提醒。

每次保存同时维护目录：先判断旧主题补充还是新主题，新主题建页后补分类索引，旧主题更新原页。本次维护的主页与内容页启用页内目录，跨页用主题入口连接，核对从 Homepage 能到达，避免只有正文没有入口。

目录按分类显示短标题与入口，长章节折叠。正文保留当前有效结论、必要理由与下一步；已确认的新方案取代旧方案时重写当前摘要，旧方案只留简短变更记录。原始资料、附件和约定的审计日志保留。

## 本地配置

Python 3.10+，运行前执行 `python -m pip install -r requirements.txt` 提供跨平台时区数据。下面的命令只保存配置，不连接 Notion，不创建主页，也不证明页面权限。

```sh
python scripts/configure.py --name "Your Name" --homepage "https://www.notion.so/your-homepage" --timezone "UTC" --sync-mode on_decision --auto-create-projects
```

用真实主页链接替换示例。默认写入 `skills/notion-project-memory/profile.local.json`；安装技能时将这个文件放入已安装的同名技能目录。Windows 若缺少 IANA 时区数据，按脚本提示安装 `tzdata`。云端不用本地脚本，使用用户自己的 Notion 配置页或本聊天确认的配置。

## 提供的内容

| 文件 | 用途 |
| --- | --- |
| skills/notion-homepage-setup | 首次连接与配置工作流 |
| skills/notion-project-memory | 决策、知识、主页与项目维护 |
| profile.example.json | 名称、URL、语言、时区、同步模式、章节映射 |
| references/homepage.md | 通用布局与归档规则，无作者页面 ID |
| scripts/configure.py | 校验并创建个人配置 |
| scripts/package.py | 生成不包含本地个人配置的公开 ZIP |
| docs/chatgpt.md | ChatGPT 云端使用和当前支持边界 |
| docs/gpt-instructions.md | 复制到网页 GPT 或项目指令的入口 |
| docs/gpt-skill.md | 网页仅需上传的统一知识文件 |
| docs/publishing.md | GitHub 与 Plugin 发布步骤 |
| docs/evaluation.md | 实际验证情况与验收场景 |

## 学习与笔记

在本知识工作流中可选择讲解、引导练习或复习，围绕当前项目的具体问题学习，在一个知识点或练习结束后整理笔记。例如：“带我学 Skill 的触发机制，每个知识点结束后自动整理到我的 Notion Learning 入口，记录我还没理解的地方。”也可说“直接给答案”或“先完成项目”切回执行。

只整理资料时无需参加练习。学习笔记区分知识来源与本次练习表现；已经讲解不等于掌握。每位用户自行授权学习内容是否自动保存，原有 `on_decision` 配置不扩大为保存所有学习聊天。详见 [学习模式与候选技能](docs/learning.md)。

## 项目总结与历史补录

可说：“总结当前项目，按我的主页把进展和决策归 Projects，把可复用知识归 Learning，查重后同步。”已有项目首次接入、阶段收尾或明确需要补录时，技能可提供一次整理入口；用户跳过就继续工作。

也可指定若干历史聊天导出、会话或项目资料，按范围整理。它先报告实际可读取的来源与缺口，再分项目归类；当前工具没有全账号聊天历史接口时，不声称能扫描全部 ChatGPT/Codex 聊天。详见 [项目总结流程](skills/notion-project-memory/references/consolidation.md)。

## 打包与发布

```sh
python scripts/package.py
```

产物在 `dist/`：Plugin ZIP 根目录包含 plugin.json 与完整套件；独立 Skill ZIP 含单个顶层 `notion-project-memory` 文件夹。Setup 技能依赖同包参考文件，随完整套件一起安装。

网页用户可下载 `notion-homepage-kit-web.zip`，解压后只有指令与统一知识两个文件，分别复制和上传；ZIP 本身不代替配置。

公开包不带作者 Homepage、项目 URL、账号配置或凭据。`.gitignore` 与 ZIP 白名单排除个人配置和运行数据；发布前仍需检查 Git 实际将上传的文件。请上传这个目录，不要上传上层私人文档工作区。版本更新不覆盖用户的 profile.local.json。

## 边界

这是技能与分发包，不是自建 Notion API 服务。它依赖用户已连接且支持写入的 Notion 工具，未捆绑账号或远程连接器。安装不意味着授权自动写入；首次由各使用者选择同步规则。技能不提供关掉聊天后的后台监听，也不保证每个新聊天都自动加载。

现有主页默认保留原结构。删除、共享、移动或大规模重排需要用户明确提出。普通决策记录无需每次再询问。当前未添加 LICENSE，不声明已经授予开源复用许可。
