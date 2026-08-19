# /src/gui/streamlit/components/resident/resident_profile_renderer.py



import streamlit as st

def render_resident_sensing(
    view_model: ResidentProfileViewModel,
) -> None:
    cols = st.columns(3)

    for index, card in enumerate(view_model.cards):
        with cols[index % 3]:
            render_card(card)

    render_searchable_table(
        view_model.events_table,
        key="resident_sensing_events",
    )