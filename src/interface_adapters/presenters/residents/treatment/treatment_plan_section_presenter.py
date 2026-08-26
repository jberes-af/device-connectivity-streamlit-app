# /src/interface_adapters/presenters/residents/treatment/treatment_section_tabs_presenter.py


from src.application.use_cases.residents.treatment.diagnosis_and_treatment_uc_dtos import (
    TherapeuticPlanDTO,
    TherapeuticGoalDTO,
    TreatmentInterventionDTO,
    TreatmentMonitoringParameterDTO,
    TreatmentPlanReviewDTO,
)

from src.domain.enums.care.treatment_enums import (
    InterventionStatus,
    TreatmentPlanStatus,
)

from src.interface_adapters.view_models.residents.treatment.treatment_plan_view_models import (
    TreatmentPlanViewModel,
    TreatmentPlanCardViewModel,
    TherapeuticGoalViewModel,
    TreatmentInterventionViewModel,
    TreatmentMonitoringParameterViewModel,
    TreatmentPlanReviewViewModel,
)

from src.interface_adapters.view_models.widgets.card_view_models import (
    MetricCardViewModel,
)

from src.interface_adapters.view_models.widgets.badge_view_model import (
    BadgeViewModel,
)

from src.interface_adapters.view_models.widgets.property_field_view_model import (
    PropertyFieldViewModel,
)

from src.interface_adapters.presenters.utils_presenters import (
    format_date,
    format_datetime,
    format_enum,
    format_date_range,
    format_measurement_value,
)


class TreatmentPlanSectionPresenter:

    def present(
            self,
            *,
            treatment_plans: tuple[TherapeuticPlanDTO, ...],
    ) -> TreatmentPlanViewModel:
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

        return TreatmentPlanViewModel(
            metrics=self._build_metrics(
                treatment_plans=ordered_plans,
            ),
            plans=tuple(
                self._build_plan(plan=plan)
                for plan in ordered_plans
            ),
        )

    def _build_metrics(
            self,
            *,
            treatment_plans: tuple[TherapeuticPlanDTO, ...],
    ) -> tuple[MetricCardViewModel, ...]:
        active_plan_count = sum(
            1
            for plan in treatment_plans
            if self._is_active(plan)
        )

        goal_count = sum(
            len(plan.goals)
            for plan in treatment_plans
        )

        active_intervention_count = sum(
            1
            for plan in treatment_plans
            for intervention in plan.interventions
            if intervention.status == InterventionStatus.ACTIVE
        )

        latest_review = self._find_latest_review(
            treatment_plans=treatment_plans,
        )

        return (
            MetricCardViewModel(
                label="Active Plans",
                value=str(active_plan_count),
            ),
            MetricCardViewModel(
                label="Goals",
                value=str(goal_count),
            ),
            MetricCardViewModel(
                label="Active Interventions",
                value=str(active_intervention_count),
            ),
            MetricCardViewModel(
                label="Last Reviewed",
                value=(
                    format_datetime(latest_review.reviewed_at)
                    if latest_review is not None
                    else "—"
                ),
            ),
        )

    def _build_plan(
            self,
            *,
            plan: TherapeuticPlanDTO,
    ) -> TreatmentPlanCardViewModel:
        return TreatmentPlanCardViewModel(
            treatment_plan_id=plan.treatment_plan.treatment_plan_id,
            title="Treatment Plan",
            status_badge=self._build_plan_status_badge(
                status=plan.treatment_plan.status,
            ),
            properties=self._build_plan_properties(
                plan=plan,
            ),
            goals=tuple(
                self._build_goal(
                    goal=goal,
                )
                for goal in plan.goals
            ),
            interventions=tuple(
                self._build_intervention(
                    intervention=intervention,
                )
                for intervention in plan.interventions
            ),
            monitoring_parameters=tuple(
                self._build_monitoring_parameter(
                    monitoring_parameter=parameter,
                )
                for parameter in plan.monitoring_parameters
            ),
            reviews=tuple(
                self._build_review(
                    review=review,
                )
                for review in sorted(
                    plan.reviews,
                    key=lambda review: review.reviewed_at,
                    reverse=True,
                )
            ),
        )

    @staticmethod
    def _build_plan_properties(
            *,
            plan: TherapeuticPlanDTO,
    ) -> tuple[PropertyFieldViewModel, ...]:
        treatment_plan = plan.treatment_plan

        return (
            PropertyFieldViewModel(
                label="Treating Provider",
                value=treatment_plan.treating_provider_id,
            ),
            PropertyFieldViewModel(
                label="Status",
                value=format_enum(
                    treatment_plan.status,
                ),
            ),
            PropertyFieldViewModel(
                label="Start Date",
                value=format_date(
                    treatment_plan.start_date,
                ),
            ),
            PropertyFieldViewModel(
                label="Expected End",
                value=format_date(
                    treatment_plan.expected_end_date,
                    empty_value="—",
                ),
            ),
            PropertyFieldViewModel(
                label="RTM Program",
                value=treatment_plan.rtm_program_id,
            ),
        )

    @staticmethod
    def _build_goal(
            *,
            goal: TherapeuticGoalDTO,
    ) -> TherapeuticGoalViewModel:
        return TherapeuticGoalViewModel(
            goal_id=goal.goal_id,
            description=goal.description,
            target_date_display=format_date(
                goal.target_date,
                empty_value="—",
            ),
        )

    def _build_intervention(
            self,
            *,
            intervention: TreatmentInterventionDTO,
    ) -> TreatmentInterventionViewModel:
        return TreatmentInterventionViewModel(
            intervention_id=intervention.intervention_id,
            treatment_type_display=format_enum(
                intervention.treatment_type,
            ),
            description=intervention.description,
            status_badge=self._build_intervention_status_badge(
                status=intervention.status,
            ),
            date_range_display=format_date_range(
                start_date=intervention.start_date,
                end_date=intervention.end_date,
            ),
        )

    @staticmethod
    def _build_monitoring_parameter(
            *,
            monitoring_parameter: TreatmentMonitoringParameterDTO,
    ) -> TreatmentMonitoringParameterViewModel:
        return TreatmentMonitoringParameterViewModel(
            monitoring_parameter_id=(
                monitoring_parameter.monitoring_parameter_id
            ),
            measure_name=(
                monitoring_parameter.measure_definition_id
            ),
            baseline_display=format_measurement_value(
                value=monitoring_parameter.baseline_value,
                unit=monitoring_parameter.unit,
            ),
            target_display=format_measurement_value(
                value=monitoring_parameter.target_value,
                unit=monitoring_parameter.unit,
            ),
        )

    @staticmethod
    def _build_review(
            *,
            review: TreatmentPlanReviewDTO,
    ) -> TreatmentPlanReviewViewModel:
        return TreatmentPlanReviewViewModel(
            review_id=review.review_id,
            reviewed_at_display=format_datetime(
                review.reviewed_at,
            ),
            provider_display=review.provider_id,
            clinical_findings=review.clinical_findings,
            treatment_decision=review.treatment_decision,
            next_review_date_display=format_date(
                review.next_review_date,
                empty_value="—",
            ),
        )

    @staticmethod
    def _is_active(
            plan: TherapeuticPlanDTO,
    ) -> bool:
        return (
                plan.treatment_plan.status
                == TreatmentPlanStatus.ACTIVE
        )

    @staticmethod
    def _find_latest_review(
            *,
            treatment_plans: tuple[TherapeuticPlanDTO, ...],
    ) -> TreatmentPlanReviewDTO | None:
        reviews = (
            review
            for plan in treatment_plans
            for review in plan.reviews
        )

        return max(
            reviews,
            key=lambda review: review.reviewed_at,
            default=None,
        )

    @staticmethod
    def _build_plan_status_badge(
            *,
            status: TreatmentPlanStatus,
    ) -> BadgeViewModel:
        return BadgeViewModel(
            label=format_enum(status),
        )

    @staticmethod
    def _build_intervention_status_badge(
            *,
            status: InterventionStatus,
    ) -> BadgeViewModel:
        return BadgeViewModel(
            label=format_enum(status),
        )
