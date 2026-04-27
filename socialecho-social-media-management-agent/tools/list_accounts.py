from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools.client import request_socialecho


class ListAccountsTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        page = int(tool_parameters.get("page", 1))
        account_type = int(tool_parameters.get("type", 1))

        result = request_socialecho(
            credentials=self.runtime.credentials,
            path="/v1/account",
            body={
                "page": page,
                "type": account_type,
            },
        )
        yield self.create_json_message(result)
