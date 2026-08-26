# /src/application/use_cases/contact/get_all_resident_records_for_user_uc.py

import logging

from src.domain.entities.person.resident_entities import (
    ResidentProfile,
    ResidentInCaseOfNeedContact,
)
from src.domain.entities.access.access_entities import (
    UserResidentAccess,
)

from src.application.ports.resident_repo_ports import (
    ResidentProfileRepositoryPort,
    ResidentContactInformationRepositoryPort,
)
from src.application.ports.access_repo_ports import (
    UserResidentAccessRepositoryPort,
)

"""
from src.application.use_cases.treatment.patient_uc_dtos import (
    PatientOverviewDevDTO,
    PatientAdministrationDTO,
    RTMEnrollmentSummaryDTO,
    PatientSearchableRecordDTO,
"""

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
            user_resident_access_repository: UserResidentAccessRepositoryPort,
            resident_profile_repository: ResidentProfileRepositoryPort,
            resident_contacts_repository: ResidentContactInformationRepositoryPort,

            # patient_repository: PatientRepositoryPort,
            # patient_diagnosis_repository: PatientDiagnosisRepositoryPort,
            # patient_provider_repository: PatientProviderRepositoryPort,
            # patient_payer_repository: PatientPayerRepositoryPort,
            # rtm_enrollment_repository: RTMEnrollmentRepositoryPort,
            # provider_repository: ProviderRepositoryPort,
            # payer_repository: PayerRepositoryPort,
    ):
        self._resident_profile_repo = resident_profile_repository
        self._user_resident_access_repo = user_resident_access_repository
        self._resident_contacts_repo = resident_contacts_repository

    def execute(
            self,
            request: GetAllResidentRecordsRequestDTO,
    ) -> GetAllResidentRecordsResultDTO:
        # --- RESIDENT RECORD FOR SELECTED PATIENT ID

        uid: str = request.user_id

        user_access_records: tuple[UserResidentAccess, ...] = (
            self._user_resident_access_repo.list_resident_access_records_for_user_id(
                user_id=uid,
            )
        )

        resident_ids: list[str] = [
            r.resident_id for r in user_access_records
        ]

        resident_profiles: dict[str, ResidentProfile] = {
            r: self._resident_profile_repo.get_by_id(r)
            for r in resident_ids
        }

        need_case_contacts: dict[str, ResidentInCaseOfNeedContact] = {
            r: self._resident_contacts_repo.get_by_id(r)
            for r in resident_ids
        }

        # --- RESIDENT RECORDS FOR SEARCHABLE TABLE

        profiles: list[ResidentProfile] = []
        need_contacts: list[ResidentInCaseOfNeedContact] = []
        table_records: list[ResidentSearchableRecordDTO] = []
        for r in resident_ids:
            profile: ResidentProfile = resident_profiles[r]
            contact: ResidentInCaseOfNeedContact = need_case_contacts[r]
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

        logging.info("use profiles %s", profiles)

        return GetAllResidentRecordsResultDTO(
            resident_profiles=tuple(profiles),
            resident_need_case_contacts=tuple(need_contacts),
            resident_table_records=tuple(table_records),
        )
