# /src/gui/streamlit/screens/renderers/resident_screen.py

from streamlit.elements.lib.column_types import Column

import logging
import streamlit as st

from src.application.use_cases.resident.resident_uc_dtos import (
    GetAllResidentRecordsRequestDTO,
    GetAllResidentRecordsResultDTO,
)

from src.gui.streamlit.components.widgets.table_searchable_renderer import (
    render_searchable_table,
)

from src.gui.streamlit.components.grids.grid_card_property_fields_button_renderer import (
    render_grid_card_properties_button,
)

from src.gui.streamlit.components.widgets.segmented_control_renderer import (
    render_vertical_segmented_control,
)

from src.gui.streamlit.screens.resident.resident_section_router import (
    render_resident_section,
)

from src.gui.streamlit.screens.resident.sections.contact_section import (
    render_contact_section,
)

from src.interface_adapters.presenters.person.resident.resident_main_page_presenter import (
    ResidentMainPagePresenter,
)

from src.interface_adapters.view_models.widgets.card_grid_view_model import (
    CardGridViewModel,
)

from src.interface_adapters.view_models.widgets.table_view_model import (
    TableViewModel,
)

from src.interface_adapters.view_models.resident.resident_main_view_model import (
    ResidentMainPageTopViewModel,
)

from src.interface_adapters.view_models.resident.segmented_controls_view_model import (
    ResidentSectionEnum,
    ResidentSegmentedControlViewModel,
)

from src.main.compose_root_application import AppContainer

logger = logging.getLogger(__name__)


def render_residents_page(
        container: AppContainer,
) -> None:
    presenter: ResidentMainPagePresenter = (
        container.resident_main_page_presenter
    )

    records_result: GetAllResidentRecordsResultDTO = (
        _load_resident_records(
            container=container,
        )
    )

    _render_top_section(
        header_vm=presenter.present_top_section(),
    )

    selected_resident_id: str = _render_resident_selection(
        records_result=records_result,
        presenter=presenter,
    )

    if selected_resident_id is None:
        st.info("No renderers records available.")
        return

    logging.info("Selected Resident ID: %s", selected_resident_id)

    _render_selected_resident_summary(
        resident_id=selected_resident_id,
        presenter=presenter,
    )

    st.divider()
    st.markdown("#### Detail Records")

    col_control, col_content = st.columns([1, 5])

    selected_section: ResidentSectionEnum = _render_section_selector(
        col=col_control,
        presenter=presenter,
    )

    logging.info("Selected section: %s", selected_section)

    if selected_section == ResidentSectionEnum.CONTACT:
        with col_content:
            render_contact_section(
                resident_id=selected_resident_id,
                resident_profiles=records_result.resident_profiles,
                resident_need_contacts=records_result.resident_need_case_contacts,
                presenter=presenter,
            )

    with col_content:
        render_resident_section(
            section=selected_section,
            resident_id=selected_resident_id,
            container=container,
        )


def _load_resident_records(
        *,
        container: AppContainer,
) -> GetAllResidentRecordsResultDTO:
    request = GetAllResidentRecordsRequestDTO(
        user_id=container.user_context.user_id,
        user_tenant_id=container.user_context.tenant_id,
        user_role=container.user_context.role,
    )

    return (
        container
        .get_resident_records_for_user_use_case
        .execute(request)
    )


def _render_resident_selection(
        *,
        records_result: GetAllResidentRecordsResultDTO,
        presenter: ResidentMainPagePresenter,
) -> str | None:
    table_vm: TableViewModel = (
        presenter.present_searchable_table(
            records_result.resident_table_records,
        )
    )

    selection: str | None = _render_table_section(
        table_vm=table_vm,
    )

    table_records = records_result.resident_table_records

    if selection is None and table_records:
        selection = table_records[0].resident_id

    return _resolve_selected_resident(
        selection=selection,
        records=table_records,
    )


def _render_selected_resident_summary(
        *,
        resident_id: str,
        presenter: ResidentMainPagePresenter,
) -> None:
    st.markdown(
        f"#### Resident {resident_id}"
    )

    card_grid_vm: CardGridViewModel = (
        presenter
        .present_selected_resident_dash_cards_demo()
    )

    render_grid_card_properties_button(
        view_model=card_grid_vm,
    )


def _render_section_selector(
        *,
        col: Column,
        presenter: ResidentMainPagePresenter,
) -> ResidentSectionEnum:
    view_model: ResidentSegmentedControlViewModel = (
        presenter
        .present_selected_resident_segmented_controls_section()
    )

    selected_section = render_vertical_segmented_control(
        col=col,
        view_model=view_model,
    )

    if selected_section is None:
        return ResidentSectionEnum.CONTACT

    return selected_section


def _render_top_section(
        *,
        header_vm: ResidentMainPageTopViewModel,
) -> None:
    st.title(
        header_vm.page_title
    )

    st.divider()


def _render_table_section(
        *,
        table_vm: TableViewModel,
) -> str | None:
    st.markdown("#### Records")

    selected_resident_id = render_searchable_table(
        view_model=table_vm,
        key="resident_records",
        domain_id_column="Resident ID",
    )

    st.divider()

    return selected_resident_id


def _resolve_selected_resident(
        *,
        selection: str | None,
        records,
) -> str | None:
    if selection is not None:
        return selection

    if not records:
        return None

    return records[0].resident_id
