# /src/infrastructure/config/firebase_app.py

from typing import Any

import firebase_admin

from firebase_admin import App, credentials


def init_firebase_admin_app(
    *,
    database_url: str,
    service_account_info: dict[str, Any],
) -> App:
    try:
        return firebase_admin.get_app()

    except ValueError:
        cred = credentials.Certificate(service_account_info)

        return firebase_admin.initialize_app(
            cred,
            {
                "databaseURL": database_url,
            },
        )