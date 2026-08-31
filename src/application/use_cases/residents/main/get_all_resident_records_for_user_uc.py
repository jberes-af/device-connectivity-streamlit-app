# /src/application/use_cases/contact/get_all_resident_records_for_user_uc.py

import logging

from src.domain.entities.person.resident_entities import (
    ResidentProfile,
    ResidentInCaseOfNeedContact,
)
from src.domain.entities.access.resource_access_entities import UserResourceAssignment

from src.application.ports.resident_repo_ports import (
    ResidentProfileRepositoryPort,
    ResidentContactInformationRepositoryPort,
)

from src.application.services.resident.get_resident_profile_service import (
    FetchResidentProfileService
)

from src.application.services.resident.get_resident_contacts_service import (
    FetchResidentContactsService,
)

from src.application.use_cases.residents.main.resident_uc_dtos import (
    ResidentSearchableRecordDTO,
    GetAllResidentRecordsRequestDTO,
    GetAllResidentRecordsResultDTO,
)

logger = logging.getLogger(__name__)


class GetAllResidentRecordsForUserUseCase:

    def __init__(
            self,
            *,
            fetch_resident_profile_repository: FetchResidentProfileService,
            fetch_resident_contacts_repository: FetchResidentContactsService,
    ):
        self._fetch_profile_repo = fetch_resident_profile_repository
        self._fetch_contacts_repo = fetch_resident_contacts_repository

        self._user_resident_access_repo = user_resident_access_repository

    def execute(
            self,
            request: GetAllResidentRecordsRequestDTO,
    ) -> GetAllResidentRecordsResultDTO:
        # --- RESIDENT RECORD FOR SELECTED PATIENT ID

        uid: str = request.user_id

        user_access_records: tuple[UserResourceAssignment, ...] = (
            self._user_resident_access_repo.list_resident_access_records_for_user_id(
                user_id=uid,
            )
        )

        resident_ids: list[str] = [
            r.resident_id for r in user_access_records
        ]

        profiles: tuple[ResidentProfile, ...] = (
            self._fetch_profile_repo.fetch_resident_profiles(
                resident_ids=resident_ids)
        )

        profiles_mapping: dict[str, ResidentProfile] = {
            r.resident_id: r
            for r in profiles
        }

        contacts: tuple[ResidentInCaseOfNeedContact, ...] = (
            self._fetch_contacts_repo.fetch_resident_contacts_profiles(
                resident_ids=resident_ids)
        )

        contacts_mapping: dict[str, ResidentInCaseOfNeedContact] = {
            r.resident_id: r
            for r in contacts
        }

        # --- RESIDENT RECORDS FOR SEARCHABLE TABLE

        profiles: list[ResidentProfile] = []
        need_contacts: list[ResidentInCaseOfNeedContact] = []
        table_records: list[ResidentSearchableRecordDTO] = []
        for r in resident_ids:
            profile: ResidentProfile = profiles_mapping[r]
            contact: ResidentInCaseOfNeedContact = contacts_mapping[r]
            table_records.append(
                ResidentSearchableRecordDTO(
                    resident_id=r,
                    full_name=profile.full_name,
                    date_of_birth=profile.date_of_birth,
                    contact_name=contact.contact_name,
                    active_status=profile.active_status,
                )
            )
            profiles.append(profile)
            need_contacts.append(contact)

        # logging.info("use profiles %s", profiles)

        return GetAllResidentRecordsResultDTO(
            resident_profiles=tuple(profiles),
            resident_need_case_contacts=tuple(need_contacts),
            resident_table_records=tuple(table_records),
        )
