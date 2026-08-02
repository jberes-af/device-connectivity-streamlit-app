# /src/gui/streamlit/screens/patient_screen.py

from src.application.use_cases.get_patient_overview.get_patient_info_uc_dtos import (
    GetPatientOverviewRequestDTO,
    GetPatientOverviewResultDTO,
    PatientOverviewDevDTO,
)

from src.application.use_cases.get_patient_overview.get_patient_overview_uc import (
    GetPatientOverviewUseCase
)

from src.gui.streamlit.components.card_renderer import render_card

from src.interface_adapters.view_models.patient.patient_overview_page_view_model import (
    PatientOverviewPageViewModel,
)

from src.main.composition_root import AppContainer

import streamlit as st


def render_patients_page(
        container: AppContainer,
) -> None:
    st.title("🚧  Patients")
    st.write("Patient census and patient records.")

    # hardcode patient_id for dev; normally user selects from UI

    request: GetPatientOverviewRequestDTO = GetPatientOverviewRequestDTO(
        patient_id="PATIENT_ID_003"
    )

    overview_result: GetPatientOverviewResultDTO = (
        container.get_patient_overview_use_case.execute(request))

    # overview_record: PatientOverviewDevDTO = overview_result.overview

    vm: PatientOverviewPageViewModel = container.patient_overview_presenter.present(overview_result)

    _render_page(vm)


def _render_page(vm: PatientOverviewPageViewModel) -> None:
    pass

    st.title(vm.page_title)

    render_card(vm.administration_card)

    render_card(vm.enrollment_card)

    # render_card(vm.provider_review_card)

    # render_card(vm.communication_card)
