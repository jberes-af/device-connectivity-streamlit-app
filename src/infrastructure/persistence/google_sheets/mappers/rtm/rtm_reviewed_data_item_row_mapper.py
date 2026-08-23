# /src/infrastructure/persistence/mappers

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.schemas.rtm_reviewed_data_item_columns import RtmReviewedDataItemColumns

from src.domain.entities.entities import RtmReviewedDataItem

from src.infrastructure.persistence.common.utils_parsing import *


class RtmReviewedDataItemRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> RtmReviewedDataItem:
        schema = RtmReviewedDataItemColumns

        return RtmReviewedDataItem(
            reviewed_data_item_id=parse_required_text(
                row.get(schema.REVIEWED_DATA_ITEM_ID),
                field_name=schema.REVIEWED_DATA_ITEM_ID,
            ),
            activity_id=parse_required_text(
                row.get(schema.ACTIVITY_ID),
                field_name=schema.ACTIVITY_ID,
            ),
            data_type=parse_optional_text(
                row.get(schema.DATA_TYPE),
                field_name=schema.DATA_TYPE,
            ),
            source_record_id=parse_required_text(
                row.get(schema.SOURCE_RECORD_ID),
                field_name=schema.SOURCE_RECORD_ID,
            ),
        )


    @staticmethod
    def to_row(
        rtm_reviewed_data_item: RtmReviewedDataItem,
    ) -> RawRow:
        schema = RtmReviewedDataItemColumns

        return {

            schema.REVIEWED_DATA_ITEM_ID:
                rtm_reviewed_data_item.reviewed_data_item_id,

            schema.ACTIVITY_ID:
                rtm_reviewed_data_item.activity_id,

            schema.DATA_TYPE:
                rtm_reviewed_data_item.data_type,

            schema.SOURCE_RECORD_ID:
                rtm_reviewed_data_item.source_record_id,

        }