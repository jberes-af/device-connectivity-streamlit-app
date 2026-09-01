# /src/infrastructure/persistence/aws/appsync_last_seen_adapter.py

from datetime import datetime, timezone

import requests

from src.application.ports.sensing.sensor_connectivity_status_port import (
    SensorConnectivityStatusPort,
)

from src.domain.entities.sensing.sensor_connectivity_entities import (
    SensorConnectivityStatus,
)


class AppSyncSensorConnectivityAdapter(
    SensorConnectivityStatusPort,
):
    GET_DEVICE_CONNECTIVITY = """
    query GetDeviceConnectivity($deviceId: ID!) {
      getDeviceConnectivity(deviceId: $deviceId) {
        deviceId
        connectivityState
        lastSeenAt
        statusAt
      }
    }
    """

    def __init__(
            self,
            *,
            endpoint: str,
            api_key: str,
    ) -> None:
        self._endpoint = endpoint
        self._api_key = api_key

    def get_status(
            self,
            *,
            sensor_id: str,
    ) -> SensorConnectivityStatus | None:

        if not self._api_key.strip():
            return None

        payload = {
            "query": self.GET_DEVICE_CONNECTIVITY,
            "variables": {
                "deviceId": sensor_id,
            },
        }

        response = requests.post(
            self._endpoint,
            headers={
                "Content-Type": "application/json",
                "x-api-key": self._api_key,
            },
            json=payload,
            timeout=10,
        )

        response.raise_for_status()

        result = response.json()

        if result.get("errors"):
            return None

        connectivity = (
            result
            .get("data", {})
            .get("getDeviceConnectivity")
        )

        if not connectivity:
            return None

        last_seen_sec = _normalize_epoch_seconds(
            connectivity.get("lastSeenAt")
        )

        status_at_sec = _normalize_epoch_seconds(
            connectivity.get("statusAt")
        )

        last_seen_at_utc = (
            datetime.fromtimestamp(
                last_seen_sec,
                tz=timezone.utc,
            )
            if last_seen_sec is not None
            else None
        )

        status_at_utc = (
            datetime.fromtimestamp(
                status_at_sec,
                tz=timezone.utc,
            )
            if status_at_sec is not None
            else None
        )

        return SensorConnectivityStatus(
            sensor_id=sensor_id,
            last_seen_at_utc=last_seen_at_utc,
            status_at_utc=status_at_utc,
            connectivity_state=connectivity.get(
                "connectivityState"
            ),
        )


def _normalize_epoch_seconds(
        value: int | float | str | None,
) -> int | None:
    if value is None:
        return None

    ts = int(value)

    if ts > 10_000_000_000:
        ts //= 1000

    return ts
