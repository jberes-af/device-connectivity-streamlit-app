# /src/infrastructure/persistence/mappers

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.schemas.communication_monitoring_data_columns import CommunicationMonitoringDataColumns

from src.domain.entities.entities import CommunicationMonitoringData

from src.infrastructure.persistence.common.utils_parsing import *


class CommunicationMonitoringDataRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> CommunicationMonitoringData:
        schema = CommunicationMonitoringDataColumns

        return CommunicationMonitoringData(
            communication_monitoring_data_id=parse_required_text(
                row.get(schema.COMMUNICATION_MONITORING_DATA_ID),
                field_name=schema.COMMUNICATION_MONITORING_DATA_ID,
            ),
            communication_id=parse_required_text(
                row.get(schema.COMMUNICATION_ID),
                field_name=schema.COMMUNICATION_ID,
            ),
            data_type=parse_optional_text(
                row.get(schema.DATA_TYPE),
                field_name=schema.DATA_TYPE,
            ),
            source_record_id=parse_optional_text(
                row.get(schema.SOURCE_RECORD_ID),
                field_name=schema.SOURCE_RECORD_ID,
            ),
            summary=parse_required_text(
                row.get(schema.SUMMARY),
                field_name=schema.SUMMARY,
            ),
        )


    @staticmethod
    def to_row(
        communication_monitoring_data: CommunicationMonitoringData,
    ) -> RawRow:
        schema = CommunicationMonitoringDataColumns

        return {

            schema.COMMUNICATION_MONITORING_DATA_ID:
                communication_monitoring_data.communication_monitoring_data_id,

            schema.COMMUNICATION_ID:
                communication_monitoring_data.communication_id,

            schema.DATA_TYPE:
                communication_monitoring_data.data_type,

            schema.SOURCE_RECORD_ID:
                communication_monitoring_data.source_record_id,

            schema.SUMMARY:
                communication_monitoring_data.summary,

        }