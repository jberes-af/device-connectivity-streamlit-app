# src/domain/lookups/care/adl_lookups.py

from collections.abc import Mapping
from typing import Final

from src.domain.enums.care.adl_enums import (
    AdlCategoryEnum,
    AdlObservationCategoryEnum,
)

AdlScoreLookup = Mapping[int, str]

ADL_CATEGORY_DEFINITIONS: Final[
    Mapping[AdlCategoryEnum, str]
] = {
    AdlCategoryEnum.BATHING:
        (
            "Washing the body, including showering or sponge bathing. "
            "Includes getting in and out of the bath or shower, washing, "
            "and drying."
        ),
    AdlCategoryEnum.CONTINENCE:
        (
            "Bladder and bowel control; includes control, frequency of "
            "episodes, and use of continence aids."
        ),
    AdlCategoryEnum.DRESSING:
        (
            "Selecting clothes, putting on and removing upper and lower "
            "body garments, and manipulating fasteners "
            "(buttons, zippers)."
        ),
    AdlCategoryEnum.EATING:
        (
            "Eating and drinking; includes bringing food to mouth, "
            "chewing/swallowing, and use of adaptive utensils."
        ),
    AdlCategoryEnum.TOILETING:
        (
            "Using the toilet; includes transfer to/from toilet, clothing "
            "management, and hygiene after elimination."
        ),
    AdlCategoryEnum.TRANSFERRING:
        (
            "Moving between surfaces, for example bed to chair, chair "
            "to standing position, and wheelchair transfers."
        ),
}

ADL_OBSERVATION_CATEGORY_DEFINITIONS: Final[
    Mapping[AdlObservationCategoryEnum, str]
] = {
    AdlObservationCategoryEnum.APPETITE_AND_INTAKE:
        (
            "Note any observations about eating or drinking, such as "
            "amount consumed, interest in food, or changes from usual "
            "patterns."
        ),
    AdlObservationCategoryEnum.SLEEP_AND_REST:
        (
            "Note sleep quality or rest patterns, including difficulty "
            "falling asleep, frequent waking, or daytime drowsiness."
        ),
    AdlObservationCategoryEnum.ENGAGEMENT_AND_INTERACTION:
        (
            "Note participation in activities, social interaction, or "
            "changes in engagement with others."
        ),
    AdlObservationCategoryEnum.MOOD_AND_AFFECT:
        (
            "Note observed emotional state or behavior, such as calmness, "
            "irritability, or changes from usual demeanor."
        ),
    AdlObservationCategoryEnum.MOBILITY:
        (
            "Note observations related to movement, steadiness, "
            "hesitation, or changes in usual mobility."
        ),
    AdlObservationCategoryEnum.COMFORT_AND_WELL_BEING:
        (
            "Note signs of comfort or discomfort, such as restlessness, "
            "positioning needs, or visible distress."
        ),
    AdlObservationCategoryEnum.ROUTINE_CHANGES:
        (
            "Note deviations from the usual routine, including schedule "
            "changes, visitors, or altered activities."
        ),
    AdlObservationCategoryEnum.OTHER:
        (
            "Note any additional observations that do not fit the "
            "categories above."
        ),
}


ADL_SCORE_DEFINITIONS: Final[
    Mapping[AdlCategoryEnum, AdlScoreLookup]
] = {
    AdlCategoryEnum.BATHING: {
        0: "Bathes safely without assistance",
        1: "Supplies or environment prepared",
        2: "Verbal reminders, staff on standby for safety",
        3: "Assistance with some body areas",
        4: "Assistance with most bathing tasks",
        5: "Staff performs bathing",
        8: "Activity did not occur",
    },
    AdlCategoryEnum.CONTINENCE: {
        0: "Able to control bladder and bowel",
        1: "Infrequent episodes",
        2: "Regular episodes",
        3: "Insufficient voluntary control",
        4: "Uses briefs, catheter, or aids",
        8: "Activity did not occur",
    },
    AdlCategoryEnum.DRESSING: {
        0: "Dresses self completely",
        1: "Clothes laid out",
        2: "Verbal cueing only",
        3: "Help with some garments (e.g. socks)",
        4: "Help with most clothing",
        5: "Fully dressed by staff",
        8: "Activity did not occur",
    },
    AdlCategoryEnum.EATING: {
        0: "Eats without help",
        1: "Tray prepared, food cut",
        2: "Cueing to continue",
        3: "Occasional physical help",
        4: "Staff feeds most bites",
        5: "Fully fed by staff",
        8: "Activity did not occur",
    },
    AdlCategoryEnum.TOILETING: {
        0: "Completes all steps",
        2: "Staff on standby for safety",
        3: "Help with clothing",
        4: "Help with hygiene and transfer",
        5: "Staff performs entire task",
        8: "Activity did not occur",
    },
    AdlCategoryEnum.TRANSFERRING: {
        0: "Transfers safely alone",
        2: "Staff on standby for safety",
        3: "One-person assist",
        4: "Two-person assist",
        5: "Full mechanical lift",
        8: "Activity did not occur",
    },
}

ADL_SCORE_LABELS: Final[
    Mapping[AdlCategoryEnum, AdlScoreLookup]
] = {
    AdlCategoryEnum.BATHING: {
        0: "Independent",
        1: "Setup Assistance",
        2: "Supervision",
        3: "Limited Assist",
        4: "Extensive Assist",
        5: "Dependent",
        8: "N/A",
    },
    AdlCategoryEnum.CONTINENCE: {
        0: "Continent",
        1: "Occasional Incontinence",
        2: "Frequent Incontinence",
        3: "Incontinent",
        4: "Managed with Device",
        8: "N/A",
    },
    AdlCategoryEnum.DRESSING: {
        0: "Independent",
        1: "Setup",
        2: "Supervision",
        3: "Limited Assist",
        4: "Extensive Assist",
        5: "Dependent",
        8: "N/A",
    },
    AdlCategoryEnum.EATING: {
        0: "Independent",
        1: "Setup",
        2: "Supervision",
        3: "Limited Assist",
        4: "Extensive Assist",
        5: "Dependent",
        8: "N/A",
    },
    AdlCategoryEnum.TOILETING: {
        0: "Independent",
        2: "Supervision",
        3: "Limited Assist",
        4: "Extensive Assist",
        5: "Dependent",
        8: "N/A",
    },
    AdlCategoryEnum.TRANSFERRING: {
        0: "Independent",
        2: "Supervision",
        3: "Limited Assist",
        4: "Extensive Assist",
        5: "Dependent",
        8: "N/A",
    },
}