# /src/main/compose_root_config.py

from dataclasses import dataclass
from pathlib import Path

#
# --- INFRASTRUCTURE CONFIGURATION

from src.infrastructure.config.app_config_loader import (
    AppConfigLoader,
)
from src.infrastructure.config.app_config_models import (
    AppRuntimeConfig,
)
from src.infrastructure.config.secret_provider import (
    EnvSecretProvider,
    StreamlitSecretProvider,
    FallbackSecretProvider,
    SecretProvider,
)

from src.infrastructure.config.settings_loader import (
    load_settings,
)

from src.infrastructure.config.settings_model import (
    Settings,
)

import logging


@dataclass(frozen=True, slots=True)
class RuntimeConfiguration:
    settings: Settings
    app_config: AppRuntimeConfig


def _resolve_project_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _build_secret_provider(
        *,
        project_root: Path,
) -> SecretProvider:
    secret_provider = FallbackSecretProvider(
        StreamlitSecretProvider(),
        EnvSecretProvider(
            env_path=project_root / ".env",
            require_env_file=False,
        ),
    )
    return secret_provider


def load_runtime_config() -> RuntimeConfiguration:
    project_root = _resolve_project_root()

    logging.info("Project root resolved: %s", project_root)

    secret_provider = _build_secret_provider(
        project_root=project_root,
    )

    settings = load_settings(
        project_root=project_root,
        secret_provider=secret_provider,
    )

    app_config = AppConfigLoader.load_from_json(
        settings.config_path,
        project_root=project_root,
    )

    return RuntimeConfiguration(
        settings=settings,
        app_config=app_config)
