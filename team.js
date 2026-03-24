#!/usr/bin/env node
import { callApi, printAndExit } from "./client.js";

const result = await callApi("/v1/team", {});
printAndExit(result);

