# /src/infrastructure/auth/firebase/pyrebase_config_mapper.py

from src.infrastructure.config.settings_model import FirebaseWebSettings

class PyrebaseConfigMapper:
    @staticmethod
    def from_settings(
        settings: FirebaseWebSettings,
    ) -> dict[str, str]:
        return {
            "apiKey": settings.client.api_key,
            "authDomain": settings.client.auth_domain,
            "databaseURL": settings.database_url,
            "projectId": settings.client.project_id,
            "storageBucket": settings.storage_bucket,
            "messagingSenderId": settings.messaging_sender_id,
            "appId": settings.client.app_id,
        }