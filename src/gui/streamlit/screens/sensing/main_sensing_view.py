# /src/gui/streamlit/screens/sensing/main_sensing_view.py

from src.application.use_cases.sensing.sensing_admin.get_device_admin_uc import (
    GetDevicesAdministrationRequestDTO,
    GetDeviceAdministrationResultDTO,
)

from src.gui.streamlit.screens.sensing.sensing_dependencies import (
    SensingPageDependencies
)

from src.gui.streamlit.screens.sensing.main_sensing_renderer import (
    render_main_sensing,
)

from src.interface_adapters.view_models.sensing.device_admin_view_models import (
    DevicesAdministrationViewModel,
)


def render_sensing_page(
        *,
        dependencies: SensingPageDependencies,
) -> None:
    request = GetDevicesAdministrationRequestDTO()

    result: GetDeviceAdministrationResultDTO = (
        dependencies
        .use_case
        .execute(
            request=request
        )
    )

    view_model: DevicesAdministrationViewModel = (
        dependencies
        .presenter
        .present(
            result=result,
        )
    )

    render_main_sensing(
        view_model=view_model,
    )
