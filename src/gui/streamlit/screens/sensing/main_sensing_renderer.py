# /src/gui/streamlit/screens/sensing/main_sensing_renderer.py

import streamlit as st

from src.interface_adapters.view_models.common.property_field_view_model import (
    PropertyFieldViewModel,
)

from src.interface_adapters.view_models.sensing.device_admin_view_models import (
    SensingAdministrationViewModel,
    GatewayOverviewRowViewModel,
    SensorOverviewRowViewModel,
)

from src.gui.streamlit.components.cards.attribute_card_renderer import (
    render_attribute_card,
)

from src.gui.streamlit.components.cards.card_property_value_renderer_hor import (
    render_card_horizontal_properties,
)


def render_main_sensing(
        view_model: SensingAdministrationViewModel,
) -> None:
    st.title("🚧 :material/sensors: Sensing")

    st.subheader(view_model.title)

    # --- TENANT SELECT-BOX

    tenant_names = tuple(
        tenant.tenant_name
        for tenant in view_model.tenants
    )

    if tenant_names:
        col, _ = st.columns([1, 2])
        with col:
            st.selectbox(
                "Select Tenant",
                options=tenant_names,
                key="sensing_selected_tenant_name",
            )

    # --- SUMMARY

    _render_summary(
        view_model=view_model,
    )

    # --- DETAILS

    st.divider()

    st.subheader("Device Details")

    sensor_tab, gateway_tab = st.tabs(
        [
            f"Sensors ({view_model.summary.sensor_count})",
            f"Gateways ({view_model.summary.gateway_count})",
        ]
    )

    with sensor_tab:
        _render_sensor_section(
            sensors=view_model.sensors,
        )

    with gateway_tab:
        _render_gateway_section(
            gateways=view_model.gateways,
        )


# -------------------------------------------------------------------------
# SUMMARY
# -------------------------------------------------------------------------


def _render_summary(
        *,
        view_model: SensingAdministrationViewModel,
) -> None:
    summary = view_model.summary

    col_sensors, col_gateways, col_assigned, col_unassigned = st.columns(4)

    with col_sensors:
        render_attribute_card(
            id="sensor_count",
            title="Online / Total Sensors",
            attribute_count=f"{summary.online_sensor_count} / {summary.sensor_count}",
            attributes=(
                f"Registered sensing devices ({summary.offline_sensor_percent:.1f}% offline)",
            ),
            key="devices_overview_sensor_count",
        )

    with col_gateways:
        render_attribute_card(
            id="gateway_count",
            title="Gateways",
            attribute_count=str(summary.gateway_count),
            attributes=(
                "Registered gateway devices",
            ),
            key="devices_overview_gateway_count",
        )

    with col_assigned:
        render_attribute_card(
            id="assigned_sensor_count",
            title="Assigned Sensors",
            attribute_count=str(summary.assigned_sensor_count),
            attributes=(
                "Sensors assigned to users",
            ),
            key="devices_overview_assigned_sensor_count",
        )

    with col_unassigned:
        render_attribute_card(
            id="unassigned_sensor_count",
            title="Unassigned Sensors",
            attribute_count=str(summary.unassigned_sensor_count),
            attributes=(
                "Sensors without a user assignment",
            ),
            key="devices_overview_unassigned_sensor_count",
        )


# -------------------------------------------------------------------------
# SENSOR SECTION
# -------------------------------------------------------------------------


def _render_sensor_section(
        *,
        sensors: tuple[SensorOverviewRowViewModel, ...],
) -> None:
    if not sensors:
        st.info("No sensors are available.")
        return

    for row_start in range(0, len(sensors), 2):
        row_sensors = sensors[row_start:row_start + 2]

        columns = st.columns(2)

        for column, sensor in zip(columns, row_sensors):
            with column:
                _render_sensor_card(
                    sensor=sensor,
                )


def _render_sensor_card(
        *,
        sensor: SensorOverviewRowViewModel,
) -> None:
    property_fields = (
        PropertyFieldViewModel(
            label="Sensor Type",
            value=sensor.sensor_type,
        ),
        PropertyFieldViewModel(
            label="Name",
            value=sensor.name,
        ),
        PropertyFieldViewModel(
            label="Location",
            value=sensor.location,
        ),
        PropertyFieldViewModel(
            label="Zone",
            value=sensor.zone,
        ),
        PropertyFieldViewModel(
            label="Purpose",
            value=sensor.sensor_purpose,
        ),
        PropertyFieldViewModel(
            label="Gateway",
            value=sensor.paired_gateway_id,
        ),
        PropertyFieldViewModel(
            label="Assigned Users",
            value=sensor.attached_users,
        ),
        PropertyFieldViewModel(
            label="Firmware",
            value=sensor.firmware_version,
        ),
        PropertyFieldViewModel(
            label="Hardware",
            value=sensor.hardware_version,
        ),
        PropertyFieldViewModel(
            label="Install Date",
            value=sensor.install_date,
        ),
        PropertyFieldViewModel(
            label="Removed Date",
            value=sensor.removed_date,
        ),
        PropertyFieldViewModel(
            label="Owned From",
            value=sensor.ownership_start_date,
        ),
        PropertyFieldViewModel(
            label="Owned To",
            value=sensor.ownership_end_date,
        ),
    )

    render_card_horizontal_properties(
        title=_sensor_title(sensor),
        property_fields=property_fields,
        key=f"sensor_{sensor.sensor_id}",
    )


def _sensor_title(
        sensor: SensorOverviewRowViewModel,
) -> str:
    if sensor.name and sensor.name != "—":
        return f"{sensor.name} · {sensor.sensor_id}"

    return sensor.sensor_id


# -------------------------------------------------------------------------
# GATEWAY SECTION
# -------------------------------------------------------------------------


def _render_gateway_section(
        *,
        gateways: tuple[GatewayOverviewRowViewModel, ...],
) -> None:
    if not gateways:
        st.info("No gateways are available.")
        return

    for row_start in range(0, len(gateways), 2):
        row_gateways = gateways[row_start:row_start + 2]

        columns = st.columns(2)

        for column, gateway in zip(columns, row_gateways):
            with column:
                _render_gateway_card(
                    gateway=gateway,
                )


def _render_gateway_card(
        *,
        gateway: GatewayOverviewRowViewModel,
) -> None:
    property_fields = (
        PropertyFieldViewModel(
            label="Assigned Users",
            value=gateway.attached_users,
        ),
        PropertyFieldViewModel(
            label="Assigned User Count",
            value=str(gateway.attached_user_count),
        ),
        PropertyFieldViewModel(
            label="Paired Sensors",
            value=gateway.paired_sensors,
        ),
        PropertyFieldViewModel(
            label="Paired Sensor Count",
            value=str(gateway.paired_sensor_count),
        ),
        PropertyFieldViewModel(
            label="MCU Firmware",
            value=gateway.firmware_version_mcu,
        ),
        PropertyFieldViewModel(
            label="Cellular Firmware",
            value=gateway.firmware_version_cellular,
        ),
        PropertyFieldViewModel(
            label="Hardware",
            value=gateway.hardware_version,
        ),
        PropertyFieldViewModel(
            label="Install Date",
            value=gateway.install_date,
        ),
        PropertyFieldViewModel(
            label="Removed Date",
            value=gateway.removed_date,
        ),
        PropertyFieldViewModel(
            label="Owned From",
            value=gateway.ownership_start_date,
        ),
        PropertyFieldViewModel(
            label="Owned To",
            value=gateway.ownership_end_date,
        ),
    )

    render_card_horizontal_properties(
        title=f"Gateway · {gateway.gateway_id}",
        property_fields=property_fields,
        key=f"gateway_{gateway.gateway_id}",
    )
