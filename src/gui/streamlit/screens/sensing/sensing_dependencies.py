# src/gui/streamlit/screens/sensing/sensing_dependencies.py

from dataclasses import dataclass

from src.application.use_cases.sensing.sensing_admin.build_view.build_sensing_admin_view_use_case import (
    BuildSensingAdministrationViewUseCase,
)

from src.interface_adapters.presenters.sensing.sensing_admin.sensing_admin_presenter import (
    SensingAdministrationPresenter,
)


@dataclass(frozen=True, slots=True)
class SensingPageDependencies:
    use_case: BuildSensingAdministrationViewUseCase
    presenter: SensingAdministrationPresenter
