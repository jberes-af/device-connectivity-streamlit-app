# /src/interface_adapters/presenters/texas_facilities_presenter.py

from src.domain.entities.patient_entities import Facility
from src.interface_adapters.view_models.table_view_model import (
    TableCellViewModel,
    TableRowViewModel,
    TableViewModel,
    TexasFacilitiesTablesViewModel,
)


class TexasFacilitiesPresenter:
    def present(
            self,
            facilities: tuple[Facility, ...],
    ) -> TexasFacilitiesTablesViewModel:
        rows = tuple(
            self._to_row(facility)
            for facility in facilities
        )

        return TexasFacilitiesTablesViewModel(
            independent_facilities_table=TableViewModel(
                title="Texas Independent Living Facilities",
                row_label_header="Entity ID",
                column_headers=(
                    "Facility",
                    "Telephone",
                    "Street",
                    "City",
                    "State",
                    "Zip Code",
                    "Administrator",
                    "Email Address",
                    "Facility Capacity",
                    "Management Co",
                    "Owner Name",
                    "Owner Telephone",
                    "Owner City",
                    "Owner State",
                ),
                rows=rows,
            )
        )

    @staticmethod
    def _to_row(
            facility: Facility,
    ) -> TableRowViewModel:
        return TableRowViewModel(
            row_key=str(facility.facility_id),
            label=facility.entity_id,
            cells=(
                TableCellViewModel(
                    value=facility.name or ""
                ),
                TableCellViewModel(
                    value=facility.telephone or ""
                ),
                TableCellViewModel(
                    value=facility.address.street or ""
                ),
                TableCellViewModel(
                    value=facility.address.city or ""
                ),
                TableCellViewModel(
                    value=facility.address.state or ""
                ),
                TableCellViewModel(
                    value=facility.address.postal_code or ""
                ),
                TableCellViewModel(
                    value=facility.administrator_name or ""
                ),
                TableCellViewModel(
                    value=facility.provider_email or ""
                ),
                TableCellViewModel(
                    value=facility.licensing.capacity or ""
                ),
                TableCellViewModel(
                    value=facility.outsourced_operator.name or ""
                ),
                TableCellViewModel(
                    value=facility.owner.name or ""
                ),
                TableCellViewModel(
                    value=facility.owner.telephone or ""
                ),
                TableCellViewModel(
                    value=facility.owner.city or ""
                ),
                TableCellViewModel(
                    value=facility.owner.state or ""
                ),
            ),
        )
