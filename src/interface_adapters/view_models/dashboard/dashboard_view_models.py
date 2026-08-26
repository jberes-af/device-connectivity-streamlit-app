# /src/interface_adapters/view_models/dashboard/dashboard_view_models.py

from dataclasses import dataclass

from src.interface_adapters.view_models.widgets.badge_view_model import (
    BadgeViewModel,
)

from src.interface_adapters.view_models.widgets.card_view_models import (
    MetricCardViewModel,
)


# --- RESIDENT ATTENTION

@dataclass(frozen=True)
class DashboardResidentAttentionRowViewModel:
    resident_id: str
    resident_name: str
    issue: str
    priority: BadgeViewModel
    since: str | None = None


@dataclass(frozen=True)
class DashboardResidentAttentionViewModel:
    title: str
    rows: tuple[DashboardResidentAttentionRowViewModel, ...]


# --- SUMMARY DETAIL

@dataclass(frozen=True)
class DashboardSummaryDetailCardViewModel:
    card_id: str
    title: str
    primary_value: str
    details: tuple[str, ...]
    button_label: str


# --- MAIN PAGE

@dataclass(frozen=True)
class DashboardMainPageViewModel:
    kpi_cards: tuple[MetricCardViewModel, ...]
    resident_attention: DashboardResidentAttentionViewModel
    summary_detail_cards: tuple[
        DashboardSummaryDetailCardViewModel,
        ...
    ]
