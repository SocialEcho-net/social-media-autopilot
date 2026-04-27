from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools.client import request_socialecho


class ListPinterestBoardsTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        account_id = int(tool_parameters.get("account_id", 0) or 0)
        if account_id <= 0:
            raise ValueError("account_id is required and must be a positive integer")

        result = request_socialecho(
            credentials=self.runtime.credentials,
            path="/v1/pinterest/boards",
            body={"account_id": account_id},
        )
        yield self.create_json_message(result)
