# demo_use_case.py

from dataclasses import dataclass


@dataclass(frozen=True)
class DomainDescriptionResult:
    domain: str
    description: str


@dataclass(frozen=True)
class IdentitySummary:
    name: str
    age: str
    id: str


@dataclass(frozen=True)
class CarePlanSummary:
    name: str
    progress: str
    last_status_date: str


@dataclass(frozen=True)
class ScheduledEvents:
    name: str
    time: str
    date: str
    location: str


@dataclass(frozen=True)
class ProviderSummary:
    name: str
    entity_name: str
    telephone: str


@dataclass(frozen=True)
class PriorityItemsSummary:
    item_1: str
    item_2: str
    item_3: str
    item_1_date: str
    item_2_date: str
    item_3_date: str


@dataclass(frozen=True)
class SensingSummary:
    sensors_online: str
    last_notification: str
    last_notification_from: str


@dataclass(frozen=True)
class UseCaseResult:
    identity: IdentitySummary
    care_plan: CarePlanSummary
    schedule_events: ScheduledEvents
    priority: PriorityItemsSummary
    provider: ProviderSummary
    sensing: SensingSummary
    column_count: int


def run_use_case():
    number_of_display_columns = 4

    identity_summary = IdentitySummary(
        name='John Doe',
        age='53 years',
        id='ka9asdao8f908a',
    )

    care_plan = CarePlanSummary(
        name='Independent Transferring (CP-8754)',
        progress='On-track',
        last_status_date='February 18, 2024',
    )

    schedule_events = ScheduledEvents(
        name='Daily Exercise',
        time='10:00 AM EST',
        date='March 6, 2024',
        location='Onsite. Exercise Room',
    )

    provider = ProviderSummary(
        name='Dr. Gary Smith',
        entity_name='City Hospital',
        telephone='(757) 123-9876',
    )

    priority_items = PriorityItemsSummary(
        item_1='Lack of appetite',
        item_2='Struggled through chair aerobics. Complains of knee pain. Discussed with Dr. Smith',
        item_3='Near fall incident',
        item_1_date='March 12, 2024',
        item_2_date='March 10, 2024',
        item_3_date='January 12, 2024',
    )

    sensing = SensingSummary(
        sensors_online='3 / 4',
        last_notification='1 hour 18 minutes ago',
        last_notification_from="John's Bed Mat",
    )

    return UseCaseResult(
        identity=identity_summary,
        care_plan=care_plan,
        schedule_events=schedule_events,
        priority=priority_items,
        provider=provider,
        sensing=sensing,
        column_count=number_of_display_columns
    )
