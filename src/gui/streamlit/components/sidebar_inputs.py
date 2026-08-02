# /src/gui/streamlit/components/sidebar_inputs.py

from dataclasses import dataclass

from src.domain.value_objects.pipeline_vos import (
    EntityTypes,
    States,
)

import streamlit as st

_SHOW_RECORDS_KEY = "pipeline_show_records"


@dataclass(frozen=True, slots=True)
class UserSidebarSelections:
    selected_entity_type: EntityTypes | None
    selected_states: tuple[States, ...]
    show_records: bool


def render_entity_type_selectbox() -> EntityTypes | None:
    return st.selectbox(
        label="Business Type",
        options=list(EntityTypes),
        format_func=lambda entity_type: (
            "Care Facility"
            if entity_type is None
            else entity_type.value
        ),
        key="selected_entity_type",
        index=list(EntityTypes).index(EntityTypes.FACILITY),
    )


def render_states_multiselect() -> tuple[States, ...]:
    selected_states = st.multiselect(
        label="States",
        options=list(States),
        format_func=lambda state: state.value,
        default=[States.TX],
        key="selected_states",
    )

    return tuple(selected_states)


def load_sidebar_inputs() -> UserSidebarSelections:
    if _SHOW_RECORDS_KEY not in st.session_state:
        st.session_state[_SHOW_RECORDS_KEY] = False

    with st.sidebar:
        st.header("Filters")

        selected_entity_type = render_entity_type_selectbox()

        st.divider()

        selected_states = render_states_multiselect()

        st.divider()

        if st.button(
                label="Show Records",
                type="primary",
                use_container_width=True,
        ):
            st.session_state[_SHOW_RECORDS_KEY] = True

    return UserSidebarSelections(
        selected_entity_type=selected_entity_type,
        selected_states=selected_states,
        show_records=st.session_state[_SHOW_RECORDS_KEY],
    )
