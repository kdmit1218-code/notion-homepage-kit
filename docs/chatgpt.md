# 在 ChatGPT 聊天中使用

核实日期：2026-10-11。以下依据当前官方文档；具体安装入口与权限以账号、工作区和实际界面为准。

## 本地与云端的区别

官方文档区分本地技能、ChatGPT 工作区技能和打包的 Plugin。把技能安装到电脑不会自动安装到网页账号，也不会传递 Notion 的连接授权。[技能控制](https://learn.chatgpt.com/docs/enterprise/skills)

独立技能适合本地桌面、Codex CLI 和 IDE；将技能打包为 Plugin 是向支持的 ChatGPT 表面分发的方法。ChatGPT 用 `@` 选择，Codex 用 `$`。[构建技能](https://learn.chatgpt.com/docs/build-skills)

## 推荐操作

1. 在 ChatGPT 中连接自己的 Notion，检查它实际提供的搜索、读取、建页与编辑能力。只读连接不能实现本工作流的自动保存。授权在 Notion/连接器页面进行。[Notion MCP 连接说明](https://developers.notion.com/guides/mcp/get-started-with-mcp)
2. 个人开发测试：按官方本地 marketplace 流程安装本套 Plugin，再开新聊天验证；本地来源安装不能当作已在网页云端公开发布。正式分享走官方 Plugin 提交流程。[连接与测试](https://developers.openai.com/plugins/deploy/connect-chatgpt)
3. 在支持 Plugin 的聊天里通过 `@` 选择本套设置技能。填写自己的显示名称、Homepage URL、语言、时区和同步规则。已有主页沿用，尚无主页时明确指定新建位置。
4. 在项目聊天中选择记录技能，说“开始 XX 项目，按我的配置每确定一个决策就同步”。后续不用重复要求总结。必要配置保存在自己的 Notion 配置页；新会话让助手读取它。
5. 检查第一次真实决策写入及 Homepage 项目入口。平台要求的确认仍由平台控制；自动记录的 Skill 不能绕过确认。

可复制的聊天启动说明：

> 使用 Notion Homepage Kit。请读取我提供的个人配置页或 Homepage 链接，在我已授权的 Notion 中按项目名称查找当前项目；缺失时创建项目页并补主页入口。每确定一个决策就更新结论、理由、影响和下一步，查重并回读验证。保留原有内容。

这段话是配置/启动示例，不能替代安装或实际工具连接。把 SKILL.md 当普通附件上传也不能被描述为已装好 Plugin。

## 向别人提供云端安装

公开目录 Plugin 可以只含技能，也可以含 MCP。当前包是技能包，使用者另连 Notion。官方提交流程为上传 Plugin ZIP、处理自动检查、提交审核，批准后由作者发布。还需要发布身份及平台要求的元数据；本次只准备了包，没有远程提交、审核或发布。[发布流程](https://developers.openai.com/plugins/deploy/submission)

如果未来要把 Notion 连接一并打包，需要按服务方支持的 OAuth 和 OpenAI 的 MCP/Plugin 规则配置连接，不能放别人账号密码；不要把现有技能包说成已有该服务。[MCP 身份认证](https://developers.openai.com/plugins/build/auth)

## API 云端是另一条路径

官方 Skills API 能上传技能并用于受支持的执行环境，但这不等于安装进普通 ChatGPT 账号。API 路线还需工具授权、应用状态、成本及部署管理。[Skills API](https://developers.openai.com/api/docs/guides/tools-skills)
