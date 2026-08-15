# /src/main/infrastructure_containers/sheets_repo_patient.py

from dataclasses import dataclass

from src.application.ports.patient_repo_ports import (
    PatientRepositoryPort,
    PatientDiagnosisRepositoryPort,
    PatientProviderRepositoryPort,
    PatientPayerRepositoryPort,
    RTMEnrollmentRepositoryPort,
)

from src.application.ports.provider_repo_ports import (
    ProviderRepositoryPort,
)

from src.application.ports.payer_repo_ports import (
    PayerRepositoryPort,
)

from src.infrastructure.config.app_config_models import (
    AppRuntimeConfig,
)
from src.infrastructure.config.settings_model import (
    Settings,
)
from src.infrastructure.persistence.google_sheets.mappers.patient.patient_row_mapper import (
    PatientRowMapper,
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

from src.infrastructure.persistence.google_sheets.mappers.patient.rtm_enrollment_row_mapper import (
    RTMEnrollmentRowMapper,
)

from src.infrastructure.persistence.google_sheets.mappers.provider.provider_row_mapper import (
    ProviderRowMapper,
)

from src.infrastructure.persistence.google_sheets.mappers.payer.payer_row_mapper import (
    PayerRowMapper,
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

from src.infrastructure.persistence.google_sheets.repos.provider.provider_repository import (
    GoogleSheetsProviderRepository,
)

from src.infrastructure.persistence.google_sheets.repos.payer.payer_repository import (
    GoogleSheetsPayerRepository,
)

from src.main.infrastructure_containers.utils_sheets_composition_root import (
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
    provider_repository: ProviderRepositoryPort
    payer_repository: PayerRepositoryPort


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

    patient_repository: PatientRepositoryPort = (
        GoogleSheetsPatientRepository(
            query_service=query_service,
            catalog=catalog,
            mapper=PatientRowMapper(),
        ))

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

    return GoogleSheetsPatientRepositories(
        patient_repository=patient_repository,
        patient_diagnosis_repository=patient_diagnosis_repository,
        patient_provider_repository=patient_provider_repository,
        patient_payer_repository=patient_payer_repository,
        rtm_enrollment_repository=rtm_enrollment_repository,
        provider_repository=provider_repository,
        payer_repository=payer_repository,
    )
