# /src/interface_adapters/presenters/resident/resident_main_page_presenter.py

from src.domain.entities.person.resident_entities import (
    ResidentProfile,
    ResidentInCaseOfNeedContact,
)

from src.application.use_cases.resident.resident_uc_dtos import (
    ResidentSearchableRecordDTO,
)

# from src.application.use_cases.resident.resident_uc_dtos import (
#    GetAllResidentRecordsRequestDTO
# )

from src.interface_adapters.view_models.common.table_view_model import (
    TableViewModel,
)

# from src.interface_adapters.view_models.common.card_grid_view_model import (
#    CardGridViewModel
# )

from src.interface_adapters.presenters.resident.searchable_table_presenter import (
    ResidentRecordsSearchableTablePresenter,
)

from src.interface_adapters.presenters.resident.demo_record_dash.demo_presenter import (
    DemoSelectedResidentCardGridPresenter
)

from src.interface_adapters.presenters.resident.resident_contact_section_presenter import (
    ResidentContactSectionPresenter,
)

from src.interface_adapters.view_models.common.card_grid_view_model import (
    CardGridViewModel,
)

from src.interface_adapters.view_models.resident.resident_main_page_view_model import (
    # ResidentTabIdEnum,
    ResidentMainPageTopViewModel,
    # ResidentRecordCardGridViewModel,
    # ResidentTabViewModel,
    # ResidentRecordTabsViewModel,
)

from src.interface_adapters.view_models.resident.segmented_controls_view_model import (
    ResidentSectionEnum,
    SECTION_ICONS,
    ResidentSegmentedControlViewModel,
)

from src.interface_adapters.presenters.resident.segmented_controls_presenter import (
    ResidentSegmentedControlPresenter)

from src.interface_adapters.view_models.resident.resident_main_page_view_model import (
    ResidentContactViewModel,
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

    """
    @staticmethod
    def _build_dashboard_cards(
    ) -> tuple[CardTitleTextButtonViewModel, ...]:
        return (
            CardTitleTextButtonViewModel(
                id="resident_profile",
                title="Resident Profile",
                card_text=(
                    "View resident demographics, contact information, "
                    "and administrative details."
                ),
                button_label="View profile",
            ),
            CardTitleTextButtonViewModel(
                id="care_plan",
                title="Care Plan",
                card_text=(
                    "View care goals, activities of daily living, "
                    "priority items, and care instructions."
                ),
                button_label="View care plan",
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
                    "and resident activity insights."
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
