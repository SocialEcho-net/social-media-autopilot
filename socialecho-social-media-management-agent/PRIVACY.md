# Privacy Policy / 隐私政策

> English (EN) — for international reviewers and Dify Marketplace.
>
> 下文 **中文** 为面向中文审核与用户的对照说明，与 EN 含义一致。

---

## EN

### What this plugin does

**SocialEcho Social Media Management Agent** is a Dify **tool plugin**. It calls the SocialEcho public HTTP API at `https://api.socialecho.net` only to perform actions the user triggers in Dify (team info, account/article/report queries, OSS presign for uploads, etc.).

### Data collected and processed

Per [Dify plugin privacy guidance](https://docs.dify.ai/en/develop-plugin/publishing/standards/privacy-protection-guidelines), this plugin may involve:

| Category | Examples in this plugin |
|----------|-------------------------|
| **Credentials** | User-provided **Team API Key** (`se_...`); optional **X-Lang** (e.g. `zh_CN`, `en`) |
| **User/tool inputs** | Page numbers, account IDs, date range, `content_type` (MIME for upload), etc. |
| **API responses** | JSON returned by SocialEcho (may include **social account handles, titles, post content snippets, or metrics** depending on the endpoint) |

**Indirect identifiers** (e.g. usernames, account titles, or content visible through the Social Echo API) may appear in API responses. They are shown only in the Dify run context and are not used by the plugin for advertising or unrelated analytics.

### Third party

- **SocialEcho (operator of `api.socialecho.net`)** receives the above data to fulfill API requests. Users should review the operator’s terms and policies on the official product site.  
- This plugin does **not** add separate advertising or analytics SDKs.

### How data is used

- To authenticate and call SocialEcho APIs on behalf of the user.  
- To return results and errors to the Dify workflow or Agent.

### Data sharing

- Data is transmitted **only** to `https://api.socialecho.net` (plus normal TLS infrastructure).  
- The plugin does not sell personal data.

### Retention

- The plugin code does not intentionally write business data to local disk.  
- Secret storage and logs follow **Dify** platform behavior.

### Security

- Treat the API key as a secret; rotate it if exposed.

### Contact

- **support@socialecho.net**  
- Source: `https://github.com/SocialEcho-net/social-media-autopilot` (subfolder `socialecho-social-media-management-agent`)

The manifest field `privacy: PRIVACY.md` points to this file, as required for Marketplace submissions.

---

## 中文

### 插件作用

本插件为 Dify **工具插件**，仅在用户于工作流/应用中使用工具时，向 `https://api.socialecho.net` 发起**用户请求**对应的 API 调用（如团队、账号/贴文/报表、获取 OSS 上传地址等）。

### 收集与处理的资料类型

- **用户配置的凭据**：**Team API Key**（`se_` 开头）；可选 **X-Lang** 响应语言。  
- **工具入参**：分页、社媒 `account_id` 列表、日期范围、上传用 `content_type`（MIME 类型）等。  
- **API 返回数据**：SocialEcho 返回的 JSON。视接口与账号授权不同，**可能含有社媒账号昵称/用户名、贴文标题或正文片段、统计指标等**；其性质可能属于**间接识别信息**（如与其他信息结合可指向特定账号或运营主体）。

本插件**不会**将上述数据用于广告投放或与本插件功能无关的画像、追踪。

### 与第三方服务的关系

- 上述业务数据在请求时由 **SocialEcho 服务端**（`api.socialecho.net` 运营方）处理。用户可查阅 SocialEcho 官网/控制台中的**用户协议与隐私条款**。  
- 本插件**未**集成独立的广告/统计类第三方 SDK。

### 使用与共享

- 数据仅通过 HTTPS 传输至 `https://api.socialecho.net`，不另售个人信息。  
- 凭据与日志的持久化方式以 **Dify 平台**对「插件凭据/运行日志」的管理为准。

### 安全与联系

- 请妥善保管 API Key，泄露时请及时轮换。  
- 联系邮箱：**support@socialecho.net**  
- 参考仓库：`https://github.com/SocialEcho-net/social-media-autopilot`

`manifest.yaml` 中 `privacy: PRIVACY.md` 已指向本说明（符合 Dify 对「隐私政策路径」的要求）。
