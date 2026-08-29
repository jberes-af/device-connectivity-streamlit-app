# src/gui/streamlit/screens/sensing/sensing_dependencies.py

from dataclasses import dataclass

from src.application.use_cases.sensing.sensing_admin.get_devices_overview_uc import (
    GetDevicesOverviewUseCase,
)


@dataclass(frozen=True, slots=True)
class SensingPageDependencies:
    use_case: GetDevicesOverviewUseCase
    presenter: SensingPagePresenter
