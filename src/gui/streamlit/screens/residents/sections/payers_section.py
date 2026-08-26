# /src/gui/streamlit/screens/residents/sections/payers_section.py

from src.gui.streamlit.screens.residents.renderers.payers_renderer import (
    render_patient_provider_section,
)

from src.application.use_cases.residents.payer.get_patient_payer_profile_uc import (
    GetPatientPayerProfileRequestDTO,
    GetPatientPayerProfileResultDTO,
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
    request = GetPatientPayerProfileRequestDTO(
        patient_id=resident_id,
    )

    use_case_result: GetPatientPayerProfileResultDTO = (
        container
        .get_payers_and_rtm_enrollment_use_case
        .execute(request=request)
    )

    view_model: ResidentPayerAndRtmEnrollmentSectionViewModel = (
        container.resident_main_page_presenter.present_payers_and_rtm_enrollment_section(
            result=use_case_result.patient_payer_profiles,
        )
    )

    render_patient_provider_section(
        resident_id=resident_id,
        view_model=view_model,
    )
