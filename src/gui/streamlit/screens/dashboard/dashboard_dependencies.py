from dataclasses import dataclass

from src.application.use_cases.dashboard.build_main_dashboard_use_case import (
    BuildMainDashboardUseCase,
)

from src.interface_adapters.presenters.dashboard.dashboard_main_presenter import (
    DashboardMainPagePresenter,
)


@dataclass(frozen=True, slots=True)
class DashboardPageDependencies:
    use_case: BuildMainDashboardUseCase
    presenter: DashboardMainPagePresenter
