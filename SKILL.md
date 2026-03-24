---
name: socialecho-openapi
description: Query SocialEcho external APIs (team, account list, article list, report) using API key from Team Management. Use for integration checks, data pulls, and API diagnostics.
---

# SocialEcho OpenAPI Skill

Use this skill to call SocialEcho external APIs with a team API key.

## Prerequisites

1. Sign up / sign in at `https://app.socialecho.net/`.
2. Create a team.
3. In Team Management, create an API key.
4. Export env vars:

```bash
export SOCIALECHO_API_KEY="your_api_key"
export SOCIALECHO_BASE_URL="https://api.socialecho.net"
export SOCIALECHO_TEAM_ID="optional_team_id"
export SOCIALECHO_LANG="zh_CN"
```

`SOCIALECHO_TEAM_ID` is optional for most calls but can be required by report queries depending on server rules.

## Setup

```bash
cd socialecho-openapi-skill
npm ci
```

## Commands

```bash
./team.js
./account.js --page 1 --type 1
./article.js --page 1 --account-ids 41,42
./report.js --start-date 2026-01-01 --end-date 2026-03-24 --time-type 1 --group day --account-ids 41,42
```

## Notes

- Success is defined as: HTTP 200 and response JSON `code == 200`.
- Scripts print response body and exit with non-zero status on failure.
- Use `SOCIALECHO_BASE_URL=https://api-dev.socialecho.net` for dev environment.

