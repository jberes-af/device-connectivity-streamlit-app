# /src/gui/streamlit/screens/main_page.py

import streamlit as st



def render_screen() -> None:
    entities = filtering_results.entity_records
    entity_type_records = (
        filtering_results.entity_type_records
    )

    st.subheader("Pipeline Records")

    if not entities:
        _render_empty_results()
        return

    _render_summary_metrics(
        entities=entities,
        entity_type_records=entity_type_records,
    )

    st.divider()

    _render_table_header_section(
        distribution_lists=distribution_lists,
        template_options=template_options,
        sender_address="justin@alertahome.com",  # sender_address,
        send_use_case=(
            send_message_to_distribution_list_use_case
        ),
    )

    selected_entity = _render_patients_results_table(
        entities
    )

    if selected_entity is None:
        st.info(
            "Select a record from the table "
            "to view its details."
        )
        return

    selected_type_record = find_entity_type_record(
        entity_id=selected_entity.entity_id,
        records=filtering_results.entity_type_records,
    )

    contacts = [
        record
        for record in filtering_results.contact_records
        if record.entity_id == selected_entity.entity_id
    ]

    activities = [
        record
        for record in filtering_results.activity_records
        if record.entity_id == selected_entity.entity_id
    ]

    st.divider()

    _render_selected_entity_header(
        entity=selected_entity,
        activities=activities,
    )

    render_record_tabs(
        entity=selected_entity,
        type_record=selected_type_record,
        contacts=contacts,
        activities=activities,
        create_contact_use_case=create_contact_use_case,
        update_contact_use_case=update_contact_use_case,
        create_activity_use_case=create_activity_use_case,
        update_activity_use_case=update_activity_use_case,
        send_email_use_case=send_email_use_case,
    )


def _render_empty_results() -> None:
    st.info(
        "No pipeline records matched the selected filters. "
        "Change the sidebar filters and try again."
    )


def _render_summary_metrics(
        *,
        entities: Sequence[PipelineEntity],
        entity_type_records: Sequence[EntityTypeRecordDTO],
) -> None:
    facility_count = sum(
        record.record_type == "Facility"
        for record in entity_type_records
    )

    pace_count = sum(
        record.record_type == "PACE Program"
        for record in entity_type_records
    )

    col_1, col_2, col_3 = st.columns(3)

    with col_1:
        st.metric(
            label="Matching Records",
            value=len(entities),
        )

    with col_2:
        st.metric(
            label="Care Facilities",
            value=facility_count,
        )

    with col_3:
        st.metric(
            label="PACE Programs",
            value=pace_count,
        )


def _render_table_header_section(
        *,
        distribution_lists: Sequence[DistributionList],
        template_options: Sequence[TemplateOption],
        sender_address: str,
        send_use_case: SendMessageToDistributionListUseCase,
) -> None:
    header_col, action_col = st.columns(
        [5, 1],
        vertical_alignment="center",
    )

    with header_col:
        st.markdown("#### Record Details")

    _render_pipeline_actions_menu(
        action_col=action_col,
        distribution_lists=distribution_lists,
        template_options=template_options,
        sender_address=sender_address,
        send_use_case=send_use_case,
    )


def _render_pipeline_actions_menu(
        *,
        action_col: Any,
        distribution_lists: Sequence[DistributionList],
        template_options: Sequence[TemplateOption],
        sender_address: str,
        send_use_case: SendMessageToDistributionListUseCase,
) -> None:
    with action_col:
        with st.container(
                horizontal=True,
                horizontal_alignment="right",
        ):
            selected_action = st.menu_button(
                "⋮",
                options=(
                    "Send Email to Distribution List",
                ),
                key="pipeline_record_actions",
                disabled=(
                        not distribution_lists
                        or not template_options
                ),
            )

    if (
            selected_action
            != "Send Email to Distribution List"
    ):
        return

    render_send_message_to_distribution_dialog(
        distribution_lists=tuple(
            distribution_lists
        ),
        template_options=tuple(
            template_options
        ),
        sender_address=sender_address,
        send_use_case=send_use_case,
    )


def _render_patients_results_table(
        entities: Sequence[PipelineEntity],
) -> PipelineEntity | None:
    """
    Render the filtered records and return the selected domain entity.

    The dataframe contains entity_id internally, but the column is hidden
    from the visible table.
    """

    table_rows = [
        _pipeline_entity_to_table_row(entity)
        for entity in entities
    ]

    dataframe = pd.DataFrame(table_rows)

    event = st.dataframe(
        dataframe,
        key="pipeline_records_table",
        width="stretch",
        height=420,
        hide_index=True,
        on_select="rerun",
        selection_mode="single-row",
        column_config={
            "entity_id": None,
            "entity_name": st.column_config.TextColumn(
                "Organization",
                width="large",
            ),
            "entity_type": st.column_config.TextColumn(
                "Business Type",
                width="medium",
            ),
            "city": st.column_config.TextColumn(
                "City",
                width="medium",
            ),
            "state": st.column_config.TextColumn(
                "State",
                width="small",
            ),
            "telephone": st.column_config.TextColumn(
                "Telephone",
                width="medium",
            ),
        },
    )

    selected_rows = event.selection.rows

    if selected_rows:
        selected_row_index = selected_rows[0]
        selected_entity_id = dataframe.iloc[selected_row_index]["entity_id"]

        st.session_state[_SELECTED_ENTITY_ID_KEY] = selected_entity_id

    selected_entity_id = st.session_state.get_all_sensor_events(
        _SELECTED_ENTITY_ID_KEY
    )

    if selected_entity_id is None:
        return None

    return next(
        (
            entity
            for entity in entities
            if entity.entity_id == selected_entity_id
        ),
        None,
    )


def _pipeline_entity_to_table_row(
        entity: PipelineEntity,
) -> dict[str, Any]:
    """
    Convert a PipelineEntity into a presentation-specific table row.

    Update the attribute names below to match your actual domain entity.
    """

    return {
        "entity_id": entity.entity_id,
        "entity_name": entity.resolved_name,
        "entity_type": enum_display_value(entity.entity_type),
        "city": entity.city,
        "state": enum_display_value(entity.state),
        "telephone": entity.phone,
    }


def _render_selected_entity_header(
        *,
        entity: PipelineEntity,
        activities: list[PipelineActivity],
        # type_record: EntityTypeRecordDTO | None,
) -> None:
    sorted_activities = sort_activity_objects_reverse_date(activities)

    st.markdown(f"### {entity.resolved_name}")

    st.caption(f"Entity ID: {entity.entity_id}")

    if sorted_activities:
        last_activity = sorted_activities[0].contact_date
        days_ago = (date.today() - last_activity).days

        st.caption(
            f"Last Contact: {last_activity.strftime('%B %d, %Y')} "
            f"({days_ago} days ago)"
        )
    else:
        st.caption("Last Contact: —")


def render_record_tabs(
        *,
        entity: PipelineEntity,
        type_record: EntityTypeRecordDTO | None,  # Facility | PaceProgram | None,
        contacts: Sequence[PipelineContact],
        activities: Sequence[PipelineActivity],
        create_contact_use_case: CreatePipelineContactUseCase,
        update_contact_use_case: UpdatePipelineContactUseCase,
        create_activity_use_case: CreatePipelineActivityUseCase,
        update_activity_use_case: UpdatePipelineActivityUseCase,
        send_email_use_case: SendEmailUseCase,
) -> None:
    overview_tab, contacts_tab, activity_tab = st.tabs(
        [
            "Overview",
            f"Contacts ({len(contacts)})",
            f"Activity ({len(activities)})",
        ]
    )

    with overview_tab:
        render_entity_tab(
            entity=entity,
            type_record=type_record,
        )

    with contacts_tab:
        render_contacts_tab(
            entity=entity,
            contacts=contacts,
            create_contact_use_case=create_contact_use_case,
            update_contact_use_case=update_contact_use_case,
            send_email_use_case=send_email_use_case,
        )

    with activity_tab:
        render_activity_tab(
            entity=entity,
            activities=activities,
            contacts=contacts,
            create_activity_use_case=create_activity_use_case,
            update_activity_use_case=update_activity_use_case,
        )
