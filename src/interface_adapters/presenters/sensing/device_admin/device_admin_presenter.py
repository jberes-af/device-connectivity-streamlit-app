# /src/interface_adapters/presenters/sensing/device_admin_presenter.py

from datetime import date

from src.application.use_cases.sensing.sensing_admin.device_admin_uc_dtos import (
    GatewayProfileDTO,
    GetDevicesOverviewResultDTO,
    SensorProfileDTO,
)

from src.interface_adapters.view_models.sensing.device_admin_view_models import (
    DeviceSummaryViewModel,
    DevicesOverviewViewModel,
    GatewayOverviewRowViewModel,
    SensorOverviewRowViewModel,
)


class DeviceAdministrationPresenter:

    def present(
            self,
            *,
            result: GetDevicesOverviewResultDTO,
    ) -> DevicesOverviewViewModel:
        sensor_rows = tuple(
            self._present_sensor(profile)
            for profile in result.sensor_profiles
        )

        gateway_rows = tuple(
            self._present_gateway(profile)
            for profile in result.gateway_profiles
        )

        assigned_sensor_count = sum(
            1
            for profile in result.sensor_profiles
            if profile.attached_user_ids
        )

        summary = DeviceSummaryViewModel(
            sensor_count=len(result.sensor_profiles),
            gateway_count=len(result.gateway_profiles),
            assigned_sensor_count=assigned_sensor_count,
            unassigned_sensor_count=(
                    len(result.sensor_profiles)
                    - assigned_sensor_count
            ),
        )

        return DevicesOverviewViewModel(
            title="Sensing Devices",
            summary=summary,
            sensors=sensor_rows,
            gateways=gateway_rows,
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
    def _enum_label(value) -> str:
        if value is None:
            return "—"

        return str(value.value)
