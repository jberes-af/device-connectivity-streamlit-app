# /src/domain/entities/contact/user_entities.py

from dataclasses import dataclass


@dataclass(frozen=True)
class UserProfile:
    user_id: str
    user_name: str
    telephone: str
    email_address: str
    user_image: str
    color_scheme: str

