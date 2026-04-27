from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools.client import parse_account_ids_csv, request_socialecho


class GetReportTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        start_date = str(tool_parameters.get("start_date", "")).strip()
        end_date = str(tool_parameters.get("end_date", "")).strip()
        if not start_date or not end_date:
            raise ValueError("start_date and end_date are required, format: YYYY-MM-DD")

        account_ids = parse_account_ids_csv(
            str(tool_parameters.get("account_ids", "")).strip() or None
        )

        body: dict[str, Any] = {
            "start_date": start_date,
            "end_date": end_date,
            "time_type": int(tool_parameters.get("time_type", 1)),
            "group": str(tool_parameters.get("group", "")).strip(),
        }
        if account_ids is not None:
            body["account_ids"] = account_ids

        result = request_socialecho(
            credentials=self.runtime.credentials,
            path="/v1/report",
            body=body,
        )
        yield self.create_json_message(result)
