# /src/infrastructure/persistence/firebase/repos/sensor_device_repository.py

from src.domain.entities.sensing.device_entities import SensorSystemProfile

from src.application.ports.sensing.realtime_database_port import (
    RealtimeDatabasePort)

from src.application.ports.sensing.device_ports import SensorDeviceRepositoryPort

from src.infrastructure.persistence.firebase.mappers.sensor_device_mappers import (
    SensorSystemRtdbDTO,
    SensorRtdbMapper,
    SensorDeviceDomainMapper,
)
# from src.application.models.sensing_models import SensorDomainObjects

from src.infrastructure.persistence.firebase.schemas.sensor_schema import (
    SensorSystemRtdbSchema,
    # SensorUserRtdbSchema,
)


class FirebaseSensorDeviceRepository(SensorDeviceRepositoryPort):

    def __init__(self, database: RealtimeDatabasePort) -> None:
        self._database = database

    def get(
            self,
            sensor_id: str,
            tenant_id: str,
    ) -> SensorSystemProfile | None:
        raw = self._database.read_node(
            SensorSystemRtdbSchema.sensor_path(sensor_id)
        )

        if raw is None:
            return None

        rtdb_objects: SensorSystemRtdbDTO = SensorRtdbMapper.system_from_raw(
            sensor_id=sensor_id,
            data=raw,
        )

        return SensorDeviceDomainMapper.system_to_domain(
            dto=rtdb_objects,
        )

    """
    def save_system(self, entity: SensorProfile) -> None:
        self._client.set(
            SensorSystemRtdbSchema.sensor_path(entity.sensor_id),
            SensorRtdbMapper.system_to_rtdb(entity.system_configuration),
        )

    def save_user_configuration(
        self,
        user_id: str,
        entity: SensorProfile,
    ) -> None:
        if entity.user_configuration is None:
            return

        self._client.set(
            SensorUserRtdbSchema.sensor_path(
                user_id=user_id,
                sensor_id=entity.sensor_id,
            ),
            SensorRtdbMapper.user_config_to_rtdb(
                entity.user_configuration
            ),
        )
    """
