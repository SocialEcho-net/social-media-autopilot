## SocialEcho Social Media Management Agent（Dify 工具插件）

**作者：** socialecho-net  
**当前版本（manifest）：** 0.1.4  
**类型：** Tool Plugin

与 `socialEchoApidocs_cn.md` 中 **§5 接口清单** 对齐，覆盖当前对外 **GET + JSON body** 与 **发布 POST** 能力。

### 工具与接口

| 工具 | 方法 | 路径 |
|------|------|------|
| 获取团队信息 | GET | `/v1/team` |
| 账号列表 | GET | `/v1/account` |
| 贴文列表 | GET | `/v1/article` |
| 数据报表 | GET | `/v1/report` |
| 获取 OSS 上传地址 | GET | `/v1/upload/url`（`content_type` 必填，见工具说明） |
| Reddit 社区列表 | GET | `/v1/reddit/communities`（`account_id`） |
| Pinterest 图版列表 | GET | `/v1/pinterest/boards`（`account_id`） |
| 发布贴文 | **POST** | `/v1/publish/article`（`body_json` 为完整 JSON 对象字符串） |

### 凭据

- `api_key`：团队 API Key（`se_` 开头）  
- `x_lang`：可选 `zh_CN` / `en`  

### 成功判定

HTTP `200` 且 JSON `code` 为 `0` 或 `200`。

### Marketplace 与隐私

- 上架与 PR 流程见 **[`MARKETPLACE.md`](./MARKETPLACE.md)**。  
- 隐私说明见 **[`PRIVACY.md`](./PRIVACY.md)**（`manifest` 中 `privacy` 已引用）。

### 开发

```bash
pip install -r requirements.txt
python -m main
```

### 打 `.difypkg` 包

在插件**上一级**目录执行：

```bash
dify plugin package ./socialecho-social-media-management-agent
```

在**当前工作目录**生成 `socialecho-social-media-management-agent` 对应的 **`.difypkg`**，用于 [dify-plugins](https://github.com/langgenius/dify-plugins) PR 或本地上传安装。

> **ClawHub** 的 Node 技能包在仓库 `socialecho-skills` 目录，与 `.difypkg` 无关。
