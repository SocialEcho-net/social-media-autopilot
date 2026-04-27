## SocialEcho Social Media Management Agent (Dify Plugin)

**Author:** socialecho-net  
**Version:** 0.1.2  
**Type:** Tool Plugin  
**ClawHub:** [socialecho-net/socialecho-social-media-management-agent](https://clawhub.ai/socialecho-net/socialecho-social-media-management-agent)

This plugin integrates the SocialEcho external API (`https://api.socialecho.net`). Logic aligns with the repo’s `socialEchoApidocs_cn.md` / OpenAPI v1.1.x.

### Tools

1. `get_team_info` — `GET /v1/team`
2. `list_accounts` — `GET /v1/account`
3. `list_articles` — `GET /v1/article` (optional `account_ids`: CSV → integer array in JSON body)
4. `get_report` — `GET /v1/report` (optional `account_ids`: CSV → integer array in JSON body)
5. `get_upload_url` — `GET /v1/upload/url` (**required** `content_type` MIME from the documented image/video allowlist)

### Credentials

- `api_key` (required): Team API Key from SocialEcho Team Management (`se_xxx`)
- `x_lang` (optional): `zh_CN` or `en`

Production base URL: `https://api.socialecho.net`.

### Request shape (important)

Most routes use **GET with a JSON body** (`Content-Type: application/json`), **not** query parameters. This plugin sends bodies accordingly.

### Success criteria

- HTTP **200**
- JSON `code` is **0** or **200**

Otherwise the tool raises so workflows can branch on errors.

### Development

```bash
pip install -r requirements.txt
python -m main
```

### Package

```bash
dify plugin package ./socialecho-social-media-management-agent
```

Produces a `.difypkg` for Dify / ClawHub upload.
