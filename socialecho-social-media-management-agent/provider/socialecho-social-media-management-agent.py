from typing import Any

from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError

from tools.client import request_socialecho


class SocialechoSocialMediaManagementAgentProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        try:
            api_key = (credentials.get("api_key") or "").strip()

            if not api_key:
                raise ValueError("api_key is required")

            # Validate by calling the lightweight team endpoint.
            request_socialecho(credentials=credentials, path="/v1/team", body={})
        except Exception as e:
            raise ToolProviderCredentialValidationError(str(e)) from e
