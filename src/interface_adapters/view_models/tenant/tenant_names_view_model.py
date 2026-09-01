# /src/interface_adapters/view_models/tenant/tenant_names_view_model.py

from dataclasses import dataclass


@dataclass(frozen=True)
class TenantNameViewModel:
    tenant_id: str
    tenant_name: str
    tenant_name_label: str


@dataclass(frozen=True)
class TenantNamesViewModel:
    title: str
    tenant_names: tuple[TenantNameViewModel, ...]
