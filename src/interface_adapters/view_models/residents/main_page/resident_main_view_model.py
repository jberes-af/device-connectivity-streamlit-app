# /src/interface_adapters/view_models/main_page/resident_main_view_model.py

from dataclasses import dataclass
from enum import StrEnum

from src.interface_adapters.view_models.widgets.card_grid_view_model import (
    CardGridViewModel)

from src.interface_adapters.view_models.widgets.tab_view_model import (
    # TabItemViewModel,
    TabViewModel,
)

from src.interface_adapters.view_models.residents.treatment.diagnosis_view_models import (
    DiagnosisSectionViewModel,
)

from src.interface_adapters.view_models.residents.treatment.treatment_plan_view_models import (
    TreatmentPlanViewModel,
)

from src.interface_adapters.view_models.residents.payer.patient_payer_view_models import (
    PatientPayerViewModel,
)

from src.interface_adapters.view_models.residents.payer.rtm_enrollment_view_models import (
    RtmEnrollmentViewModel
)


# --- MAIN TOP

@dataclass(frozen=True)
class ResidentMainPageTopViewModel:
    page_title: str
    page_subtitle: str


# --- CARE PLAN SEGMENTED CONTROL

@dataclass(frozen=True)
class ResidentCarePlanViewModel:
    section_title: str
    care_plan_card_grid: CardGridViewModel


# --- RESIDENT CONTACTS SEGMENTED CONTROL

@dataclass(frozen=True)
class ResidentContactViewModel:
    section_title: str
    resident_profile_card_grid: CardGridViewModel
    in_case_of_need_card_grid: CardGridViewModel


# --- PROVIDER SEGMENTED CONTROL

@dataclass(frozen=True)
class ResidentProviderViewModel:
    section_title: str
    provider_card_grid: tuple[CardGridViewModel, ...]


# --- PAYER SEGMENTED CONTROL

class PayerTabIdEnum(StrEnum):
    COVERAGES = "coverages"
    RTM_ENROLLMENT = "rtm_enrollment"


PAYER_SEGMENT_ORDER: tuple[PayerTabIdEnum, ...] = (
    PayerTabIdEnum.COVERAGES,
    PayerTabIdEnum.RTM_ENROLLMENT,
)

_TAB_LABELS = {
    PayerTabIdEnum.COVERAGES: "Coverage",
    PayerTabIdEnum.RTM_ENROLLMENT: "RTM Enrollment",
}


@dataclass(frozen=True)
class ResidentPayerAndRtmEnrollmentSectionViewModel:
    section_title: str
    section_tabs: TabViewModel
    patient_payers: PatientPayerViewModel
    rtm_enrollment: RtmEnrollmentViewModel


# --- TREATMENT SEGMENTED CONTROL

class TreatmentSectionTabIdEnum(StrEnum):
    DIAGNOSES = "diagnoses"
    TREATMENT_PLANS = "treatment_plans"
    RTM_NECESSITY = "rtm_necessity"


TREATMENT_SEGMENT_ORDER: tuple[TreatmentSectionTabIdEnum, ...] = (
    TreatmentSectionTabIdEnum.DIAGNOSES,
    TreatmentSectionTabIdEnum.TREATMENT_PLANS,
    TreatmentSectionTabIdEnum.RTM_NECESSITY,
)


@dataclass(frozen=True)
class ResidentTreatmentSectionViewModel:
    section_title: str
    treatment_section_tabs: TabViewModel
    diagnoses: DiagnosisSectionViewModel
    treatment_plans: TreatmentPlanViewModel
    rtm_necessity: CardGridViewModel


"""
# --- RTM SEGMENTED CONTROL

@dataclass(frozen=True)
class ResidentRtmViewModel:
    section_title: str
    rtm_card_grid: CardGridViewModel


@dataclass(frozen=True, slots=True)
class ResidentOverviewViewModel:
    message: str


@dataclass(frozen=True, slots=True)
class ResidentTabViewModel:
    tab_id: ResidentTabIdEnum
    label: str


@dataclass(frozen=True, slots=True)
class ResidentRecordTabsViewModel:
    tabs: tuple[ResidentTabViewModel, ...]
"""
