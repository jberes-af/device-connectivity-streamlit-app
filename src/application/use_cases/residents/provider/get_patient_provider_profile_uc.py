# /src/application/use_cases/residents/provider/get_patient_provider_profile_uc.py

from src.domain.entities.care.provider_entities import ProviderProfile

from src.domain.entities.resident.patient_entities import PatientProvider

from src.application.ports.patient_repo_ports import (
    PatientProviderRepositoryPort,
)

from src.application.services.provider.get_provider_profile_service import (
    FetchProviderProfileService,
)

from src.application.use_cases.residents.provider.patient_provider_uc_dtos import (
    PatientProviderProfileDTO,
    GetPatientProviderProfileRequestDTO,
    GetPatientProviderProfileResultDTO,
)


class GetPatientProviderProfileUseCase:

    def __init__(
            self,
            *,
            fetch_provider_profile_service: FetchProviderProfileService,
            patient_provider_repository: PatientProviderRepositoryPort,
    ) -> None:
        self._fetch_provider_service = fetch_provider_profile_service
        self._patient_provider_repo = patient_provider_repository

    def execute(
            self,
            request: GetPatientProviderProfileRequestDTO,
    ) -> GetPatientProviderProfileResultDTO:
        patient_providers: tuple[PatientProvider, ...] = (
            self._patient_provider_repo
            .list_providers_for_patient_id(
                patient_id=request.patient_id,
            )
        )

        provider_profiles: tuple[ProviderProfile, ...] = (
            self._fetch_provider_service.fetch_provider_profiles(
                provider_ids=tuple(
                    patient_provider.provider_id
                    for patient_provider in patient_providers
                ),
            )
        )

        provider_by_id: dict[str, ProviderProfile] = {
            provider.provider_id: provider
            for provider in provider_profiles
        }

        result_profiles = tuple(
            PatientProviderProfileDTO(
                patient_provider_id=patient_provider.patient_provider_id,
                provider_id=patient_provider.provider_id,
                national_provider_identifier=(
                    provider_by_id[
                        patient_provider.provider_id
                    ].national_provider_identifier
                ),
                first_name=provider_by_id[
                    patient_provider.provider_id
                ].first_name,
                middle_name=provider_by_id[
                    patient_provider.provider_id
                ].middle_name,
                last_name=provider_by_id[
                    patient_provider.provider_id
                ].last_name,
                role=patient_provider.role,
                credentials=provider_by_id[
                    patient_provider.provider_id
                ].credentials,
                specialty=provider_by_id[
                    patient_provider.provider_id
                ].specialty,
                organization_id=provider_by_id[
                    patient_provider.provider_id
                ].organization_id,
                effective_date=patient_provider.effective_date,
                termination_date=patient_provider.termination_date,
                is_active=provider_by_id[
                    patient_provider.provider_id
                ].is_active,
            )
            for patient_provider in patient_providers
        )

        return GetPatientProviderProfileResultDTO(
            provider_profiles=result_profiles,
        )
