# repository.py.tpl


# AUTO GENERATED

from src.application.ports.provider_review_repository_port import (
    ProviderReviewRepositoryPort,
)

from src.domain.entities.provider_review_entities import (
    ProviderReview,
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

from src.infrastructure.persistence.google_sheets.mappers import (
    ProviderReviewRowMapper,
)


from src.infrastructure.persistence.google_sheets.schemas import (
    ProviderReviewColumns,
)


class GoogleSheetsProviderReviewRepository(
    GoogleSheetsRepository,
    ProviderReviewRepositoryPort,
):

    TABLE_NAME = "provider_review"
    ID_COLUMN = ProviderReviewColumns.PATIENT_ID


    def __init__(
        self,
        *,
        query_service: GoogleSheetsQueryService,
        catalog: GoogleSheetCatalog,
        mapper: ProviderReviewRowMapper,
    ) -> None:

        super().__init__(
            query_service=query_service,
            catalog=catalog,
        )

        self._mapper = mapper

    def list_provider_reviews(self) -> tuple[ProviderReview, ...]:

        return tuple(
            self._mapper.from_raw(row)
            for row in self._read_rows()
        )


    def get_by_id(
            self,
            patient_id: str,
    ) -> ProviderReview:
        raw_row = self._find_single_row(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=patient_id,
        )

        return self._mapper.from_raw(raw_row)
