# /screens/renderers/sections/treatment_section.py

from src.application.use_cases.patient.diagnosis_and_treatment_uc_dtos import (
    GetDiagnosesAndTreatmentRequestDTO,
    GetDiagnosisAndTreatmentResultDTO,
)

from src.gui.streamlit.screens.resident.renderers.treatment_plan_renderer import (
    render_resident_treatment_plan,
)

from src.main.compose_root_application import AppContainer


def render_treatment_plan_section(
        *,
        resident_id: str,
        container: AppContainer,
) -> None:
    request = GetDiagnosesAndTreatmentRequestDTO(
        patient_id=resident_id,
    )

    result: GetDiagnosisAndTreatmentResultDTO = (
        container
        .get_patient_diagnosis_and_treatment_use_case
        .execute(request=request)
    )

    print(result)

    """
    view_model = (
        container
        .resident_treatment_section_presenter
        .present(result=result)
    )

    render_resident_treatment_plan(
        resident_id=resident_id,
        view_model=view_model,
    )
    """


"""
def render_treatment_section(
        *,
        resident_id: str,
        container: AppContainer,
) -> None:
    # 1. Execute application use case
    request = GetDiagnosesAndTreatmentRequestDTO(
        patient_id=resident_id,
    )

    result = (
        container
        .get_patient_diagnosis_and_treatment_use_case
        .execute(request)
    )

    # 2. Present application result
    view_model = (
        container
        .treatment_plan_section_presenter
        .present(
            treatment_plans=result.treatment_plans,
        )
    )

    # 3. Render GUI
    render_resident_treatment_plan(
        view_model=view_model,
    )
"""
