# /src/interface_adapters/presenters/contact/demo_record_dash/demo_presenter.py

from typing import Any

from src.interface_adapters.presenters.residents.main_page.demo_record_dash.demo_use_case import (
    run_use_case,
    UseCaseResult)

from src.interface_adapters.view_models.widgets.card_view_models import (
    CardPropertyFieldsButtonViewModel)

from src.interface_adapters.view_models.widgets.card_grid_view_model import (
    CardGridViewModel)

from src.interface_adapters.view_models.widgets.property_field_view_model import (
    PropertyFieldViewModel)


class DemoSelectedResidentCardGridPresenter:

    def present_cards_grid(
            self,
    ) -> CardGridViewModel:
        use_case_result: UseCaseResult = run_use_case()

        return CardGridViewModel(
            columns=use_case_result.column_count,
            cards=self._build_dashboard_cards(result=use_case_result),
        )

    def _build_dashboard_cards(
            self,
            result: UseCaseResult
    ) -> tuple[CardPropertyFieldsButtonViewModel, ...]:
        identity_card: CardPropertyFieldsButtonViewModel = (
            self._build_dashboard_card_identity(
                summary_info=result.identity
            ))

        care_plan: CardPropertyFieldsButtonViewModel = (
            self._build_dashboard_card_care_plan(
                summary_info=result.care_plan
            ))

        next_event: CardPropertyFieldsButtonViewModel = (
            self._build_dashboard_card_schedule_events(
                summary_info=result.schedule_events
            ))

        priority_items: CardPropertyFieldsButtonViewModel = (
            self._build_dashboard_card_priority_items(
                summary_info=result.priority
            ))

        provider: CardPropertyFieldsButtonViewModel = (
            self._build_dashboard_card_provider(
                summary_info=result.provider
            ))

        return tuple([
            identity_card, priority_items, next_event, care_plan, provider
        ])

    @staticmethod
    def _build_dashboard_card_identity(
            summary_info: Any,
    ) -> CardPropertyFieldsButtonViewModel:
        property_fields: list[PropertyFieldViewModel] = [
            PropertyFieldViewModel(
                label="Name",
                value=summary_info.name,
            ),
            PropertyFieldViewModel(
                label="Age",
                value=summary_info.age,
            ),
            PropertyFieldViewModel(
                label="ID",
                value=summary_info.id,
            ),
        ]

        return CardPropertyFieldsButtonViewModel(
            id="identity",
            title="Resident Identity",
            property_fields=tuple(property_fields),
            description="Resident's summary identity information",
            button_label="More",
            button_icon=":material/chevron_right:",
        )

    @staticmethod
    def _build_dashboard_card_care_plan(
            summary_info: Any,
    ) -> CardPropertyFieldsButtonViewModel:
        property_fields: list[PropertyFieldViewModel] = [
            PropertyFieldViewModel(
                label="Name",
                value=summary_info.name,
            ),
            PropertyFieldViewModel(
                label="Progress",
                value=summary_info.progress,
            ),
            PropertyFieldViewModel(
                label="Last Update",
                value=summary_info.last_status_date,
            ),
        ]

        return CardPropertyFieldsButtonViewModel(
            id="care_plan",
            title="Care Plan",
            property_fields=tuple(property_fields),
            description="Resident's treatment plan summary",
            button_label="More",
            button_icon=":material/chevron_right:",
        )

    @staticmethod
    def _build_dashboard_card_schedule_events(
            summary_info: Any,
    ) -> CardPropertyFieldsButtonViewModel:
        property_fields: list[PropertyFieldViewModel] = [
            PropertyFieldViewModel(
                label="Name",
                value=summary_info.name,
            ),
            PropertyFieldViewModel(
                label="Time",
                value=summary_info.time,
            ),
            PropertyFieldViewModel(
                label="Date",
                value=summary_info.date,
            ),
            PropertyFieldViewModel(
                label="Venue",
                value=summary_info.location,
            ),
        ]

        return CardPropertyFieldsButtonViewModel(
            id="schedule_events",
            title="Next Session",
            property_fields=tuple(property_fields),
            description="Resident's next scheduled treatment session.",
            button_label="More",
            button_icon=":material/chevron_right:",
        )

    @staticmethod
    def _build_dashboard_card_priority_items(
            summary_info: Any,
    ) -> CardPropertyFieldsButtonViewModel:
        property_fields: list[PropertyFieldViewModel] = [
            PropertyFieldViewModel(
                label=summary_info.item_1_date,
                value=summary_info.item_1,
            ),
            PropertyFieldViewModel(
                label=summary_info.item_2_date,
                value=summary_info.item_2,
            ),
            PropertyFieldViewModel(
                label=summary_info.item_3_date,
                value=summary_info.item_3,
            ),
        ]

        return CardPropertyFieldsButtonViewModel(
            id="priority_items",
            title="Priority Items",
            property_fields=tuple(property_fields),
            description="Resident's next scheduled treatment session.",
            button_label="More",
            button_icon=":material/chevron_right:",
        )

    @staticmethod
    def _build_dashboard_card_provider(
            summary_info: Any,
    ) -> CardPropertyFieldsButtonViewModel:
        property_fields: list[PropertyFieldViewModel] = [
            PropertyFieldViewModel(
                label="Name",
                value=summary_info.name,
            ),
            PropertyFieldViewModel(
                label="Entity",
                value=summary_info.entity_name,
            ),
            PropertyFieldViewModel(
                label="Telephone",
                value=summary_info.telephone,
            ),
        ]

        return CardPropertyFieldsButtonViewModel(
            id="provider",
            title="Provider",
            property_fields=tuple(property_fields),
            description="Resident's provider summary.",
            button_label="More",
            button_icon=":material/chevron_right:",
        )
