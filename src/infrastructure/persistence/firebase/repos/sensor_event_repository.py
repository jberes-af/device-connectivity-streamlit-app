# /src/infrastructure/persistence/firebase/repos/sensor_event_repository.py

from src.domain.entities.sensing.device_entities import SensorEvent

from src.application.ports.sensing.realtime_database_port import (
    RealtimeDatabasePort)

from src.application.ports.sensing.device_ports import SensorEventRepositoryPort

from src.infrastructure.persistence.firebase.mappers.sensor_event_mapper import (
    build_raw_sensor_event_objects_from_all,
    build_raw_sensor_event_objects_from_last,
    SensorEventDomainMapper,
    SensorEventRtdbMapper,
)

from src.infrastructure.persistence.firebase.schemas.sensor_schema import (
    SensorEventRtdbSchema,
)


class FirebaseSensorEventRepository(SensorEventRepositoryPort):

    def __init__(self, database: RealtimeDatabasePort) -> None:
        self._database = database

    def get_all_sensor_events(
            self,
            sensor_id: str,
    ) -> tuple[SensorEvent, ...]:
        raw = self._database.read_node(
            SensorEventRtdbSchema.sensor_event_all_path(sensor_id)
        )

        if raw is None:
            return ()

        raw_objects = build_raw_sensor_event_objects_from_all(
            sensor_id=sensor_id,
            data=raw,
        )

        rtdb_objects = SensorEventRtdbMapper.from_raw(
            raw_events=raw_objects,
        )

        domain_events: list[SensorEvent] = (
            SensorEventDomainMapper.many_to_domain(
                dto=rtdb_objects,
            )
        )

        domain_events.sort(
            key=lambda event: event.activated_at_utc,
        )

        return tuple(domain_events)

    def get_last_sensor_event(
            self,
            sensor_id: str,
    ) -> SensorEvent | None:
        raw = self._database.read_node(
            SensorEventRtdbSchema.sensor_event_last_path(sensor_id)
        )

        if raw is None:
            return None

        raw_objects = build_raw_sensor_event_objects_from_last(
            sensor_id=sensor_id,
            data=raw,
        )

        rtdb_objects = SensorEventRtdbMapper.from_raw(
            raw_events=raw_objects,
        )

        if not rtdb_objects:
            return None

        latest = max(
            rtdb_objects,
            key=lambda event: event.timestamp_utc,
        )

        return SensorEventDomainMapper.to_domain(latest)
