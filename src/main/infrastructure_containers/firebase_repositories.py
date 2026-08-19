# /src/main/infrastructure_containers/firebase_repositories.py

from dataclasses import dataclass

from src.application.ports.sensing.device_ports import (
    GatewayRepositoryPort,
    SensorRepositoryPort,
)
from src.application.ports.sensing.user_sensing_port import (
    UserSensingRepositoryPort,
)
from src.application.ports.sensing.realtime_database_port import (
    RealtimeDatabasePort,
)

from src.infrastructure.persistence.firebase.repos.gateway_repository import (
    FirebaseGatewayRepository,
)
from src.infrastructure.persistence.firebase.repos.sensor_repository import (
    FirebaseSensorRepository,
)
from src.infrastructure.persistence.firebase.repos.user_sensing_repository import (
    FirebaseUserSensingRepository,
)


@dataclass(frozen=True, slots=True)
class FirebaseSensingRepositories:
    gateway_repository: GatewayRepositoryPort
    sensor_repository: SensorRepositoryPort
    user_sensing_repository: UserSensingRepositoryPort


def build_firebase_sensing_repositories(
        database: RealtimeDatabasePort,
) -> FirebaseSensingRepositories:
    return FirebaseSensingRepositories(
        gateway_repository=FirebaseGatewayRepository(database=database),
        sensor_repository=FirebaseSensorRepository(database=database),
        user_sensing_repository=FirebaseUserSensingRepository(database=database),
    )
