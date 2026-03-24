#!/usr/bin/env node
import { callApi, parseArgs, parseCsvIds, printAndExit } from "./client.js";

const args = parseArgs(process.argv);
const page = args.page ?? 1;
const accountIds = parseCsvIds(args["account-ids"]);

const result = await callApi("/v1/article", {
  page,
  account_ids: accountIds
});

printAndExit(result);

