# /src/infrastructure/persistence/firebase/mappers/sensor_rtdb_mapper.py

class SensorRtdbMapper:

    @staticmethod
    def to_domain(
        sensor_id: str,
        data: dict,
    ) -> SensorSystem:
        return SensorSystem(
            sensor_id=sensor_id,
            brand=data.get(SensorRtdbSchema.FIELD_BRAND, ""),
            sensor_type=data.get(SensorRtdbSchema.FIELD_TYPE, ""),
            icon=data.get(SensorRtdbSchema.FIELD_ICON),
        )