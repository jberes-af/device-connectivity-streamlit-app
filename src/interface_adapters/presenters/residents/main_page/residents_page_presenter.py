# /src/interface_adapters/presenters/main_page/residents_page_presenter.py

# --- DOMAIN

from src.domain.entities.resident.resident_entities import (
    ResidentProfile,
    ResidentInCaseOfNeedContact,
)

# --- APPLICATION
from src.application.use_cases.residents.main.resident_uc_dtos import (
    ResidentSearchableRecordDTO,
)

from src.application.use_cases.residents.treatment.get_patient_diagnosis_and_treatment_uc import (
    GetDiagnosisAndTreatmentResultDTO,
)

from src.application.use_cases.residents.provider.patient_provider_uc_dtos import (
    PatientProviderProfileDTO,
)

from src.application.use_cases.residents.payer.patient_payer_and_rtm_enrollment_uc_dtos import (
    GetPatientPayersAndRtmEnrollmentResultDTO,
)

# --- VIEW MODELS


from src.interface_adapters.view_models.residents.main_page.segmented_controls_view_model import (
    ResidentSectionEnum,
    SECTION_ICONS,
    ResidentSegmentedControlViewModel,
)

from src.interface_adapters.view_models.widgets.table_view_model import (
    TableViewModel,
)

# from src.interface_adapters.view_models.widgets.card_grid_view_model import (
#    CardGridViewModel
# )

from src.interface_adapters.presenters.residents.main_page.searchable_table_presenter import (
    ResidentRecordsSearchableTablePresenter,
)

from src.interface_adapters.presenters.residents.main_page.demo_record_dash.demo_presenter import (
    DemoSelectedResidentCardGridPresenter
)

from src.interface_adapters.presenters.residents.contact.resident_contact_section_presenter import (
    ResidentContactSectionPresenter,
)

from src.interface_adapters.view_models.widgets.card_grid_view_model import (
    CardGridViewModel,
)

from src.interface_adapters.view_models.residents.main_page.resident_main_view_model import (
    ResidentMainPageTopViewModel,
    ResidentContactViewModel,
    ResidentPayerAndRtmEnrollmentSectionViewModel,
    ResidentProviderViewModel,
    ResidentTreatmentSectionViewModel,
)

# --- PRESENTERS

from src.interface_adapters.presenters.residents.main_page.segmented_controls_presenter import (
    ResidentSegmentedControlPresenter,
)

from src.interface_adapters.presenters.residents.treatment.treatment_section_tabs_presenter import (
    TreatmentSectionPresenter,
)

from src.interface_adapters.presenters.residents.provider.patient_provider_section_presenter import (
    PatientProviderSectionPresenter
)

from src.interface_adapters.presenters.residents.payer.payer_and_rtm_enrollment_section_presenter import (
    PatientPayerAndRtmEnrollmentSectionPresenter,
)


class ResidentMainPagePresenter:

    @staticmethod
    def present_top_section(
    ) -> ResidentMainPageTopViewModel:
        return ResidentMainPageTopViewModel(
            page_title=":material/groups: Residents",
            page_subtitle="Resident census and records.",
        )

    @staticmethod
    def present_searchable_table(
            records: tuple[ResidentSearchableRecordDTO, ...],
    ) -> TableViewModel:
        return ResidentRecordsSearchableTablePresenter().present(
            records=records
        )

    @staticmethod
    def present_selected_resident_dash_cards_demo(
    ) -> CardGridViewModel:
        return (DemoSelectedResidentCardGridPresenter()
                .present_cards_grid()
                )

    @staticmethod
    def present_selected_resident_segmented_controls_section(
    ) -> ResidentSegmentedControlViewModel:
        return (
            ResidentSegmentedControlPresenter()
            .present_segmented_controls())

    @staticmethod
    def present_resident_contact_records(
            resident_profile: ResidentProfile,
            resident_need_case_contact: ResidentInCaseOfNeedContact,
    ) -> ResidentContactViewModel:
        return ResidentContactSectionPresenter().present(
            profile=resident_profile,
            need_case_contact=resident_need_case_contact,
            icon=SECTION_ICONS.get(ResidentSectionEnum.CONTACT)
        )

    @staticmethod
    def present_resident_treatment_section(
            result: GetDiagnosisAndTreatmentResultDTO,
    ) -> ResidentTreatmentSectionViewModel:
        return TreatmentSectionPresenter().present(
            result=result,
            icon=SECTION_ICONS.get(ResidentSectionEnum.TREATMENTS)
        )

    @staticmethod
    def present_patient_providers_section(
            result: tuple[PatientProviderProfileDTO, ...],
    ) -> ResidentProviderViewModel:
        return PatientProviderSectionPresenter().present(
            provider_profiles=result,
            icon=SECTION_ICONS.get(ResidentSectionEnum.PROVIDERS)
        )

    @staticmethod
    def present_payers_and_rtm_enrollment_section(
            result: GetPatientPayersAndRtmEnrollmentResultDTO,
    ) -> ResidentPayerAndRtmEnrollmentSectionViewModel:
        return PatientPayerAndRtmEnrollmentSectionPresenter().present(
            result=result,
            icon=SECTION_ICONS.get(ResidentSectionEnum.PAYERS)
        )

    """
    @staticmethod
    def _build_dashboard_cards(
    ) -> tuple[CardTitleTextButtonViewModel, ...]:
        return (
            CardTitleTextButtonViewModel(
                id="resident_profile",
                title="Resident Profile",
                card_text=(
                    "View contact demographics, contact information, "
                    "and administrative details."
                ),
                button_label="View profile",
            ),
            CardTitleTextButtonViewModel(
                id="care_plan",
                title="Care Plan",
                card_text=(
                    "View treatment goals, activities of daily living, "
                    "priority items, and treatment instructions."
                ),
                button_label="View treatment plan",
            ),
            CardTitleTextButtonViewModel(
                id="sensing",
                title="Sensing",
                card_text=(
                    "View assigned sensors, activity events, "
                    "movement, and monitoring information."
                ),
                button_label="View sensing",
            ),
            CardTitleTextButtonViewModel(
                id="analytics",
                title="Analytics",
                card_text=(
                    "View trends, comparisons, baselines, "
                    "and contact activity insights."
                ),
                button_label="View analytics",
            ),
        )

    def present_selected_record_card_grid(
            self,
    ) -> CardGridViewModel:
        return CardGridViewModel(
            cards=self._build_dashboard_cards(),
            columns=3,
        )

    def present_selected_record_card_grid(
            self,
    ) -> ResidentRecordCardGridViewModel:
        return ResidentRecordCardGridViewModel(
            cards=self._build_dashboard_cards(),
            columns=3,
        
        )

    def present_selected_record_tabs_section(
            self,
    ) -> ResidentRecordTabsViewModel:
        return ResidentRecordTabsViewModel(
            tabs=(
                ResidentTabViewModel(
                    tab_id=ResidentTabIdEnum.PROFILE,
                    label="Profile",
                ),
                ResidentTabViewModel(
                    tab_id=ResidentTabIdEnum.CARE_PLAN,
                    label="Care Plan",
                ),
                ResidentTabViewModel(
                    tab_id=ResidentTabIdEnum.TREATMENT_PLAN,
                    label="Treatment Plan",
                ),
                ResidentTabViewModel(
                    tab_id=ResidentTabIdEnum.PROVIDER,
                    label="Provider",
                ),
                ResidentTabViewModel(
                    tab_id=ResidentTabIdEnum.SENSING,
                    label="Sensing",
                ),
                ResidentTabViewModel(
                    tab_id=ResidentTabIdEnum.COMMUNICATION,
                    label="Communication",
                ),
                ResidentTabViewModel(
                    tab_id=ResidentTabIdEnum.PAYER,
                    label="Payer",
                ),
                ResidentTabViewModel(
                    tab_id=ResidentTabIdEnum.BILLING,
                    label="Billing",
                ),
            )
        )
    """
