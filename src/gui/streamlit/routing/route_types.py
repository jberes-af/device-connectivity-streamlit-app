# /src/gui/streamlit/routing/route_types.py

from collections.abc import Callable
from dataclasses import dataclass

from src.main.compose_root_application import AppContainer

RouteHandler = Callable[
    [AppContainer],
    None,
]


@dataclass(frozen=True, slots=True)
class Route:
    route_id: str
    label: str
    handler: RouteHandler
    icon: str | None = None
