# /src/main/infrastructure_containers/firebase_repositories.py

from dataclasses import dataclass

from src.application.ports.sensing.device_ports import (
    GatewayRepositoryPort,
    SensorDeviceRepositoryPort, SensorEventRepositoryPort,
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
from src.infrastructure.persistence.firebase.repos.sensor_device_repository import (
    FirebaseSensorDeviceRepository,
)

from src.infrastructure.persistence.firebase.repos.sensor_event_repository import (
    FirebaseSensorEventRepository,
)

from src.infrastructure.persistence.firebase.repos.user_sensing_repository import (
    FirebaseUserSensingRepository,
)


@dataclass(frozen=True, slots=True)
class FirebaseSensingRepositories:
    gateway_repository: GatewayRepositoryPort
    sensor_device_repository: SensorDeviceRepositoryPort
    sensor_event_repository: SensorEventRepositoryPort
    user_sensing_repository: UserSensingRepositoryPort


def build_firebase_sensing_repositories(
        database: RealtimeDatabasePort,
) -> FirebaseSensingRepositories:
    return FirebaseSensingRepositories(
        gateway_repository=FirebaseGatewayRepository(database=database),
        sensor_device_repository=FirebaseSensorDeviceRepository(database=database),
        sensor_event_repository=FirebaseSensorEventRepository(database=database),
        user_sensing_repository=FirebaseUserSensingRepository(database=database),
    )
