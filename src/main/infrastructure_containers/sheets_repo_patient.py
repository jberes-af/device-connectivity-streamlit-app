# /src/main/infrastructure_containers/sheets_repo_patient.py

from dataclasses import dataclass

from src.application.ports.patient_repo_ports import (
    PatientDiagnosisRepositoryPort,
    PatientProviderRepositoryPort,
    PatientPayerRepositoryPort,
)

from src.infrastructure.config.app_config_models import (
    AppRuntimeConfig,
)
from src.infrastructure.config.settings_model import (
    Settings,
)

from src.infrastructure.persistence.google_sheets.mappers.patient.patient_diagnosis_row_mapper import (
    PatientDiagnosisRowMapper,
)

from src.infrastructure.persistence.google_sheets.mappers.patient.patient_provider_row_mapper import (
    PatientProviderRowMapper,
)

from src.infrastructure.persistence.google_sheets.mappers.patient.patient_payer_row_mapper import (
    PatientPayerRowMapper,
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

from src.main.infrastructure_containers.utils_sheets_composition_root import (
    build_google_sheets_query_service,
    build_google_sheet_catalog,
)


@dataclass(frozen=True, slots=True)
class GoogleSheetsPatientRepositories:
    patient_diagnosis_repository: PatientDiagnosisRepositoryPort
    patient_provider_repository: PatientProviderRepositoryPort
    patient_payer_repository: PatientPayerRepositoryPort
    # patient_repository: PatientRepositoryPort
    # rtm_enrollment_repository: RTMEnrollmentRepositoryPort
    # provider_repository: ProviderRepositoryPort
    # payer_repository: PayerRepositoryPort


def build_google_sheets_patient_repositories(
        *,
        settings: Settings,
        app_config: AppRuntimeConfig,
) -> GoogleSheetsPatientRepositories:
    query_service = build_google_sheets_query_service(
        settings=settings,
    )

    catalog = build_google_sheet_catalog(
        settings=settings,
        app_config=app_config,
    )

    patient_diagnosis_repository: PatientDiagnosisRepositoryPort = (
        GoogleSheetsPatientDiagnosisRepository(
            query_service=query_service,
            catalog=catalog,
            mapper=PatientDiagnosisRowMapper(),
        ))

    patient_provider_repository: PatientProviderRepositoryPort = (
        GoogleSheetsPatientProviderRepository(
            query_service=query_service,
            catalog=catalog,
            mapper=PatientProviderRowMapper(),
        ))

    patient_payer_repository: PatientPayerRepositoryPort = (
        GoogleSheetsPatientPayerRepository(
            query_service=query_service,
            catalog=catalog,
            mapper=PatientPayerRowMapper(),
        ))

    """
    patient_repository: PatientRepositoryPort = (
        GoogleSheetsPatientRepository(
            query_service=query_service,
            catalog=catalog,
            mapper=PatientRowMapper(),
        ))
    rtm_enrollment_repository: RTMEnrollmentRepositoryPort = (
        GoogleSheetsRTMEnrollmentRepository(
            query_service=query_service,
            catalog=catalog,
            mapper=RTMEnrollmentRowMapper(),
        ))

    provider_repository: ProviderRepositoryPort = (
        GoogleSheetsProviderRepository(
            query_service=query_service,
            catalog=catalog,
            mapper=ProviderRowMapper(),
        ))

    payer_repository: PayerRepositoryPort = (
        GoogleSheetsPayerRepository(
            query_service=query_service,
            catalog=catalog,
            mapper=PayerRowMapper(),
        ))
   
    """

    return GoogleSheetsPatientRepositories(
        patient_diagnosis_repository=patient_diagnosis_repository,
        patient_provider_repository=patient_provider_repository,
        patient_payer_repository=patient_payer_repository,
    )
