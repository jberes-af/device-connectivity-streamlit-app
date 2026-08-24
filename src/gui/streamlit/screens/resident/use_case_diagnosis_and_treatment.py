# /src/gui/streamlit/screens/person/use_case_diagnosis_and_treatment.py

from dataclasses import dataclass

# --- APPLICATION

from src.application.use_cases.patient.diagnosis_and_treatment_uc_dtos import (
    GetDiagnosesAndTreatmentRequestDTO,
    GetDiagnosisAndTreatmentResultDTO,
)

from src.application.use_cases.patient.get_patient_diagnosis_and_treatment_uc import (
    GetPatientDiagnosesAndTreatmentsUseCase,
)

@dataclass(frozen=True)
class DiagnosisAndTreatmentUseCaseResults:
    result_diagnosis_and_treatment: GetDiagnosisAndTreatmentResultDTO


def run_diagnosis_and_treatment_use_case(
        resident_id: str,
        use_case: GetPatientDiagnosesAndTreatmentsUseCase,
) -> DiagnosisAndTreatmentUseCaseResults:
    request = GetDiagnosesAndTreatmentRequestDTO(
        patient_id=resident_id,
    )

    result: GetDiagnosisAndTreatmentResultDTO = (
        use_case.execute(request=request)
    )

    return DiagnosisAndTreatmentUseCaseResults(
        result_diagnosis_and_treatment=result,
    )
