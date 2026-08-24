# /src/interface_adapters/presenters/person/resident_sensing_section_presenter.py

from src.application.use_cases.sensing.device_profiles.user_sensing_account_uc_dtos import (
    UserSensingAccountResultDTO,
)

from src.interface_adapters.view_models.common.card_grid_view_model import (
    CardGridViewModel
)

from src.interface_adapters.view_models.common.tab_view_model import (
    TabItemViewModel,
    TabViewModel,
)

from src.interface_adapters.view_models.sensing.resident_sensing_view_model import (
    # SensingTabIdEnum,
    SENSING_SEGMENT_ORDER,
    # SensorProfileViewModel,
    SensorSectionViewModel,
)

from src.interface_adapters.view_models.common.card_view_models import (
    CardAttributeNameCountListViewModel,
)


class ResidentSensingSectionPresenter:

    def present_sensing_section(
            self,
            result: UserSensingAccountResultDTO,
    ) -> SensorSectionViewModel:
        dash_card_grid: CardGridViewModel = (
            self._present_dash_card_grid(
                sensing_data=result,
            )

        )

        sensing_detail_sections: TabViewModel = (
            self._present_sensing_tabs_section()

        )

        return SensorSectionViewModel(
            section_header="Sensing",
            dash_card_grid_vm=dash_card_grid,
            sensing_detail_section_vm=sensing_detail_sections,
        )

    def _present_dash_card_grid(
            self,
            sensing_data: UserSensingAccountResultDTO
    ) -> CardGridViewModel:
        return CardGridViewModel(
            columns=4,
            cards=self._build_dashboard_cards(
                sensing_data=sensing_data,
            ),
        )

    @staticmethod
    def _present_sensing_tabs_section(
    ) -> TabViewModel[str]:
        tabs = tuple(
            TabItemViewModel(
                tab_id=segment.value,
                label=segment.value.replace("_", " ").title(),
                content=f"{segment.value} content",
            )
            for segment in SENSING_SEGMENT_ORDER
        )

        return TabViewModel(
            tabs=tabs,
        )

    @staticmethod
    def _build_dashboard_cards(
            sensing_data: UserSensingAccountResultDTO,
    ) -> tuple[CardAttributeNameCountListViewModel, ...]:
        sensor_attributes: list[str] = [
            f"{r.system_config.sensor_type.title().strip()} ∙ ID: {r.sensor_id}"
            for r in sensing_data.sensor_profiles
        ]

        gateway_attributes: list[str] = [
            f"ID: {r.gateway_id}"
            for r in sensing_data.gateway_profiles
        ]

        location_attributes: set[str] = {
            f"{r.user_config.location.strip()}"
            for r in sensing_data.sensor_profiles
            if r.user_config is not None
        }

        zone_attributes: set[str] = {
            f"{r.user_config.zone.strip()}"
            for r in sensing_data.sensor_profiles
            if r.user_config is not None
        }

        return (
            CardAttributeNameCountListViewModel(
                id="resident_sensor_attributes",
                title="Sensors",
                attribute_count=str(len(sensing_data.sensor_ids)),
                attributes=tuple(sensor_attributes),
            ),
            CardAttributeNameCountListViewModel(
                id="resident_location_attributes",
                title="Locations",
                attribute_count=str(len(location_attributes)),
                attributes=tuple(location_attributes),
            ),
            CardAttributeNameCountListViewModel(
                id="resident_zon_attributes",
                title="Zones",
                attribute_count=str(len(zone_attributes)),
                attributes=tuple(zone_attributes),
            ),
            CardAttributeNameCountListViewModel(
                id="resident_gateway_attributes",
                title="Gateways",
                attribute_count=str(len(sensing_data.gateway_ids)),
                attributes=tuple(gateway_attributes),
            ),
        )


"""
@staticmethod
def present_searchable_table(
        records: tuple[ResidentSearchableRecordDTO, ...],
) -> TableViewModel:
    return ResidentRecordsSearchableTablePresenter().present(
        records=records
    )

"""
