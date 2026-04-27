#!/usr/bin/env node

export function parseArgs(argv) {
  const args = {};
  for (let i = 2; i < argv.length; i += 1) {
    const token = argv[i];
    if (!token.startsWith("--")) continue;
    const key = token.slice(2);
    const next = argv[i + 1];
    if (!next || next.startsWith("--")) {
      args[key] = true;
      continue;
    }
    args[key] = next;
    i += 1;
  }
  return args;
}

export function getOption(args, name, required = true, fallback = "") {
  const v = args[name] ?? fallback;
  if (required && !v) {
    throw new Error(`Missing option: --${name}`);
  }
  return v;
}

export function buildRequestOptions(args) {
  return {
    apiKey: getOption(args, "api-key"),
    baseUrl: getOption(args, "base-url", false, "https://api.socialecho.net"),
    teamId: getOption(args, "team-id", false, ""),
    lang: getOption(args, "lang", false, "zh_CN")
  };
}

/**
 * SocialEcho 外部 API：多数为 GET，业务参数放在 JSON body（非 QueryString）。
 * @param {string} path 如 `/v1/team`
 * @param {Record<string, unknown>} body 请求体对象；无参数时传 `{}`
 */
export async function callApi(path, body = {}, options) {
  const { apiKey, baseUrl, teamId, lang } = options;

  const url = `${baseUrl}${path}`;

  const headers = {
    Authorization: `Bearer ${apiKey}`,
    "Content-Type": "application/json",
    "X-Lang": lang
  };
  if (teamId) headers["X-Team-Id"] = teamId;

  const resp = await fetch(url, {
    method: "GET",
    headers,
    body: JSON.stringify(body)
  });
  const status = resp.status;
  let resBody;
  try {
    resBody = await resp.json();
  } catch {
    resBody = { parse_error: true };
  }

  const ok =
    status === 200 && (resBody?.code === 200 || resBody?.code === 0);
  return { ok, status, body: resBody, url };
}

/** @deprecated 历史兼容名；新代码请用 parseAccountIdArray */
export function parseCsvIds(raw) {
  if (!raw) return "";
  return String(raw)
    .split(",")
    .map((x) => x.trim())
    .filter(Boolean)
    .join(",");
}

/** 将 `1,2,3` 转为整数数组；无输入时返回 `undefined`（可省略该字段） */
export function parseAccountIdArray(raw) {
  if (!raw) return undefined;
  const arr = String(raw)
    .split(",")
    .map((x) => x.trim())
    .filter(Boolean)
    .map((x) => Number(x))
    .filter((n) => Number.isFinite(n));
  return arr.length ? arr : undefined;
}

export function printAndExit(result) {
  console.log(JSON.stringify(result, null, 2));
  if (!result.ok) process.exit(1);
}
