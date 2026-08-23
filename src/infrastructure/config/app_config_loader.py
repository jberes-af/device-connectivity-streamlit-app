# /src/infrastructure/config/app_config_loader.py

from pathlib import Path
from typing import Any, Mapping

import json

from src.infrastructure.config.app_config_models import (
    AppRuntimeConfig,
    GoogleSheetsConfig,
    SheetSpec,
)


class AppConfigLoader:
    GOOGLE_SHEETS_TABLE_GROUPS = (
        "tables_access",
        "tables_billing",
        "tables_care_plan",
        "tables_diagnosis"
        "tables_patient",
        "tables_payer",
        "tables_provider",
        "tables_resident",
        "tables_rtm",
        "tables_tenant",
        "tables_treatment",
        "tables_user",
    )

    @staticmethod
    def load_from_json(
            path: Path,
            *,
            project_root: Path,
    ) -> AppRuntimeConfig:
        if not path.exists():
            raise FileNotFoundError(
                f"config.json not found: {path}"
            )

        with path.open("r", encoding="utf-8") as file:
            raw: dict[str, Any] = json.load(file)

        return AppConfigLoader.parse(
            raw,
            project_root=project_root,
        )

    @staticmethod
    def parse(
            raw: Mapping[str, Any],
            *,
            project_root: Path,
    ) -> AppRuntimeConfig:
        google_sheets = AppConfigLoader._parse_google_sheets(
            raw=raw,
        )

        return AppRuntimeConfig(
            google_sheets=google_sheets,
        )

    @staticmethod
    def _parse_google_sheets(
            raw: Mapping[str, Any],
    ) -> GoogleSheetsConfig:
        try:
            google_sheets_raw = raw["google_sheets"]
        except KeyError as exc:
            raise ValueError(
                "Missing required config key: google_sheets"
            ) from exc

        if not isinstance(google_sheets_raw, Mapping):
            raise ValueError(
                "google_sheets must be an object"
            )

        tables: dict[str, SheetSpec] = {}

        for group_name in AppConfigLoader.GOOGLE_SHEETS_TABLE_GROUPS:
            tables_raw = google_sheets_raw.get(group_name)

            if not isinstance(tables_raw, Mapping):
                raise ValueError(
                    f"google_sheets.{group_name} "
                    "must be an object"
                )

            for table_name, table_raw in tables_raw.items():

                if not isinstance(table_raw, Mapping):
                    raise ValueError(
                        f"google_sheets.{group_name}."
                        f"{table_name} must be an object"
                    )

                tables[str(table_name)] = (
                    AppConfigLoader._parse_sheet_spec(
                        group_name=group_name,
                        table_name=str(table_name),
                        raw=table_raw,
                    )
                )

        return GoogleSheetsConfig(
            tables=tables,
        )

    @staticmethod
    def _parse_sheet_spec(
            *,
            group_name: str,
            table_name: str,
            raw: Mapping[str, Any],
    ) -> SheetSpec:

        file_name = raw.get("file_name")
        worksheet_name = raw.get("worksheet_name")
        worksheet_range = raw.get("worksheet_range")

        prefix = (
            f"google_sheets.{group_name}.{table_name}"
        )

        if (
                not isinstance(file_name, str)
                or not file_name.strip()
        ):
            raise ValueError(
                f"{prefix}.file_name "
                "must be a non-empty string"
            )

        if (
                not isinstance(worksheet_name, str)
                or not worksheet_name.strip()
        ):
            raise ValueError(
                f"{prefix}.worksheet_name "
                "must be a non-empty string"
            )

        if (
                not isinstance(worksheet_range, str)
                or not worksheet_range.strip()
        ):
            raise ValueError(
                f"{prefix}.worksheet_range "
                "must be a non-empty string"
            )

        return SheetSpec(
            file_name=file_name.strip(),
            worksheet_name=worksheet_name.strip(),
            worksheet_range=worksheet_range.strip(),
        )
