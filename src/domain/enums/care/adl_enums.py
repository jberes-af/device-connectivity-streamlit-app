# src/domain/enums/care/adl_enums.py

from enum import StrEnum

class AdlCategorySensorLinkEnum(StrEnum):
    BATHING = "ambulating"
    DRESSING = "dressing"
    EATING = "eating"
    HYGIENE = "hygiene"
    SITTING = "sitting"
    SLEEPING = "sleeping"
    TOILETING = "toileting"
    TRANSFERRING = "transferring"

    @property
    def label(self) -> str:
        return {
            AdlCategorySensorLinkEnum.BATHING: "Bathing",
            AdlCategorySensorLinkEnum.DRESSING: "Dressing",
            AdlCategorySensorLinkEnum.EATING: "Eating",
            AdlCategorySensorLinkEnum.HYGIENE: "Hygiene",
            AdlCategorySensorLinkEnum.SITTING: "Sitting",
            AdlCategorySensorLinkEnum.SLEEPING: "Sleeping",
            AdlCategorySensorLinkEnum.TOILETING: "Toileting",
            AdlCategorySensorLinkEnum.TRANSFERRING: "Transferring",
        }[self]


class AdlCategoryEnum(StrEnum):
    BATHING = "bathing"
    CONTINENCE = "continence"
    DRESSING = "dressing"
    EATING = "eating"
    TOILETING = "toileting"
    TRANSFERRING = "transferring"

    @property
    def label(self) -> str:
        return {
            AdlCategoryEnum.BATHING: "Bathing",
            AdlCategoryEnum.CONTINENCE: "Continence",
            AdlCategoryEnum.DRESSING: "Dressing",
            AdlCategoryEnum.EATING: "Eating",
            AdlCategoryEnum.TOILETING: "Toileting",
            AdlCategoryEnum.TRANSFERRING: "Transferring",
        }[self]


class AdlObservationCategoryEnum(StrEnum):
    APPETITE_AND_INTAKE = "appetite_and_intake"
    SLEEP_AND_REST = "sleep_and_rest"
    ENGAGEMENT_AND_INTERACTION = "engagement_and_interaction"
    MOOD_AND_AFFECT = "mood_and_affect"
    MOBILITY = "mobility"
    COMFORT_AND_WELL_BEING = "comfort_and_well_being"
    ROUTINE_CHANGES = "routine_changes"
    OTHER = "other"

    @property
    def label(self) -> str:
        return {
            AdlObservationCategoryEnum.APPETITE_AND_INTAKE:
                "Appetite and Intake",
            AdlObservationCategoryEnum.SLEEP_AND_REST:
                "Sleep and Rest",
            AdlObservationCategoryEnum.ENGAGEMENT_AND_INTERACTION:
                "Engagement and Interaction",
            AdlObservationCategoryEnum.MOOD_AND_AFFECT:
                "Mood and Affect",
            AdlObservationCategoryEnum.MOBILITY:
                "Mobility",
            AdlObservationCategoryEnum.COMFORT_AND_WELL_BEING:
                "Comfort and Well-Being",
            AdlObservationCategoryEnum.ROUTINE_CHANGES:
                "Routine Changes",
            AdlObservationCategoryEnum.OTHER:
                "Other",
        }[self]


"""
from dataclasses import dataclass
from enum import StrEnum

AdlCategoryDefinitionsLookup = {
    "bathing": "Washing the body, including showering or sponge bathing. Includes getting in and out of the bath or shower, washing, and drying.",
    "continence": "Bladder and bowel control; includes control, frequency of episodes, use of continence aids.",
    "dressing": "Selecting clothes, putting on and removing upper and lower body garments, and manipulating fasteners (buttons, zippers).",
    "eating": "Eating and drinking; includes bringing food to mouth, chewing/swallowing, use of adaptive utensils.",
    "toileting": "Using the toilet; includes transfer to/from toilet, clothing management, hygiene after elimination.",
    "transferring": "Moving between surfaces, for example bed to chair, chair to standing position, wheelchair transfers.",
}

AdlScoreDefinitionsBathingLookup = {
    "0": "Bathes safely without assistance",
    "1": "Supplies or environment prepared",
    "2": "Verbal reminders, staff on standby for safety",
    "3": "Assistance with some body areas",
    "4": "Assistance with most bathing tasks",
    "5": "Staff performs bathing",
    "8": "Activity did not occur",
}

AdlScoreDefinitionsContinenceLookup = {
    "0": "Able to control bladder and bowel.",
    "1": "Infrequent episodes",
    "2": "Regular episodes",
    "3": "Insufficient voluntary control",
    "4": "Uses briefs, catheter, or aids",
    "8": "Activity did not occur",
}

AdlScoreDefinitionsDressingLookup = {
    "0": "Dresses self completely",
    "1": "Clothes laid out",
    "2": "Verbal cueing only",
    "3": "Help with come garments (e.g. socks)",
    "4": "Help with most clothing",
    "5": "Fully dressed by staff",
    "8": "Activity did not occur",
}

AdlScoreDefinitionsEatingLookup = {
    "0": "Eats without help",
    "1": "Tray prepared, food cut",
    "2": "Cueing to continue",
    "3": "Occasional physical help",
    "4": "Staff feeds most bites",
    "5": "Fully fed by staff",
    "8": "Activity did not occur",
}

AdlScoreDefinitionsToiletingLookup = {
    "0": "Completes all steps",
    "2": "Staff on standby for safety",
    "3": "Help with clothing",
    "4": "Help with hygiene and transfer",
    "5": "Staff performs entire task",
    "8": "Activity did not occur",
}

AdlScoreDefinitionsTransferringLookup = {
    "0": "Transfers safely along",
    "2": "Staff on standby for safety",
    "3": "One-person assist",
    "4": "Two-person assist",
    "5": "Full mechanical lift",
    "8": "Activity did not occur",
}

AdlObservationCategoryDefinitionsLookup = {
    "appetite_and_intake": "Note any observations about eating or drinking, such as amount consumed, interest in food, or changes from usual patterns.",
    "sleep_and_rest": "Note sleep quality or rest patterns, including difficulty falling asleep, frequent waking, or daytime drowsiness.",
    "engagement_and_interaction": "Note participation in activities, social interaction, or changes in engagement with others.",
    "mood_and_affect": "Note observed emotional state or behavior, such as calmness, irritability, or changes from usual demeanor.",
    "mobility": "Note observations related to movement, steadiness, hesitation, or changes in usual mobility.",
    "comfort_and_well-being": "Note signs of comfort or discomfort, such as restlessness, positioning needs, or visible distress.",
    "routine_changes": "Note deviations from the usual routine, including schedule changes, visitors, or altered activities.",
    "other": "Note any additional observations that do not fit the categories above.",
}

AdlScoreLabelsBathingLookup = {
    "0": "Independent",
    "1": "Setup Assistance",
    "2": "Supervision",
    "3": "Limited Assist",
    "4": "Extensive Assist",
    "5": "Dependent",
    "8": "N/A",
}

AdlScoreLabelsContinenceLookup = {
    "0": "Continent",
    "1": "Occasional Incontinence",
    "2": "Frequent Incontinence",
    "3": "Incontinent",
    "4": "Managed with Device",
    "8": "N/A",
}

AdlScoreLabelsDressingLookup = {
    "0": "Independent",
    "1": "Setup",
    "2": "Supervision",
    "3": "Limited Assist",
    "4": "Extensive Assist",
    "5": "Dependent",
    "8": "N/A",
}

AdlScoreLabelsEatingLookup = {
    "0": "Independent",
    "1": "Setup",
    "2": "Supervision",
    "3": "Limited Assist",
    "4": "Extensive Assist",
    "5": "Dependent",
    "8": "N/A",
}

AdlScoreLabelsToiletingLookup = {
    "0": "Independent",
    "2": "Supervision",
    "3": "Limited Assist",
    "4": "Extensive Assist",
    "5": "Dependent",
    "8": "N/A",
}

AdlScoreLabelsTransferringLookup = {
    "0": "Independent",
    "2": "Supervision",
    "3": "Limited Assist",
    "4": "Extensive Assist",
    "5": "Dependent",
    "8": "N/A",
}



@dataclass(frozen=True)
class AdlScoreLabelLookups:
    bathing: AdlScoreLabelsBathingLookup
    continence: AdlScoreLabelsContinenceLookup
    dressing: AdlScoreLabelsDressingLookup
    eating: AdlScoreLabelsEatingLookup
    toileting: AdlScoreLabelsToiletingLookup
    transferring: AdlScoreLabelsTransferringLookup


class AdlCategoryEnum(StrEnum):
    BATHING = "Bathing"
    CONTINENCE = "Continence"
    DRESSING = "Dressing"
    EATING = "Eating"
    TOILETING = "Toileting"
    TRANSFERRING = "Transferring"


class AdlObservationCategoryEnum(StrEnum):
    APPETITE_AND_INTAKE = "Appetite and Intake"
    SLEEP_AND_REST = "Sleep and Rest"
    ENGAGEMENT_AND_INTERACTION = "Engagement and Interaction"
    MOOD_AND_AFFECT = "Mood and Affect"
    MOBILITY = "Mobility"
    COMFORT_AND_WELL_BEING = "Comfort and Well-Being"
    ROUTINE_CHANGES = "Routine Changes"
    OTHER = "Other"
"""
