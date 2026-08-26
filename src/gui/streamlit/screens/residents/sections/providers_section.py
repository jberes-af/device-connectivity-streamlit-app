# /src/gui/streamlit/screens/residents/sections/providers_section.py

from src.gui.streamlit.screens.residents.renderers.providers_renderer import (
    render_patient_provider_section,
)

from src.application.use_cases.residents.provider.patient_provider_uc_dtos import (
    GetPatientProviderProfileRequestDTO,
    GetPatientProviderProfileResultDTO,
)

from src.interface_adapters.view_models.residents.main_page.resident_main_view_model import (
    ResidentProviderViewModel,
)

from src.main.compose_root_application import AppContainer


def render_providers_section(
        *,
        resident_id: str,
        container: AppContainer,
) -> None:
    request = GetPatientProviderProfileRequestDTO(
        patient_id=resident_id,
    )

    use_case_result: GetPatientProviderProfileResultDTO = (
        container
        .get_patient_provider_profile_use_case
        .execute(request=request)
    )

    view_model: ResidentProviderViewModel = (
        container.resident_main_page_presenter.present_patient_providers_section(
            result=use_case_result.provider_profiles,
        )
    )

    render_patient_provider_section(
        resident_id=resident_id,
        view_model=view_model,
    )
