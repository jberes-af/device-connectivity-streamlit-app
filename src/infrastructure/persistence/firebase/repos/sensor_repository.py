# /src/infrastructure/persistence/firebase/repos/sensor_repository.py


from src.application.ports.sensing.realtime_database_port import RtdbClientPort


from src.infrastructure.persistence.firebase.mappers.sensor_mapper import SensorRtdbMapper
from src.infrastructure.persistence.firebase.schemas.sensor_schema import (
    SensorSystemRtdbSchema,
    SensorUserRtdbSchema,
)

from src.domain.entities.device.sensor_entities import SensorProfile


class FirebaseSensorRepository:
    def __init__(self, client: RtdbClientPort) -> None:
        self._client = client

    def get(
        self,
        sensor_id: str,
        tenant_id: str,
        user_id: str | None = None,
    ) -> SensorProfile | None:
        system_data = self._client.get(
            SensorSystemRtdbSchema.sensor_path(sensor_id)
        )

        if system_data is None:
            return None

        user_data = None
        if user_id is not None:
            user_data = self._client.get(
                SensorUserRtdbSchema.sensor_path(
                    user_id=user_id,
                    sensor_id=sensor_id,
                )
            )

        return SensorRtdbMapper.to_domain(
            sensor_id=sensor_id,
            tenant_id=tenant_id,
            system_data=system_data,
            user_data=user_data,
        )

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
