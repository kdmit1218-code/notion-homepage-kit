# 学习模式与候选技能

核实日期：2026-10-11。目标是在学习节点形成可复习的知识笔记；普通项目工作仍直接推进。本套的学习流程见 [learning.md](../skills/notion-project-memory/references/learning.md)。

## Claude 的两种相关功能

Claude for Education 的 Learning mode 在学习中用引导问题帮助推理，强调理解基础，是产品功能。[Anthropic 官方介绍](https://www.anthropic.com/news/introducing-claude-for-education)

Claude Code 的 Learning 是会话输出风格：解释实现选择，并留少量代码让用户练习。可以用 `/output-style learning` 选择；它作用于会话，与按任务加载的 Skill 不同。本套没有安装或切换用户的 Claude 配置。[Claude Code 官方文档](https://code.claude.com/docs/en/output-styles)

因此，不能把这些功能当成一个现成官方学习 Skill 直接安装。可以借鉴引导思考与实际练习的思路，在 Notion 工作流中实现相应模式。

## 查找结果

本次按 find-skills 流程检查技能目录、仓库和实际 SKILL.md。本机没有可执行的 npx，CLI 搜索未成功，改用网页与源仓库核实。未安装第三方教学技能。

优先参考 **github/awesome-copilot 的 mentoring-juniors**：面向初级开发者的苏格拉底式指导。检查时目录显示约 6.9K 安装，源仓库约 39.9K stars；这些是热度指标，不能替代行为验证。仓库在 GitHub 组织下，内容是社区贡献，不是 Anthropic 官方功能。[技能目录](https://skills.sh/github/awesome-copilot/mentoring-juniors)、[仓库](https://github.com/github/awesome-copilot)、[技能原文](https://github.com/github/awesome-copilot/blob/main/skills/mentoring-juniors/SKILL.md)

可选安装命令（需要 Node.js / npx 环境）：

```sh
npx skills add https://github.com/github/awesome-copilot --skill mentoring-juniors
```

该技能强调提问，严格限制直接给答案。适合专门的训练会话；我们的项目还需要按时完成，所以本套提供可切换的讲解、练习、复习，不将其整套规则加入常规项目执行。若用户主动选择此导师技能，由它负责教学，本套负责笔记写入，避免重复保存。

## 本套的补充

1. 用真实项目作为例子，按已有背景选择难度；用户可随时要求答案。
2. 知识点或练习结束后再整理，避免每轮问答生成碎片页面；主题页复用，正文只存一份。
3. 区分来源事实、解释和待核实内容，并保留来源及版本；后续纠错有变更说明。
4. 区分知识正确性与学习表现，用真实练习作为证据，不虚构掌握度。
5. 留下复习问题与实际薄弱点，下次从笔记继续；长对话可存阶段小结。
6. 复习建议与定时提醒分开处理，本套未新增后台调度。

这次是自有流程与参考文档的增量更新，没有复制或捆绑第三方技能全文，也不依赖其安装。现有个人配置保持兼容；学习方式和是否记录由当前用户在会话内选择。
