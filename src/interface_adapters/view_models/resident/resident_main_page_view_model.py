# /src/interface_adapters/view_models/resident/resident_main_page_view_model.py

from dataclasses import dataclass

from src.interface_adapters.view_models.common.card_grid_view_model import (
    CardGridViewModel)

# from enum import StrEnum

# from src.interface_adapters.view_models.common.card_view_models import (
#    CardTitleTextButtonViewModel,
# )

"""
class ResidentTabIdEnum(StrEnum):
    PROFILE = "profile"
    CARE_PLAN = "care_plan"
    TREATMENT_PLAN = "treatment_plan"
    PROVIDER = "provider"
    SENSING = "sensing"
    COMMUNICATION = "communication"
    PAYER = "payer"
    BILLING = "billing"
"""


@dataclass(frozen=True)
class ResidentMainPageTopViewModel:
    page_title: str
    page_subtitle: str


@dataclass(frozen=True)
class ResidentContactViewModel:
    section_title: str
    resident_info_card_grid: CardGridViewModel
    in_case_of_need_card_grid: CardGridViewModel


"""
@dataclass(frozen=True, slots=True)
class ResidentOverviewViewModel:
    message: str


@dataclass(frozen=True, slots=True)
class ResidentTabViewModel:
    tab_id: ResidentTabIdEnum
    label: str


@dataclass(frozen=True, slots=True)
class ResidentRecordCardGridViewModel:
    cards: tuple[CardTitleTextButtonViewModel, ...]
    columns: int = 3


@dataclass(frozen=True, slots=True)
class ResidentRecordTabsViewModel:
    tabs: tuple[ResidentTabViewModel, ...]
"""
