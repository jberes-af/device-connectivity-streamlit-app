# /src/interface_adapters/presenters/dashboard/dashboard_main_presenter.py

from src.domain.enums.priority_items.priority_item_enums import (
    PriorityItemLevelEnum,
)

from src.application.use_cases.dashboard.main_dashboard_uc_dtos import (
    # BuildDashboardMainPageRequestDTO,
    BuildDashboardMainPageResultDTO, MainDashboardDTO,
)

from src.interface_adapters.view_models.widgets.badge_view_model import (
    BadgeVariant,
    BadgeViewModel,
)

from src.interface_adapters.view_models.dashboard.dashboard_view_models import (
    DashboardMainPageViewModel,
    DashboardResidentAttentionRowViewModel,
    DashboardResidentAttentionViewModel,
    DashboardSummaryDetailCardViewModel,
    MetricCardViewModel,
)

from src.interface_adapters.presenters.utils_presenters import (
    format_change_since_yesterday,
    format_elapsed_time,
    format_percentage,
    format_percentage_delta,
    format_signed_delta,
)


class DashboardMainPagePresenter:

    def present(
            self,
            result: BuildDashboardMainPageResultDTO,
    ) -> DashboardMainPageViewModel:
        return DashboardMainPageViewModel(
            kpi_cards=self._present_kpi_cards(result.dashboard),
            resident_attention=self._present_resident_attention(result.dashboard),
            summary_detail_cards=self._present_summary_detail_cards(result.dashboard),
        )

    @staticmethod
    def _present_kpi_cards(
            result: MainDashboardDTO,
    ) -> tuple[MetricCardViewModel, ...]:
        return (
            MetricCardViewModel(
                label="Residents Requiring Attention",
                value=str(result.residents_requiring_attention_count),
                delta=format_signed_delta(
                    result.residents_requiring_attention_delta,
                ),
                help_text=(
                    "Residents with active priority items, care exceptions, "
                    "overdue reviews, or monitoring issues."
                ),
            ),
            MetricCardViewModel(
                label="Priority Items",
                value=str(result.priority_items_today_count),
                delta=format_signed_delta(
                    result.priority_items_today_delta,
                ),
                help_text="Priority items requiring attention today.",
            ),
            MetricCardViewModel(
                label="Care Plans Current",
                value=format_percentage(
                    result.care_plans_current_rate,
                ),
                delta=format_percentage_delta(
                    result.care_plans_current_delta,
                ),
                help_text="Residents with a current care-plan assessment.",
            ),
            MetricCardViewModel(
                label="Care Exceptions",
                value=str(result.care_exception_count),
                delta=format_signed_delta(
                    result.care_exception_delta,
                ),
                help_text="Active care or routine exceptions requiring review.",
            ),
        )

    @staticmethod
    def _present_resident_attention(
            result: MainDashboardDTO,
    ) -> DashboardResidentAttentionViewModel:
        rows = tuple(
            DashboardResidentAttentionRowViewModel(
                resident_id=item.resident_id,
                resident_name=item.resident_name,
                issue=item.issue_summary,
                priority=_present_priority_badge(
                    item.priority,
                ),
                since=format_elapsed_time(
                    item.occurred_at,
                ),
            )
            for item in result.residents_requiring_attention
        )

        return DashboardResidentAttentionViewModel(
            title="Residents Requiring Attention",
            rows=rows,
        )

    @staticmethod
    def _present_summary_detail_cards(
            result: MainDashboardDTO,
    ) -> tuple[DashboardSummaryDetailCardViewModel, ...]:
        return (
            DashboardSummaryDetailCardViewModel(
                card_id="care_routine_changes",
                title="Care & Routine Changes",
                primary_value=(
                    f"{result.residents_with_care_changes_count} residents"
                ),
                details=(
                    f"{result.care_routine_exception_count} exceptions",
                    format_change_since_yesterday(
                        result.care_routine_change_delta,
                    ),
                ),
                button_label="View affected residents",
            ),
            DashboardSummaryDetailCardViewModel(
                card_id="assessments_reviews",
                title="Assessments & Reviews",
                primary_value=(
                    f"{result.overdue_assessment_count} overdue"
                ),
                details=(
                    f"{result.assessments_due_today_count} due today",
                    f"{result.assessments_due_week_count} due this week",
                ),
                button_label="View assessments",
            ),
            DashboardSummaryDetailCardViewModel(
                card_id="monitoring_status",
                title="Monitoring Status",
                primary_value=(
                    f"{result.monitored_resident_count} / "
                    f"{result.total_monitorable_resident_count} monitored"
                ),
                details=(
                    (
                        f"{result.online_sensor_count} / "
                        f"{result.total_sensor_count} sensors online"
                    ),
                    f"{result.sensor_issue_count} sensor issues",
                ),
                button_label="View sensing",
            ),
            DashboardSummaryDetailCardViewModel(
                card_id="todays_schedule",
                title="Today's Schedule",
                primary_value=(
                    f"{result.appointments_today_count} appointments"
                ),
                details=(
                    f"{result.provider_review_count} reviews",
                    f"{result.follow_up_count} follow-ups",
                ),
                button_label="View schedule",
            ),
        )


def _present_priority_badge(
        priority,
) -> BadgeViewModel:
    match priority:
        case PriorityItemLevelEnum.CRITICAL:
            return BadgeViewModel(
                label="Critical",
                variant=BadgeVariant.ERROR,
            )

        case PriorityItemLevelEnum.HIGH:
            return BadgeViewModel(
                label=PriorityItemLevelEnum.HIGH,
                variant=BadgeVariant.WARNING,
            )

        case PriorityItemLevelEnum.MEDIUM:
            return BadgeViewModel(
                label=PriorityItemLevelEnum.MEDIUM,
                variant=BadgeVariant.INFO,
            )

        case PriorityItemLevelEnum.LOW.lower():
            return BadgeViewModel(
                label=PriorityItemLevelEnum.LOW,
                variant=BadgeVariant.NEUTRAL,
            )

        case _:
            return BadgeViewModel(
                label="Unknown",
                variant=BadgeVariant.NEUTRAL,
            )
