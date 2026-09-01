# /src/interface_adapters/presenters/sensing/sensing_admin/sensing_admin_presenter.py

from datetime import date
from enum import StrEnum

# from src.domain.entities.tenant.tenant_entities import TenantProfile

from src.application.use_cases.sensing.sensing_admin.build_view.build_admin_view_uc_dtos import (
    GatewayProfileDTO,
    SensorProfileDTO,
    TenantProfileDTO,
    BuildSensingAdminViewResultDTO,
)

from src.interface_adapters.view_models.sensing.device_admin_view_models import (
    SensingSummaryViewModel,
    SensingAdministrationViewModel,
    GatewayOverviewRowViewModel,
    SensorOverviewRowViewModel,
    TenantOptionViewModel,
)


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

        online_sensor_ratio: str = (
            f"{online_sensor_count} / {sensor_count}"
        )

        offline_sensor_percentage: float = 100. * (1 - (online_sensor_count / sensor_count))
        offline_sensor_pct_str: str = f"{offline_sensor_percentage}"

        summary = SensingSummaryViewModel(
            sensor_count=len(result.sensor_profiles),
            gateway_count=len(result.gateway_profiles),
            assigned_sensor_count=assigned_sensor_count,
            unassigned_sensor_count=(
                    len(result.sensor_profiles)
                    - assigned_sensor_count
            ),
            online_sensor_count=online_sensor_count,
            # online_sensor_ratio=online_sensor_ratio,
            offline_sensor_percent=offline_sensor_pct_str,
        )

        return SensingAdministrationViewModel(
            title="Tenant Devices",
            tenants=tenants,
            selected_tenant_name=result.selected_tenant_name,
            summary=summary,
            sensors=sensor_rows,
            gateways=gateway_rows,
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

            install_date=self._date(profile.install_date),
            removed_date=self._date(profile.removed_date),

            ownership_start_date=self._date(
                profile.owned_from_date
            ),

            ownership_end_date=self._date(
                profile.owned_to_date
            ),
        )

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

            install_date=self._date(profile.install_date),
            removed_date=self._date(profile.removed_date),

            ownership_start_date=self._date(
                profile.owned_from_date
            ),

            ownership_end_date=self._date(
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
    def _date(value: date | None) -> str:
        return value.strftime("%m/%d/%Y") if value else "—"

    @staticmethod
    def _enum_label(value: StrEnum | str | None) -> str:
        if value is None:
            return "—"

        if isinstance(value, StrEnum):
            return str(value.value)

        return str(value)
