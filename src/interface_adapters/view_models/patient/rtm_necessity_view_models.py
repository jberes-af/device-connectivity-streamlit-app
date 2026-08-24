# /src/interface_adapters/view_models/patient/rtm_necessity_view_models.py

from dataclasses import dataclass

from src.interface_adapters.view_models.widgets.card_view_models import (
    MetricCardViewModel,
)

from src.interface_adapters.view_models.widgets.badge_view_model import (
    BadgeViewModel,
)

from src.interface_adapters.view_models.widgets.property_field_view_model import (
    PropertyFieldViewModel,
)


@dataclass(frozen=True)
class RtmNecessityHistoryRowViewModel:
    rtm_necessity_id: str
    effective_from_display: str
    effective_to_display: str
    status_badge: BadgeViewModel
    determined_by_display: str
    last_reviewed_display: str


@dataclass(frozen=True)
class RtmNecessityDetailViewModel:
    rtm_necessity_id: str
    status_badge: BadgeViewModel

    diagnosis_properties: tuple[PropertyFieldViewModel, ...]
    indication_properties: tuple[PropertyFieldViewModel, ...]
    monitoring_properties: tuple[PropertyFieldViewModel, ...]
    determination_properties: tuple[PropertyFieldViewModel, ...]


@dataclass(frozen=True)
class RtmNecessityTabViewModel:
    metrics: tuple[MetricCardViewModel, ...]
    current_record: RtmNecessityDetailViewModel | None
    history_rows: tuple[RtmNecessityHistoryRowViewModel, ...]
