# /src/infrastructure/persistence/firebase/mappers/gateway_mappers.py

from dataclasses import dataclass
from typing import Any, Mapping

from src.application.models.sensing_models import GatewayDomainObjects
from src.infrastructure.persistence.firebase.schemas.gateway_schema import (
    GatewayRtdbSchema)

from src.domain.entities.sensing.device_entities import (
    GatewayProfile,
    GatewaySensorLink,
)

from src.domain.entities.sensing.user_sensing_entities import (
    UserGatewayLink,
)


@dataclass(frozen=True, slots=True)
class GatewayRtdbDTO:
    timezone_name: str | None
    utc_offset: str | None
    sensor_ids: tuple[str, ...]
    user_ids: tuple[str, ...]


class GatewayRtdbMapper:

    @staticmethod
    def from_raw(
            data: Mapping[str, Any],
    ) -> GatewayRtdbDTO:
        return GatewayRtdbDTO(
            timezone_name=None,
            utc_offset=None,
            sensor_ids=tuple(
                data.get(GatewayRtdbSchema.FIELD_SENSORS, [])
            ),
            user_ids=tuple(
                data.get(GatewayRtdbSchema.FIELD_USERS, [])
            ),
        )

    @staticmethod
    def to_rtdb(entity: GatewayProfile) -> dict[str, Any]:
        # GatewayProfile currently has no RTDB-specific mutable fields.
        # Return an empty payload until domain fields are added.
        return {}


class GatewayDomainMapper:

    @staticmethod
    def to_domain(
            *,
            gateway_id: str,
            dto: GatewayRtdbDTO,
    ) -> GatewayDomainObjects:
        return GatewayDomainObjects(
            gateway_profile=GatewayProfile(
                gateway_id=gateway_id,
                timezone=dto.timezone_name,
            ),
            gateway_sensor_links=tuple(
                GatewaySensorLink(
                    gateway_id=gateway_id,
                    sensor_id=sensor_id,
                )
                for sensor_id in dto.sensor_ids
            ),
            gateway_user_links=tuple(
                UserGatewayLink(
                    user_id=user_id,
                    gateway_id=gateway_id,
                )
                for user_id in dto.user_ids
            ),
        )
