# /src/gui/streamlit/routing/route_types.py

from collections.abc import Callable
from dataclasses import dataclass

from src.main.compose_root_application import AppContainer


BoundRouteHandler = Callable[
    [],
    None,
]

LegacyRouteHandler = Callable[
    [AppContainer],
    None,
]


@dataclass(frozen=True, slots=True)
class Route:
    route_id: str
    label: str
    handler: BoundRouteHandler | None = None
    legacy_handler: LegacyRouteHandler | None = None
    icon: str | None = None

    def __post_init__(self) -> None:
        has_handler = self.handler is not None
        has_legacy_handler = self.legacy_handler is not None

        if has_handler == has_legacy_handler:
            raise ValueError(
                "Route must define exactly one of "
                "'handler' or 'legacy_handler'."
            )
