# src/application/ports/realtime_database_port.py

from typing import Any, Mapping, Protocol


class RealtimeDatabasePort(Protocol):

    def read_node(self, path: str) -> Any:
        ...

    def node_exists(self, path: str) -> bool:
        ...

    def list_children_keys(self, path: str) -> list[str]:
        ...

    def update_paths(self, updates: Mapping[str, Any]) -> None:
        ...