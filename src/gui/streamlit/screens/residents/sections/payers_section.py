# /src/gui/streamlit/screens/residents/sections/payers_section.py

from src.application.use_cases.residents.payer.patient_payer_and_rtm_enrollment_uc_dtos import (
    GetPatientPayersAndRtmEnrollmentRequestDTO,
    GetPatientPayersAndRtmEnrollmentResultDTO,
)

from src.gui.streamlit.screens.residents.renderers.payers_renderer import (
    render_resident_payers_and_rtm_enrollment,
)

from src.interface_adapters.view_models.residents.main_page.resident_main_view_model import (
    ResidentPayerAndRtmEnrollmentSectionViewModel,
)

from src.main.compose_root_application import AppContainer


def render_payers_section(
        *,
        resident_id: str,
        container: AppContainer,
) -> None:
    request = GetPatientPayersAndRtmEnrollmentRequestDTO(
        patient_id=resident_id,
    )

    result: GetPatientPayersAndRtmEnrollmentResultDTO = (
        container
        .get_payers_and_rtm_enrollment_use_case
        .execute(request=request)
    )

    view_model: ResidentPayerAndRtmEnrollmentSectionViewModel = (
        container
        .resident_main_page_presenter
        .present_payers_and_rtm_enrollment_section(
            result=result,
        )
    )

    render_resident_payers_and_rtm_enrollment(
        view_model=view_model,
    )
