# /src/infrastructure/persistence/google_sheets/repos/user/user_profile.py

from src.application.ports.user_repo_ports import (
    UserProfileRepositoryPort,
)

from src.domain.entities.person.user_entities import UserProfile

# from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.google_sheets.base_repository import (
    GoogleSheetsRepository,
)

from src.infrastructure.persistence.google_sheets.google_sheet_catalog import (
    GoogleSheetCatalog,
)

from src.infrastructure.persistence.google_sheets.sheets_query_service import (
    GoogleSheetsQueryService,
)

from src.infrastructure.persistence.google_sheets.mappers.user.user_profile_row_mapper import (
    UserProfileRowMapper,
)

from src.infrastructure.persistence.google_sheets.schemas.user.user_profile_columns import (
    UserProfileColumns,
)


class GoogleSheetsUserProfileRepository(
    GoogleSheetsRepository,
    UserProfileRepositoryPort,
):
    TABLE_NAME = "user_profile"
    ID_COLUMN = UserProfileColumns.USER_ID

    def __init__(
            self,
            *,
            query_service: GoogleSheetsQueryService,
            catalog: GoogleSheetCatalog,
            mapper: UserProfileRowMapper,
    ) -> None:
        super().__init__(
            query_service=query_service,
            catalog=catalog,
        )

        self._mapper = mapper

    def list_user_profiles(self) -> tuple[UserProfile, ...]:
        return tuple(
            self._mapper.to_domain(row)
            for row in self._read_rows()
        )

    def get_by_id(
            self,
            user_id: str,
    ) -> UserProfile:
        raw_row = self._find_single_row(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=user_id,
        )

        return self._mapper.to_domain(raw_row)

    """
    def append_open_event(
            self,
            event: UserProfile,
    ) -> None:
        raw_row: RawRow = self._mapper.to_row(event)

        self._append_raw_row(
            row=raw_row,
            columns=UserProfileColumns.ORDER,
        )
    """
