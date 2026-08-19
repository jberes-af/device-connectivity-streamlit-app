# /src/interface_adapters/presenters/resident/demo_top_metrics_presenter.py

from src.interface_adapters.view_models.common.metric_view_model import (
    MetricViewModel,
)

from src.interface_adapters.view_models.common.card_grid_view_model import (
    CardGridViewModel,
)


class DemoResidentDashMetricsPresenter:

    @staticmethod
    def present() -> CardGridViewModel:
        return CardGridViewModel(
            columns=3,
            cards=(
                MetricViewModel(
                    label="Today's Priority Items",
                    value="8",
                    delta="+2",
                    help_text="Items requiring attention.",
                ),
                MetricViewModel(
                    label="Care Plan Assessment",
                    value="91%",
                    delta="-1.6%",
                    help_text="Current care plan compliance.",
                ),
                MetricViewModel(
                    label="Care Exceptions",
                    value="2",
                    delta=None,
                    help_text="Count of missed, delayed, or declined care delivery.",
                ),
            ),
        )
