# /src/interface_adapters/view_models/common/metric_view_model.py

from dataclasses import dataclass


@dataclass(frozen=True)
class MetricViewModel:
    label: str
    value: str
    delta: str | None = None
    help_text: str | None = None
