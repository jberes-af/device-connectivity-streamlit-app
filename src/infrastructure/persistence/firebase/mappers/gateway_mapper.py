from __future__ import annotations

from typing import Any, Mapping

from firebase.schemas.gateway_schema import GatewayRtdbSchema

# Adjust this import to match your project.
from src.domain.entities.device.gateway_entities import GatewayProfile


class GatewayRtdbMapper:
    @staticmethod
    def to_domain(
        gateway_id: str,
        tenant_id: str,
        data: Mapping[str, Any] | None,
    ) -> GatewayProfile:
        _ = data or {}

        # GatewayProfile is intentionally kept persistence-neutral.
        # Add sensor/user association objects separately rather than embedding
        # Firebase node structure in the entity.
        return GatewayProfile(
            gateway_id=gateway_id,
            tenant_id=tenant_id,
        )

    @staticmethod
    def to_rtdb(entity: GatewayProfile) -> dict[str, Any]:
        # GatewayProfile currently has no RTDB-specific mutable fields.
        # Return an empty payload until domain fields are added.
        return {}
