# /src/infrastructure/config/settings_loader.py

from pathlib import Path
from typing import Any

from src.infrastructure.config.aws_settings_loader import load_appsync_settings
from src.infrastructure.config.firebase_settings_loader import (
    load_firebase_admin_settings,
    load_firebase_client_settings,
    load_firebase_web_settings,
)

from src.infrastructure.config.google_settings_loader import (
    load_google_service_account_key,
    load_spreadsheet_ids,
)

# from src.infrastructure.config.m365_settings_loader import (load_microsoft365_settings,)

from src.infrastructure.config.path_settings_loader import (
    resolve_config_path,
)

from src.infrastructure.config.secret_provider import SecretProvider

from src.infrastructure.config.settings_model import (
    FirebaseAdminSettings,
    FirebaseClientSettings,
    FirebaseWebSettings,
    Settings, AppSynSettings,
    # M365Settings,
)


def load_settings(
        *,
        project_root: Path,
        secret_provider: SecretProvider,
) -> Settings:
    project_root = project_root.resolve()

    config_path = resolve_config_path(project_root)

    google_service_account: dict[str, Any] = load_google_service_account_key(secret_provider)

    spreadsheet_ids_by_file: dict[str, str] = load_spreadsheet_ids(secret_provider)

    firebase_admin: FirebaseAdminSettings = load_firebase_admin_settings(
        secret_provider=secret_provider)

    firebase_client: FirebaseClientSettings = load_firebase_client_settings(
        secret_provider=secret_provider)

    firebase_web: FirebaseWebSettings = load_firebase_web_settings(
        secret_provider=secret_provider,
        client=firebase_client,
    )

    appsync: AppSynSettings = load_appsync_settings(
        secret_provider=secret_provider)

    # m365_auth: M365Settings = load_microsoft365_settings(secret_provider)

    return Settings(
        project_root=project_root,
        config_path=config_path,

        google_service_account=google_service_account,
        spreadsheet_ids_by_file=spreadsheet_ids_by_file,

        firebase_client=firebase_client,
        firebase_web=firebase_web,
        firebase_admin=firebase_admin,

        # m365_authentication=m365_auth,

        appsync=appsync,
    )
