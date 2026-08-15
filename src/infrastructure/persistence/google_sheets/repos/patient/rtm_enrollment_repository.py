# /src/infrastructure/persistence/google_sheets/repos/patient/rtm_enrollment_repository.py


from src.application.ports.patient_repo_ports import (
    RTMEnrollmentRepositoryPort,
)

from src.domain.entities.person.patient_entities import (
    RTMEnrollment,
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

from src.infrastructure.persistence.google_sheets.mappers.patient.rtm_enrollment_row_mapper import (
    RTMEnrollmentRowMapper,
)


from src.infrastructure.persistence.google_sheets.schemas.patient.rtm_enrollment_columns import (
    RTMEnrollmentColumns,
)


class GoogleSheetsRTMEnrollmentRepository(
    GoogleSheetsRepository,
    RTMEnrollmentRepositoryPort,
):

    TABLE_NAME = "rtm_enrollment"
    ID_COLUMN = RTMEnrollmentColumns.PATIENT_ID


    def __init__(
        self,
        *,
        query_service: GoogleSheetsQueryService,
        catalog: GoogleSheetCatalog,
        mapper: RTMEnrollmentRowMapper,
    ) -> None:

        super().__init__(
            query_service=query_service,
            catalog=catalog,
        )

        self._mapper = mapper

    def list_rtm_enrollments(self) -> tuple[RTMEnrollment, ...]:

        return tuple(
            self._mapper.to_domain(row)
            for row in self._read_rows()
        )


    def get_by_id(
            self,
            patient_id: str,
    ) -> RTMEnrollment:
        raw_row = self._find_single_row(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=patient_id,
        )

        return self._mapper.to_domain(raw_row)
