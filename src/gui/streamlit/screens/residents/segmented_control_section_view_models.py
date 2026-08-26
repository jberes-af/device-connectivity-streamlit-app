# # src/gui/streamlit/screens/renderers/segmented_control_section_view_models.py

from scripts.resident_section_types import (
    SectionUseCaseResult,
    ResidentSectionViewModel)

from src.interface_adapters.presenters.residents.sensing.resident_sensing_section_presenter import (
    ResidentSensingSectionPresenter)

from src.interface_adapters.view_models.residents.main_page import (
    ResidentSectionEnum)

from src.main.compose_root_application import AppContainer


def get_view_model(
        selected_resident_id: str,
        selected_control: ResidentSectionEnum,
        use_case_results: SectionUseCaseResult,
        container: AppContainer,
) -> ResidentSectionViewModel | None:
    if selected_control == ResidentSectionEnum.SENSING:
        if use_case_results is None:
            return None

        return (
            ResidentSensingSectionPresenter()
            .present_sensing_section(
                use_case_results.result_user_sensing_account
            )
        )

    elif selected_control == ResidentSectionEnum.TREATMENTS:
        if use_case_results is None:
            return None

        return (
            ResidentTreatmentSectionPresenter()
            .present(
                use_case_results.result_diagnosis_and_treatment
            )
        )

    return None
