# /src/interface_adapters/view_models/contact/resident_sensing_view_model.py

from dataclasses import dataclass
from enum import StrEnum

from src.interface_adapters.view_models.widgets.card_grid_view_model import (
    CardGridViewModel,
)

from src.interface_adapters.view_models.widgets.tab_view_model import (
    TabViewModel,
)


class SensingTabIdEnum(StrEnum):
    ANALYTICS = "analytics"
    DATA = "data"
    LIVE_STATUS = "live_status"
    PROFILES = "user_sensing_account"


SENSING_SEGMENT_ORDER: tuple[SensingTabIdEnum, ...] = (
    SensingTabIdEnum.ANALYTICS,
    SensingTabIdEnum.DATA,
    SensingTabIdEnum.LIVE_STATUS,
    SensingTabIdEnum.PROFILES,
)


@dataclass(frozen=True)
class SensorProfileViewModel:
    sensor_id: str
    tenant_id: str
    name: str
    sensor_type: str
    location: str
    zone: str
    hardware_version: str | None = None
    firmware_version: str | None = None


@dataclass(frozen=True)
class SensorSectionViewModel:
    section_header: str
    dash_card_grid_vm: CardGridViewModel
    sensing_detail_section_vm: TabViewModel
