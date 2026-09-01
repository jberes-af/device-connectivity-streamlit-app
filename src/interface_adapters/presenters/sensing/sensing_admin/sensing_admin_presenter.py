# /src/interface_adapters/presenters/sensing/sensing_admin/sensing_admin_presenter.py

from datetime import datetime
from enum import StrEnum

# from src.domain.entities.tenant.tenant_entities import TenantProfile

from src.application.use_cases.sensing.sensing_admin.build_view.build_admin_view_uc_dtos import (
    GatewayProfileDTO,
    SensorProfileDTO,
    TenantProfileDTO,
    SensorLastSeenDTO,
    MostRecentSensorEventDTO,
    BuildSensingAdminViewResultDTO,
)

from src.interface_adapters.view_models.sensing.device_admin_view_models import (
    SensingSummaryViewModel,
    SensingAdministrationViewModel,
    GatewayOverviewRowViewModel,
    SensorOverviewRowViewModel,
    OfflineSensorRowViewModel,
    TenantOptionViewModel,
)

from src.interface_adapters.presenters.utils_presenters import (
    format_date,
    format_datetime,
    format_utc_to_timezone,
)

_DEFAULT_TIME_ZONE: str = "America/New_York"


class SensingAdministrationPresenter:

    def present(
            self,
            *,
            result: BuildSensingAdminViewResultDTO,
    ) -> SensingAdministrationViewModel:
        # --- TENANTS

        tenants: tuple[TenantOptionViewModel, ...] = (
            self._present_tenants(
                profiles=result.tenant_profiles,
            ))

        # --- GATEWAYS

        gateway_rows = tuple(
            self._present_gateway(profile)
            for profile in result.gateway_profiles
        )

        # --- SENSORS

        sensor_count = len(result.sensor_profiles)

        sensor_rows = tuple(
            self._present_sensor(profile)
            for profile in result.sensor_profiles
        )

        assigned_sensor_count: int = sum(
            1
            for profile in result.sensor_profiles
            if profile.attached_user_ids
        )

        online_sensor_count: int = sum(
            1
            for status in result.sensor_online_statuses
            if status.connectivity_state == "ONLINE"
        )

        offline_sensor_ids: tuple[str, ...] = ()
        if online_sensor_count:
            offline_sensor_ids = tuple([
                status.sensor_id
                for status in result.sensor_online_statuses
                if status.connectivity_state != "ONLINE"
            ])

        offline_sensor_count: int = sensor_count - online_sensor_count

        offline_sensor_percent = (
            100.0 * offline_sensor_count / sensor_count
            if sensor_count
            else 0.0
        )

        offline_sensors: tuple[OfflineSensorRowViewModel, ...] = (
            self._present_offline_sensor(
                profiles=result.sensor_profiles,
                connectivity_statuses=result.sensor_online_statuses,
                last_activations=result.most_recent_events,
                offline_sensor_ids=offline_sensor_ids,
            ))

        summary = SensingSummaryViewModel(
            sensor_count=sensor_count,
            gateway_count=len(result.gateway_profiles),
            assigned_sensor_count=assigned_sensor_count,
            unassigned_sensor_count=(
                    sensor_count - assigned_sensor_count
            ),
            online_sensor_count=online_sensor_count,
            offline_sensor_count=offline_sensor_count,
            offline_sensor_percent=offline_sensor_percent,
        )

        return SensingAdministrationViewModel(
            title="Tenant Devices",
            tenants=tenants,
            selected_tenant_name=result.selected_tenant_name,
            summary=summary,
            sensors=sensor_rows,
            gateways=gateway_rows,
            offline_sensors=offline_sensors,
        )

    @staticmethod
    def _present_tenants(
            profiles: tuple[TenantProfileDTO, ...]
    ) -> tuple[TenantOptionViewModel, ...]:
        vms = [
            TenantOptionViewModel(
                tenant_id=record.tenant_id,
                tenant_name=record.tenant_name,
                tenant_name_label=f"{record.tenant_name} • {record.tenant_id}",
                # tenant_type=record.tenant_type,
                # tenant_street=record.tenant_street,
                # tenant_city=record.tenant_city,
                # tenant_state=record.tenant_state,
                # tenant_postal_code=record.tenant_postal_code,
                # tenant_display_state_zip=f"{record.tenant_state} • {record.tenant_postal_code}",
                # tenant_telephone=record.tenant_telephone,
                # tenant_manager=record.tenant_manager,
            )
            for record in profiles
        ]

        return tuple(
            sorted(
                vms,
                key=lambda vm: vm.tenant_name.casefold(),
            )
        )

    def _present_sensor(
            self,
            profile: SensorProfileDTO,
    ) -> SensorOverviewRowViewModel:
        return SensorOverviewRowViewModel(
            sensor_id=profile.sensor_id,
            sensor_type=self._enum_label(profile.sensor_type),
            name=self._text(profile.name),
            location=self._text(profile.location),
            zone=self._text(profile.zone),

            paired_gateway_id=self._text(
                profile.paired_gateway_id
            ),

            attached_user_count=len(
                profile.attached_user_ids
            ),

            attached_users=self._join(
                profile.attached_user_ids
            ),

            sensor_purpose=self._enum_label(
                profile.sensor_purpose
            ),

            firmware_version=self._text(
                profile.firmware_version
            ),

            hardware_version=self._text(
                profile.hardware_version
            ),

            install_date=format_date(profile.install_date),
            removed_date=format_date(profile.removed_date),

            ownership_start_date=format_date(
                profile.owned_from_date
            ),

            ownership_end_date=format_date(
                profile.owned_to_date
            ),
        )

    @staticmethod
    def _present_offline_sensor(
            profiles: tuple[SensorProfileDTO, ...],
            connectivity_statuses: tuple[SensorLastSeenDTO, ...],
            last_activations: tuple[MostRecentSensorEventDTO, ...],
            offline_sensor_ids: tuple[str, ...],
    ) -> tuple[OfflineSensorRowViewModel, ...]:

        last_event_mapping: dict[str, MostRecentSensorEventDTO] = {
            r.sensor_id: r
            for r in last_activations
        }

        connectivity_mapping: dict[str, SensorLastSeenDTO] = {
            r.sensor_id: r
            for r in connectivity_statuses
        }

        profile_mapping: dict[str, SensorProfileDTO] = {
            p.sensor_id: p
            for p in profiles
        }

        vm: list[OfflineSensorRowViewModel] = []
        for sensor_id in offline_sensor_ids:
            last_seen_at_default_timezone: datetime = format_utc_to_timezone(
                utc_time=connectivity_mapping[sensor_id].last_seen_at_utc,
                timezone=_DEFAULT_TIME_ZONE)

            status_at_default_timezone: datetime = format_utc_to_timezone(
                utc_time=connectivity_mapping[sensor_id].status_at_utc,
                timezone=_DEFAULT_TIME_ZONE)

            last_activated_at_default_timezone: datetime = format_utc_to_timezone(
                utc_time=last_event_mapping[sensor_id].activated_at,
                timezone=_DEFAULT_TIME_ZONE)

            vm.append(
                OfflineSensorRowViewModel(
                    sensor_id=sensor_id,
                    sensor_type=profile_mapping[sensor_id].sensor_type,
                    name=profile_mapping[sensor_id].name,
                    location=profile_mapping[sensor_id].location,
                    zone=profile_mapping[sensor_id].zone,
                    paired_gateway_id=profile_mapping[sensor_id].paired_gateway_id,
                    last_seen_at_default_timezone=format_datetime(last_seen_at_default_timezone),
                    status_at_default_timezone=format_datetime(status_at_default_timezone),
                    connectivity_state=connectivity_mapping[sensor_id].connectivity_state,
                    last_activated_at_default_timezone=format_datetime(last_activated_at_default_timezone),
                )
            )
        return tuple(vm)

    def _present_gateway(
            self,
            profile: GatewayProfileDTO,
    ) -> GatewayOverviewRowViewModel:
        return GatewayOverviewRowViewModel(
            gateway_id=profile.gateway_id,

            attached_user_count=len(
                profile.attached_user_ids
            ),

            attached_users=self._join(
                profile.attached_user_ids
            ),

            paired_sensor_count=len(
                profile.paired_sensor_ids
            ),

            paired_sensors=self._join(
                profile.paired_sensor_ids
            ),

            firmware_version_mcu=self._text(
                profile.firmware_version_mcu
            ),

            firmware_version_cellular=self._text(
                profile.firmware_version_cellular
            ),

            hardware_version=self._text(
                profile.hardware_version
            ),

            install_date=format_date(profile.install_date),
            removed_date=format_date(profile.removed_date),

            ownership_start_date=format_date(
                profile.owned_from_date
            ),

            ownership_end_date=format_date(
                profile.owned_to_date
            ),
        )

    @staticmethod
    def _text(value: str | None) -> str:
        return value or "—"

    @staticmethod
    def _join(values: tuple[str, ...]) -> str:
        return ", ".join(values) if values else "—"

    @staticmethod
    def _enum_label(value: StrEnum | str | None) -> str:
        if value is None:
            return "—"

        if isinstance(value, StrEnum):
            return str(value.value)

        return str(value)
