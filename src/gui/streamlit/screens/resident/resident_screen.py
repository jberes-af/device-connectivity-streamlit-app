# /src/gui/streamlit/screens/resident_screen.py

"""
Page Flow:
render_residents_page()
→ load resident records
→ present + render searchable table
→ resolve selected resident
→ render selected resident summary cards
→ render segmented control
→ run section-specific use case(s)
→ present section-specific view model
→ render section-specific UI
"""

from collections.abc import Callable
from streamlit.elements.lib.column_types import Column

import logging
import streamlit as st

# --- DOMAIN

from src.domain.entities.person.resident_entities import (
    ResidentProfile,
    ResidentInCaseOfNeedContact,
)

# --- APPLICATION

from src.application.use_cases.resident.resident_uc_dtos import (
    GetAllResidentRecordsRequestDTO,
    GetAllResidentRecordsResultDTO,
)

# --- GUI

from src.gui.streamlit.components.widgets.table_searchable_renderer import (
    render_searchable_table,
)

from src.gui.streamlit.components.grids.grid_card_property_fields_button_renderer import (
    render_grid_card_properties_button
)

from src.gui.streamlit.components.widgets.segmented_control_renderer import (
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
from src.gui.streamlit.components.resident.resident_contact_renderer import (
    render_resident_contact_info,
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

from src.gui.streamlit.screens.resident.use_case_dispatcher_sensing import (
    SensingUseCaseResults,
    run_sensing_use_cases,
)

# --- INTERFACE ADAPTERS

# from src.interface_adapters.view_models.patient.patient_overview_page_view_model import (    PatientOverviewPageViewModel,)

from src.interface_adapters.view_models.common.table_view_model import TableViewModel

from src.interface_adapters.view_models.resident.segmented_controls_view_model import (
    ResidentSectionEnum,
)

from src.interface_adapters.view_models.resident.resident_main_page_view_model import (
    ResidentMainPageTopViewModel,
)

from src.interface_adapters.view_models.common.card_grid_view_model import (
    CardGridViewModel
)

from src.interface_adapters.view_models.sensing.resident_sensing_view_model import (
    SensorSectionViewModel,
)

from src.interface_adapters.view_models.resident.resident_main_page_view_model import (
    ResidentContactViewModel,
)

# from src.interface_adapters.presenters.resident.demo_record_dash.demo_presenter import (
#     DemoSelectedResidentCardGridPresenter
# )

from src.interface_adapters.presenters.resident.resident_main_page_presenter import (
    ResidentMainPagePresenter,
)

from src.interface_adapters.presenters.resident.segmented_controls_presenter import (
    ResidentSegmentedControlPresenter)

from src.interface_adapters.presenters.resident.resident_sensing_section_presenter import (
    ResidentSensingSectionPresenter
)

from src.interface_adapters.presenters.resident.resident_contact_section_presenter import (
    ResidentContactSectionPresenter,
)

# --- MAIN

from src.main.compose_root_application import AppContainer

logger = logging.getLogger(__name__)

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
    ResidentSectionEnum.CONTACT: render_resident_contact_info,
    ResidentSectionEnum.SENSING: render_resident_sensing,
    ResidentSectionEnum.TREATMENT_PLAN: render_resident_treatment_plan,
}

SectionUseCaseResult = (
    SensingUseCaseResults
    #    | ResidentContactUseCaseResults
    #    | ProviderUseCaseResults
)

ResidentSectionViewModel = (
        SensorSectionViewModel
        | ResidentContactViewModel
)


def render_residents_page(
        container: AppContainer,
) -> None:
    records_request = GetAllResidentRecordsRequestDTO(
        user_id=container.user_context.user_id,
        user_tenant_id=container.user_context.tenant_id,
        user_role=container.user_context.role,
    )

    logging.info("Records request assigned")

    records_result: GetAllResidentRecordsResultDTO = (
        container.get_resident_records_for_user_use_case.execute(records_request))

    table_vm: TableViewModel = (
        container.resident_main_page_presenter.present_searchable_table(
            records_result.resident_table_records))

    presenter: ResidentMainPagePresenter = container.resident_main_page_presenter

    logging.info("Main page presenter assigned")

    _render_top_section(
        header_vm=presenter.present_top_section(),
    )

    selected_resident_id: str | None = _render_table_section(
        table_vm=table_vm,
    )

    selected_resident_id = _set_selected_resident(
        selection=selected_resident_id,
        records=records_result.resident_table_records,
    )

    _render_selected_resident_dash_cards(
        resident_id=selected_resident_id,
        presenter=presenter,
    )

    logging.info("Rendered dash cards")

    selected_resident_profile: ResidentProfile = (
        _get_selected_resident_profile(
            resident_id=selected_resident_id,
            results=records_result,
        ))

    selected_resident_need_contact: ResidentInCaseOfNeedContact = (
        _get_selected_resident_in_case_of_need_contact(
            resident_id=selected_resident_id,
            results=records_result,
        ))

    st.divider()

    # selected_control: ResidentSectionEnum
    # col_content: Column
    _render_selected_resident_segmented_control_section(
        selected_resident_id=selected_resident_id,
        container=container,
        selected_resident_profile=selected_resident_profile,
        selected_resident_need_contact=selected_resident_need_contact,
    )

    logging.info("Rendered segmented control segment content area")


def _dispatch_renderer_handler(
        domain_key: ResidentSectionEnum,
        resident_id: str,
) -> None:
    # logger.info("Renderer dispatch requested: key=%r resident_id=%s", domain_key, resident_id)

    handler = _RENDERERS.get(domain_key)

    # logger.info("Renderer lookup: key=%r handler=%r", domain_key, handler)

    if handler is None:
        return

    # logger.info("Calling renderer: %s", handler.__name__)

    handler(resident_id)


def run_use_case_dispatcher(
        domain_key: ResidentSectionEnum,
        resident_id: str,
        app_container: AppContainer,
) -> SectionUseCaseResult | None:
    match domain_key:
        case ResidentSectionEnum.SENSING:
            return run_sensing_use_cases(
                resident_id=resident_id,
                app_container=app_container,
            )

        case _:
            return None


def _render_top_section(
        header_vm: ResidentMainPageTopViewModel,
) -> None:
    st.title(header_vm.page_title)
    # st.write(header_vm.page_subtitle)

    # metrics_grid_vm: CardGridViewModel = DemoResidentDashMetricsPresenter.present()

    # render_metric_card_grid(metrics_grid_vm)

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

    st.divider()

    return selected_resident_id


def _set_selected_resident(
        selection: str,
        records,
) -> str:
    if selection is None and records:
        selection = records[0].resident_id
    return selection


def _render_selected_resident_dash_cards(
        resident_id: str,
        presenter: ResidentMainPagePresenter,
):
    st.markdown(f"#### Resident {resident_id}")

    card_grid_vm: CardGridViewModel = (
        presenter.present_selected_resident_dash_cards_demo())

    render_grid_card_properties_button(view_model=card_grid_vm)


def _render_selected_resident_segmented_control_section(
        selected_resident_id: str,
        container: AppContainer,
        selected_resident_profile: ResidentProfile,
        selected_resident_need_contact: ResidentInCaseOfNeedContact,
) -> None:  # tuple[ResidentSectionEnum, Column]:
    st.markdown(f"#### Detail Records")

    # --- RENDER SEGMENTED CONTROLS VERTICAL TOOLBAR

    col_control, col_content = st.columns([1, 5])

    selected_control: ResidentSectionEnum = (
        render_vertical_segmented_control(
            col=col_control,
            view_model=(ResidentSegmentedControlPresenter
                        .present_segmented_controls()),
        ))

    logger.info(
        "Segmented control selected: %r | type=%s", selected_control, type(selected_control).__name__)

    if not selected_control:
        selected_control = ResidentSectionEnum.CONTACT

    logger.info("Resolved selected control: %r", selected_control)

    # --- GET USE CASE RESULTS

    """
    sensing: SensingUseCaseResults
    """

    if selected_control != ResidentSectionEnum.CONTACT:
        use_case_results: SectionUseCaseResult = run_use_case_dispatcher(
            domain_key=selected_control,
            resident_id=selected_resident_id,
            app_container=container,
        )

        logger.info(
            "Use case dispatcher result: control=%r result=%r",
            selected_control,
            use_case_results,
        )

    # --- GET VIEW MODEL

    if selected_control != ResidentSectionEnum.CONTACT:
        section_vm: ResidentSectionViewModel = (
            _get_segmented_control_section_view_model(
                selected_resident_id=selected_resident_id,
                selected_control=selected_control,
                use_case_results=use_case_results,
                container=container,
            ))
    else:
        section_vm: ResidentContactViewModel = ResidentContactSectionPresenter().present(
            profile=selected_resident_profile,
            need_case_contact=selected_resident_need_contact,
        )

    # logger.info("Section VM result: control=%r vm=%r", selected_control, section_vm)

    # --- RENDER VIEW MODEL

    if section_vm is not None:
        _render_segmented_control_selection_vm(
            selected_control=selected_control,
            col_content=col_content,
            selected_resident_id=selected_resident_id,
            vm=section_vm,
        )
        return

    _render_selected_control_details(
        col=col_content,
        resident_id=selected_resident_id,
        domain_name=selected_control,
    )


def _render_segmented_control_selection_vm(
        selected_control: ResidentSectionEnum,
        col_content: Column,
        selected_resident_id: str,
        vm: ResidentSectionViewModel,
) -> None:
    with col_content:
        match selected_control:

            case ResidentSectionEnum.SENSING:
                render_resident_sensing(
                    resident_id=selected_resident_id,
                    section_dash_vm=vm,
                )

            case ResidentSectionEnum.CONTACT:
                render_resident_contact_info(
                    resident_id=selected_resident_id,
                    view_model=vm,
                )


def _get_segmented_control_section_view_model(
        selected_control: ResidentSectionEnum,
        use_case_results: SectionUseCaseResult,
) -> ResidentSectionViewModel | None:
    if selected_control == ResidentSectionEnum.SENSING:
        if use_case_results is None:
            return None

        return (
            ResidentSensingSectionPresenter()
            .present_sensing_section(
                use_case_results.result_user_sensing_account
            )
        )

    return None


def _render_selected_control_details(
        col: Column,
        resident_id: str,
        domain_name: ResidentSectionEnum,
) -> None:
    domain_label: str = domain_name.value.replace("_", " ").title()

    with col:
        with st.container(border=True):
            st.markdown(f"#### {domain_label} • {resident_id}")

            _dispatch_renderer_handler(
                domain_key=domain_name,
                resident_id=resident_id,
            )


def _present_contact_section(
        resident_id: str,
        results: GetAllResidentRecordsResultDTO,
) -> ResidentContactViewModel | None:
    profile = next(
        (
            profile
            for profile in results.resident_profiles
            if profile.resident_id == resident_id
        ),
        None,
    )

    need_contact = next(
        (
            contact
            for contact in results.resident_need_case_contacts
            if contact.resident_id == resident_id
        ),
        None,
    )

    if profile is None or need_contact is None:
        return None

    return ResidentContactSectionPresenter().present(
        profile=profile,
        need_case_contact=need_contact,
    )


def _get_selected_resident_profile(
        resident_id: str,
        results: GetAllResidentRecordsResultDTO,
) -> ResidentProfile:
    for profile in results.resident_profiles:
        if profile.resident_id == resident_id:
            return profile


def _get_selected_resident_in_case_of_need_contact(
        resident_id: str,
        results: GetAllResidentRecordsResultDTO,
) -> ResidentInCaseOfNeedContact:
    for record in results.resident_need_case_contacts:
        if record.resident_id == resident_id:
            return record
