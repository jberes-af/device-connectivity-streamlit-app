from __future__ import annotations

from typing import Any, Mapping

from firebase.schemas.sensor_schema import (
    SensorSystemRtdbSchema,
    SensorUserRtdbSchema,
)

# Adjust these imports to match your project.
from src.domain.entities.device.sensor_entities import (
    SensorProfile,
    SensorProfileSystemConfiguration,
    SensorProfileUserConfiguration,
)


class SensorRtdbMapper:
    @staticmethod
    def system_to_domain(
        sensor_id: str,
        data: Mapping[str, Any] | None,
    ) -> SensorProfileSystemConfiguration:
        raw = data or {}

        return SensorProfileSystemConfiguration(
            sensor_id=sensor_id,
            brand=str(raw.get(SensorSystemRtdbSchema.FIELD_BRAND, "") or ""),
            sensor_type=str(raw.get(SensorSystemRtdbSchema.FIELD_TYPE, "") or ""),
            icon=raw.get(SensorSystemRtdbSchema.FIELD_ICON),
            hardware_version=None,
            firmware_version=None,
        )

    @staticmethod
    def user_config_to_domain(
        sensor_id: str,
        data: Mapping[str, Any] | None,
    ) -> SensorProfileUserConfiguration:
        raw = data or {}

        return SensorProfileUserConfiguration(
            sensor_id=sensor_id,
            name=raw.get(SensorUserRtdbSchema.FIELD_NAME),
            location=raw.get(SensorUserRtdbSchema.FIELD_LOCATION),
            zone=raw.get(SensorUserRtdbSchema.FIELD_ZONE),
            image=raw.get(SensorUserRtdbSchema.FIELD_IMAGE),
            color=None,
        )

    @staticmethod
    def to_domain(
        sensor_id: str,
        tenant_id: str,
        system_data: Mapping[str, Any] | None,
        user_data: Mapping[str, Any] | None = None,
    ) -> SensorProfile:
        return SensorProfile(
            sensor_id=sensor_id,
            tenant_id=tenant_id,
            system_configuration=SensorRtdbMapper.system_to_domain(
                sensor_id=sensor_id,
                data=system_data,
            ),
            user_configuration=SensorRtdbMapper.user_config_to_domain(
                sensor_id=sensor_id,
                data=user_data,
            ) if user_data is not None else None,
        )

    @staticmethod
    def system_to_rtdb(
        entity: SensorProfileSystemConfiguration,
    ) -> dict[str, Any]:
        return {
            SensorSystemRtdbSchema.FIELD_BRAND: entity.brand,
            SensorSystemRtdbSchema.FIELD_TYPE: entity.sensor_type,
            SensorSystemRtdbSchema.FIELD_ICON: entity.icon,
        }

    @staticmethod
    def user_config_to_rtdb(
        entity: SensorProfileUserConfiguration,
    ) -> dict[str, Any]:
        return {
            SensorUserRtdbSchema.FIELD_NAME: entity.name,
            SensorUserRtdbSchema.FIELD_LOCATION: entity.location,
            SensorUserRtdbSchema.FIELD_ZONE: entity.zone,
            SensorUserRtdbSchema.FIELD_IMAGE: entity.image,
        }
