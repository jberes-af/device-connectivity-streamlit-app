# /src/gui/streamlit/screens/resident/sections/sensing_section.py

# No Streamlit calls

# from datetime import date, timedelta

from src.application.use_cases.sensing.device_profiles.user_sensing_account_uc_dtos import (
    UserSensingAccountRequestDTO,
    UserSensingAccountResultDTO,
)

# from src.application.use_cases.sensing.trends.build_sensor_events_use_case import (
# SensorEventsRequestDTO,
# SensorEventsResultDTO,
# )

from src.gui.streamlit.screens.resident.renderers.sensing_renderer import (
    render_resident_sensing,
)

from src.interface_adapters.view_models.sensing.resident_sensing_view_model import (
    SensorSectionViewModel,
)

from src.interface_adapters.presenters.sensing.resident_sensing_section_presenter import (
    ResidentSensingSectionPresenter)

from src.main.compose_root_application import AppContainer


def render_sensing_section(
        *,
        resident_id: str,
        container: AppContainer,
):
    request_user_sensing_account = UserSensingAccountRequestDTO(
        user_id=container.user_context.user_id,
    )

    result_user_sensing_account: UserSensingAccountResultDTO = (
        container.get_user_sensing_account_use_case.execute(
            request=request_user_sensing_account,
        ))

    """
    TBD: built plotly charts for trend / sparkline graphs
    # Development Hard-code
    today: date = date.today()
    yesterday: date = today - timedelta(days=1)
    start_date: date = yesterday - timedelta(days=90)

    request_sensor_events = SensorEventsRequestDTO(
        sensor_ids=result_user_sensing_account.sensor_ids,
        start_date=start_date,
        end_date=yesterday,
    )

    result_sensor_events: SensorEventsResultDTO = (
        container.build_sensor_event_timeline_use_case.execute(
            request=request_sensor_events,
        ))

    vm: ResidentSectionViewModel = (
        ResidentSensingSectionPresenter()
        .present_sensing_section(
            result_sensor_events.
        )
    )

    """

    if result_user_sensing_account is None:
        return None

    vm_sensing_dashboard: SensorSectionViewModel = (
        ResidentSensingSectionPresenter()
        .present_sensing_section(
            result_user_sensing_account
        )
    )

    render_resident_sensing(
        resident_id=resident_id,
        section_dash_vm=vm_sensing_dashboard,
    )
