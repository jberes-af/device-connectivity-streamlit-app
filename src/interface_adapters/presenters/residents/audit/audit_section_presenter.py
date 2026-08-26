# /src/interface_adapters/presenters/audit/audit_section_presenter.py


from src.interface_adapters.view_models.residents.main_page import (
    ResidentMainPageTopViewModel,
)

# from src.interface_adapters.view_models.widgets.table_view_model import (
#     TableViewModel,
# )

from src.interface_adapters.view_models.widgets.card_view_models import (
    CardTitleTextButtonViewModel,
)

from src.interface_adapters.view_models.widgets.card_grid_view_model import (
    CardGridViewModel
)

# from src.interface_adapters.presenters.contact.searchable_table_presenter import (
#     ResidentRecordsSearchableTablePresenter,
# )


class AuditSectionPresenter:

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
