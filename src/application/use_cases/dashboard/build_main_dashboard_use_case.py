# /src/application/use_cases/dashboard/build_main_dashboard_use_case.py


from datetime import datetime

from src.domain.enums.priority_items.priority_item_enums import (
    PriorityItemLevelEnum,
)

from src.application.use_cases.dashboard.main_dashboard_uc_dtos import (
    DashboardResidentAttentionDTO,
    MainDashboardDTO,
    # BuildDashboardMainPageRequestDTO,
    BuildDashboardMainPageResultDTO,
)


class BuildMainDashboardUseCase:

    def __init__(
            self,
    ):
        ...

    def execute(
            self,
            # request: BuildDashboardMainPageRequestDTO,
    ) -> BuildDashboardMainPageResultDTO:
        residents_attention = tuple([
            DashboardResidentAttentionDTO(
                resident_id='1a2b3c4d5e6f78g9',
                resident_name="First-1 Last-1",
                issue_summary="Refused medication. (placeholder value)",
                priority=PriorityItemLevelEnum.HIGH,
                occurred_at=datetime(
                    year=2026,
                    month=9,
                    day=3,
                    hour=11,
                    minute=59,
                    second=59,
                ),
            ),
            DashboardResidentAttentionDTO(
                resident_id='9z8y7x6w5v4u3t2s1e',
                resident_name="First-2 Last-2",
                issue_summary="Nighttime bed exit. (placeholder value)",
                priority=PriorityItemLevelEnum.MEDIUM,
                occurred_at=datetime(
                    year=2026,
                    month=9,
                    day=3,
                    hour=8,
                    minute=4,
                    second=2,
                ),

            ),
        ]
        )

        dashboard: MainDashboardDTO = MainDashboardDTO(
            residents_requiring_attention_count=3,
            residents_requiring_attention_delta=-2,

            priority_items_today_count=1,
            priority_items_today_delta=1,

            care_plans_current_rate=0.985,
            care_plans_current_delta=0.013,

            care_exception_count=5,
            care_exception_delta=1,

            residents_requiring_attention=residents_attention,

            residents_with_care_changes_count=4,
            care_routine_exception_count=6,
            care_routine_change_delta=+ 2,

            overdue_assessment_count=3,
            assessments_due_today_count=0,
            assessments_due_week_count=3,

            monitored_resident_count=22,
            total_monitorable_resident_count=22,
            online_sensor_count=78,
            total_sensor_count=81,
            sensor_issue_count=1,

            appointments_today_count=13,
            provider_review_count=5,
            follow_up_count=4,

        )

        return BuildDashboardMainPageResultDTO(
            dashboard=dashboard
        )
