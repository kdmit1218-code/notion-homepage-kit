# 个人配置与授权

每个使用者连接自己的 Notion；OAuth 在连接器的授权页面完成。技能不保存账号密码或访问令牌，也不继承作者账号的连接。配置只描述行为和目的地。

## 首次设置

1. 检查实际可用的读取、搜索、建页、编辑工具。无法写入时清楚说明仅能查询或生成草稿；不得声称已启用自动同步。
2. 必要输入：显示名称、已有 Homepage URL 或明确的新主页创建请求；语言与时区可从当前会话推断并告知。主页默认标题是“显示名称’s Homepage”，可改。
3. 有 URL 时 fetch 核实标题、父级与结构。只有名称时搜索并展示可信候选；多个匹配让用户选择。查不到时区分无权限、搜索不完整和确实尚未创建。
4. 创建新主页时用默认布局模板，填入用户信息，不复制作者或其他账号页面。用户指定父级时使用该父级；未指定时遵循连接器私有草稿规则。
5. 明确当前使用者的写入范围：`on_decision`（确定决策即记录）、是否允许新项目自动建页与补主页入口，或 `manual`（用户要求才写）。缺少选择不能擅自打开自动写入。
6. 本地可写 `profile.local.json`；云端可在已指定主页下创建个人配置页，仅在用户要求持久设置时保存。校验一次后无需每轮重新问。切换账号或主页时重新核实映射。

## 配置字段

| 字段 | 含义 |
| --- | --- |
| display_name | 显示名称，不是登录名 |
| homepage_title | 搜索和显示的主页名称 |
| homepage_url | 已核实的当前用户主页 URL |
| language / timezone | 记录语言与 IANA 时区 |
| sync_mode | on_decision 或 manual |
| auto_create_projects | 当前用户是否允许自动创建项目 |
| homepage_layout | preserve 保留原结构；starter 新建时使用模板 |
| sections | Projects、Current、Learning、Quick Access、Archive 等实际标题映射 |
| project_aliases | 别名到已核实的项目主页 URL 映射；不能从公共示例继承 |

无需配置密码、Notion token、OpenAI key。脚本不会发起登录或读写 Notion；它只保存本地配置。项目别名和 URL 是私人配置，默认排除在发布包之外。
