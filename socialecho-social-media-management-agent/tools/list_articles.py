from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools.client import parse_account_ids_csv, request_socialecho


class ListArticlesTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        page = int(tool_parameters.get("page", 1))
        account_ids = parse_account_ids_csv(
            str(tool_parameters.get("account_ids", "")).strip() or None
        )

        body: dict[str, Any] = {"page": page}
        if account_ids is not None:
            body["account_ids"] = account_ids

        result = request_socialecho(
            credentials=self.runtime.credentials,
            path="/v1/article",
            body=body,
        )
        yield self.create_json_message(result)
