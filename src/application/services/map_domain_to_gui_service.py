# /src/application/services/map_domain_to_gui_service.py


from src.domain.entities.person.patient_entities import (
    Facility,
    PaceProgram,
)

from src.application.dto.filter_pipeline_uc_dtos import (
    DisplayFieldDTO,
    EntityTypeRecordDTO,
)


class EntityTypeRecordMapper:
    def from_facility(
            self,
            facility: Facility,
    ) -> EntityTypeRecordDTO:
        mgt_co = _display_mgt_co(facility.management_co)

        return EntityTypeRecordDTO(
            entity_id=facility.entity_id,
            alternate_id=facility.facility_id or "",
            record_type="Facility",
            fields=(
                DisplayFieldDTO(
                    key="owner_name",
                    label="Owner Name",
                    value=_display_proper_name(facility.owner_name),
                ),
                DisplayFieldDTO(
                    key="owner_location",
                    label="City • State",
                    value=_format_location(
                        facility.owner_city,
                        facility.owner_state,
                    ),
                ),
                DisplayFieldDTO(
                    key="owner_telephone",
                    label="Owner Telephone",
                    value=_display_text(facility.owner_telephone),
                ),
                DisplayFieldDTO(
                    key="contact_name",
                    label="Contact Name",
                    value=_display_proper_name(
                        facility.administrator_name
                    ),
                ),
                DisplayFieldDTO(
                    key="contact_email",
                    label="Contact Email",
                    value=_display_email(
                        facility.administrator_email
                    ),
                ),
                DisplayFieldDTO(
                    key="management_company",
                    label="Management Co",
                    value=_display_text(mgt_co),
                ),
                DisplayFieldDTO(
                    key="capacity",
                    label="Capacity",
                    value=_format_count(
                        facility.capacity,
                        "beds",
                    ),
                ),
            ),
        )

    def from_pace_program(
            self,
            pace_program: PaceProgram,
    ) -> EntityTypeRecordDTO:
        return EntityTypeRecordDTO(
            entity_id=pace_program.entity_id,
            alternate_id=pace_program.h_number,
            record_type="PACE Program",
            fields=(
                DisplayFieldDTO(
                    key="owner_name",
                    label="Owner Name",
                    value=_display_text(
                        pace_program.owner_name
                    ),
                ),
                DisplayFieldDTO(
                    key="owner_location",
                    label="City • State",
                    value=_format_location(
                        pace_program.owner_city,
                        pace_program.owner_state,
                    ),
                ),
                DisplayFieldDTO(
                    key="owner_telephone",
                    label="Owner Telephone",
                    value=_display_text(
                        pace_program.owner_contact_tel
                    ),
                ),
                DisplayFieldDTO(
                    key="contact_name",
                    label="Contact Name",
                    value=_display_proper_name(
                        pace_program.owner_contact_name
                    ),
                ),
                DisplayFieldDTO(
                    key="contact_email",
                    label="Contact Email",
                    value=_display_email(
                        pace_program.owner_contact_email
                    ),
                ),
                DisplayFieldDTO(
                    key="affiliate",
                    label="Affiliate",
                    value=_display_proper_name(
                        pace_program.affiliate
                    ),
                ),
                DisplayFieldDTO(
                    key="census",
                    label="Census",
                    value=_format_count(
                        pace_program.census,
                        "participants",
                    ),
                ),
            ),
        )


def _display_text(value: object | None) -> str:
    if value is None:
        return "---"

    text = str(value).strip()
    return text or "---"


def _display_email(value: object | None) -> str:
    if value is None:
        return "---"

    text = str(value).strip().lower()
    return text or "---"


def _display_proper_name(value: object | None) -> str:
    if value is None:
        return "---"

    text = str(value).strip().title()
    return text or "---"


def _format_location(
        city: str | None,
        state: str | None,
) -> str:
    city = city.strip().title() if city else "---"
    state = state.strip().upper() if state else "---"
    return f"{city} • {state}"


def _format_count(
        value: int | None,
        unit: str,
) -> str:
    if value is None:
        return "---"

    return f"{value:,} {unit}"


def _display_mgt_co(value: object | None) -> str:
    if value is None:
        return "---"

    text = (str(value)
            .replace("LLC", "")
            .replace("INC", "")
            .replace("LP", "")
            .strip()
            .title())
    return text or "---"
