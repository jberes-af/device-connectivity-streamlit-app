# /src/interface_adapters/presenters/residents/treatment/rtm_necessity_section_presenter.py

from src.application.use_cases.residents.treatment.diagnosis_and_treatment_uc_dtos import (
    RtmNecessityDTO,
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

from src.interface_adapters.presenters.utils_presenters import (
    format_optional_datetime,
    format_enum,
    format_enum_values,
    format_values,
    format_datetime,
)


class RtmNecessitySectionPresenter:

    def present(
            self,
            *,
            records: tuple[RtmNecessityDTO, ...],
    ) -> CardGridViewModel:
        ordered_records: tuple[RtmNecessityDTO, ...] = tuple(
            sorted(
                records,
                key=lambda record: (
                    self._is_current(record),
                    record.effective_from,
                ),
                reverse=True,
            )
        )

        cards: tuple[CardPropertyFieldsViewModel, ...] = tuple(
            self._build_card(
                record=record,
                is_current=self._is_current(record),
            )
            for record in ordered_records
        )

        return CardGridViewModel(
            columns=1,
            cards=cards,
        )

    @staticmethod
    def _is_current(
            record: RtmNecessityDTO,
    ) -> bool:
        return record.effective_to is None

    def _build_card(
            self,
            *,
            record: RtmNecessityDTO,
            is_current: bool,
    ) -> CardPropertyFieldsViewModel:
        title = "RTM Medical Necessity"

        return CardPropertyFieldsViewModel(
            id=record.rtm_necessity_id,
            title=title,
            description=None,
            property_fields=self._build_property_fields(
                record=record,
            ),
        )

    @staticmethod
    def _build_property_fields(
            *,
            record: RtmNecessityDTO,
    ) -> tuple[PropertyFieldViewModel, ...]:
        return (
            PropertyFieldViewModel(
                label="Status",
                value=format_enum(
                    record.status,
                ),
            ),
            PropertyFieldViewModel(
                label="RTM Program",
                value=record.rtm_program_id,
            ),

            PropertyFieldViewModel(
                label="Primary Diagnosis",
                value=record.primary_diagnosis_code,
            ),
            PropertyFieldViewModel(
                label="Secondary Diagnoses",
                value=format_values(
                    record.secondary_diagnosis_codes,
                ),
            ),

            PropertyFieldViewModel(
                label="Clinical Indications",

                value=format_enum_values(
                    record.clinical_indications,
                ),
            ),
            PropertyFieldViewModel(
                label="Indication Notes",
                value=(
                        record.clinical_indication_notes
                        or "—"
                ),
            ),

            PropertyFieldViewModel(
                label="Monitoring Reasons",
                value=format_enum_values(
                    record.monitoring_reasons,
                ),
            ),
            PropertyFieldViewModel(
                label="Monitoring Rationale",
                value=record.monitoring_rationale,
            ),

            PropertyFieldViewModel(
                label="Expected Benefit",
                value=record.expected_clinical_benefit,
            ),
            PropertyFieldViewModel(
                label="Clinical Uses",
                value=format_enum_values(
                    record.intended_clinical_uses,
                ),
            ),

            PropertyFieldViewModel(
                label="Determined By",
                value=record.determined_by_provider_id,
            ),
            PropertyFieldViewModel(
                label="Determined At",
                value=format_datetime(
                    record.determined_at,
                ),
            ),

            PropertyFieldViewModel(
                label="Attested",
                value=(
                    "Yes"
                    if record.is_attested
                    else "No"
                ),
            ),
            PropertyFieldViewModel(
                label="Attestation Version",
                value=record.attestation_version,
            ),

            PropertyFieldViewModel(
                label="Effective From",
                value=format_datetime(
                    record.effective_from,
                ),
            ),
            PropertyFieldViewModel(
                label="Effective To",
                value=format_optional_datetime(
                    record.effective_to,
                    empty_value="Present",
                ),
            ),

            PropertyFieldViewModel(
                label="Last Reviewed",
                value=format_optional_datetime(
                    record.last_reviewed_at,
                ),
            ),
            PropertyFieldViewModel(
                label="Last Reviewed By",
                value=(
                        record.last_reviewed_by_provider_id
                        or "—"
                ),
            ),
        )
