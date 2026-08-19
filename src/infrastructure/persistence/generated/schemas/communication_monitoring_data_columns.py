# /src/infrastructure/persistence/schemas

class CommunicationMonitoringDataColumns:
    COMMUNICATION_MONITORING_DATA_ID: str = "communication_monitoring_data_id"
    COMMUNICATION_ID: str = "communication_id"
    DATA_TYPE: str = "data_type"
    SOURCE_RECORD_ID: str = "source_record_id"
    SUMMARY: str = "summary"
    ORDER = (
COMMUNICATION_MONITORING_DATA_ID,
COMMUNICATION_ID,
DATA_TYPE,
SOURCE_RECORD_ID,
SUMMARY,
)