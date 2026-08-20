# /src/interface_adapters/view_models/patient/patient_overview_page_view_model.py

from dataclasses import dataclass

from src.interface_adapters.view_models.common.card_view_models import (
    CardPropertyFieldsViewModel,
)


@dataclass(frozen=True)
class PatientOverviewPageViewModel:
    page_title: str
    administration_card: CardPropertyFieldsViewModel
    enrollment_card: CardPropertyFieldsViewModel
    # provider_review_card: CardViewModel
    # communication_card: CardViewModel
