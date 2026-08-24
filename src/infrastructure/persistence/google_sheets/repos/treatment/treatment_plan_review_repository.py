# /src/infrastructure/persistence/google_sheets/repos/treatment/treatment_plan_review.py

from typing import Sequence

from src.application.ports.treatment_repo_ports import (
    TreatmentPlanReviewRepositoryPort,
)

from src.domain.entities.care.treatment_entities import (
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

from src.infrastructure.persistence.google_sheets.mappers.treatment.treatment_plan_review_row_mapper import (
    TreatmentPlanReviewRowMapper,
)

from src.infrastructure.persistence.google_sheets.schemas.treatment.treatment_plan_review_columns import (
    TreatmentPlanReviewColumns,
)


class GoogleSheetsTreatmentPlanReviewRepository(
    GoogleSheetsRepository,
    TreatmentPlanReviewRepositoryPort,
):
    TABLE_NAME = "treatment_plan_review"
    ID_COLUMN = TreatmentPlanReviewColumns.REVIEW_ID

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

    def list_treatment_plan_reviews(
            self,
    ) -> tuple[TreatmentPlanReview, ...]:
        return tuple(
            self._mapper.to_domain(row)
            for row in self._read_rows()
        )

    def list_for_treatment_plan_id(
            self,
            treatment_plan_id: str,
    ) -> tuple[TreatmentPlanReview, ...]:
        raw_rows: list[RawRow] = self._find_rows(
            rows=self._read_rows(),
            column_name=TreatmentPlanReviewColumns.TREATMENT_PLAN_ID,
            value=treatment_plan_id,
        )

        return tuple(
            self._mapper.to_domain(row)
            for row in raw_rows
        )

    def get_by_id(
            self,
            review_id: str,
    ) -> TreatmentPlanReview:
        raw_row: RawRow = self._find_single_row(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=review_id,
        )

        return self._mapper.to_domain(raw_row)

    def get_by_ids(
            self,
            review_ids: Sequence[str],
    ) -> tuple[TreatmentPlanReview, ...]:
        raw_rows: list[RawRow] = self._find_rows_for_multiple_values(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            values=review_ids,
        )

        return tuple(
            self._mapper.to_domain(row)
            for row in raw_rows
        )

    """
    def add(
            self,
            review: TreatmentPlanReview,
    ) -> None:
        raw_row: RawRow = self._mapper.to_row(review)

        self._append_raw_row(
            row=raw_row,
            columns=TreatmentPlanReviewColumns.ORDER,
        )
    """
