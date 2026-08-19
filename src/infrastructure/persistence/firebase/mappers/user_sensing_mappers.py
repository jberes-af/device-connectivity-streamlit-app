# /src/infrastructure/persistence/firebase/mappers/user_sensing_mappers.py

from dataclasses import dataclass
from typing import Any, Mapping

from src.application.models.sensing_models import UserSensingDomainObjects
from src.infrastructure.persistence.firebase.schemas.user_sensing_schema import (
    UserRtdbSchema,
)

from src.domain.entities.sensing.user_sensing_entities import (
    UserSensingAccount,
    UserSensorProfile,
    UserAdlSensorLink,
    UserAlertaRoutineLink,
    UserGatewayLink,
    UserSensorLink
)


@dataclass(frozen=True, slots=True)
class SensorUserRtdbDTO:
    sensor_id: str
    name: str
    location: str
    zone: str


@dataclass(frozen=True, slots=True)
class UserRtdbDTO:
    user_name: str
    email_rtdb: str
    email_auth: str | None
    telephone: str
    adl_objects: Any
    routine_ids: tuple[str, ...]
    sensor_profiles: tuple[SensorUserRtdbDTO, ...]
    gateway_ids: tuple[str, ...]
    grouping: Any | None = None
    notes: Any | None = None
    journal: Any | None = None
    settings: Any | None = None


class UserRtdbMapper:

    @staticmethod
    def from_raw(
            data: Mapping[str, Any],
    ) -> UserRtdbDTO:
        account = data.get(UserRtdbSchema.COLLECTION_ACCOUNT, {})

        user_name = str(
            account.get(UserRtdbSchema.FIELD_NAME, "") or ""
        )
        telephone = str(
            account.get(UserRtdbSchema.FIELD_TELEPHONE, "") or ""
        )
        email_rtdb = str(
            account.get(UserRtdbSchema.FIELD_EMAIL_RTDB, "") or ""
        )

        routines = data.get(UserRtdbSchema.FIELD_ROUTINE_IDS, {})
        routine_ids = tuple(routines.keys()) if isinstance(routines, Mapping) else ()

        gateways = data.get(UserRtdbSchema.COLLECTION_GATEWAY_IDS, {})
        gateway_ids = tuple(gateways.keys()) if isinstance(gateways, Mapping) else ()

        devices = data.get(UserRtdbSchema.COLLECTION_SENSOR_IDS, {})

        sensor_profiles = tuple(
            SensorUserRtdbDTO(
                sensor_id=sensor_id,
                name=str(profile.get("name", "") or ""),
                location=str(profile.get("location", "") or ""),
                zone=str(profile.get("zone", "") or ""),
            )
            for sensor_id, profile in devices.items()
            if isinstance(profile, Mapping)
        )

        return UserRtdbDTO(
            user_name=user_name,
            email_rtdb=email_rtdb,
            email_auth=None,
            telephone=telephone,
            adl_objects=data.get(UserRtdbSchema.FIELD_ADL_ENTITIES),
            routine_ids=routine_ids,
            sensor_profiles=sensor_profiles,
            gateway_ids=gateway_ids,
        )

    """
    @staticmethod
    def to_rtdb(entity: UserAccount) -> dict[str, Any]:
        profile = entity.user_profile

        return {
            UserRtdbSchema.FIELD_NAME: profile.user_name,
            UserRtdbSchema.FIELD_TELEPHONE: profile.user_telephone,
            UserRtdbSchema.FIELD_EMAIL: profile.user_email_address,
        }
    """


class UserDomainMapper:

    @staticmethod
    def to_domain(
            *,
            user_id: str,
            tenant_id: str,
            dto: UserRtdbDTO,
    ) -> UserSensingDomainObjects:
        return UserSensingDomainObjects(
            user_profile=UserSensingAccount(
                user_id=user_id,
                user_name=dto.user_name,
                telephone=dto.telephone,
                email_address=dto.email_rtdb,
            ),
            user_sensor_links=tuple(
                UserSensorLink(
                    tenant_id=tenant_id,
                    user_id=user_id,
                    sensor_id=s.sensor_id,
                )
                for s in dto.sensor_profiles
            ),
            user_gateway_links=tuple(
                UserGatewayLink(
                    tenant_id=tenant_id,
                    user_id=user_id,
                    gateway_id=g,
                )
                for g in dto.gateway_ids
            ),
            adl_sensor_links=tuple(
                UserAdlSensorLink(
                    user_id=user_id,
                    activity=record,
                )
                for record in dto.adl_objects
            ),
            alerta_routine_links=tuple(
                UserAlertaRoutineLink(
                    user_id=user_id,
                    routine_id=record,
                )
                for record in dto.routine_ids
            ),

            user_sensor_profiles=tuple(
                UserSensorProfile(
                    sensor_id=record.sensor_id,
                    name=record.name,
                    location=record.location,
                    zone=record.zone,
                )
                for record in dto.sensor_profiles
            ),
        )
