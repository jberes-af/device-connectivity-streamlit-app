from __future__ import annotations

from firebase.mappers.gateway_mapper import GatewayRtdbMapper
from firebase.repositories._protocols import RtdbClientProtocol
from firebase.schemas.gateway_schema import GatewayRtdbSchema

from src.domain.entities.device.gateway_entities import GatewayProfile


class FirebaseGatewayRepository:
    def __init__(self, client: RtdbClientProtocol) -> None:
        self._client = client

    def get(
        self,
        gateway_id: str,
        tenant_id: str,
    ) -> GatewayProfile | None:
        raw = self._client.get(
            GatewayRtdbSchema.gateway_path(gateway_id)
        )

        if raw is None:
            return None

        return GatewayRtdbMapper.to_domain(
            gateway_id=gateway_id,
            tenant_id=tenant_id,
            data=raw,
        )

    def save(self, entity: GatewayProfile) -> None:
        self._client.set(
            GatewayRtdbSchema.gateway_path(entity.gateway_id),
            GatewayRtdbMapper.to_rtdb(entity),
        )
