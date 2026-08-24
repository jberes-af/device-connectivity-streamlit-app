# /src/gui/streamlit/screens/renderers/resident_section_router.py

from collections.abc import Callable

import logging

from src.interface_adapters.view_models.resident.segmented_controls_view_model import (
    ResidentSectionEnum,
)

from src.gui.streamlit.screens.resident.sections.appointments_section import (
    render_appointments_section,
)

from src.gui.streamlit.screens.resident.sections.billing_section import (
    render_billing_section,
)

from src.gui.streamlit.screens.resident.sections.care_plan_section import (
    render_care_plan_section,
)

from src.gui.streamlit.screens.resident.sections.clinical_docs_section import (
    render_clinical_docs_section,
)

from src.gui.streamlit.screens.resident.sections.communications_section import (
    render_communications_section,
)

from src.gui.streamlit.screens.resident.sections.contact_section import (
    render_contact_section,
)

from src.gui.streamlit.screens.resident.sections.payers_section import (
    render_payers_section,
)

from src.gui.streamlit.screens.resident.sections.priority_items_section import (
    render_priority_items_section,
)

from src.gui.streamlit.screens.resident.sections.providers_section import (
    render_providers_section,
)

from src.gui.streamlit.screens.resident.sections.sensing_section import (
    render_sensing_section,
)

from src.gui.streamlit.screens.resident.sections.treatment_section import (
    render_treatment_plan_section,
)

from src.main.compose_root_application import AppContainer

logger = logging.getLogger(__name__)

ResidentSectionHandler = Callable[..., None]

_SECTION_HANDLERS: dict[
    ResidentSectionEnum,
    ResidentSectionHandler,
] = {
    # ResidentSectionEnum.CONTACT:
        # render_contact_section,

    ResidentSectionEnum.PRIORITY_ITEMS:
        render_priority_items_section,

    ResidentSectionEnum.APPOINTMENTS:
        render_appointments_section,

    ResidentSectionEnum.CARE_PLAN:
        render_care_plan_section,

    ResidentSectionEnum.TREATMENT_PLAN:
        render_treatment_plan_section,

    ResidentSectionEnum.CLINICAL_DOCS:
        render_clinical_docs_section,

    ResidentSectionEnum.PROVIDERS:
        render_providers_section,

    ResidentSectionEnum.COMMUNICATIONS:
        render_communications_section,

    ResidentSectionEnum.PAYERS:
        render_payers_section,

    ResidentSectionEnum.SENSING:
        render_sensing_section,

    ResidentSectionEnum.BILLING:
        render_billing_section,
}


def render_resident_section(
        *,
        section: ResidentSectionEnum,
        resident_id: str,
        container: AppContainer,
) -> None:
    handler = _SECTION_HANDLERS.get(section)

    if handler is None:
        return

    logging.info("Handler object: %s", handler)

    handler(
        resident_id=resident_id,
        container=container,
    )
