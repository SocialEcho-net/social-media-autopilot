## SocialEcho Social Media Management Agent（Dify 工具插件）

**作者：** socialecho-net  
**当前版本（manifest）：** 0.1.3  
**类型：** Tool Plugin

面向 **Dify** 工作流与 Agent 的 **SocialEcho 开放 API** 工具集，请求发往生产环境 `https://api.socialecho.net`，行为与仓库内 `socialEchoApidocs_cn.md` / OpenAPI 一致。

### 工具列表

1. `get_team_info` — `GET /v1/team`  
2. `list_accounts` — `GET /v1/account`  
3. `list_articles` — `GET /v1/article`（`account_ids` 为逗号字符串，在 JSON body 中转为**整数数组**）  
4. `get_report` — `GET /v1/report`（同上）  
5. `get_upload_url` — `GET /v1/upload/url`（**必填** `content_type` MIME，白名单见工具说明与 OpenAPI 文档）

### 凭据

- `api_key`：SocialEcho 控制台 **团队 API Key**（`se_` 开头）  
- `x_lang`：可选，如 `zh_CN`、`en`  

### 请求形态

与线上一致：多数为 **GET + `application/json` 请求体**，**不是**用 Query 传参。

### 成功判定

HTTP `200` 且 JSON `code` 为 `0` 或 `200`。

### 向 Dify Marketplace 发布

维护与 PR 提交流程见同目录 **[`MARKETPLACE.md`](./MARKETPLACE.md)**（对应[官方指南](https://docs.dify.ai/zh/develop-plugin/publishing/marketplace-listing/release-to-dify-marketplace)）。

**隐私政策：** [`PRIVACY.md`](./PRIVACY.md)（`manifest` 中 `privacy` 已指向本文件。）

### 开发调试

```bash
pip install -r requirements.txt
python -m main
```

### 打 `.difypkg` 包

在插件**上一级**目录执行：

```bash
dify plugin package ./socialecho-social-media-management-agent
```

生成物用于：本地上传安装、或向 [`langgenius/dify-plugins`](https://github.com/langgenius/dify-plugins) 提 PR 以**上架 Marketplace**。

> **ClawHub** 上的 [socialecho-skills 技能包](https://clawhub.ai) 是另一套交付形态（非 `.difypkg`），不要与 Dify 插件包混淆。
