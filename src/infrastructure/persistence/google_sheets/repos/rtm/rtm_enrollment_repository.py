# /src/infrastructure/persistence/google_sheets/repos/treatment/rtm_enrollment_repository.py

from typing import Sequence

from src.domain.entities.care.rtm_entities import RtmEnrollment

from src.application.ports.rtm_repo_ports import RtmEnrollmentRepositoryPort

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

from src.infrastructure.persistence.google_sheets.mappers.rtm.rtm_enrollment_row_mapper import (
    RtmEnrollmentRowMapper,
)

from src.infrastructure.persistence.google_sheets.schemas.rtm.rtm_enrollment_columns import (
    RtmEnrollmentColumns,
)


class GoogleSheetsRtmEnrollmentRepository(
    GoogleSheetsRepository,
    RtmEnrollmentRepositoryPort,
):
    TABLE_NAME = "rtm_enrollment"
    ID_COLUMN = RtmEnrollmentColumns.ENROLLMENT_ID

    def __init__(
            self,
            *,
            query_service: GoogleSheetsQueryService,
            catalog: GoogleSheetCatalog,
            mapper: RtmEnrollmentRowMapper,
    ) -> None:
        super().__init__(
            query_service=query_service,
            catalog=catalog,
        )

        self._mapper = mapper

    def list_rtm_enrollments(self) -> tuple[RtmEnrollment, ...]:
        return tuple(
            self._mapper.to_domain(row)
            for row in self._read_rows()
        )

    def get_by_id(
            self,
            rtm_enrollment_id: str,
    ) -> RtmEnrollment:
        raw_row = self._find_single_row(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=rtm_enrollment_id,
        )

        return self._mapper.to_domain(raw_row)

    def get_by_ids(
            self,
            rtm_enrollment_ids: Sequence[str],
    ) -> tuple[RtmEnrollment, ...]:
        raw_rows: list[RawRow] = self._find_rows_for_multiple_values(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            values=rtm_enrollment_ids,
        )

        return tuple(
            self._mapper.to_domain(row)
            for row in raw_rows
        )

    def list_rtm_enrollment_patient_id(
            self,
            patient_id: str,
    ) -> tuple[RtmEnrollment, ...]:
        raw_rows: list[RawRow] = self._find_rows(
            rows=self._read_rows(),
            column_name=RtmEnrollmentColumns.PATIENT_ID,
            value=patient_id,
        )

        return tuple(
            self._mapper.to_domain(row)
            for row in raw_rows
        )
