# /src/interface_adapters/presenters/provider/provider_section_presenter.py


from src.application.use_cases.resident.resident_uc_dtos import (
    GetAllResidentRecordsRequestDTO
)

from src.interface_adapters.view_models.resident.resident_main_view_model import (
    ResidentTabIdEnum,
    ResidentMainPageTopViewModel,
    ResidentRecordCardGridViewModel,
    ResidentTabViewModel,
    ResidentRecordTabsViewModel,
)

# from src.interface_adapters.view_models.common.table_view_model import (
#     TableViewModel,
# )

from src.interface_adapters.view_models.common.card_view_models import (
    CardTitleTextButtonViewModel,
)

from src.interface_adapters.view_models.common.card_grid_view_model import (
    CardGridViewModel
)

# from src.interface_adapters.presenters.resident.searchable_table_presenter import (
#     ResidentRecordsSearchableTablePresenter,
# )


class ProviderSectionPresenter:

    def present(
            self,
            profile: ResidentProfile,
            need_case_contact: ResidentInCaseOfNeedContact,
            icon: str,
    ) -> ResidentContactViewModel:

        return ResidentContactViewModel(
            # section_title=":material/contact_page: Contact Information",
            section_title=f"{icon} Provider Information",
            resident_info_card_grid=self._present_resident_info_card_grid(
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


