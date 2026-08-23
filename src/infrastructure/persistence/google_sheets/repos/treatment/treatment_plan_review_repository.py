# /src/infrastructure/persistence/google_sheets/repos/TreatmentPlanReview.py


# AUTO GENERATED

from src.application.ports.treatment_plan_review_repository_port import (
    TreatmentPlanReviewRepositoryPort,
)

from src.domain.entities.treatment_plan_review_entities import (
    TreatmentPlanReview,
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

from src.infrastructure.persistence.mappers.treatment_plan_review.treatment_plan_review_row_mapper import (
    TreatmentPlanReviewRowMapper,
)


from src.infrastructure.persistence.schemas.treatment_plan_review.treatment_plan_review_columns import (
    TreatmentPlanReviewColumns,
)


class GoogleSheetsTreatmentPlanReviewRepository(
    GoogleSheetsRepository,
    TreatmentPlanReviewRepositoryPort,
):

    TABLE_NAME = "treatment_plan_review"
    ID_COLUMN = TreatmentPlanReviewColumns.ENTITY_ID


    def __init__(
        self,
        *,
        query_service: GoogleSheetsQueryService,
        catalog: GoogleSheetCatalog,
        mapper: TreatmentPlanReviewRowMapper,
    ) -> None:

        super().__init__(
            query_service=query_service,
            catalog=catalog,
        )

        self._mapper = mapper

    def list_treatment_plan_reviews(self) -> tuple[TreatmentPlanReview, ...]:

        return tuple(
            self._mapper.to_domain(row)
            for row in self._read_rows()
        )


    def get_by_id(
            self,
            patient_id: str,
    ) -> TreatmentPlanReview:
        raw_row = self._find_single_row(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=patient_id,
        )

        return self._mapper.to_domain(raw_row)

    def append_open_event(
            self,
            event: TreatmentPlanReview,
    ) -> None:
        raw_row: RawRow = self._mapper.to_row(event)

        self._append_raw_row(
            row=raw_row,
            columns=TreatmentPlanReviewColumns.ORDER,
        )
