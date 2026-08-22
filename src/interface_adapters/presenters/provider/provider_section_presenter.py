# /src/interface_adapters/presenters/provider/provider_section_presenter.py


from src.application.use_cases.resident.resident_uc_dtos import (
    GetAllResidentRecordsRequestDTO
)

from src.interface_adapters.view_models.resident.resident_main_page_view_model import (
    ResidentTabIdEnum,
    ResidentMainPageTopViewModel,
    ResidentRecordCardGridViewModel,
    ResidentTabViewModel,
    ResidentRecordTabsViewModel,
)

# from src.interface_adapters.view_models.common.table_view_model import (
#     TableViewModel,
# )

from src.interface_adapters.view_models.common.card_view_models import (
    CardTitleTextButtonViewModel,
)

from src.interface_adapters.view_models.common.card_grid_view_model import (
    CardGridViewModel
)

# from src.interface_adapters.presenters.resident.searchable_table_presenter import (
#     ResidentRecordsSearchableTablePresenter,
# )


class ProviderSectionPresenter:

    @staticmethod
    def present_top_section(
    ) -> ResidentMainPageTopViewModel:
        return ResidentMainPageTopViewModel(
            page_title=":material/groups: Residents",
            page_subtitle="Resident census and records.",
        )

    def present_selected_record_card_grid(
            self,
    ) -> CardGridViewModel:
        return CardGridViewModel(
            cards=self._build_cards(),
            columns=3,
        )

    @staticmethod
    def _build_cards(
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
