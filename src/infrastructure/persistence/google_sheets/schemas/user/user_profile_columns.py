# /src/infrastructure/persistence/schemas/user/user_profile_columns.py

class UserProfileColumns:
    USER_ID: str = "user_id"
    USER_NAME: str = "user_name"
    USER_TELEPHONE: str = "user_telephone"
    USER_EMAIL_ADDRESS: str = "user_email_address"
    USER_IMAGE: str = "user_image"
    COLOR_SCHEME: str = "color_scheme"
    ORDER = (
        USER_ID,
        USER_NAME,
        USER_TELEPHONE,
        USER_EMAIL_ADDRESS,
        USER_IMAGE,
        COLOR_SCHEME,
    )
