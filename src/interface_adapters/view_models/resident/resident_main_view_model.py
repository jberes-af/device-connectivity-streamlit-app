# /src/interface_adapters/view_models/resident/resident_main_view_model.py

from dataclasses import dataclass
from enum import StrEnum

from src.interface_adapters.view_models.widgets.card_grid_view_model import (
    CardGridViewModel)

from src.interface_adapters.view_models.widgets.tab_view_model import (
    TabViewModel,
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
    provider_card_grid: CardGridViewModel


# --- PAYER SEGMENTED CONTROL

class PayerTabIdEnum(StrEnum):
    COVERAGES = "coverages"
    RTM_ENROLLMENT = "rtm_enrollment"


PAYER_SEGMENT_ORDER: tuple[PayerTabIdEnum, ...] = (
    PayerTabIdEnum.COVERAGES,
    PayerTabIdEnum.RTM_ENROLLMENT,
)


@dataclass(frozen=True)
class ResidentPayerViewModel:
    section_title: str
    payer_card_grid: CardGridViewModel
    payer_details_section_vm: TabViewModel


# --- RTM SEGMENTED CONTROL

@dataclass(frozen=True)
class ResidentRtmViewModel:
    section_title: str
    rtm_card_grid: CardGridViewModel


# --- TREATMENT SEGMENTED CONTROL

class TreatmentTabIdEnum(StrEnum):
    DIAGNOSES = "diagnoses"
    TREATMENT_PLANS = "treatment_plans"
    RTM_NECESSITY = "rtm_necessity"


TREATMENT_SEGMENT_ORDER: tuple[TreatmentTabIdEnum, ...] = (
    TreatmentTabIdEnum.DIAGNOSES,
    TreatmentTabIdEnum.RTM_NECESSITY,
)


@dataclass(frozen=True)
class ResidentTreatmentViewModel:
    section_title: str
    treatment_card_grid: CardGridViewModel
    treatment_details_section_vm: TabViewModel


"""
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
