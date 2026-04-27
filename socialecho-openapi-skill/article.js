#!/usr/bin/env node
import {
  buildRequestOptions,
  callApi,
  parseArgs,
  parseAccountIdArray,
  printAndExit
} from "./client.js";

const args = parseArgs(process.argv);
const options = buildRequestOptions(args);
const page = Number(args.page ?? 1);
const accountIds = parseAccountIdArray(args["account-ids"]);

const body = { page };
if (accountIds !== undefined) body.account_ids = accountIds;

const result = await callApi("/v1/article", body, options);

printAndExit(result);
