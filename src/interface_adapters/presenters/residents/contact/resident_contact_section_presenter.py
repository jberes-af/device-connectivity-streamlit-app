# /src/interface_adapters/presenters/contact/resident_contact_section_presenter.py

import logging

from src.domain.entities.person.resident_entities import (
    ResidentProfile,
    ResidentInCaseOfNeedContact,
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

from src.interface_adapters.view_models.residents.main_page.resident_main_view_model import (
    ResidentContactViewModel,
)

from src.interface_adapters.presenters.utils_presenters import (
    format_optional,
    format_bool,
    format_date,
    format_state_postal,
)

logger = logging.getLogger(__name__)


class ResidentContactSectionPresenter:

    def present(
            self,
            profile: ResidentProfile,
            need_case_contact: ResidentInCaseOfNeedContact,
            icon: str,
    ) -> ResidentContactViewModel:
        # logging.info("resident profile %s", profile)
        # logging.info("need case contact %s", need_case_contact)

        return ResidentContactViewModel(
            # section_title=":material/contact_page: Contact Information",
            section_title=f"{icon} Contact Information",
            resident_profile_card_grid=self._present_resident_info_card_grid(
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
                        value=profile.full_name
                    ),
                    PropertyFieldViewModel(
                        label="Preferred Name",
                        value=profile.preferred_name
                    ),
                    PropertyFieldViewModel(
                        label="Date of Birth",
                        value=format_date(profile.date_of_birth),
                    ),
                    PropertyFieldViewModel(
                        label="Resident ID",
                        value=profile.resident_id,
                    ),
                    PropertyFieldViewModel(
                        label="Telephone",
                        value=format_optional(profile.telephone),
                    ),
                    PropertyFieldViewModel(
                        label="Email",
                        value=format_optional(profile.email),
                    ),
                    PropertyFieldViewModel(
                        label="Street",
                        value=format_optional(profile.address_line_1),
                    ),
                    PropertyFieldViewModel(
                        label="City",
                        value=format_optional(profile.city),
                    ),
                    PropertyFieldViewModel(
                        label="State • Zip",
                        value=format_state_postal(
                            state=profile.state,
                            postal_code=profile.postal_code,
                        ),
                    ),
                    PropertyFieldViewModel(
                        label="Room",
                        value=format_optional(profile.room_reference),
                    ),
                    PropertyFieldViewModel(
                        label="Tenant ID",
                        value=profile.tenant_id,
                    ),
                    PropertyFieldViewModel(
                        label="Status",
                        value=format_bool(profile.active_status),
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
                        value=format_optional(
                            need_case_contact.contact_name
                        ),
                    ),
                    PropertyFieldViewModel(
                        label="Telephone",
                        value=format_optional(
                            need_case_contact.contact_telephone
                        ),
                    ),
                    PropertyFieldViewModel(
                        label="Email",
                        value=format_optional(
                            need_case_contact.contact_email
                        ),
                    ),
                    PropertyFieldViewModel(
                        label="Address",
                        value=format_optional(
                            need_case_contact.contact_address
                        ),
                    ),
                    PropertyFieldViewModel(
                        label="Relationship",
                        value=format_optional(
                            need_case_contact.contact_relationship
                        ),
                    ),
                ),
            ),
        )
