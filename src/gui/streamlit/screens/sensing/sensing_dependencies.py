# src/gui/streamlit/screens/sensing/sensing_dependencies.py

from dataclasses import dataclass

from src.application.use_cases.sensing.sensing_admin.get_device_admin_uc import (
    GetDeviceAdministrationUseCase,
)

from src.interface_adapters.presenters.sensing.device_admin.device_admin_presenter import (
    DeviceAdministrationPresenter,
)


@dataclass(frozen=True, slots=True)
class SensingPageDependencies:
    use_case: GetDeviceAdministrationUseCase
    presenter: DeviceAdministrationPresenter
