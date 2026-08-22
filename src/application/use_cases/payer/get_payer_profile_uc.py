# /src/application/use_cases/payer/get_payer_overview_uc.py

from src.domain.entities.billing.payer_entities import PayerProfile

from src.application.ports.payer_repo_ports import (
    PayerRepositoryPort,
)

from src.application.services.get_payer_profile_service import (
    FetchPayerProfileService,
)

from src.application.use_cases.payer.payer_profile_uc_dtos import (
    GetPayerProfileRequestDTO,
    GetPayerProfileResultDTO,
)


class GetPayerProfileUseCase:

    def __init__(
            self,
            *,
            payer_repository: PayerRepositoryPort,
            fetch_payer_profile_service: FetchPayerProfileService,
    ):
        self._payer_repository = payer_repository
        self._fetch_payer_service = fetch_payer_profile_service

    def execute(
            self,
            request: GetPayerProfileRequestDTO,
    ) -> GetPayerProfileResultDTO:
        profile: PayerProfile = (
            self._fetch_payer_service.fetch_payer_profile(
                payer_id=request.payer_id))

        return GetPayerProfileResultDTO(
            payer_profile=profile,
        )
