# /src/infrastructure/persistence/firebase/firebase_rtdb_adapter.py

# from collections import defaultdict
from dataclasses import dataclass
from typing import Any, Mapping

from firebase_admin import db

from src.application.ports.sensing.realtime_database_port import RealtimeDatabasePort

import json

_ILLEGAL = set(".#$[]")


@dataclass(frozen=True)
class FirebasePath:
    value: str

    def __post_init__(self) -> None:
        v = self.value.strip()
        if not v:
            raise ValueError("firebase_auth path must be non-empty")
        if not v.startswith("/"):
            raise ValueError("firebase_auth path must start with '/'")
        if "//" in v:
            raise ValueError("firebase_auth path must not contain '//'")
        object.__setattr__(self, "value", v)


class FirebaseRtdbAdapter(RealtimeDatabasePort):
    def __init__(self, app) -> None:
        self._app = app

    def read_node(self, path: str) -> Any:
        firebase_path = FirebasePath(path)
        return db.reference(firebase_path.value, app=self._app).get()

    def node_exists(self, path: str) -> bool:
        firebase_path = FirebasePath(path)
        return db.reference(firebase_path.value, app=self._app).get() is not None

    def list_children_keys(self, path: str) -> list[str]:
        firebase_path = FirebasePath(path)
        value = db.reference(firebase_path.value, app=self._app).get()
        if not isinstance(value, Mapping):
            return []
        return [k for k in value.keys() if isinstance(k, str)]

    def update_paths(self, updates: Mapping[str, Any]) -> None:
        normalized = _normalize_update_payload(updates)
        _assert_jsonable(normalized)

        """
        grouped: dict[str, dict[str, Any]] = defaultdict(dict)

        for full_path, value in normalized.items():
            parent, child = _split_parent_child(full_path)
            grouped[parent][child] = value

        for parent_path, patch in grouped.items():
            ref_path = "/" if parent_path == "" else f"/{parent_path}"
            db.reference(ref_path, app=self._app).update(patch)
        """

        db.reference("/", app=self._app).update(normalized)


def _normalize_update_payload(payload: Mapping[str, Any]) -> dict[str, Any]:
    out: dict[str, Any] = {}

    for raw_key, val in payload.items():
        if not isinstance(raw_key, str):
            raise TypeError(f"RTDB update key must be str, got {type(raw_key)}")

        key = raw_key.strip()
        if key.startswith("/"):
            key = key[1:]
        if not key:
            raise ValueError("RTDB update key cannot be empty")

        for seg in key.split("/"):
            if not seg:
                raise ValueError(f"RTDB path contains empty segment: {raw_key!r}")
            if any(ch in _ILLEGAL for ch in seg):
                raise ValueError(f"RTDB path segment has illegal chars: {raw_key!r}")

        try:
            json.dumps(val)
        except TypeError as e:
            raise TypeError(f"RTDB value for key '{key}' is not JSON-serializable") from e

        out[key] = val

    return out


def _assert_jsonable(payload: Mapping[str, Any]) -> None:
    try:
        json.dumps(payload)
    except TypeError as e:
        raise TypeError(f"Payload is not JSON-serializable: {e}") from e


def _split_parent_child(path: str) -> tuple[str, str]:
    if "/" not in path:
        return "", path
    parent, child = path.rsplit("/", 1)
    if not child:
        raise ValueError(f"Invalid update path (empty leaf): {path!r}")
    return parent, child
