# /src/interface_adapters/view_models/main_page/segmented_controls_view_model.py

from dataclasses import dataclass
from enum import StrEnum

class ResidentSectionEnum(StrEnum):
    APPOINTMENTS = "appointments"
    BILLING = "billing"
    CARE_PLAN = "care_plan"
    CLINICAL_DOCS = "clinical_docs"
    COMMUNICATIONS = "communication"
    PAYERS = "payers"
    PRIORITY_ITEMS = "priority_items"
    PROVIDERS = "providers"
    CONTACT = "contact_info"
    SENSING = "sensing"
    TREATMENTS = "treatments"

RESIDENT_SEGMENT_ORDER: tuple[ResidentSectionEnum, ...] = (
    ResidentSectionEnum.CONTACT,
    ResidentSectionEnum.PRIORITY_ITEMS,
    ResidentSectionEnum.APPOINTMENTS,
    ResidentSectionEnum.CARE_PLAN,
    ResidentSectionEnum.TREATMENTS,
    ResidentSectionEnum.CLINICAL_DOCS,
    ResidentSectionEnum.PROVIDERS,
    ResidentSectionEnum.COMMUNICATIONS,
    ResidentSectionEnum.PAYERS,
    ResidentSectionEnum.SENSING,
    ResidentSectionEnum.BILLING,
)

SECTION_ICONS: dict[ResidentSectionEnum, str] = {
    ResidentSectionEnum.CONTACT: ":material/contact_page:",
    ResidentSectionEnum.PRIORITY_ITEMS: ":material/priority_high:",
    ResidentSectionEnum.APPOINTMENTS: ":material/calendar_month:",
    ResidentSectionEnum.CARE_PLAN: ":material/assignment_add:",
    ResidentSectionEnum.TREATMENTS: ":material/medical_services:",
    ResidentSectionEnum.CLINICAL_DOCS: ":material/clinical_notes:",
    ResidentSectionEnum.PROVIDERS: ":material/medical_services:",
    ResidentSectionEnum.COMMUNICATIONS: ":material/communication:",
    ResidentSectionEnum.PAYERS: ":material/savings:",
    ResidentSectionEnum.SENSING: ":material/sensors:",
    ResidentSectionEnum.BILLING: ":material/receipt_long:",
}


"""

class ResidentSectionEnum(StrEnum):
    RESIDENT = "profile"
    CARE_PLAN = "care_plan"
    TREATMENTS = "treatments"
    SENSING = "sensing"
    COMMUNICATIONS = "communication"
    BILLING = "billing"
    PRIORITIES = "priorities"


RESIDENT_SEGMENT_ORDER: tuple[ResidentSectionEnum, ...] = (
    ResidentSectionEnum.RESIDENT,
    ResidentSectionEnum.PRIORITIES,
    ResidentSectionEnum.CARE_PLAN,
    ResidentSectionEnum.TREATMENTS,
    ResidentSectionEnum.COMMUNICATIONS,
    ResidentSectionEnum.BILLING,
    ResidentSectionEnum.SENSING,
)
"""


@dataclass(frozen=True)
class ResidentSegmentOptionViewModel:
    id: ResidentSectionEnum
    label: str
    icon: str | None = None


@dataclass(frozen=True)
class ResidentSegmentedControlViewModel:
    label: str
    options: list[ResidentSegmentOptionViewModel]
    selected_id: ResidentSectionEnum | None = None
    key: str | None = None


