# /src/infrastructure/config/aws_settings_loader.py

from src.infrastructure.config.secret_provider import SecretProvider

from src.infrastructure.config.settings_model import (
    AppSynSettings,
)


def load_appsync_settings(
        secret_provider: SecretProvider,
) -> AppSynSettings:
    return AppSynSettings(
        api_key=secret_provider.get_required("AWS_APPSYNC_API_KEY"),
        endpoint=secret_provider.get_required("AWS_APPSYNC_URL"),
    )
