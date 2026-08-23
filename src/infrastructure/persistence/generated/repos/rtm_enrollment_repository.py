# /src/infrastructure/persistence/google_sheets/repos/RtmEnrollment.py


# AUTO GENERATED

from src.application.ports.rtm_enrollment_repository_port import (
    RtmEnrollmentRepositoryPort,
)

from src.domain.entities.rtm_enrollment_entities import (
    RtmEnrollment,
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

from src.infrastructure.persistence.mappers.rtm_enrollment.rtm_enrollment_row_mapper import (
    RtmEnrollmentRowMapper,
)


from src.infrastructure.persistence.schemas.rtm_enrollment.rtm_enrollment_columns import (
    RtmEnrollmentColumns,
)


class GoogleSheetsRtmEnrollmentRepository(
    GoogleSheetsRepository,
    RtmEnrollmentRepositoryPort,
):

    TABLE_NAME = "rtm_enrollment"
    ID_COLUMN = RtmEnrollmentColumns.ENTITY_ID


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
            patient_id: str,
    ) -> RtmEnrollment:
        raw_row = self._find_single_row(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=patient_id,
        )

        return self._mapper.to_domain(raw_row)

    def append_open_event(
            self,
            event: RtmEnrollment,
    ) -> None:
        raw_row: RawRow = self._mapper.to_row(event)

        self._append_raw_row(
            row=raw_row,
            columns=RtmEnrollmentColumns.ORDER,
        )
