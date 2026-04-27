#!/usr/bin/env node
import { buildRequestOptions, callApi, parseArgs, printAndExit } from "./client.js";

/** 与 `socialEchoApidocs_cn.md` 中 `GET /v1/upload/url` 的 `content_type` 枚举一致 */
export const CONTENT_TYPE_ENUM = [
  "image/jpeg",
  "image/jpg",
  "image/png",
  "image/gif",
  "image/webp",
  "image/bmp",
  "video/mp4",
  "video/avi",
  "video/mov",
  "video/wmv",
  "video/flv",
  "video/webm",
  "video/mkv",
  "video/3gp",
  "video/quicktime"
];

const args = parseArgs(process.argv);

const contentType = String(
  args["content-type"] || args.content_type || ""
).trim();
if (!contentType) {
  console.error(
    "Usage: ./upload.js --api-key <key> --content-type <mime> [--base-url ...] [--lang zh_CN]\n" +
      "mime must be one of: " +
      CONTENT_TYPE_ENUM.join(", ")
  );
  process.exit(2);
}

if (!CONTENT_TYPE_ENUM.includes(contentType)) {
  console.error("Invalid --content-type. Allowed:\n" + CONTENT_TYPE_ENUM.join("\n"));
  process.exit(2);
}

const options = buildRequestOptions(args);

const result = await callApi(
  "/v1/upload/url",
  { content_type: contentType },
  options
);
printAndExit(result);
