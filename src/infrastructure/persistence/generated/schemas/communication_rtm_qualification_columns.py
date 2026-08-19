# /src/infrastructure/persistence/schemas

class CommunicationRTMQualificationColumns:
    COMMUNICATION_ID: str = "communication_id"
    WAS_INTERACTIVE: str = "was_interactive"
    PATIENT_OR_CAREGIVER_PARTICIPATED: str = "patient_or_caregiver_participated"
    CLINICAL_MANAGEMENT_OCCURRED: str = "clinical_management_occurred"
    COMPLETED_SUCCESSFULLY: str = "completed_successfully"
    QUALIFYING_MINUTES: str = "qualifying_minutes"
    COUNTS_TOWARD_RTM_PERIOD: str = "counts_toward_rtm_period"
    QUALIFICATION_NOTES: str = "qualification_notes"
    CONFIRMED_BY_PROVIDER_ID: str = "confirmed_by_provider_id"
    CONFIRMED_AT: str = "confirmed_at"
    ORDER = (
COMMUNICATION_ID,
WAS_INTERACTIVE,
PATIENT_OR_CAREGIVER_PARTICIPATED,
CLINICAL_MANAGEMENT_OCCURRED,
COMPLETED_SUCCESSFULLY,
QUALIFYING_MINUTES,
COUNTS_TOWARD_RTM_PERIOD,
QUALIFICATION_NOTES,
CONFIRMED_BY_PROVIDER_ID,
CONFIRMED_AT,
)