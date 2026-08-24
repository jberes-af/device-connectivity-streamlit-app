# /src/interface_adapters/presenters/person/resident_searchable_table_presenter.py

from src.application.use_cases.resident.resident_uc_dtos import (
    ResidentSearchableRecordDTO,
)

from src.interface_adapters.view_models.common.table_view_model import (
    TableCellViewModel,
    TableRowViewModel,
    TableViewModel,
)


class ResidentRecordsSearchableTablePresenter:
    def present(
            self,
            records: tuple[ResidentSearchableRecordDTO, ...],
    ) -> TableViewModel:
        rows = tuple(
            self._to_row(record)
            for record in records
        )

        return TableViewModel(
            title="User-accessible Resident Records",
            row_label_header="Resident ID",
            column_headers=(
                "Name",
                "Date of Birth",
                "Primary Contact Name",
                "Active Status",
            ),
            rows=rows,
        )

    @staticmethod
    def _to_row(
            record: ResidentSearchableRecordDTO,
    ) -> TableRowViewModel:
        return TableRowViewModel(
            row_key=record.resident_id,
            label=record.resident_id,
            cells=(
                TableCellViewModel(
                    value=record.full_name,
                ),
                TableCellViewModel(
                    value=record.date_of_birth.isoformat(),
                ),
                TableCellViewModel(
                    value=record.contact_name or "",
                ),
                TableCellViewModel(
                    value=(
                        "Active"
                        if record.active_status
                        else "Inactive"
                    ),
                ),
            ),
        )
