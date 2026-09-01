# /src/application/use_cases/contact/get_all_resident_records_for_user_uc.py

import logging

from src.application.context import AccessScope

from src.application.services.resident.get_resident_contacts_service import (
    FetchResidentContactsService,
)

from src.application.services.resident.get_resident_profile_service import (
    FetchResidentProfileService,
)

from src.application.use_cases.residents.main.resident_uc_dtos import (
    GetAllResidentRecordsRequestDTO,
    GetAllResidentRecordsResultDTO,
    ResidentSearchableRecordDTO,
)

from src.domain.entities.resident.resident_entities import (
    ResidentInCaseOfNeedContact,
    ResidentProfile,
)

from src.domain.enums.access.permission_enums import (
    PermissionEnum,
)

from src.domain.enums.access.resource_access_enums import (
    ResourceScopeEnum,
)

logger = logging.getLogger(__name__)


class GetAllResidentRecordsForUserUseCase:

    def __init__(
            self,
            *,
            fetch_resident_profile_service: FetchResidentProfileService,
            fetch_resident_contacts_service: FetchResidentContactsService,
    ) -> None:
        self._fetch_profile_service = fetch_resident_profile_service
        self._fetch_contacts_service = fetch_resident_contacts_service

    def execute(
            self,
            *,
            request: GetAllResidentRecordsRequestDTO,
            access_scope: AccessScope,
    ) -> GetAllResidentRecordsResultDTO:
        # --- AUTHORIZE CAPABILITY

        if (
                PermissionEnum.RESIDENT_VIEW
                not in access_scope.permissions
        ):
            raise PermissionError(
                "User does not have permission to view residents."
            )

        # --- RESOLVE AUTHORIZED RESIDENT PROFILES

        profiles: tuple[ResidentProfile, ...] = (

            self._fetch_authorized_profiles(
                access_scope=access_scope,
            ))

        logging.info("profiles: %s", profiles)

        resident_ids = tuple(
            profile.resident_id
            for profile in profiles
        )
        logging.info("resident_ids: %s", resident_ids)

        # --- FETCH RELATED CONTACT RECORDS

        contacts: tuple[ResidentInCaseOfNeedContact, ...] = (
            self._fetch_contacts_service
            .fetch_resident_contacts_profiles(
                resident_ids=resident_ids,
            )
        )

        logging.info("contacts: %s", contacts)

        contacts_by_resident_id = {
            contact.resident_id: contact
            for contact in contacts
        }

        # --- BUILD SEARCHABLE TABLE RECORDS

        table_records: list[ResidentSearchableRecordDTO] = []

        for profile in profiles:
            contact = contacts_by_resident_id.get(
                profile.resident_id
            )

            table_records.append(
                ResidentSearchableRecordDTO(
                    resident_id=profile.resident_id,
                    full_name=profile.full_name,
                    date_of_birth=profile.date_of_birth,
                    contact_name=(
                        contact.contact_name
                        if contact is not None
                        else None
                    ),
                    active_status=profile.active_status,
                )
            )

        return GetAllResidentRecordsResultDTO(
            resident_profiles=profiles,
            resident_need_case_contacts=contacts,
            resident_table_records=tuple(table_records),
        )

    def _fetch_authorized_profiles(
            self,
            *,
            access_scope: AccessScope,
    ) -> tuple[ResidentProfile, ...]:
        if (
                access_scope.resident_scope
                == ResourceScopeEnum.ASSIGNED
        ):
            return (
                self._fetch_profile_service
                .fetch_resident_profiles(
                    resident_ids=tuple(
                        access_scope.resident_ids
                    ),
                )
            )

        if (
                access_scope.resident_scope
                == ResourceScopeEnum.TENANT
        ):
            return (
                self._fetch_profile_service
                .fetch_resident_profiles_for_tenant_ids(
                    tenant_ids=tuple(
                        access_scope.tenant_ids
                    ),
                )
            )

        if (
                access_scope.resident_scope
                == ResourceScopeEnum.PLATFORM
        ):
            return (
                self._fetch_profile_service
                .fetch_all_resident_profiles()
            )

        raise PermissionError(
            "Unsupported resident access scope."
        )
