# /src/application/use_cases/build_sensor_events_use_case.py

from src.domain.entities.sensing.device_entities import SensorEvent
from src.domain.entities.sensing.sensor_connectivity_entities import (
    SensorConnectivityStatus
)

from src.application.ports.sensing.sensor_connectivity_status_port import (
    SensorConnectivityStatusPort
)

from src.application.ports.sensing.device_ports import (
    SensorEventRepositoryPort,
)

from src.application.use_cases.sensing.live_status.sensor_connectivity_uc_dtos import (
    SensorLastSeenDTO,
    MostRecentSensorEventDTO,
    GetSensorLiveStatusRequestDTO,
    GetSensorLiveStatusResultDTO,
)


class GetSensorLiveStatusUseCase:

    def __init__(
            self,
            *,
            appsync_connectivity_port: SensorConnectivityStatusPort,
            sensor_event_repository: SensorEventRepositoryPort,
    ) -> None:
        self._connectivity_port = appsync_connectivity_port
        self._event_repo = sensor_event_repository

    def execute(
            self,
            request: GetSensorLiveStatusRequestDTO,
    ) -> GetSensorLiveStatusResultDTO:
        sensor_online_statuses: list[SensorLastSeenDTO] = []
        most_recent_events: list[MostRecentSensorEventDTO] = []

        for sensor_id in request.sensor_ids:
            connectivity: SensorConnectivityStatus = self._connectivity_port.get_status(
                sensor_id=sensor_id,
            )

            last_event: SensorEvent = self._event_repo.get_last_sensor_event(
                sensor_id=sensor_id,
            )

            sensor_online_statuses.append(
                SensorLastSeenDTO(
                    sensor_id=sensor_id,
                    last_seen_at_utc=(
                        connectivity.last_seen_at_utc
                        if connectivity is not None
                        else None
                    ),
                    status_at_utc=(
                        connectivity.status_at_utc
                        if connectivity is not None
                        else None
                    ),
                    connectivity_state=(
                        connectivity.connectivity_state
                        if connectivity is not None
                        else None
                    ),
                )
            )

            most_recent_events.append(
                MostRecentSensorEventDTO(
                    sensor_id=sensor_id,
                    activated_at=(
                        last_event.activated_at_utc
                        if last_event is not None
                        else None
                    ),
                )
            )

        return GetSensorLiveStatusResultDTO(
            sensor_online_statuses=tuple(sensor_online_statuses),
            most_recent_events=tuple(most_recent_events),
        )
