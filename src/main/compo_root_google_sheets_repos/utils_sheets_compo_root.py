# utils_sheets_compo_root
from googleapiclient.discovery import build

from src.infrastructure.auth.google_sheets.google_api_scopes import SHEETS_SCOPES_READ_WRITE
from src.infrastructure.auth.google_sheets.service_account_credentials_provider import \
    GoogleServiceAccountCredentialsProvider
from src.infrastructure.config.app_config_models import AppRuntimeConfig
from src.infrastructure.config.settings_model import Settings
from src.infrastructure.persistence.google_sheets.google_sheet_catalog import GoogleSheetCatalog, GoogleSheetLocator
from src.infrastructure.persistence.google_sheets.sheets_query_service import GoogleSheetsQueryService


def build_google_sheets_query_service(
        *,
        settings: Settings,
) -> GoogleSheetsQueryService:
    credentials_provider = (
        GoogleServiceAccountCredentialsProvider(
            service_account_info=(
                settings.google_service_account
            ),
            scopes=SHEETS_SCOPES_READ_WRITE,
        )
    )

    credentials = credentials_provider.load()

    sheets_service = build(
        "sheets",
        "v4",
        credentials=credentials,
        cache_discovery=False,
    )

    return GoogleSheetsQueryService(
        sheets_service=sheets_service,
    )


def build_google_sheet_catalog(
        *,
        settings: Settings,
        app_config: AppRuntimeConfig,
) -> GoogleSheetCatalog:
    tables: dict[str, GoogleSheetLocator] = {}

    for table_name, table in app_config.google_sheets.tables.items():
        spreadsheet_id = settings.spreadsheet_ids_by_file[
            table.file_name
        ]

        tables[table_name] = GoogleSheetLocator(
            spreadsheet_id=spreadsheet_id,
            worksheet_name=table.worksheet_name,
            worksheet_range=table.worksheet_range,
        )

    return GoogleSheetCatalog(
        _tables=tables,
    )
