# /src/infrastructure/persistence/mappers

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.google_sheets.schemas import CarePlanInstructionColumns

from src.domain.entities.entities import CarePlanInstruction

from src.infrastructure.persistence.common.utils_parsing import *


class CarePlanInstructionRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> CarePlanInstruction:
        schema = CarePlanInstructionColumns

        return CarePlanInstruction(
            instruction_id=parse_required_text(
                row.get(schema.INSTRUCTION_ID),
                field_name=schema.INSTRUCTION_ID,
            ),
            care_plan_id=parse_required_text(
                row.get(schema.CARE_PLAN_ID),
                field_name=schema.CARE_PLAN_ID,
            ),
            category=parse_optional_text(
                row.get(schema.CATEGORY),
                field_name=schema.CATEGORY,
            ),
            title=parse_required_text(
                row.get(schema.TITLE),
                field_name=schema.TITLE,
            ),
            instruction=parse_required_text(
                row.get(schema.INSTRUCTION),
                field_name=schema.INSTRUCTION,
            ),
            applies_to_goal_id=parse_optional_text(
                row.get(schema.APPLIES_TO_GOAL_ID),
                field_name=schema.APPLIES_TO_GOAL_ID,
            ),
            active=parse_optional_text(
                row.get(schema.ACTIVE),
                field_name=schema.ACTIVE,
            ),
        )


    @staticmethod
    def to_row(
        care_plan_instruction: CarePlanInstruction,
    ) -> RawRow:
        schema = CarePlanInstructionColumns

        return {

            schema.INSTRUCTION_ID:
                care_plan_instruction.instruction_id,

            schema.CARE_PLAN_ID:
                care_plan_instruction.care_plan_id,

            schema.CATEGORY:
                care_plan_instruction.category,

            schema.TITLE:
                care_plan_instruction.title,

            schema.INSTRUCTION:
                care_plan_instruction.instruction,

            schema.APPLIES_TO_GOAL_ID:
                care_plan_instruction.applies_to_goal_id,

            schema.ACTIVE:
                care_plan_instruction.active,

        }