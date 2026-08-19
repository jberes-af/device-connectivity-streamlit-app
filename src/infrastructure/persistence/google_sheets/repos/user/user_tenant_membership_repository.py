# /src/infrastructure/persistence/google_sheets/repos/user/user_tenant_membership.py


from src.application.ports.user_repo_ports import (
    UserTenantMembershipRepositoryPort,
)

from src.domain.entities.person.user_entities import UserTenantMembership

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.google_sheets.base_repository import (
    GoogleSheetsRepository,
)

from src.infrastructure.persistence.google_sheets.google_sheet_catalog import (
    GoogleSheetCatalog,
)

from src.infrastructure.persistence.google_sheets.sheets_query_service import (
    GoogleSheetsQueryService,
)

from src.infrastructure.persistence.google_sheets.mappers.user.user_tenant_membership_row_mapper import (
    UserTenantMembershipRowMapper,
)

from src.infrastructure.persistence.google_sheets.schemas.user.user_tenant_membership_columns import (
    UserTenantMembershipColumns,
)


class GoogleSheetsUserTenantMembershipRepository(
    GoogleSheetsRepository,
    UserTenantMembershipRepositoryPort,
):
    TABLE_NAME = "user_tenant_membership"
    ID_COLUMN = UserTenantMembershipColumns.USER_ID

    def __init__(
            self,
            *,
            query_service: GoogleSheetsQueryService,
            catalog: GoogleSheetCatalog,
            mapper: UserTenantMembershipRowMapper,
    ) -> None:
        super().__init__(
            query_service=query_service,
            catalog=catalog,
        )

        self._mapper = mapper

    def list_all_user_tenant_memberships(self) -> tuple[UserTenantMembership, ...]:
        return tuple(
            self._mapper.to_domain(row)
            for row in self._read_rows()
        )

    def list_tenant_memberships_by_user_id(
            self,
            user_id: str,
    ) -> tuple[UserTenantMembership, ...]:

        raw_rows: list[RawRow] = self._find_rows(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=user_id,
        )

        return tuple(
            self._mapper.to_domain(row)
            for row in raw_rows
        )

    def get_by_user_and_tenant(
            self,
            user_id: str,
            tenant_id: str,
    ) -> UserTenantMembership:
        raw_row = self._find_single_row_by_fields(
            rows=self._read_rows(),
            filters={
                UserTenantMembershipColumns.USER_ID: user_id,
                UserTenantMembershipColumns.TENANT_ID: tenant_id,
            },
        )

        return self._mapper.to_domain(raw_row)

    """
    def append_open_event(
            self,
            event: UserTenantMembership,
    ) -> None:
        raw_row: RawRow = self._mapper.to_row(event)

        self._append_raw_row(
            row=raw_row,
            columns=UserTenantMembershipColumns.ORDER,
        )
    """
