# /src/infrastructure/persistence/firebase/mappers/sensor_device_mappers.py

from dataclasses import dataclass
from typing import Any, Mapping

from src.domain.entities.sensing.device_entities import (
    SensorSystemProfile,
)

from src.infrastructure.persistence.firebase.schemas.sensor_schema import (
    SensorSystemRtdbSchema,
)


@dataclass(frozen=True, slots=True)
class SensorSystemRtdbDTO:
    sensor_id: str
    brand: str
    sensor_type: str
    icon: str | None = None


class SensorRtdbMapper:

    @staticmethod
    def system_from_raw(
            *,
            sensor_id: str,
            data: Mapping[str, Any] | None,
    ) -> SensorSystemRtdbDTO:
        raw = data or {}

        return SensorSystemRtdbDTO(
            sensor_id=sensor_id,
            brand=str(
                raw.get(SensorSystemRtdbSchema.FIELD_BRAND, "") or ""
            ),
            sensor_type=str(
                raw.get(SensorSystemRtdbSchema.FIELD_TYPE, "") or ""
            ),
            icon=(
                str(raw[SensorSystemRtdbSchema.FIELD_ICON])
                if raw.get(SensorSystemRtdbSchema.FIELD_ICON) is not None
                else None
            ),
        )


class SensorDeviceDomainMapper:

    @staticmethod
    def system_to_domain(
            *,
            dto: SensorSystemRtdbDTO,
            tenant_id: str | None = None,
    ) -> SensorSystemProfile:
        return SensorSystemProfile(
            sensor_id=dto.sensor_id,
            tenant_id=tenant_id,
            brand=dto.brand,
            sensor_type=dto.sensor_type,
            icon=dto.icon,
        )
