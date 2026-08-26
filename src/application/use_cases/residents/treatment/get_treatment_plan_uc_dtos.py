# /src/application/use_cases/residents/treatment/get_treatment_plan_uc_dtos.py


from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class TreatmentInformationDTO:
    treating_provider: str
    treatment_plan_start_date: date
    expected_treatment_end_date: date | None
    treatment_status: str
    treatment_types: tuple[str, ...]


@dataclass(frozen=True)
class OutcomeMeasureDTO:
    name: str
    unit: str | None
    baseline_value: float | None
    current_value: float | None
    expected_target: float | None
    change_from_baseline: float | None
    measurement_period_start: date
    measurement_period_end: date
    provider_success_criteria: str


@dataclass(frozen=True)
class TreatmentPlanHistoryEntryDTO:
    changed_at: date
    changed_by_provider: str
    change_description: str
    previous_value: str | None
    new_value: str | None
    reason: str


@dataclass(frozen=True)
class TreatmentPlanReadDTO:
    # diagnosis: DiagnosisAndMedicalNecessityDTO
    treatment: TreatmentInformationDTO
    outcome_measures: tuple[OutcomeMeasureDTO, ...]
    history: tuple[TreatmentPlanHistoryEntryDTO, ...]
