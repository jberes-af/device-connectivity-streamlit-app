# /src/gui/streamlit/routing/routes.py

from src.gui.streamlit.routing.route_types import Route

from src.application.context import AccessScope
from src.main.compose_root_application import AppContainer


from src.gui.streamlit.screens.sensing.sensing_dependencies import (
    SensingPageDependencies
)

from src.gui.streamlit.screens.sensing.main_sensing_view import (
    render_sensing_page,
)


def build_routes(
        sensing_dependencies: SensingPageDependencies,
) -> tuple[Route, ...]:
    def render_sensing() -> None:
        render_sensing_page(
            dependencies=sensing_dependencies,
        )

    """
    def render_dashboard() -> None:
        render_dashboard_page(
            dependencies=dashboard_dependencies,
        )


    def render_residents() -> None:
        render_residents_page(
            container=app_container,
            access_scope=access_scope,
        )

    return (
        Route(
            route_id="dashboard",
            label="Dashboard",
            handler=render_dashboard,
            icon=":material/dashboard:",
        ),
        Route(
            route_id="residents",
            label="Residents",
            handler=render_residents,
            icon=":material/groups:",
        ),
        Route(
            route_id="sensing",
            label="Sensing",
            # legacy_handler=render_sensing_page,
            handler=render_sensing,
            icon=":material/sensors:",
        ),
        Route(
            route_id="schedule",
            label="Schedule",
            legacy_handler=render_schedule_page,
            icon=":material/calendar_month:",
        ),
        Route(
            route_id="reports",
            label="Reports",
            legacy_handler=render_reports_page,
            icon=":material/analytics:",
        ),
        Route(
            route_id="billing",
            label="Billing",
            legacy_handler=render_billing_page,
            icon=":material/receipt_long:",
        ),
        Route(
            route_id="administration",
            label="Administration",
            legacy_handler=render_administration_page,
            icon=":material/note_alt:",
        ),
    )
    """

    return (
        Route(
            route_id="sensing",
            label="Sensing",
            # legacy_handler=render_sensing_page,
            handler=render_sensing,
            icon=":material/sensors:",
        ),
    )
