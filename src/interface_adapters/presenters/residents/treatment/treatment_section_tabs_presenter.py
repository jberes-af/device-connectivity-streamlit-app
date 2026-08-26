# /src/interface_adapters/presenters/treatment_plan/treatment_section_tabs_presenter.py

from src.application.use_cases.residents.treatment.get_patient_diagnosis_and_treatment_uc import (
    GetDiagnosisAndTreatmentResultDTO,
)

from src.interface_adapters.view_models.residents.main_page.resident_main_view_model import (
    TREATMENT_SEGMENT_ORDER,
    ResidentTreatmentSectionViewModel,
)

from src.interface_adapters.view_models.widgets.card_grid_view_model import (
    CardGridViewModel,
)

from src.interface_adapters.view_models.widgets.tab_view_model import (
    TabItemViewModel,
    TabViewModel,
)

# from src.interface_adapters.view_models.widgets.table_view_model import (
#     TableViewModel,
# )

# from src.interface_adapters.presenters.contact.searchable_table_presenter import (
#     ResidentRecordsSearchableTablePresenter,
# )

from src.interface_adapters.view_models.residents.treatment.diagnosis_view_models import (
    DiagnosisSectionViewModel,
)

from src.interface_adapters.view_models.residents.treatment.treatment_plan_view_models import (
    TreatmentPlanViewModel,
)

from src.interface_adapters.presenters.residents.treatment.diagnosis_section_presenter import (
    DiagnosisSectionPresenter,
)

from src.interface_adapters.presenters.residents.treatment.treatment_plan_section_presenter import (
    TreatmentPlanSectionPresenter,
)

from src.interface_adapters.presenters.residents.treatment.rtm_necessity_section_presenter import (
    RtmNecessitySectionPresenter,
)


class TreatmentSectionPresenter:

    def present(
            self,
            *,
            result: GetDiagnosisAndTreatmentResultDTO,
            icon: str,
    ) -> ResidentTreatmentSectionViewModel:  # TreatmentPlanTabViewModel:

        treatment_detail_sections: TabViewModel = (
            self._present_treatment_tabs_section()
        )

        diagnoses: DiagnosisSectionViewModel = (
            DiagnosisSectionPresenter().present(
                results_diagnoses=result.diagnoses,
                # selected_patient_diagnosis_id=result.patient_id
            )
        )

        treatment_plans: TreatmentPlanViewModel = (
            TreatmentPlanSectionPresenter().present(
                treatment_plans=result.treatment_plans,
            )
        )

        rtm_necessity: CardGridViewModel = (
            RtmNecessitySectionPresenter().present(
                records=result.rtm_necessity_records,
            )
        )

        return ResidentTreatmentSectionViewModel(
            section_title=f"{icon} Treatments",
            # section_title="Treatment Details",
            treatment_section_tabs=treatment_detail_sections,
            diagnoses=diagnoses,
            treatment_plans=treatment_plans,
            rtm_necessity=rtm_necessity,
        )

    @staticmethod
    def _present_treatment_tabs_section(
    ) -> TabViewModel:
        tabs = tuple(
            TabItemViewModel(
                tab_id=segment.value,
                label=segment.value.replace("_", " ").title().replace("Rtm", "RTM"),
                content=f"{segment.value} content",
            )
            for segment in TREATMENT_SEGMENT_ORDER
        )

        return TabViewModel(
            tabs=tabs,
        )

    """
    def present2(
            self,
            use_case_results: Any,
            icon: str,

    ) -> ResidentTreatmentSectionViewModel:
        treatment_detail_sections: TabViewModel = (
            self._present_treatment_tabs_section()
        )

        return ResidentTreatmentSectionViewModel(
            section_title=f"{icon} Treatments",
            treatment_card_grid="Resident census and records.",
            treatment_details_section_vm="Resident census and records.",
        )
    """

    """
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
    """


"""
ordered_plans: tuple[TherapeuticPlanDTO, ...] = tuple(
    sorted(
        treatment_plans,
        key=lambda plan: (
            self._is_active(plan),
            plan.treatment_plan.start_date,
        ),
        reverse=True,
    )
)

return TreatmentPlanTabViewModel(
    metrics=self._build_metrics(
        treatment_plans=ordered_plans,
    ),
    plans=tuple(
        self._build_plan(plan=plan)
        for plan in ordered_plans
    ),
)
"""
