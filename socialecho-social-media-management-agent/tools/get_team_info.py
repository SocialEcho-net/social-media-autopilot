from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools.client import request_socialecho


class GetTeamInfoTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        result = request_socialecho(
            credentials=self.runtime.credentials,
            path="/v1/team",
            body={},
        )
        yield self.create_json_message(result)
