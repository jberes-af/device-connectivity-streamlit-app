# /src/infrastructure/persistence/firebase/repos/gateway_repository.py

from src.domain.entities.sensing.device_entities import GatewayProfile

from src.application.models.sensing_models import GatewayDomainObjects

from src.application.ports.sensing.realtime_database_port import (
    RealtimeDatabasePort)

from src.application.ports.sensing.device_ports import GatewayRepositoryPort

from src.infrastructure.persistence.firebase.mappers.gateway_mappers import (
    GatewayDomainMapper,
    GatewayRtdbMapper,
    GatewayRtdbDTO,
)

from src.infrastructure.persistence.firebase.schemas.gateway_schema import (
    GatewayRtdbSchema
)


class FirebaseGatewayRepository(GatewayRepositoryPort):

    def __init__(self, database: RealtimeDatabasePort) -> None:
        self._database = database

    def get(
            self,
            gateway_id: str,
    ) -> GatewayDomainObjects | None:
        raw = self._database.read_node(
            GatewayRtdbSchema.gateway_path(gateway_id)
        )

        if raw is None:
            return None

        rtdb_objects: GatewayRtdbDTO = GatewayRtdbMapper.from_raw(raw)

        return GatewayDomainMapper.to_domain(
            gateway_id=gateway_id,
            dto=rtdb_objects,
        )

    def save(self, gateway: GatewayProfile) -> None:
        self._database.update_paths(
            {
                GatewayRtdbSchema.gateway_path(gateway.gateway_id):
                    GatewayRtdbMapper.to_rtdb(gateway)
            }
        )
