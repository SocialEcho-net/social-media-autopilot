#!/usr/bin/env node
import { callApi, parseArgs, printAndExit } from "./client.js";

const args = parseArgs(process.argv);

const page = args.page ?? 1;
const type = args.type ?? 1;

const result = await callApi("/v1/account", { page, type });
printAndExit(result);

