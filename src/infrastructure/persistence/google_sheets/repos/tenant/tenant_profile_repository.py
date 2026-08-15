# /src/infrastructure/persistence/google_sheets/repos/tenant/tenant_profile_repository.py


from src.application.ports.tenant_repo_ports import (
    TenantProfileRepositoryPort,
)

from src.domain.entities.person.tenant_entities import (
    TenantProfile,
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

from src.infrastructure.persistence.google_sheets.mappers.tenant.tenant_profile_row_mapper import (
    TenantProfileRowMapper,
)

from src.infrastructure.persistence.google_sheets.schemas.tenant.tenant_profile_columns import (
    TenantProfileColumns,
)


class GoogleSheetsTenantProfileRepository(
    GoogleSheetsRepository,
    TenantProfileRepositoryPort,
):
    TABLE_NAME = "tenant_profile"
    ID_COLUMN = TenantProfileColumns.TENANT_ID

    def __init__(
            self,
            *,
            query_service: GoogleSheetsQueryService,
            catalog: GoogleSheetCatalog,
            mapper: TenantProfileRowMapper,
    ) -> None:
        super().__init__(
            query_service=query_service,
            catalog=catalog,
        )

        self._mapper = mapper

    def list_tenant_profiles(self) -> tuple[TenantProfile, ...]:
        return tuple(
            self._mapper.to_domain(row)
            for row in self._read_rows()
        )

    def get_by_id(
            self,
            tenant_id: str,
    ) -> TenantProfile:
        raw_row = self._find_single_row(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=tenant_id,
        )

        return self._mapper.to_domain(raw_row)

    def append_open_event(
            self,
            event: TenantProfile,
    ) -> None:
        raw_row: RawRow = self._mapper.to_row(event)

        self._append_raw_row(
            row=raw_row,
            columns=TenantProfileColumns.ORDER,
        )
