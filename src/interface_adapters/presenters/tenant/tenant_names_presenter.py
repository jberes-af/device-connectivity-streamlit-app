# /src/interface_adapters/presenters/tenant/tenant_names_presenter.py

from src.application.use_cases.tenant.tenant_profiles_uc_dtos import (
    TenantProfileDTO,
    GetTenantProfilesResultDTO,
)

from src.interface_adapters.view_models.tenant.tenant_names_view_model import (
    TenantNameViewModel,
    TenantNamesViewModel,
)


class TenantNamesPresenter:

    def present(
            self,
            *,
            result: GetTenantProfilesResultDTO,
    ) -> TenantNamesViewModel:
        view_models: tuple[TenantNameViewModel, ...] = (
            self._present_tenant_names(
                profiles=result.tenant_profiles,
            ))

        return TenantNamesViewModel(
            title="Tenant Names",
            tenant_names=view_models,
        )

    @staticmethod
    def _present_tenant_names(
            profiles: tuple[TenantProfileDTO, ...]
    ) -> tuple[TenantNameViewModel, ...]:
        return tuple(
            [
                TenantNameViewModel(
                    tenant_id=record.tenant_id,
                    tenant_name=record.tenant_name,
                    tenant_name_label=f"{record.tenant_name} • {record.tenant_id}",
                )
                for record in profiles
            ]
        )

    """
    @staticmethod
    def _text(value: str | None) -> str:
        return value or "—"

    @staticmethod
    def _join(values: tuple[str, ...]) -> str:
        return ", ".join(values) if values else "—"

    @staticmethod
    def _date(value: date | None) -> str:
        return value.strftime("%m/%d/%Y") if value else "—"

    @staticmethod
    def _enum_label(value: StrEnum | str | None) -> str:
        if value is None:
            return "—"

        if isinstance(value, StrEnum):
            return str(value.value)

        return str(value)
    """
