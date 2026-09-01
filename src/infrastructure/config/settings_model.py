# /src/infrastructure/config/settings_model.py

from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True, slots=True)
class AppSynSettings:
    api_key: str
    endpoint: str


@dataclass(frozen=True, slots=True)
class FirebaseClientSettings:
    api_key: str
    auth_domain: str
    project_id: str
    app_id: str


@dataclass(frozen=True)
class FirebaseAdminSettings:
    database_url: str
    service_account_info: dict[str, Any]


@dataclass(frozen=True, slots=True)
class FirebaseWebSettings:
    client: FirebaseClientSettings
    database_url: str
    storage_bucket: str
    messaging_sender_id: str

"""
@dataclass(frozen=True)
class M365Settings:
    m365_tenant_id: str
    m365_client_id: str
    m365_client_secret: str
"""


@dataclass(frozen=True)
class Settings:
    project_root: Path
    config_path: Path

    google_service_account: Mapping[str, str]
    spreadsheet_ids_by_file: Mapping[str, str]

    firebase_client: FirebaseClientSettings
    firebase_web: FirebaseWebSettings
    firebase_admin: FirebaseAdminSettings

    # m365_authentication: M365Settings

    appsync: AppSynSettings
