# /src/interface_adapters/presenters/resident/resident_contact_section_presenter.py

from datetime import date, datetime

from src.domain.entities.person.resident_entities import (
    ResidentProfile,
    ResidentInCaseOfNeedContact,
)

from src.interface_adapters.view_models.common.card_view_models import (
    CardPropertyFieldsViewModel,
)

from src.interface_adapters.view_models.common.property_field_view_model import (
    PropertyFieldViewModel,
)

from src.interface_adapters.view_models.common.card_grid_view_model import (
    CardGridViewModel,
)

from src.interface_adapters.view_models.resident.resident_main_page_view_model import (
    ResidentContactViewModel,
)


class ResidentContactSectionPresenter:

    def present(
            self,
            profile: ResidentProfile,
            need_case_contact: ResidentInCaseOfNeedContact,
    ) -> ResidentContactViewModel:
        return ResidentContactViewModel(
            section_title=":material/contact_page: Contact Information",
            resident_info_card_grid=self._present_resident_info_card_grid(
                profile=profile,
            ),
            in_case_of_need_card_grid=self._present_need_contact_card_grid(
                need_case_contact=need_case_contact,
            ),
        )

    def _present_resident_info_card_grid(
            self,
            profile: ResidentProfile,
    ) -> CardGridViewModel:
        return CardGridViewModel(
            columns=1,
            cards=self._build_profile_cards(
                profile=profile,
            ),
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
    def _build_profile_cards(
            profile: ResidentProfile,
    ) -> tuple[CardPropertyFieldsViewModel, ...]:
        return (
            CardPropertyFieldsViewModel(
                title="Resident Profile",
                id="resident_contact_profile",
                property_fields=(
                    PropertyFieldViewModel(
                        label="Resident Name",
                        value=profile.full_name,
                    ),
                    PropertyFieldViewModel(
                        label="Preferred Name",
                        value=profile.preferred_name,
                    ),
                    PropertyFieldViewModel(
                        label="Date of Birth",
                        value=_format_date(profile.date_of_birth),
                    ),
                    PropertyFieldViewModel(
                        label="Resident ID",
                        value=profile.resident_id,
                    ),
                    PropertyFieldViewModel(
                        label="Telephone",
                        value=_format_optional(profile.telephone),
                    ),
                    PropertyFieldViewModel(
                        label="Email",
                        value=_format_optional(profile.email),
                    ),
                    PropertyFieldViewModel(
                        label="Street",
                        value=_format_optional(profile.address_line_1),
                    ),
                    PropertyFieldViewModel(
                        label="City",
                        value=_format_optional(profile.city),
                    ),
                    PropertyFieldViewModel(
                        label="State • Zip",
                        value=_format_state_postal(
                            state=profile.state,
                            postal_code=profile.postal_code,
                        ),
                    ),
                    PropertyFieldViewModel(
                        label="Room",
                        value=_format_optional(profile.room_reference),
                    ),
                    PropertyFieldViewModel(
                        label="Tenant ID",
                        value=profile.tenant_id,
                    ),
                    PropertyFieldViewModel(
                        label="Status",
                        value=_format_bool(profile.active_status),
                    ),
                ),
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


def _format_optional(value: str | None) -> str:
    return value or "—"


def _format_bool(value: bool | None) -> str:
    if value is None:
        return "Unknown"
    if value:
        return "Active"
    return "Inactive"


def _format_date(
        value: datetime | date | None,
) -> str:
    if value is None:
        return "—"

    return value.strftime("%b %d, %Y")


def _format_state_postal(
        state: str | None,
        postal_code: str | None,
) -> str:
    parts = [
        value
        for value in (state, postal_code)
        if value
    ]

    return " • ".join(parts) if parts else "—"
