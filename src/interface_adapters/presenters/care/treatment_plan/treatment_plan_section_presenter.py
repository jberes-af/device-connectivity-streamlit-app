# /src/interface_adapters/presenters/treatment_plan/treatment_plan_section_presenter.py


from src.application.use_cases.resident.resident_uc_dtos import (
    GetAllResidentRecordsRequestDTO
)

from src.interface_adapters.view_models.resident.resident_main_view_model import (
    TreatmentTabIdEnum,
    TREATMENT_SEGMENT_ORDER,
    ResidentTreatmentViewModel,
)

from src.interface_adapters.view_models.widgets.card_view_models import (
    CardPropertyFieldsViewModel,
)

from src.interface_adapters.view_models.widgets.property_field_view_model import (
    PropertyFieldViewModel,
)

from src.interface_adapters.view_models.widgets.card_grid_view_model import (
    CardGridViewModel,
)

from src.interface_adapters.view_models.widgets.tab_view_model import (
    TabItemViewModel,
    TabViewModel,
)

from src.interface_adapters.presenters.utils_presenters import (
    format_optional,
    format_bool,
    format_date,
    format_state_postal,
)


# from src.interface_adapters.view_models.widgets.table_view_model import (
#     TableViewModel,
# )

# from src.interface_adapters.presenters.person.searchable_table_presenter import (
#     ResidentRecordsSearchableTablePresenter,
# )


class TreatmentPlanSectionPresenter:

    def present(
            self,
            use_case_results: Any,
            icon: str,

    ) -> ResidentTreatmentViewModel:
        treatment_detail_sections: TabViewModel = (
            self._present_treatment_tabs_section()
        )

        return ResidentTreatmentViewModel(
            section_title=f"{icon} Treatments",
            treatment_card_grid="Resident census and records.",
            treatment_details_section_vm="Resident census and records.",
        )

    @staticmethod
    def _present_treatment_tabs_section(
    ) -> TabViewModel[str]:
        tabs = tuple(
            TabItemViewModel(
                tab_id=segment.value,
                label=segment.value.replace("_", " ").title(),
                content=f"{segment.value} content",
            )
            for segment in TREATMENT_SEGMENT_ORDER
        )

        return TabViewModel(
            tabs=tabs,
        )

    def _present_need_contact_card_grid(
            self,
            need_case_contact: ResidentInCaseOfNeedContact,
    ) -> CardGridViewModel:
        return CardGridViewModel(
            columns=1,
            cards=self._build_need_contact_cards(
                need_case_contact=need_case_contact,
            ),
        )

    @staticmethod
    def _build_need_contact_cards(
            need_case_contact: ResidentInCaseOfNeedContact,
    ) -> tuple[CardPropertyFieldsViewModel, ...]:
        return (
            CardPropertyFieldsViewModel(
                title="In Case of Need Contact",
                id="resident_need_contact",
                property_fields=(
                    PropertyFieldViewModel(
                        label="Contact Name",
                        value=_format_optional(
                            need_case_contact.contact_name
                        ),
                    ),
                    PropertyFieldViewModel(
                        label="Telephone",
                        value=_format_optional(
                            need_case_contact.contact_telephone
                        ),
                    ),
                    PropertyFieldViewModel(
                        label="Email",
                        value=_format_optional(
                            need_case_contact.contact_email
                        ),
                    ),
                    PropertyFieldViewModel(
                        label="Address",
                        value=_format_optional(
                            need_case_contact.contact_address
                        ),
                    ),
                    PropertyFieldViewModel(
                        label="Relationship",
                        value=_format_optional(
                            need_case_contact.contact_relationship
                        ),
                    ),
                ),
            ),
        )
