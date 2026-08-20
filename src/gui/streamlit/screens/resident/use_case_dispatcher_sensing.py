# /src/gui/streamlit/screens/resident/use_case_dispatcher_sensing.py

from dataclasses import dataclass
from datetime import date, timedelta

# --- APPLICATION

from src.application.use_cases.sensing.device_profiles.user_sensing_account_uc_dtos import (
    UserSensingAccountRequestDTO,
    UserSensingAccountResultDTO,
)

from src.application.use_cases.sensing.trends.build_sensor_events_use_case import (
    SensorEventsRequestDTO,
    SensorEventsResultDTO,
)

from src.main.compose_root_application import AppContainer


@dataclass(frozen=True)
class SensingUseCaseResults:
    result_user_sensing_account: UserSensingAccountResultDTO
    result_sensor_events: SensorEventsResultDTO


def run_sensing_use_cases(
        app_container: AppContainer,
) -> SensingUseCaseResults:
    request_usa = UserSensingAccountRequestDTO(
        user_id=app_container.user_context.user_id,
    )

    result_user_sensing_account: UserSensingAccountResultDTO = (
        app_container.get_user_sensing_account_use_case.execute(
            request=request_usa,
        ))

    """
    CHANGE!  ok for dev
    """

    today: date = date.today()
    yesterday: date = today - timedelta(days=1)
    start_date: date = yesterday - timedelta(days=90)

    request_se = SensorEventsRequestDTO(
        sensor_ids=result_user_sensing_account.sensor_ids,
        start_date=start_date,
        end_date=yesterday,
    )

    result_sensor_events: SensorEventsResultDTO = (
        app_container.build_sensor_event_timeline_use_case.execute(
            request=request_se,
        ))

    return SensingUseCaseResults(
        result_user_sensing_account=result_user_sensing_account,
        result_sensor_events=result_sensor_events,
    )
