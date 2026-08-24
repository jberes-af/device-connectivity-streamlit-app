# /src/application/services/care/get_rtm_service.py

from typing import Sequence

from src.domain.entities.care.rtm_entities import (
    RtmMedicalNecessity,
)

from src.application.ports.rtm_repo_ports import (
    RtmNecessityRepositoryPort,
)


class FetchRtmNecessityService:

    def __init__(
            self,
            *,
            rtm_necessity_repository: RtmNecessityRepositoryPort,
    ):
        self._necessity_repo = rtm_necessity_repository

    def fetch_rtm_enrollment(
            self,
            rtm_necessity_id: str,
    ) -> RtmMedicalNecessity:
        return self._necessity_repo.get_by_id(rtm_necessity_id=rtm_necessity_id)

    def fetch_rtm_necessity(
            self,
            rtm_necessity_ids: Sequence[str],
    ) -> tuple[RtmMedicalNecessity, ...]:
        return tuple(
            self._necessity_repo.get_by_ids(
                rtm_necessity_ids=rtm_necessity_ids)
        )

    def fetch_rtm_necessity_records_for_patient(
            self,
            patient_id: str,
    ) -> tuple[RtmMedicalNecessity, ...]:
        return tuple(
            self._necessity_repo.list_rtm_necessity_records_patient_id(
                patient_id=patient_id)
        )
