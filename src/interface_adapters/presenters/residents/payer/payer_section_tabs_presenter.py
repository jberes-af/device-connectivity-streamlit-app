# /src/interface_adapters/presenters/treatment_plan/payer_section_tabs_presenter.py

from src.application.use_cases.residents.payer.patient_payer_uc_dtos import (
    PatientPayerProfileDTO,
)

from src.interface_adapters.view_models.widgets.card_grid_view_model import (
    CardGridViewModel,
)

from src.interface_adapters.view_models.widgets.card_view_models import (
    CardPropertyFieldsViewModel,
)

from src.interface_adapters.view_models.widgets.property_field_view_model import (
    PropertyFieldViewModel,
)

from src.interface_adapters.view_models.residents.payer.patient_payer_view_models import (
    PatientPayerViewModel,
)

from src.interface_adapters.presenters.utils_presenters import (
    format_date,
    format_enum,
    format_optional,
)


class PatientPayerSectionPresenter:

    def present(
            self,
            *,
            payer_profiles: tuple[PatientPayerProfileDTO, ...],
            icon: str,
    ) -> PatientPayerViewModel:

        ordered_records = tuple(
            sorted(
                payer_profiles,
                key=lambda record: (
                    not record.is_primary,
                    record.payer_name.lower(),
                ),
            )
        )

        payer_card_grids = tuple(
            CardGridViewModel(
                columns=1,
                cards=(
                    self._build_card(
                        record=record,
                    ),
                ),
            )
            for record in ordered_records
        )

        return PatientPayerViewModel(
            section_title=f"{icon} Payers",
            patient_payer_card_grids=payer_card_grids,
        )

    def _build_card(
            self,
            *,
            record: PatientPayerProfileDTO,
    ) -> CardPropertyFieldsViewModel:

        title = (
            f"{record.payer_name}"
            + (" — Primary" if record.is_primary else "")
        )

        return CardPropertyFieldsViewModel(
            id=record.patient_payer_id,
            title=title,
            description=None,
            property_fields=self._build_property_fields(
                record=record,
            ),
        )

    @staticmethod
    def _build_property_fields(
            *,
            record: PatientPayerProfileDTO,
    ) -> tuple[PropertyFieldViewModel, ...]:

        return (
            PropertyFieldViewModel(
                label="Payer ID",
                value=record.payer_id,
            ),
            PropertyFieldViewModel(
                label="Payer Type",
                value=format_enum(
                    record.payer_type,
                ),
            ),
            PropertyFieldViewModel(
                label="Member ID",
                value=format_optional(
                    record.member_id,
                ),
            ),
            PropertyFieldViewModel(
                label="Group Number",
                value=format_optional(
                    record.group_number,
                ),
            ),
            PropertyFieldViewModel(
                label="Effective Date",
                value=format_date(
                    record.effective_date,
                ),
            ),
            PropertyFieldViewModel(
                label="Termination Date",
                value=format_date(
                    record.termination_date,
                    empty_value="—",
                ),
            ),
            PropertyFieldViewModel(
                label="Primary",
                value=(
                    "Yes"
                    if record.is_primary
                    else "No"
                ),
            ),
        )