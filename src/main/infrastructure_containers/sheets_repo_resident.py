# /src/main/infrastructure_containers/sheets_repo_resident.py

from dataclasses import dataclass

from src.application.ports.resident_repo_ports import (
    ResidentProfileRepositoryPort,
    ResidentContactInformationRepositoryPort,
)

from src.infrastructure.config.app_config_models import (
    AppRuntimeConfig,
)
from src.infrastructure.config.settings_model import (
    Settings,
)

from src.infrastructure.persistence.google_sheets.mappers.resident.resident_profile_row_mapper import (
    ResidentProfileRowMapper,
)
from src.infrastructure.persistence.google_sheets.mappers.resident.resident_contact_information_row_mapper import (
    ResidentContactInformationRowMapper
)

from src.infrastructure.persistence.google_sheets.repos.resident.resident_profile_repository import (
    GoogleSheetsResidentProfileRepository,
)
from src.infrastructure.persistence.google_sheets.repos.resident.resident_contact_information_repository import (
    GoogleSheetsResidentContactInformationRepository,
)

from src.main.infrastructure_containers.utils_sheets_composition_root import (
    build_google_sheets_query_service,
    build_google_sheet_catalog,
)


@dataclass(frozen=True, slots=True)
class GoogleSheetsResidentRepositories:
    resident_profile_repository: ResidentProfileRepositoryPort
    resident_contact_info_repository: ResidentContactInformationRepositoryPort
    # user_resident_access_repository: UserResidentAccessRepositoryPort


def build_google_sheets_resident_repositories(
        *,
        settings: Settings,
        app_config: AppRuntimeConfig,
) -> GoogleSheetsResidentRepositories:
    query_service = build_google_sheets_query_service(
        settings=settings,
    )

    catalog = build_google_sheet_catalog(
        settings=settings,
        app_config=app_config,
    )

    resident_profile_repo: ResidentProfileRepositoryPort = (
        GoogleSheetsResidentProfileRepository(
            query_service=query_service,
            catalog=catalog,
            mapper=ResidentProfileRowMapper(),
        ))

    resident_contact_info_repo: ResidentContactInformationRepositoryPort = (
        GoogleSheetsResidentContactInformationRepository(
            query_service=query_service,
            catalog=catalog,
            mapper=ResidentContactInformationRowMapper(),
        ))

    """
    user_resident_access_repo: UserResidentAccessRepositoryPort = (
        GoogleSheetsUserResidentAccessRepository(
            query_service=query_service,
            catalog=catalog,
            mapper=UserResidentAccessRowMapper(),
        ))
    """

    return GoogleSheetsResidentRepositories(
        resident_profile_repository=resident_profile_repo,
        resident_contact_info_repository=resident_contact_info_repo,
        # user_resident_access_repository=user_resident_access_repo,
    )
