# # src/gui/streamlit/screens/renderers/segmented_control_section_renderer.py

import streamlit as st
from streamlit.elements.lib.column_types import Column

from src.domain.entities.person.resident_entities import ResidentProfile, ResidentInCaseOfNeedContact
from src.gui.streamlit.screens.resident.renderers.resident_contact_renderer import render_resident_contact_info
from src.gui.streamlit.screens.resident.renderers import render_resident_sensing
from src.gui.streamlit.components.widgets.segmented_control_renderer import render_vertical_segmented_control
from src.gui.streamlit.screens.resident.resident_screen import logger, _dispatch_renderer_handler
from scripts.resident_section_types import SectionUseCaseResult, ResidentSectionViewModel
from src.gui.streamlit.screens.resident.segmented_control_section_view_models import get_view_model
from src.gui.streamlit.screens.resident.use_case_runners.dispatch_runner import run_use_case_dispatcher
from src.interface_adapters.presenters.person.resident.resident_main_page_presenter import ResidentMainPagePresenter
from src.interface_adapters.view_models.resident.resident_main_view_model import ResidentContactViewModel
from src.interface_adapters.view_models.resident.segmented_controls_view_model import ResidentSegmentedControlViewModel, \
    ResidentSectionEnum
from src.main.compose_root_application import AppContainer


def render_selected_resident_segmented_control_section(
        selected_resident_id: str,
        container: AppContainer,
        selected_resident_profile: ResidentProfile,
        selected_resident_need_contact: ResidentInCaseOfNeedContact,
        presenter_main: ResidentMainPagePresenter,
        # vm_segmented_controls: ResidentSegmentedControlViewModel,
) -> None:  # tuple[ResidentSectionEnum, Column]:
    st.markdown(f"#### Detail Records")

    # --- RENDER SEGMENTED CONTROLS VERTICAL TOOLBAR

    col_control, col_content = st.columns([1, 5])

    vm_segmented_controls: ResidentSegmentedControlViewModel = (
        presenter_main.present_selected_resident_segmented_controls_section()
    )

    selected_control: ResidentSectionEnum = (
        render_vertical_segmented_control(
            col=col_control,
            view_model=vm_segmented_controls,
        ))

    logger.info(
        "Segmented control selected: %r | type=%s",
        selected_control, type(selected_control).__name__)

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

        # logger.info("Use case dispatcher result: control=%r result=%r", selected_control, use_case_results)

    # --- GET VIEW MODEL

    if selected_control != ResidentSectionEnum.CONTACT and use_case_results:
        section_vm: ResidentSectionViewModel = (
            get_view_model(
                selected_resident_id=selected_resident_id,
                selected_control=selected_control,
                use_case_results=use_case_results,
                container=container,
            ))
    else:

        section_vm: ResidentContactViewModel = (
            presenter_main.present_resident_contact_records(
                resident_profile=selected_resident_profile,
                resident_need_case_contact=selected_resident_need_contact,
            ))

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
