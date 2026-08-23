# /src/infrastructure/persistence/schemas

class RtmReviewedDataItemColumns:
    REVIEWED_DATA_ITEM_ID: str = "reviewed_data_item_id"
    ACTIVITY_ID: str = "activity_id"
    DATA_TYPE: str = "data_type"
    SOURCE_RECORD_ID: str = "source_record_id"
    ORDER = (
REVIEWED_DATA_ITEM_ID,
ACTIVITY_ID,
DATA_TYPE,
SOURCE_RECORD_ID,
)