# /src/application/services/get_sensor_service.py


from src.application.ports.sensing.realtime_database_port import (
    RealtimeDatabasePort,
)

class GetSensorService:

    def __init__(
        self,
        sensor_repository: RealtimeDatabasePort,
    ) -> None:
        self._sensor_repository = sensor_repository

    def execute(
        self,
        request: GetSensorRequestDTO,
    ) -> GetSensorResponseDTO:

        sensor = self._sensor_repository.get(
            sensor_id=request.sensor_id,
            tenant_id=request.tenant_id,
        )

        ...