#!/usr/bin/env node

export function getEnv(name, required = true, fallback = "") {
  const v = process.env[name] ?? fallback;
  if (required && !v) {
    throw new Error(`Missing env: ${name}`);
  }
  return v;
}

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

function buildQuery(params) {
  const usp = new URLSearchParams();
  for (const [k, v] of Object.entries(params)) {
    if (v === undefined || v === null || v === "") continue;
    usp.set(k, String(v));
  }
  return usp.toString();
}

export async function callApi(path, params = {}) {
  const apiKey = getEnv("SOCIALECHO_API_KEY");
  const baseUrl = getEnv("SOCIALECHO_BASE_URL", false, "https://api.socialecho.net");
  const teamId = getEnv("SOCIALECHO_TEAM_ID", false, "");
  const lang = getEnv("SOCIALECHO_LANG", false, "zh_CN");

  const qs = buildQuery(params);
  const url = `${baseUrl}${path}${qs ? `?${qs}` : ""}`;

  const headers = {
    Authorization: `Bearer ${apiKey}`,
    "X-Lang": lang
  };
  if (teamId) headers["X-Team-Id"] = teamId;

  const resp = await fetch(url, { method: "GET", headers });
  const status = resp.status;
  let body;
  try {
    body = await resp.json();
  } catch {
    body = { parse_error: true };
  }

  const ok = status === 200 && body?.code === 200;
  return { ok, status, body, url };
}

export function parseCsvIds(raw) {
  if (!raw) return "";
  return String(raw)
    .split(",")
    .map((x) => x.trim())
    .filter(Boolean)
    .join(",");
}

export function printAndExit(result) {
  console.log(JSON.stringify(result, null, 2));
  if (!result.ok) process.exit(1);
}

