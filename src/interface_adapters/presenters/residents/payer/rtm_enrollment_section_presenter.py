# /src/interface_adapters/presenters/residents/payer/rtm_enrollment_section_presenter.py

from src.application.use_cases.residents.rtm.rtm_enrollment_uc_dtos import (
    RtmEnrollmentDTO,
)

from src.interface_adapters.view_models.residents.payer.rtm_enrollment_view_models import (
    RtmEnrollmentViewModel,
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
    format_date,
    format_enum,
    format_optional,
    format_optional_datetime,
)


class RtmEnrollmentSectionPresenter:

    def present(
            self,
            *,
            enrollments: tuple[RtmEnrollmentDTO, ...],
    ) -> RtmEnrollmentViewModel:
        ordered_enrollments = tuple(
            sorted(
                enrollments,
                key=lambda enrollment: (
                    enrollment.service_start_date,
                    enrollment.enrollment_date,
                ),
                reverse=True,
            )
        )

        return RtmEnrollmentViewModel(
            section_title="RTM Enrollment",
            enrollment_card_grid=CardGridViewModel(
                columns=1,
                cards=tuple(
                    self._build_card(
                        enrollment=enrollment,
                    )
                    for enrollment in ordered_enrollments
                ),
            ),
        )

    def _build_card(
            self,
            *,
            enrollment: RtmEnrollmentDTO,
    ) -> CardPropertyFieldsViewModel:
        return CardPropertyFieldsViewModel(
            id=enrollment.enrollment_id,
            title=self._build_title(
                enrollment=enrollment,
            ),
            description=None,
            property_fields=self._build_property_fields(
                enrollment=enrollment,
            ),
        )

    @staticmethod
    def _build_title(
            *,
            enrollment: RtmEnrollmentDTO,
    ) -> str:
        return (
            f"RTM Enrollment — "
            f"{format_enum(enrollment.enrollment_status)}"
        )

    @staticmethod
    def _build_property_fields(
            *,
            enrollment: RtmEnrollmentDTO,
    ) -> tuple[PropertyFieldViewModel, ...]:
        return (
            PropertyFieldViewModel(
                label="Enrollment Status",
                value=format_enum(
                    enrollment.enrollment_status,
                ),
            ),
            PropertyFieldViewModel(
                label="Enrollment Date",
                value=format_date(
                    enrollment.enrollment_date,
                ),
            ),
            PropertyFieldViewModel(
                label="Service Start",
                value=format_date(
                    enrollment.service_start_date,
                ),
            ),
            PropertyFieldViewModel(
                label="Service End",
                value=format_date(
                    enrollment.service_end_date,
                    empty_value="Present",
                ),
            ),
            PropertyFieldViewModel(
                label="Consent Status",
                value=format_enum(
                    enrollment.consent_status,
                ),
            ),
            PropertyFieldViewModel(
                label="Consent Obtained",
                value=format_optional_datetime(
                    enrollment.consent_obtained_at,
                ),
            ),
            PropertyFieldViewModel(
                label="Consent Method",
                value=(
                    format_enum(enrollment.consent_method)
                    if enrollment.consent_method is not None
                    else "—"
                ),
            ),
            PropertyFieldViewModel(
                label="Consent Document",
                value=format_optional(
                    enrollment.consent_document_reference,
                ),
            ),
            PropertyFieldViewModel(
                label="Discontinuation Reason",
                value=format_optional(
                    enrollment.discontinuation_reason,
                ),
            ),
        )
