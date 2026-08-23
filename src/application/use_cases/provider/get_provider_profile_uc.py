# /src/application/use_cases/provider/get_provider_profile_uc.py

from src.application.services.get_provider_profile_service import (
    FetchProviderProfileService
)

from src.domain.entities.care.provider_entities import ProviderProfile

from src.domain.entities.person.patient_entities import (
    PatientProvider,
)

from src.application.ports.patient_repo_ports import (
    PatientProviderRepositoryPort,
)

from src.application.ports.provider_repo_ports import (
    ProviderRepositoryPort,
)

from src.application.use_cases.provider.provider_profile_uc_dtos import (
    GetProviderProfileRequestDTO,
    GetProviderProfileResultDTO,
)


class GetPatientProviderProfileUseCase:

    def __init__(
            self,
            *,
            provider_repository: ProviderRepositoryPort,
            fetch_provider_profile_service: FetchProviderProfileService,
    ):
        self._provider_repository = provider_repository
        self._fetch_provider_service = fetch_provider_profile_service

    def execute(
            self,
            request: GetProviderProfileRequestDTO,
    ) -> GetProviderProfileResultDTO:
        profile: ProviderProfile = (
            self._fetch_provider_service.fetch_provider_profile(
                provider_id=request.provider_id))

        return GetProviderProfileResultDTO(
            provider_profile=profile,
        )
