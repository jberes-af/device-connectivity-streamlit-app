# /src/gui/streamlit/screens/residents/sections/treatment_section_renderer.py

from streamlit.elements.lib.column_types import Column
from streamlit.delta_generator import DeltaGenerator
from typing import Sequence

# import logging
import streamlit as st

from src.gui.streamlit.components.cards.card_property_value_renderer_hor import (
    render_card_horizontal_properties,
)

from src.interface_adapters.view_models.widgets.card_view_models import (
    MetricCardViewModel,
)

from src.interface_adapters.view_models.widgets.tab_view_model import (
    TabViewModel,
)

from src.interface_adapters.view_models.widgets.card_grid_view_model import (
    CardGridViewModel,
)

from src.interface_adapters.view_models.residents.main_page.resident_main_view_model import (
    ResidentTreatmentSectionViewModel,
)

from src.interface_adapters.view_models.residents.treatment.treatment_plan_view_models import (
    TreatmentPlanViewModel,
    TreatmentPlanCardViewModel,
    TherapeuticGoalViewModel,
    TreatmentInterventionViewModel,
    TreatmentMonitoringParameterViewModel,
    TreatmentPlanReviewViewModel,
)


def render_resident_treatment_section(
        resident_id: str,
        view_model: ResidentTreatmentSectionViewModel,
) -> None:
    # st.markdown("#### 🚧 Treatments")
    st.markdown(f"#### {view_model.section_title}")

    tabs: Sequence[DeltaGenerator] = _render_tab_widget(
        tabs_vm=view_model.treatment_section_tabs
    )

    diagnoses_tab: DeltaGenerator = tabs[0]
    treatment_plan_tab: DeltaGenerator = tabs[1]
    rtm_necessity_tab: DeltaGenerator = tabs[2]

    _render_diagnoses_tab(
        tab=diagnoses_tab,
        models=view_model.diagnoses.diagnoses_card_grid
    )

    _render_treatment_plan_tab(
        tab=treatment_plan_tab,
        model=view_model.treatment_plans
    )

    _render_rtm_necessity_tab(
        tab=rtm_necessity_tab,
        model=view_model.rtm_necessity
    )


def _render_tab_widget(
        tabs_vm: TabViewModel,
) -> Sequence[DeltaGenerator]:
    st.write("")

    tabs = st.tabs(
        [tab.label for tab in tabs_vm.tabs]
    )

    for tab_container, tab_vm in zip(
            tabs,
            tabs_vm.tabs,
            strict=True,
    ):
        with tab_container:
            st.write(tab_vm.content)

    return tabs


def _render_diagnoses_tab(
        tab: DeltaGenerator,
        models: tuple[CardGridViewModel, ...]
) -> None:
    with tab:
        for model in models:
            _render_diagnosis_tab_content(
                view_model=model,
            )

            st.write("")


def _render_rtm_necessity_tab(
        tab: DeltaGenerator,
        model: CardGridViewModel,
) -> None:
    with tab:
        _render_rtm_necessity_tab_content(
            view_model=model,
        )

        st.write("")


def _render_treatment_plan_tab(
        tab: DeltaGenerator,
        model: TreatmentPlanViewModel,
) -> None:
    with tab:
        _render_treatment_plan_tab_content(
            view_model=model,
        )

        st.write("")


def _render_diagnosis_tab_content(
        view_model: CardGridViewModel,
) -> None:
    # st.markdown("#### 🚧 Resident")
    # st.markdown(f"#### {view_model.section_title}")

    """
    logger.info(
        "ENTER render_resident_resident resident_id=%s",
        resident_id,
    )

    st.warning(
        f"DEBUG: render_resident_resident entered for {resident_id}"
    )
    """

    cols: Column = st.columns(view_model.columns)

    # logging.info("Resident Contact Section Columns %s", cols_p)

    for i, vm in enumerate(view_model.cards):
        with cols[i % len(cols)]:
            render_card_horizontal_properties(
                title=vm.title,
                property_fields=vm.property_fields,
                key=f"{vm.id}_{i}",
            )


def _render_rtm_necessity_tab_content(
        view_model: CardGridViewModel,
) -> None:
    # st.markdown("#### 🚧 Resident")

    cols: Column = st.columns(view_model.columns)

    for i, vm in enumerate(view_model.cards):
        with cols[i % len(cols)]:
            render_card_horizontal_properties(
                title=vm.title,
                property_fields=vm.property_fields,
                key=f"{vm.id}_{i}",
            )


def _render_treatment_plan_tab_content(
        view_model: TreatmentPlanViewModel,
) -> None:
    _render_treatment_plan_metrics(
        vm=view_model.metrics
    )
    _render_treatment_plan_plans(
        vm=view_model.plans
    )


def _render_treatment_plan_metrics(
        vm: tuple[MetricCardViewModel, ...],
) -> None:
    if not vm:
        return

    columns = st.columns(len(vm))

    for column, metric in zip(
            columns,
            vm,
            strict=True,
    ):
        with column:
            st.metric(
                label=metric.label,
                value=metric.value,
            )


def _render_treatment_plan_plans(
        vm: tuple[TreatmentPlanCardViewModel, ...],
) -> None:
    if not vm:
        st.info("No treatment plans available.")
        return

    for index, plan_vm in enumerate(vm):

        render_card_horizontal_properties(
            title=plan_vm.title,
            property_fields=plan_vm.properties,
            key=f"{plan_vm.treatment_plan_id}_{index}",
        )

        _render_treatment_plan_goals(
            vm=plan_vm.goals,
        )

        _render_treatment_plan_interventions(
            vm=plan_vm.interventions,
        )

        _render_treatment_plan_monitoring_parameters(
            vm=plan_vm.monitoring_parameters,
        )

        _render_treatment_plan_reviews(
            vm=plan_vm.reviews,
        )

        if index < len(vm) - 1:
            st.divider()


def _render_treatment_plan_goals(
        vm: tuple[TherapeuticGoalViewModel, ...],
) -> None:
    if not vm:
        return

    st.markdown("##### Therapeutic Goals")

    for goal in vm:
        with st.container(border=True):
            st.markdown(
                f"**{goal.description}**"
            )
            st.caption(
                f"Target date: {goal.target_date_display}"
            )


def _render_treatment_plan_interventions(
        vm: tuple[TreatmentInterventionViewModel, ...],
) -> None:
    if not vm:
        return

    st.markdown("##### Interventions")

    for intervention in vm:
        with st.container(border=True):
            col_main, col_status = st.columns(
                [4, 1],
            )

            with col_main:
                st.markdown(
                    f"**{intervention.treatment_type_display}**"
                )

                st.write(
                    intervention.description
                )

                st.caption(
                    intervention.date_range_display
                )

            with col_status:
                st.markdown(
                    intervention.status_badge.label
                )


def _render_treatment_plan_monitoring_parameters(
        vm: tuple[TreatmentMonitoringParameterViewModel, ...],
) -> None:
    if not vm:
        return

    st.markdown("##### Monitoring Parameters")

    rows = [
        {
            "Measure": parameter.measure_name,
            "Baseline": parameter.baseline_display,
            "Target": parameter.target_display,
        }
        for parameter in vm
    ]

    st.dataframe(
        rows,
        use_container_width=True,
        hide_index=True,
    )


def _render_treatment_plan_reviews(
        vm: tuple[TreatmentPlanReviewViewModel, ...],
) -> None:
    if not vm:
        return

    st.markdown("##### Reviews")

    for index, review in enumerate(vm):
        label = (
            f"{review.reviewed_at_display}"
            f" — {review.provider_display}"
        )

        with st.expander(
                label,
                expanded=(index == 0),
        ):
            st.markdown("**Clinical Findings**")
            st.write(
                review.clinical_findings
            )

            st.markdown("**Treatment Decision**")
            st.write(
                review.treatment_decision
            )

            st.caption(
                f"Next review: "
                f"{review.next_review_date_display}"
            )
