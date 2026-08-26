# /src/interface_adapters/presenters/provider/patient_provider_section_presenter.py

from src.application.use_cases.residents.provider.patient_provider_uc_dtos import (
    PatientProviderProfileDTO,
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
    ResidentProviderViewModel,
)

from src.interface_adapters.presenters.utils_presenters import (
    format_date,
    format_enum,
    format_optional,
)


class PatientProviderSectionPresenter:

    def present(
            self,
            *,
            provider_profiles: tuple[
                PatientProviderProfileDTO,
                ...
            ],
            icon: str,
    ) -> ResidentProviderViewModel:
        ordered_records: tuple[
            PatientProviderProfileDTO,
            ...
        ] = tuple(
            sorted(
                provider_profiles,
                key=lambda record: (
                    record.last_name.lower(),
                    record.first_name.lower(),
                ),
            )
        )

        provider_card_grids: tuple[
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

        return ResidentProviderViewModel(
            section_title=f"{icon} Providers",
            provider_card_grid=provider_card_grids,
        )

    def _build_card(
            self,
            *,
            record: PatientProviderProfileDTO,
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
            record: PatientProviderProfileDTO,
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
            record: PatientProviderProfileDTO,
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
