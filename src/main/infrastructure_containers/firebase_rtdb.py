# /src/main/infrastructure_containers/firebase_rtdb.py

from src.application.ports.sensing.realtime_database_port import (
    RealtimeDatabasePort,
)

from src.infrastructure.config.settings_model import Settings

from src.infrastructure.persistence.firebase.firebase_app import (
    init_firebase_admin_app
)

from src.infrastructure.persistence.firebase.firebase_rtdb_adapter import (
    FirebaseRtdbAdapter)


def build_realtime_database_adapter(
        settings: Settings,
):
    # --- Firebase Admin SDK, used for backend RTDB

    fb_admin_app = init_firebase_admin_app(
        database_url=settings.firebase_admin.database_url,
        service_account_info=settings.firebase_admin.service_account_info,
    )

    rtdb: RealtimeDatabasePort = FirebaseRtdbAdapter(app=fb_admin_app)
    return rtdb
