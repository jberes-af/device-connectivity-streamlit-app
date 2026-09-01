# /src/main/infrastructure_containers/compose_root_aws_appsync.py

from src.application.ports.sensing.sensor_connectivity_status_port import (
    SensorConnectivityStatusPort,
)

from src.infrastructure.config.settings_model import (
    Settings,
)

from src.infrastructure.persistence.aws.appsync_last_seen_adapter import (
    AppSyncSensorConnectivityAdapter,
)


def build_aws_appsync_adapter(
        *,
        settings: Settings,
) -> SensorConnectivityStatusPort:
    return AppSyncSensorConnectivityAdapter(
        endpoint=settings.appsync.endpoint,
        api_key=settings.appsync.api_key,
    )
