# /src/infrastructure/persistence/schemas/payer/payer_columns.py

class PayerColumns:
    PAYER_ID: str = "payer_id"
    PAYER_NAME: str = "payer_name"
    PAYER_TYPE: str = "payer_type"
    ELECTRONIC_PAYER_ID: str = "electronic_payer_id"
    CLAIMS_ADDRESS_LINE_1: str = "claims_address_line_1"
    CLAIMS_ADDRESS_LINE_2: str = "claims_address_line_2"
    CITY: str = "city"
    STATE: str = "state"
    POSTAL_CODE: str = "postal_code"
    TELEPHONE: str = "telephone"
    WEBSITE: str = "website"
    ACCEPTS_ELECTRONIC_CLAIMS: str = "accepts_electronic_claims"
    ORDER = (
        PAYER_ID,
        PAYER_NAME,
        PAYER_TYPE,
        ELECTRONIC_PAYER_ID,
        CLAIMS_ADDRESS_LINE_1,
        CLAIMS_ADDRESS_LINE_2,
        CITY,
        STATE,
        POSTAL_CODE,
        TELEPHONE,
        WEBSITE,
        ACCEPTS_ELECTRONIC_CLAIMS,
    )
