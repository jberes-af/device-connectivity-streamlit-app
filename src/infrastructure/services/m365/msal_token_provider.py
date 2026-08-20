# src/infrastructure/m365/msal_token_provider.py

from dataclasses import dataclass, field

from docs.m365_email_ports import AccessTokenProviderPort

import msal


class TokenProviderError(RuntimeError):
    """Raised when an access token cannot be acquired."""


@dataclass(frozen=True)
class MsalClientSecretTokenProvider(AccessTokenProviderPort):
    tenant_id: str
    client_id: str
    client_secret: str

    _app: msal.ConfidentialClientApplication | None = field(
        default=None,
        init=False,
        repr=False,
        compare=False,
    )

    _GRAPH_SCOPE = "https://graph.microsoft.com/.default"

    def get_access_token(self) -> str:
        app = self._get_app()

        result = app.acquire_token_for_client(
            scopes=[self._GRAPH_SCOPE],
            # scopes=["https://graph.microsoft.com/.default"]
        )

        token = result.get("access_token")
        if token:
            return str(token)

        error = str(result.get("error") or "unknown_error")
        desc = str(result.get("error_description") or "").strip()
        correlation_id = str(result.get("correlation_id") or "").strip()

        msg = f"Token acquisition failed: {error}"
        if desc:
            msg += f" | {desc}"
        if correlation_id:
            msg += f" | correlation_id={correlation_id}"

        raise TokenProviderError(msg)

    # temporary backward-compatible alias
    def get_token(self) -> str:
        return self.get_access_token()

    def _get_app(self) -> msal.ConfidentialClientApplication:
        if self._app is None:
            tenant_id = self.tenant_id.strip()
            client_id = self.client_id.strip()
            client_secret = self.client_secret.strip()

            if not tenant_id:
                raise TokenProviderError("M365 tenant_id is empty")
            if not client_id:
                raise TokenProviderError("M365 client_id is empty")
            if not client_secret:
                raise TokenProviderError("M365 client_secret is empty")

            authority = f"https://login.microsoftonline.com/{tenant_id}"

            app = msal.ConfidentialClientApplication(
                client_id=client_id,
                client_credential=client_secret,
                authority=authority,
            )
            object.__setattr__(self, "_app", app)

        assert self._app is not None
        return self._app
