from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools.client import request_socialecho

# Same allowlist as socialEchoApidocs_cn.md §5.5 (GET /v1/upload/url — content_type)
CONTENT_TYPE_ENUM = frozenset(
    {
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
        "video/quicktime",
    }
)


class GetUploadUrlTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        content_type = str(tool_parameters.get("content_type", "")).strip()
        if not content_type:
            raise ValueError("content_type is required (MIME type of the file to upload).")
        if content_type not in CONTENT_TYPE_ENUM:
            raise ValueError(
                "content_type must be one of the allowed MIME values; see tool description."
            )

        result = request_socialecho(
            credentials=self.runtime.credentials,
            path="/v1/upload/url",
            body={"content_type": content_type},
        )
        yield self.create_json_message(result)
