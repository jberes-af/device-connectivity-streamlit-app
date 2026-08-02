# /src/infrastructure/persistence/google_sheets/repos/provider_admin_repo.py


from src.application.ports.patient_repo_ports import (
    ProviderRepositoryPort,
)

from src.domain.entities.patient_entities import (
    Patient,
)

from src.infrastructure.persistence.google_sheets.base_repository import (
    GoogleSheetsRepository,
)

from src.infrastructure.persistence.google_sheets.google_sheet_catalog import (
    GoogleSheetCatalog,
)

from src.infrastructure.persistence.google_sheets.sheets_query_service import (
    GoogleSheetsQueryService,
)

from src.infrastructure.persistence.mappers.patient.patient_row_mapper import (
    PatientRowMapper,
)


class GoogleSheetsProviderRepository(
    GoogleSheetsRepository,
    ProviderRepositoryPort,
):

    TABLE_NAME = "provider"

    def __init__(
            self,
            *,
            query_service: GoogleSheetsQueryService,
            catalog: GoogleSheetCatalog,
            mapper: ProviderRowMapper,
    ) -> None:
        super().__init__(
            query_service=query_service,
            catalog=catalog,
        )

        self._mapper = mapper

    def list_providers(
            self,
    ) -> tuple[Provider, ...]:
        raw_rows = self._read_rows()

        return tuple(
            self._mapper.to_domain(row)
            for row in raw_rows
        )

