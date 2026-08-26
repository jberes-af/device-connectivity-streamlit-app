# /src/interface_adapters/view_models/residents/payer/rtm_enrollment_view_models.py

from dataclasses import dataclass

from src.interface_adapters.view_models.widgets.card_grid_view_model import (
    CardGridViewModel,
)


@dataclass(frozen=True)
class RtmEnrollmentViewModel:
    section_title: str
    enrollment_card_grid: CardGridViewModel