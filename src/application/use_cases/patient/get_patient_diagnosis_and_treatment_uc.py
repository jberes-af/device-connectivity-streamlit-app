# /src/application/use_cases/patient/get_patient_diagnosis_and_treatment_uc.py.py

import logging

from src.domain.entities.person.patient_entities import PatientDiagnosis

from src.domain.entities.care.rtm_entities import RtmMedicalNecessity

from src.domain.entities.care.diagnosis_entities import DiagnosisDefinition

from src.domain.entities.care.treatment_entities import (
    TreatmentPlan,
    TherapeuticGoal,
    TreatmentMonitoringParameter,
    TreatmentIntervention,
)

from src.application.services.care.get_diagnosis_definition_service import (
    FetchDiagnosisDefinitionService
)

from src.application.services.person.get_patient_diagnosis_service import (
    FetchPatientDiagnosisService
)

from src.application.services.care.get_rtm_service import (
    FetchRtmNecessityService,
)

from src.application.services.care.get_treatment_service import (
    FetchTreatmentPlanService,
    FetchTherapeuticGoalService,
    FetchTreatmentInterventionService,
    FetchTreatmentMonitoringParameterService,
    FetchTreatmentPlanReviewService,
)

from src.application.use_cases.patient.diagnosis_and_treatment_uc_dtos import (
    DiagnosisDTO,
    RtmNecessityDTO,
    TherapeuticGoalDTO,
    TherapeuticPlanDTO,
    TreatmentPlanDTO,
    TreatmentInterventionDTO,
    TreatmentMonitoringParameterDTO,
    TreatmentPlanReviewDTO,

    GetDiagnosesAndTreatmentRequestDTO,
    GetDiagnosisAndTreatmentResultDTO,
)

logger = logging.getLogger(__name__)


class GetPatientDiagnosesAndTreatmentsUseCase:

    def __init__(
            self,
            *,
            fetch_diagnosis_definition_service: FetchDiagnosisDefinitionService,
            fetch_patient_diagnosis_service: FetchPatientDiagnosisService,
            fetch_treatment_plan_service: FetchTreatmentPlanService,
            fetch_therapeutic_goal_service: FetchTherapeuticGoalService,
            fetch_rtm_necessity_service: FetchRtmNecessityService,
            fetch_treatment_intervention_service: FetchTreatmentInterventionService,
            fetch_treatment_monitoring_parameter_service:
            FetchTreatmentMonitoringParameterService,
            fetch_treatment_plan_review_service: FetchTreatmentPlanReviewService,
    ) -> None:
        self._diagnosis_definition_service = fetch_diagnosis_definition_service
        self._patient_diagnosis_service = fetch_patient_diagnosis_service
        self._treatment_plan_service = fetch_treatment_plan_service
        self._therapeutic_goal_service = fetch_therapeutic_goal_service
        self._necessity_service = fetch_rtm_necessity_service
        self._treatment_intervention_service = (
            fetch_treatment_intervention_service
        )
        self._treatment_monitoring_parameter_service = (
            fetch_treatment_monitoring_parameter_service
        )
        self._treatment_plan_review_service = (
            fetch_treatment_plan_review_service
        )

    def execute(
            self,
            request: GetDiagnosesAndTreatmentRequestDTO,
    ) -> GetDiagnosisAndTreatmentResultDTO:
        patient_id = request.patient_id

        diagnoses: tuple[DiagnosisDTO, ...] = (
            self._build_diagnoses(patient_id=patient_id)
        )

        treatment_plans: tuple[TherapeuticPlanDTO, ...] = (
            self._build_treatment_plans(patient_id=patient_id)
        )

        rtm_necessity_records: tuple[RtmNecessityDTO, ...] = (
            self._build_rtm_necessity_records(patient_id=patient_id)
        )

        return GetDiagnosisAndTreatmentResultDTO(
            patient_id=patient_id,
            diagnoses=diagnoses,
            treatment_plans=treatment_plans,
            rtm_necessity_records=rtm_necessity_records,
        )

    def _build_diagnoses(
            self,
            patient_id: str,
    ) -> tuple[DiagnosisDTO, ...]:
        patient_diagnoses: tuple[PatientDiagnosis, ...] = (
            self._patient_diagnosis_service
            .fetch_diagnosis_profiles_for_patient(patient_id)
        )

        diagnosis_ids: tuple[str, ...] = tuple(
            [diagnosis.diagnosis_id for diagnosis in patient_diagnoses]
        )

        diagnoses_definitions: tuple[DiagnosisDefinition, ...] = (
            self._diagnosis_definition_service
            .fetch_diagnosis_profiles(diagnosis_ids=diagnosis_ids)
        )

        diagnosis_id_mapping = {
            record.diagnosis_id: record
            for record in diagnoses_definitions
        }

        return tuple([
            DiagnosisDTO(
                patient_diagnosis_id=pd.patient_diagnosis_id,
                diagnosis_id=pd.diagnosis_id,
                diagnosis_name=diagnosis_id_mapping[pd.diagnosis_id].diagnosis_name,
                diagnosis_description=(
                    diagnosis_id_mapping[pd.diagnosis_id].diagnosis_description),
                diagnosed_date=pd.diagnosed_date,
                resolved_date=pd.resolved_date,
                is_primary=pd.is_primary,
            )
            for pd in patient_diagnoses
        ]
        )

    def _build_treatment_plans(
            self,
            patient_id: str,
    ) -> tuple[TherapeuticPlanDTO, ...]:
        treatment_plans: tuple[TreatmentPlan, ...] = (
            self._treatment_plan_service
            .fetch_treatment_plans_for_patient(patient_id)
        )

        results: list[TherapeuticPlanDTO] = []

        for plan in treatment_plans:
            goals = (
                self._therapeutic_goal_service
                .fetch_goals_for_treatment_plan(
                    treatment_plan_id=plan.treatment_plan_id,
                )
            )

            logger.info(
                "use: diagnosis & treatment: goals row_count=%d",len(goals))

            interventions = (
                self._treatment_intervention_service
                .fetch_interventions_for_treatment_plan(
                    treatment_plan_id=plan.treatment_plan_id,
                )
            )

            logger.info(
                "use: diagnosis & treatment: interventions row_count=%d",len(interventions))

            monitoring_parameters = (
                self._treatment_monitoring_parameter_service
                .fetch_monitoring_parameters_for_treatment_plan(
                    treatment_plan_id=plan.treatment_plan_id,
                )
            )

            logger.info(
                "use: diagnosis & treatment: monitoring_parameters row_count=%d",len(monitoring_parameters))

            reviews = (
                self._treatment_plan_review_service
                .fetch_reviews_for_treatment_plan(
                    treatment_plan_id=plan.treatment_plan_id,
                )
            )

            logger.info(
                "use: diagnosis & treatment: reviews row_count=%d",len(reviews))

            results.append(
                TherapeuticPlanDTO(
                    treatment_plan=TreatmentPlanDTO(
                        treatment_plan_id=plan.treatment_plan_id,
                        rtm_program_id=plan.rtm_program_id,
                        patient_id=plan.patient_id,
                        treating_provider_id=plan.treating_provider_id,
                        start_date=plan.start_date,
                        expected_end_date=plan.expected_end_date,
                        status=plan.status,
                        created_at=plan.created_at,
                        updated_at=plan.updated_at,
                    ),

                    goals=tuple(
                        # Whatever your goal DTO is named
                        TherapeuticGoalDTO(
                            goal_id=goal.goal_id,
                            treatment_plan_id=goal.treatment_plan_id,
                            description=goal.description,
                            target_date=goal.target_date,
                        )
                        for goal in goals
                    ),

                    interventions=tuple(
                        TreatmentInterventionDTO(
                            intervention_id=item.intervention_id,
                            treatment_plan_id=item.treatment_plan_id,
                            treatment_type=item.treatment_type,
                            description=item.description,
                            start_date=item.start_date,
                            end_date=item.end_date,
                            status=item.status,
                        )
                        for item in interventions
                    ),

                    monitoring_parameters=tuple(
                        TreatmentMonitoringParameterDTO(
                            monitoring_parameter_id=item.monitoring_parameter_id,
                            treatment_plan_id=item.treatment_plan_id,
                            goal_id=item.goal_id,
                            measure_definition_id=item.measure_definition_id,
                            baseline_value=item.baseline_value,
                            target_value=item.target_value,
                            unit=item.unit,
                        )
                        for item in monitoring_parameters
                    ),

                    reviews=tuple(
                        TreatmentPlanReviewDTO(
                            review_id=item.review_id,
                            treatment_plan_id=item.treatment_plan_id,
                            provider_id=item.provider_id,
                            reviewed_at=item.reviewed_at,
                            clinical_findings=item.clinical_findings,
                            treatment_decision=item.treatment_decision,
                            next_review_date=item.next_review_date,
                        )
                        for item in reviews
                    ),
                )
            )

        return tuple(results)

    def _build_rtm_necessity_records(
            self,
            patient_id: str,
    ) -> tuple[RtmNecessityDTO, ...]:
        records: tuple[RtmMedicalNecessity, ...] = (
            self._necessity_service
            .fetch_rtm_necessity_records_for_patient(
                patient_id=patient_id,
            )
        )

        return tuple(
            RtmNecessityDTO(
                rtm_necessity_id=record.rtm_necessity_id,
                patient_id=record.patient_id,
                rtm_program_id=record.rtm_program_id,
                treatment_plan_id=record.treatment_plan_id,
                primary_diagnosis_code=record.primary_diagnosis_code,
                secondary_diagnosis_codes=record.secondary_diagnosis_codes,
                clinical_indications=record.clinical_indications,
                clinical_indication_notes=record.clinical_indication_notes,
                monitoring_reasons=record.monitoring_reasons,
                monitoring_rationale=record.monitoring_rationale,
                expected_clinical_benefit=record.expected_clinical_benefit,
                intended_clinical_uses=record.intended_clinical_uses,
                determined_by_provider_id=record.determined_by_provider_id,
                determined_at=record.determined_at,
                is_attested=record.is_attested,
                attestation_version=record.attestation_version,
                effective_from=record.effective_from,
                effective_to=record.effective_to,
                status=record.status,
                last_reviewed_at=record.last_reviewed_at,
                last_reviewed_by_provider_id=(
                    record.last_reviewed_by_provider_id
                ),
            )
            for record in records
        )
