# /src/gui/streamlit/screens/resident/sections/contact_section.py

from src.domain.entities.person.resident_entities import (
    ResidentProfile,
    ResidentInCaseOfNeedContact,
)

from src.gui.streamlit.screens.resident.renderers.resident_contact_renderer import (
    render_resident_contact_info)

from src.interface_adapters.presenters.person.resident.resident_main_page_presenter import (
    ResidentMainPagePresenter)

from src.interface_adapters.view_models.resident.resident_main_view_model import (
    ResidentContactViewModel)


# use case is already run in resident_screen.py

def render_contact_section(
        *,
        resident_id: str,
        # container: AppContainer,
        resident_profiles: tuple[ResidentProfile, ...],
        resident_need_contacts: tuple[ResidentInCaseOfNeedContact, ...],
        presenter: ResidentMainPagePresenter,
) -> None:
    resident_profile: ResidentProfile | None = next(
        (
            profile
            for profile in resident_profiles
            if profile.resident_id == resident_id
        ),
        None,
    )

    need_contact: ResidentInCaseOfNeedContact | None = next(
        (
            contact
            for contact in resident_need_contacts
            if contact.resident_id == resident_id
        ),
        None,
    )

    if resident_profile is None:
        return

    if need_contact is None:
        return

    section_vm: ResidentContactViewModel = (
        presenter.present_resident_contact_records(
            resident_profile=resident_profile,
            resident_need_case_contact=need_contact,
        ))

    render_resident_contact_info(
        resident_id=resident_id,
        view_model=section_vm,
    )
