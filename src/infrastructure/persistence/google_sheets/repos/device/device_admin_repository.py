# /src/infrastructure/persistence/google_sheets/repos/device/device_admin_repository.py

from typing import Sequence

from src.application.ports.sensing.device_ports import (
    DeviceAdministrationRepositoryPort,
)

from src.domain.entities.sensing.device_entities import (
    DeviceAdministrationProfile,
)

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.google_sheets.base_repository import (
    GoogleSheetsRepository,
)

from src.infrastructure.persistence.google_sheets.google_sheet_catalog import (
    GoogleSheetCatalog,
)

from src.infrastructure.persistence.google_sheets.sheets_query_service import (
    GoogleSheetsQueryService,
)

from src.infrastructure.persistence.google_sheets.mappers.device.device_profile_row_mapper import (
    DeviceAdministrationProfileRowMapper,
)

from src.infrastructure.persistence.google_sheets.schemas.device.device_profile_columns import (
    DeviceAdministrationProfileColumns,
)


class GoogleSheetsDeviceAdministrationProfileRepository(
    GoogleSheetsRepository,
    DeviceAdministrationRepositoryPort,
):
    TABLE_NAME = "device_admin_profile"
    ID_COLUMN = DeviceAdministrationProfileColumns.DEVICE_ID

    def __init__(
            self,
            *,
            query_service: GoogleSheetsQueryService,
            catalog: GoogleSheetCatalog,
            mapper: DeviceAdministrationProfileRowMapper,
    ) -> None:
        super().__init__(
            query_service=query_service,
            catalog=catalog,
        )

        self._mapper = mapper

    def list_device_admin_profiles(self) -> tuple[DeviceAdministrationProfile, ...]:
        return tuple(
            self._mapper.to_domain(row)
            for row in self._read_rows()
        )

    def get_by_id(
            self,
            device_id: str,
    ) -> DeviceAdministrationProfile:
        raw_row: RawRow = self._find_single_row(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=device_id,
        )

        return self._mapper.to_domain(raw_row)

    def get_by_ids(
            self,
            device_ids: Sequence[str],
    ) -> tuple[DeviceAdministrationProfile, ...]:
        raw_rows: list[RawRow] = self._find_rows_for_multiple_values(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            values=device_ids,
        )

        return tuple(
            self._mapper.to_domain(row)
            for row in raw_rows
        )

    def list_devices_for_tenant_id(
            self,
            tenant_id: str,
    ) -> tuple[DeviceAdministrationProfile, ...]:
        raw_rows: list[RawRow] = self._find_rows(
            rows=self._read_rows(),
            column_name=DeviceAdministrationProfileColumns.TENANT_ID,
            value=tenant_id,
        )

        return tuple(
            self._mapper.to_domain(row)
            for row in raw_rows
        )

    def list_devices_for_tenant_ids(
            self,
            tenant_ids: tuple[str, ...],
    ) -> tuple[DeviceAdministrationProfile, ...]:
        raw_rows: list[RawRow] = self._find_rows_for_multiple_values(
            rows=self._read_rows(),
            column_name=DeviceAdministrationProfileColumns.TENANT_ID,
            values=tenant_ids,
        )

        return tuple(
            self._mapper.to_domain(row)
            for row in raw_rows
        )
