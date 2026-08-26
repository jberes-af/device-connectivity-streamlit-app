# payer_and_rtm_enrollment_section_presenter.py

from src.application.use_cases.residents.payer.patient_payer_and_rtm_enrollment_uc_dtos import (
    GetPatientPayersAndRtmEnrollmentResultDTO,
)

from src.interface_adapters.presenters.residents.payer.patient_payer_section_presenter import (
    PatientPayerSectionPresenter,
)

from src.interface_adapters.presenters.residents.payer.rtm_enrollment_section_presenter import (
    RtmEnrollmentSectionPresenter,
)

from src.interface_adapters.view_models.residents.main_page.resident_main_view_model import (
    ResidentPayerAndRtmEnrollmentSectionViewModel,
)

from src.interface_adapters.view_models.widgets.tab_view_model import (
    TabItemViewModel,
    TabViewModel,
)

from src.interface_adapters.view_models.residents.main_page.resident_main_view_model import (
    PayerTabIdEnum,
    PAYER_SEGMENT_ORDER
)



class PatientPayerAndRtmEnrollmentSectionPresenter:

    def present(
            self,
            *,
            result: GetPatientPayersAndRtmEnrollmentResultDTO,
            icon: str,
    ) -> ResidentPayerAndRtmEnrollmentSectionViewModel:
        return ResidentPayerAndRtmEnrollmentSectionViewModel(
            section_title=f"{icon} Payer & RTM Enrollment",
            section_tabs=self._build_tabs(),
            patient_payers=(
                PatientPayerSectionPresenter().present(
                    payer_profiles=result.patient_payer_profiles,
                    icon="",
                )
            ),
            rtm_enrollment=(
                RtmEnrollmentSectionPresenter().present(
                    enrollments=result.rtm_enrollments,
                )
            ),
        )

    @staticmethod
    def _build_tabs() -> TabViewModel:
        return TabViewModel(
            tabs=tuple(
                TabItemViewModel(
                    tab_id=tab_id.value,
                    label=tab_id.value.replace("_", " ").title(),
                    content="",
                )
                for tab_id in PAYER_SEGMENT_ORDER
            )
        )
