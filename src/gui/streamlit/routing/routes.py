# /src/gui/streamlit/routing/routes.py

from src.gui.streamlit.routing.route_types import Route

from src.gui.streamlit.screens.administration_screen import (
    render_administration_page,
)

from src.gui.streamlit.screens.billing_screen import render_billing_page

from src.gui.streamlit.screens.dashboard_screen import render_dashboard_page

from src.gui.streamlit.screens.resident.resident_screen import render_residents_page

from src.gui.streamlit.screens.reports_screen import render_reports_page

from src.gui.streamlit.screens.schedule_screen import render_schedule_page

ROUTES: tuple[Route, ...] = (
    Route(
        route_id="dashboard",
        label="Dashboard",
        handler=render_dashboard_page,
        icon=":material/dashboard:",
    ),
    Route(
        route_id="residents",
        label="Residents",
        handler=render_residents_page,
        icon=":material/groups:",
    ),
    Route(
        route_id="schedule",
        label="Schedule",
        handler=render_schedule_page,
        icon=":material/calendar_month:",
    ),
    Route(
        route_id="reports",
        label="Reports",
        handler=render_reports_page,
        icon=":material/analytics:",
    ),
    Route(
        route_id="billing",
        label="Billing",
        handler=render_billing_page,
        icon=":material/receipt_long:",
    ),
    Route(
        route_id="administration",
        label="Administration",
        handler=render_administration_page,
        icon=":material/note_alt:",
    ),
)
