# /src/interface_adapters/view_models/residents/payer/patient_payer_view_models.py

from dataclasses import dataclass

from src.interface_adapters.view_models.widgets.card_grid_view_model import (
    CardGridViewModel,
)


@dataclass(frozen=True)
class PatientPayerViewModel:
    section_title: str
    patient_payer_card_grids: tuple[CardGridViewModel, ...]
