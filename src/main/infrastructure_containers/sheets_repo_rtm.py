# /src/main/infrastructure_containers/sheets_repo_rtm.py

from dataclasses import dataclass

from src.application.ports.rtm_repo_ports import (
    RtmEnrollmentRepositoryPort,
    RtmNecessityRepositoryPort,
)

from src.infrastructure.config.app_config_models import (
    AppRuntimeConfig,
)
from src.infrastructure.config.settings_model import (
    Settings,
)

from src.infrastructure.persistence.google_sheets.mappers.rtm.rtm_enrollment_row_mapper import (
    RtmEnrollmentRowMapper,
)

from src.infrastructure.persistence.google_sheets.mappers.rtm.rtm_necessity_row_mapper import (
    RtmNecessityRowMapper
)

from src.infrastructure.persistence.google_sheets.repos.rtm.rtm_enrollment_repository import (
    GoogleSheetsRtmEnrollmentRepository,
)

from src.infrastructure.persistence.google_sheets.repos.rtm.rtm_necessity_repository import (
    GoogleSheetsRtmNecessityRepository,
)

from src.main.infrastructure_containers.utils_sheets_composition_root import (
    build_google_sheets_query_service,
    build_google_sheet_catalog,
)


@dataclass(frozen=True, slots=True)
class GoogleSheetsRtmRepositories:
    rtm_enrollment_repository: RtmEnrollmentRepositoryPort
    rtm_necessity_repository: RtmNecessityRepositoryPort


def build_google_sheets_rtm_repositories(
        *,
        settings: Settings,
        app_config: AppRuntimeConfig,
) -> GoogleSheetsRtmRepositories:
    query_service = build_google_sheets_query_service(
        settings=settings,
    )

    catalog = build_google_sheet_catalog(
        settings=settings,
        app_config=app_config,
    )

    rtm_enrollment_repository: RtmEnrollmentRepositoryPort = (
        GoogleSheetsRtmEnrollmentRepository(
            query_service=query_service,
            catalog=catalog,
            mapper=RtmEnrollmentRowMapper(),
        ))

    rtm_necessity_repo: RtmNecessityRepositoryPort = (
        GoogleSheetsRtmNecessityRepository(
            query_service=query_service,
            catalog=catalog,
            mapper=RtmNecessityRowMapper(),
        ))

    return GoogleSheetsRtmRepositories(
        rtm_enrollment_repository=rtm_enrollment_repository,
        rtm_necessity_repository=rtm_necessity_repo
    )
