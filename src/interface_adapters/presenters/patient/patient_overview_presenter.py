# patient_overview_presenter.py

from src.application.use_cases.patient.patient_uc_dtos import (
    GetPatientOverviewResultDTO,
    PatientOverviewDevDTO,
)

from src.interface_adapters.view_models.patient.patient_overview_page_view_model import (
    PatientOverviewPageViewModel,
)

from src.interface_adapters.view_models.common.card_view_models import (
    CardViewModel,
)
# from src.interface_adapters.view_models.common.metric_view_model import MetricViewModel
from src.interface_adapters.view_models.common.badge_view_model import (
    BadgeViewModel,
    BadgeStyle,
)
from src.interface_adapters.view_models.common.property_field_view_model import (
    PropertyFieldViewModel,
)
from src.interface_adapters.view_models.common.property_grid_view_model import (
    PropertyGridViewModel,
)


class PatientOverviewPresenter:

    def present(
            self,
            result: GetPatientOverviewResultDTO,
    ) -> PatientOverviewPageViewModel:
        overview = result.overview

        return PatientOverviewPageViewModel(

            page_title=overview.administration.full_name,

            administration_card=self._build_admin_card(
                overview,
            ),

            enrollment_card=self._build_enrollment_card(
                overview,
            ),

            # provider_review_card=self._build_provider_review_card(
            #    overview,
            # ),

            # communication_card=self._build_communication_card(
            #    overview,
            # ),
        )

    @staticmethod
    def _build_admin_card(
            overview: PatientOverviewDevDTO,
    ) -> CardViewModel:
        admin = overview.administration

        return CardViewModel(

            title="Patient Administration",

            icon="👤",

            property_grid=PropertyGridViewModel(

                columns=3,

                fields=(

                    PropertyFieldViewModel(
                        "Date of Birth",
                        admin.date_of_birth.strftime("%B %d, %Y"),
                    ),

                    PropertyFieldViewModel(
                        "Diagnosis",
                        admin.primary_diagnosis,
                    ),

                    PropertyFieldViewModel(
                        "Provider",
                        admin.treating_provider,
                    ),

                    PropertyFieldViewModel(
                        "Payer",
                        admin.primary_payer,
                    ),

                    PropertyFieldViewModel(
                        "Telephone",
                        admin.telephone or "",
                    ),

                    PropertyFieldViewModel(
                        "Email",
                        admin.email or "",
                    ),
                ),
            ),
        )

    @staticmethod
    def _build_enrollment_card(
            overview: PatientOverviewDevDTO,
    ) -> CardViewModel:
        enrollment = overview.enrollment_summary

        return CardViewModel(

            title="RTM Enrollment",

            icon="📡",

            badge=BadgeViewModel(
                text=enrollment.enrollment_status,
                style=BadgeStyle.SUCCESS,
            ),

            property_grid=PropertyGridViewModel(

                columns=3,

                fields=(

                    PropertyFieldViewModel(
                        "Enrollment",
                        enrollment.enrollment_status,
                    ),

                    PropertyFieldViewModel(
                        "Consent",
                        enrollment.consent_status,
                    ),

                    PropertyFieldViewModel(
                        "Assigned Device",
                        enrollment.assigned_device or "",
                    ),
                ),
            ),
        )
