# /src/gui/streamlit/screens/resident_screen.py

from collections.abc import Callable
from datetime import datetime
from datetime import datetime, date, timedelta

from streamlit.elements.lib.column_types import Column
from typing import Any

import streamlit as st

# --- APPLICATION

from src.application.use_cases.resident.resident_uc_dtos import (
    GetAllResidentRecordsRequestDTO,
    GetAllResidentRecordsResultDTO,
)

from src.application.use_cases.sensing.profiles.user_sensing_account_uc_dtos import (
    UserSensingAccountRequestDTO,
    UserSensingAccountResultDTO,
)

from src.application.use_cases.sensing.trends.build_sensor_events_use_case import (
    SensorEventsRequestDTO,
    SensorEventsResultDTO,
)

# --- GUI

from src.gui.streamlit.components.common.table_searchable_renderer import (
    render_searchable_table,
)

from src.gui.streamlit.components.common.card_grid_renderer import (
    # render_card_grid,
    render_metric_card_grid,
)

from src.gui.streamlit.components.common.dashboard_card_grid_renderer import (
    render_dashboard_card_grid
)

from src.gui.streamlit.components.common.segmented_control_renderer import (
    render_vertical_segmented_control,
)

from src.gui.streamlit.components.resident.care_plan_renderer import (
    render_resident_care_plan,
)
from src.gui.streamlit.components.resident.clinical_docs_renderer import (
    render_resident_clinical_docs,
)
from src.gui.streamlit.components.resident.communications_renderer import (
    render_resident_communications,
)
from src.gui.streamlit.components.resident.payers_renderer import (
    render_resident_payers,
)
from src.gui.streamlit.components.resident.priority_items_renderer import (
    render_resident_priority_items,
)
from src.gui.streamlit.components.resident.providers_renderer import (
    render_resident_providers,
)
from src.gui.streamlit.components.resident.resident_renderer import (
    render_resident_resident,
)
from src.gui.streamlit.components.resident.treatment_plan_renderer import (
    render_resident_treatment_plan,
)
from src.gui.streamlit.components.resident.sensing_renderer import (
    render_resident_sensing,
)

from src.gui.streamlit.components.resident.appointments_renderer import (
    render_resident_appointments,
)
from src.gui.streamlit.components.resident.billing_renderer import (
    render_resident_billing,
)

# --- INTERFACE ADAPTERS

# from src.interface_adapters.view_models.patient.patient_overview_page_view_model import (    PatientOverviewPageViewModel,)

from src.interface_adapters.view_models.common.table_view_model import TableViewModel

from src.interface_adapters.view_models.resident.resident_main_page_view_model import (
    ResidentMainPageTopViewModel,
)

from src.interface_adapters.presenters.resident.demo_top_metrics_presenter import (
    DemoResidentDashMetricsPresenter
)

from src.interface_adapters.view_models.common.card_grid_view_model import (
    CardGridViewModel
)

from src.interface_adapters.presenters.resident.demo_record_dash.demo_presenter import (
    DemoSelectedResidentCardGridPresenter
)

from src.interface_adapters.presenters.resident.demo_record_dash.demo_segmented_controls_presenter import (
    ResidentSegmentedControlPresenter)

from src.interface_adapters.view_models.resident.segmented_controls_view_model import (
    ResidentSectionEnum,
)

from src.interface_adapters.presenters.resident.resident_sensing_section_presenter import (
    ResidentSensingSectionPresenter
)

from src.interface_adapters.view_models.sensing.resident_sensing_view_model import (
    SensorSectionViewModel,
)

# --- MAIN

from src.main.compose_root_application import AppContainer

# --- PROGRAM

Renderer = Callable[[str], None]

_RENDERERS: dict[ResidentSectionEnum, Renderer] = {
    ResidentSectionEnum.APPOINTMENTS: render_resident_appointments,
    ResidentSectionEnum.BILLING: render_resident_billing,
    ResidentSectionEnum.CARE_PLAN: render_resident_care_plan,
    ResidentSectionEnum.CLINICAL_DOCS: render_resident_clinical_docs,
    ResidentSectionEnum.COMMUNICATIONS: render_resident_communications,
    ResidentSectionEnum.PAYERS: render_resident_payers,
    ResidentSectionEnum.PRIORITY_ITEMS: render_resident_priority_items,
    ResidentSectionEnum.PROVIDERS: render_resident_providers,
    ResidentSectionEnum.RESIDENT: render_resident_resident,
    ResidentSectionEnum.SENSING: render_resident_sensing,
    ResidentSectionEnum.TREATMENT_PLAN: render_resident_treatment_plan,
}


def render_residents_page(
        container: AppContainer,
) -> None:
    records_request = GetAllResidentRecordsRequestDTO(
        user_id=container.user_context.user_id,
        user_tenant_id=container.user_context.tenant_id,
        user_role=container.user_context.role,
    )

    records_result: GetAllResidentRecordsResultDTO = (
        container.get_resident_records_for_user_use_case.execute(records_request))

    table_vm: TableViewModel = (
        container.resident_main_page_presenter.present_searchable_table(
            records_result.resident_table_records))

    presenter = container.resident_main_page_presenter

    _render_top_section(
        header_vm=presenter.present_top_section(),
    )

    selected_resident_id: str = _render_table_section(
        table_vm=table_vm,
    )

    if selected_resident_id:

        _render_selected_resident_dash_cards(
            resident_id=selected_resident_id,
        )

        st.divider()

        selected_control: ResidentSectionEnum
        col_content: Column
        selected_control, col_content = (
            _render_selected_resident_segmented_control_section())

        """
        DEV ONLY: test to filter on sensing section
        """

        if selected_control:

            if selected_control == "sensing":

                result_user_sensing_account: UserSensingAccountResultDTO
                result_sensor_events: SensorEventsResultDTO

                use_case_results = _dispatch_run_use_case(
                    domain_key=selected_control,
                    app_container=container,
                )

                result_user_sensing_account = use_case_results[0]
                result_sensor_events = use_case_results[1]

                section_dash_vm: SensorSectionViewModel = (
                    ResidentSensingSectionPresenter()
                    .present_sensing_section(result_user_sensing_account)
                )

                # trends_vm: SensorTrendsViewModel = (ResidentSensingTrendsPresenter().present(result_sensor_events))

                with col_content:
                    with st.container(border=False):
                        render_resident_sensing(
                            resident_id=selected_resident_id,
                            section_dash_vm=section_dash_vm,
                            # section_trends_vm=trends_vm
                        )

            else:
                _render_selected_control_details(
                    col=col_content,
                    resident_id=selected_resident_id,
                    domain_name=selected_control,
                )


def _render_selected_resident_dash_cards(
        resident_id: str,
):
    st.markdown(f"#### Resident {resident_id}")

    card_grid_vm: CardGridViewModel = DemoSelectedResidentCardGridPresenter().present_cards_grid()

    render_dashboard_card_grid(view_model=card_grid_vm)


def _render_selected_resident_segmented_control_section(
) -> tuple[ResidentSectionEnum, Column]:
    st.markdown(f"#### Detail Records")

    col_control, col_content = st.columns([1, 5])

    selected_control: ResidentSectionEnum = (
        render_vertical_segmented_control(
            col=col_control,
            view_model=ResidentSegmentedControlPresenter.present_segmented_controls(),
        ))

    return selected_control, col_content


def _render_top_section(
        header_vm: ResidentMainPageTopViewModel,
) -> None:
    st.title(header_vm.page_title)
    # st.write(header_vm.page_subtitle)

    metrics_grid_vm: CardGridViewModel = DemoResidentDashMetricsPresenter.present()

    render_metric_card_grid(metrics_grid_vm)

    st.divider()


def _render_table_section(
        table_vm: TableViewModel,
) -> str:
    st.markdown(f"#### Records")

    selected_resident_id = render_searchable_table(
        view_model=table_vm,
        key="resident_records",
        domain_id_column="Resident ID",
    )

    return selected_resident_id


def _dispatch_renderer(
        domain_key: ResidentSectionEnum,
        resident_id: str,
) -> None:
    handler = _RENDERERS.get(domain_key)

    if handler is None:
        return

    handler(resident_id)


def _render_selected_control_details(
        col: Column,
        resident_id: str,
        domain_name: ResidentSectionEnum,
) -> None:
    domain_label: str = domain_name.value.replace("_", " ").title()

    with col:
        with st.container(border=True):
            st.markdown(f"#### {domain_label} • {resident_id}")

            _dispatch_renderer(
                domain_key=domain_name,
                resident_id=resident_id,
            )


def _dispatch_run_use_case(
        domain_key: ResidentSectionEnum,
        app_container: AppContainer,
) -> Any:
    match domain_key:
        case "sensing":
            request_usa = UserSensingAccountRequestDTO(
                user_id=app_container.user_context.user_id,
            )

            result_user_sensing_account: UserSensingAccountResultDTO = (
                app_container.get_user_sensing_account_use_case.execute(
                    request=request_usa,
                ))

            """
            CHANGE!  ok for dev
            """

            today: date = date.today()
            yesterday: date = today - timedelta(days=1)
            start_date: date = yesterday - timedelta(days=90)

            request_se = SensorEventsRequestDTO(
                sensor_ids=result_user_sensing_account.sensor_ids,
                start_date=start_date,
                end_date=yesterday,
            )

            result_sensor_events: SensorEventsResultDTO = (
                app_container.build_sensor_event_timeline_use_case.execute(
                    request=request_se,
                ))

            return result_user_sensing_account, result_sensor_events
