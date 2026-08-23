# /src/interface_adapters/presenters/resident/segmented_controls_presenter.py

from src.interface_adapters.view_models.resident.segmented_controls_view_model import (
    ResidentSectionEnum,
    RESIDENT_SEGMENT_ORDER,
    SECTION_ICONS,
    ResidentSegmentOptionViewModel,
    ResidentSegmentedControlViewModel,
)


class ResidentSegmentedControlPresenter:

    @staticmethod
    def present_segmented_controls() -> ResidentSegmentedControlViewModel:
        options = [
            ResidentSegmentOptionViewModel(
                id=control,
                label=control.value.replace("_", " ").title(),
                icon=SECTION_ICONS.get(control),
            )
            for control in RESIDENT_SEGMENT_ORDER
        ]

        return ResidentSegmentedControlViewModel(
            label="Resident Section",
            options=options,
            selected_id=ResidentSectionEnum.CONTACT,
            key="resident_segmented_controls",
        )


"""

class ResidentSegmentedControlPresenter:

    @staticmethod
    def present_segmented_controls() -> ResidentSegmentedControlViewModel:
        options = [
            ResidentSegmentOptionViewModel(
                id=control,
                label=control.value.replace("_", " ").title(),
            )
            for control in RESIDENT_SEGMENT_ORDER
        ]

        return ResidentSegmentedControlViewModel(
            label="Resident Section",
            options=options,
            selected_id=ResidentSectionEnum.CONTACT,
            key="resident_segmented_controls",
        )
"""
