# /src/infrastructure/persistence/google_sheets/repos/patient_admin_repo.py


from src.application.ports.patient_repo_ports import (
    PatientRepositoryPort,
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

from src.infrastructure.persistence.schemas.patient.patient_columns import (
    PatientColumns,
)


class GoogleSheetsPatientRepository(
    GoogleSheetsRepository,
    PatientRepositoryPort,
):
    TABLE_NAME = "patient"

    ID_COLUMN = PatientColumns.PATIENT_ID

    def __init__(
            self,
            *,
            query_service: GoogleSheetsQueryService,
            catalog: GoogleSheetCatalog,
            mapper: PatientRowMapper,
    ) -> None:
        super().__init__(
            query_service=query_service,
            catalog=catalog,
        )

        self._mapper = mapper

    def list_patients(self) -> tuple[Patient, ...]:
        return tuple(
            self._mapper.to_domain(row)
            for row in self._read_rows()
        )

    def get_by_id(
            self,
            patient_id: str,
    ) -> Patient:
        raw_row = self._find_single_row(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=patient_id,
        )

        return self._mapper.to_domain(raw_row)

    """
    def add_patient(
            self,
            patient_record: PatientAdministration,
    ) -> PatientAdministration:
        table_location: tuple[str, str] = _get_table_location(
            name="patients",
            locator=self._locator,
        )
        spreadsheet_id = table_location[0]
        range_a1 = table_location[1]

        row = self._mapper.to_row(patient_record)

        self._query_service.append_values(
            spreadsheet_id=spreadsheet_id,
            range_a1=range_a1,
            values=[row],
        )

        return patient_record

    def update_patient(
            self,
            patient_record: PatientAdministration,
    ) -> PatientAdministration:
        normalized_activity_id = patient_record.patient_id.strip()

        if not normalized_activity_id:
            raise ValueError(
                "activity_id cannot be empty"
            )

        spreadsheet_id, table_range = _get_table_location(
            name="patients",
            locator=self._locator,
        )

        raw_rows = self._query_service.read_values(
            spreadsheet_id=spreadsheet_id,
            range_a1=table_range,
        )

        row_number = self._find_patient_row_number(
            rows=raw_rows,
            activity_id=normalized_activity_id,
        )

        row = self._mapper.to_row(patient_record)

        if not row:
            raise ValueError(
                "The activity mapper returned an empty row."
            )

        final_column = _column_number_to_letter(
            len(row)
        )

        worksheet_name = _worksheet_name_from_range(
            table_range
        )

        target_range = (
            f"'{worksheet_name}'!"
            f"A{row_number}:"
            f"{final_column}{row_number}"
        )

        self._query_service.update_values(
            spreadsheet_id=spreadsheet_id,
            range_a1=target_range,
            values=[row],
        )

        return patient_record

    @staticmethod
    def _find_patient_row_number(
            *,
            rows: list[RawRow],
            activity_id: str,
    ) -> int:
        normalized_activity_id = activity_id.strip()

        if not normalized_activity_id:
            raise ValueError(
                "activity_id cannot be empty"
            )

        matches: list[int] = []

        for sheet_row_number, row in enumerate(
                rows,
                start=2,
        ):
            row_activity_id = (
                row.get(
                    PatientAdminColumns.ACTIVITY_ID,
                    "",
                )
                .strip()
            )

            if row_activity_id == normalized_activity_id:
                matches.append(sheet_row_number)

        if not matches:
            raise PatientNotFoundError(
                f"Activity ID "
                f"{normalized_activity_id!r} "
                "was not found."
            )

        if len(matches) > 1:
            raise DuplicatePatientIdError(
                f"Activity ID "
                f"{normalized_activity_id!r} "
                f"appears in sheet rows {matches}."
            )

        return matches[0]
    """
