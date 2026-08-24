# /src/interface_adapters/view_models/patient/diagnosis_view_models.py

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

from src.interface_adapters.view_models.widgets.card_grid_view_model import (
    CardGridViewModel,
)

from src.interface_adapters.view_models.widgets.card_view_models import (
    CardPropertyFieldsViewModel,
)


@dataclass(frozen=True)
class DiagnosisTableRowViewModel:
    patient_diagnosis_id: str
    diagnosis_name: str
    primary_badge: BadgeViewModel | None
    diagnosed_date_display: str
    resolved_date_display: str
    status_badge: BadgeViewModel


@dataclass(frozen=True)
class DiagnosisDetailViewModel:
    patient_diagnosis_id: str
    title: str
    status_badge: BadgeViewModel
    properties: tuple[PropertyFieldViewModel, ...]


@dataclass(frozen=True)
class DiagnosisTabViewModel:
    metrics: tuple[MetricCardViewModel, ...]
    rows: tuple[DiagnosisTableRowViewModel, ...]
    selected_detail: DiagnosisDetailViewModel | None


@dataclass(frozen=True)
class DiagnosisTableRowViewModel:
    patient_diagnosis_id: str
    diagnosis_name: str
    diagnosis_code: str
    primary_display: str
    diagnosed_date_display: str
    resolved_date_display: str
    status_display: str


@dataclass(frozen=True)
class DiagnosisSectionViewModel:
    metric_grid: CardGridViewModel
    rows: tuple[DiagnosisTableRowViewModel, ...]
    detail_card: CardPropertyFieldsViewModel | None
