# /src/main/compo_root_patient_repos.py

from dataclasses import dataclass

from src.application.ports.patient_repo_ports import (
    PatientRepositoryPort,
    PatientDiagnosisRepositoryPort,
    PatientProviderRepositoryPort,
    PatientPayerRepositoryPort,
    RTMEnrollmentRepositoryPort,
)

from src.infrastructure.config.app_config_models import (
    AppRuntimeConfig,
)
from src.infrastructure.config.settings_model import (
    Settings,
)
from src.infrastructure.persistence.mappers.patient.patient_row_mapper import (
    PatientRowMapper,
)

from src.infrastructure.persistence.mappers.patient.patient_diagnosis_row_mapper import (
    PatientDiagnosisRowMapper,
)

from src.infrastructure.persistence.mappers.patient.patient_provider_row_mapper import (
    PatientProviderRowMapper,
)

from src.infrastructure.persistence.mappers.patient.patient_payer_row_mapper import (
    PatientPayerRowMapper,
)

from src.infrastructure.persistence.mappers.patient.rtm_enrollment_row_mapper import (
    RTMEnrollmentRowMapper,
)

from src.infrastructure.persistence.google_sheets.repos.patient.patient_repository import (
    GoogleSheetsPatientRepository,
)

from src.infrastructure.persistence.google_sheets.repos.patient.patient_diagnosis_repository import (
    GoogleSheetsPatientDiagnosisRepository,
)

from src.infrastructure.persistence.google_sheets.repos.patient.patient_provider_repository import (
    GoogleSheetsPatientProviderRepository,
)

from src.infrastructure.persistence.google_sheets.repos.patient.patient_payer_repository import (
    GoogleSheetsPatientPayerRepository,
)

from src.infrastructure.persistence.google_sheets.repos.patient.rtm_enrollment_repository import (
    GoogleSheetsRTMEnrollmentRepository,
)

from src.main.compo_root_google_sheets_repos.utils_sheets_compo_root import (
    build_google_sheets_query_service,
    build_google_sheet_catalog,
)


@dataclass(frozen=True, slots=True)
class GoogleSheetsPatientRepositories:
    patient_repository: PatientRepositoryPort
    patient_diagnosis_repository: PatientDiagnosisRepositoryPort
    patient_provider_repository: PatientProviderRepositoryPort
    patient_payer_repository: PatientPayerRepositoryPort
    rtm_enrollment_repository: RTMEnrollmentRepositoryPort


def build_google_sheets_patient_repositories(
        *,
        settings: Settings,
        app_config: AppRuntimeConfig,
) -> GoogleSheetsPatientRepositories:
    patient_repository = build_patient_repository(
        settings=settings, app_config=app_config)

    patient_diagnosis_repository = build_patient_diagnosis_repository(
        settings=settings, app_config=app_config
    )

    patient_provider_repository = build_patient_provider_repository(
        settings=settings, app_config=app_config
    )

    patient_payer_repository = build_patient_payer_repository(
        settings=settings, app_config=app_config
    )

    rtm_enrollment_repository = build_rtm_enrollment_repository(
        settings=settings, app_config=app_config
    )

    return GoogleSheetsPatientRepositories(
        patient_repository=patient_repository,
        patient_diagnosis_repository=patient_diagnosis_repository,
        patient_provider_repository=patient_provider_repository,
        patient_payer_repository=patient_payer_repository,
        rtm_enrollment_repository=rtm_enrollment_repository,
    )


def build_patient_repository(
        *,
        settings: Settings,
        app_config: AppRuntimeConfig,
) -> PatientRepositoryPort:
    query_service = build_google_sheets_query_service(
        settings=settings,
    )

    catalog = build_google_sheet_catalog(
        settings=settings,
        app_config=app_config,
    )

    mapper = PatientRowMapper()

    return GoogleSheetsPatientRepository(
        query_service=query_service,
        catalog=catalog,
        mapper=mapper,
    )


def build_patient_diagnosis_repository(
        *,
        settings: Settings,
        app_config: AppRuntimeConfig,
) -> PatientDiagnosisRepositoryPort:
    query_service = build_google_sheets_query_service(
        settings=settings,
    )

    catalog = build_google_sheet_catalog(
        settings=settings,
        app_config=app_config,
    )

    mapper = PatientDiagnosisRowMapper()

    return GoogleSheetsPatientDiagnosisRepository(
        query_service=query_service,
        catalog=catalog,
        mapper=mapper,
    )


def build_patient_provider_repository(
        *,
        settings: Settings,
        app_config: AppRuntimeConfig,
) -> PatientProviderRepositoryPort:
    query_service = build_google_sheets_query_service(
        settings=settings,
    )

    catalog = build_google_sheet_catalog(
        settings=settings,
        app_config=app_config,
    )

    mapper = PatientProviderRowMapper()

    return GoogleSheetsPatientProviderRepository(
        query_service=query_service,
        catalog=catalog,
        mapper=mapper,
    )


def build_patient_payer_repository(
        *,
        settings: Settings,
        app_config: AppRuntimeConfig,
) -> PatientPayerRepositoryPort:
    query_service = build_google_sheets_query_service(
        settings=settings,
    )

    catalog = build_google_sheet_catalog(
        settings=settings,
        app_config=app_config,
    )

    mapper = PatientPayerRowMapper()

    return GoogleSheetsPatientPayerRepository(
        query_service=query_service,
        catalog=catalog,
        mapper=mapper,
    )


def build_rtm_enrollment_repository(
        *,
        settings: Settings,
        app_config: AppRuntimeConfig,
) -> RTMEnrollmentRepositoryPort:
    query_service = build_google_sheets_query_service(
        settings=settings,
    )

    catalog = build_google_sheet_catalog(
        settings=settings,
        app_config=app_config,
    )

    mapper = RTMEnrollmentRowMapper()

    return GoogleSheetsRTMEnrollmentRepository(
        query_service=query_service,
        catalog=catalog,
        mapper=mapper,
    )
