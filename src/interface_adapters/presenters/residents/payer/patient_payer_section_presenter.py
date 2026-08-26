# /src/interface_adapters/presenters/residents/payer/patient_payer_section_presenter.py

from src.application.use_cases.residents.payer.get_patient_payer_profile_uc import (
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

from src.interface_adapters.view_models.residents.main_page.resident_main_view_model import (
    PatientPayerViewModel,
)

from src.interface_adapters.presenters.utils_presenters import (
    format_date,
    format_enum,
    format_optional,
)


class PatientProviderPresenter:

    def present(
            self,
            *,
            payer_profiles: tuple[PatientPayerProfileDTO, ...],
            icon: str,
    ) -> PatientPayerViewModel:
        ordered_records: tuple[
            PatientPayerProfileDTO,
            ...
        ] = tuple(
            sorted(
                payer_profiles,
                key=lambda record: (
                    record.last_name.lower(),
                    record.first_name.lower(),
                ),
            )
        )

        payer_card_grids: tuple[
            CardGridViewModel,
            ...
        ] = tuple(
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
            section_title=f"{icon} Providers",
            payers=payer_card_grids,
        )

    def _build_card(
            self,
            *,
            record: PatientPayerProfileDTO,
    ) -> CardPropertyFieldsViewModel:
        return CardPropertyFieldsViewModel(
            id=record.patient_provider_id,
            title=self._format_provider_name(
                record=record,
            ),
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
                label="Provider ID",
                value=record.provider_id,
            ),
            PropertyFieldViewModel(
                label="NPI",
                value=format_optional(
                    record.national_provider_identifier,
                ),
            ),
            PropertyFieldViewModel(
                label="Role",
                value=format_enum(
                    record.role,
                ),
            ),
            PropertyFieldViewModel(
                label="Organization ID",
                value=format_optional(
                    record.organization_id,
                ),
            ),
            PropertyFieldViewModel(
                label="Specialty",
                value=format_optional(
                    record.specialty,
                ),
            ),
            PropertyFieldViewModel(
                label="Credentials",
                value=format_optional(
                    record.credentials,
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
                label="Active",
                value=(
                    "Yes"
                    if record.is_active
                    else "No"
                ),
            ),
        )

    @staticmethod
    def _format_provider_name(
            *,
            record: PatientPayerProfileDTO,
    ) -> str:
        name_parts = (
            record.first_name,
            record.middle_name,
            record.last_name,
        )

        return " ".join(
            part.strip()
            for part in name_parts
            if part and part.strip()
        )
