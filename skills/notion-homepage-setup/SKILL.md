---
name: notion-homepage-setup
description: "安装 Notion Homepage Kit 后的首次设置：连接用户自己的 Notion、指定或创建个人 Homepage、配置语言时区及自动记录范围。用户要求安装、配置或切换本套 Notion 工作流时使用。"
---

# 首次设置

读取同包 [../notion-project-memory/references/setup.md](../notion-project-memory/references/setup.md)，按其中流程配置当前使用者。布局参考 [../notion-project-memory/references/homepage.md](../notion-project-memory/references/homepage.md)。

用已连接的 Notion 工具检查能力；需要账号授权时让用户走连接器 OAuth 页面，不收集账号密码。收集显示名称、主页 URL 或建页位置、语言、时区和自动记录偏好。只询问当前缺失的信息。

已有主页先读取并沿用结构；新主页在用户指定的父页面下创建。用户未指定位置但明确要创建时按当前工具的私有草稿模式执行，然后返回链接。不能把默认模板内的示例当作个人数据。

启用自动记录前让当前用户明确选择：按决策同步并允许新项目自动建页，或只在要求时保存。已有会话授权可以直接沿用。保存的配置不包含密码或令牌。

本地使用者可运行包内 `scripts/configure.py` 创建私有 profile；云端使用者可将已确认配置保存在其主页下的“Homepage Kit｜个人配置”页。配置页仅在用户希望持久保存设置时创建，返回链接供下次选择。配置本身不是 Skill，也不因配置而启用平台共享权限。

最后核实主页、项目入口位置与配置内容；说明已设置和实际缺失的工具。引导用户在项目聊天中选择 notion-project-memory。无需试写一个虚构项目。
