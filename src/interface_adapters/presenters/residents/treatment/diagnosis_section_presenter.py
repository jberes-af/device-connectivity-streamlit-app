# /src/interface_adapters/presenters/residents/treatment/diagnosis_section_presenter.py

from datetime import date

from src.application.use_cases.residents.treatment.diagnosis_and_treatment_uc_dtos import (
    DiagnosisDTO,
)

from src.interface_adapters.view_models.residents.treatment.diagnosis_view_models import (
    DiagnosisSectionViewModel,
)

from src.interface_adapters.view_models.widgets.card_view_models import (
    CardPropertyFieldsViewModel,
)

from src.interface_adapters.view_models.widgets.property_field_view_model import (
    PropertyFieldViewModel,
)

from src.interface_adapters.view_models.widgets.card_grid_view_model import (
    CardGridViewModel,
)

from src.interface_adapters.presenters.utils_presenters import (
    format_date,
    format_optional,
)


class DiagnosisSectionPresenter:

    def present(
            self,
            *,
            results_diagnoses: tuple[DiagnosisDTO, ...],
    ) -> DiagnosisSectionViewModel:
        ordered_diagnoses: tuple[DiagnosisDTO, ...] = (
            self._get_ordered_diagnoses(
                diagnoses=results_diagnoses,
            )
        )

        diagnosis_card_grids: tuple[CardGridViewModel, ...] = (
            self._build_diagnosis_card_grids(
                diagnoses=ordered_diagnoses,
            )
        )

        return DiagnosisSectionViewModel(
            diagnoses_card_grid=diagnosis_card_grids,
        )

    def _build_diagnosis_card_grids(
            self,
            *,
            diagnoses: tuple[DiagnosisDTO, ...],
    ) -> tuple[CardGridViewModel, ...]:
        return tuple(
            CardGridViewModel(
                columns=1,
                cards=(
                    self._build_diagnosis_card(
                        diagnosis=diagnosis,
                    ),
                ),
            )
            for diagnosis in diagnoses
        )

    @staticmethod
    def _build_diagnosis_card(
            *,
            diagnosis: DiagnosisDTO,
    ) -> CardPropertyFieldsViewModel:
        return CardPropertyFieldsViewModel(
            id=(
                f"diagnosis_"
                f"{diagnosis.patient_diagnosis_id}"
            ),
            title=diagnosis.diagnosis_name,
            property_fields=(
                PropertyFieldViewModel(
                    label="Status",
                    value=(
                        "Active"
                        if diagnosis.resolved_date is None
                        else "Resolved"
                    ),
                ),
                PropertyFieldViewModel(
                    label="Primary",
                    value=(
                        "Yes"
                        if diagnosis.is_primary
                        else "No"
                    ),
                ),
                PropertyFieldViewModel(
                    label="Diagnosis ID",
                    value=format_optional(
                        diagnosis.diagnosis_id,
                    ),
                ),
                PropertyFieldViewModel(
                    label="Diagnosed Date",
                    value=format_date(
                        diagnosis.diagnosed_date,
                        empty_value="—",
                    ),
                ),
                PropertyFieldViewModel(
                    label="Resolved Date",
                    value=format_date(
                        diagnosis.resolved_date,
                        empty_value="—",
                    ),
                ),
                PropertyFieldViewModel(
                    label="Description",
                    value=format_optional(
                        diagnosis.diagnosis_description,
                    ),
                ),
            ),
        )

    @staticmethod
    def _get_ordered_diagnoses(
            *,
            diagnoses: tuple[DiagnosisDTO, ...],
    ) -> tuple[DiagnosisDTO, ...]:
        return tuple(
            sorted(
                diagnoses,
                key=lambda diagnosis: (
                    diagnosis.is_primary,
                    diagnosis.resolved_date is None,
                    diagnosis.diagnosed_date or date.min,
                ),
                reverse=True,
            )
        )


"""

class DiagnosisSectionPresenter:

    def present(
            self,
            *,
            results_diagnoses: tuple[DiagnosisDTO, ...],
            # selected_patient_diagnosis_id: str | None = None,
    ) -> DiagnosisSectionViewModel:
        ordered_diagnoses: tuple[DiagnosisDTO, ...] = (
            self._get_ordered_diagnoses(d=results_diagnoses))

        diagnoses_card_grid: tuple[CardGridViewModel, ...] = (
            self._present_diagnoses_card_grid(diagnoses=ordered_diagnoses)
        )

        return DiagnosisSectionViewModel(
            diagnoses_card_grid=diagnoses_card_grid
        )

    def _present_diagnoses_card_grid(
            self,
            diagnoses: tuple[DiagnosisDTO, ...],
    ) -> tuple[CardGridViewModel, ...]:
        # cards: list[CardPropertyFieldsViewModel] = [
        cards: tuple[CardGridItemViewModel, ...] = tuple([
            self._build_diagnosis_card(diagnosis=d) for d in diagnoses
        ])

        return tuple([
            CardGridViewModel(
                columns=1,
                cards=(card,),
            )
            for card in cards
        ])

    @staticmethod
    def _build_diagnosis_card(
            diagnosis: DiagnosisDTO,
    ) -> CardPropertyFieldsViewModel:
        return CardPropertyFieldsViewModel(
            title=f"Diagnosis: {diagnosis.diagnosis_id}",
            id=f"diagnosis_{diagnosis.diagnosis_id}",
            property_fields=(
                PropertyFieldViewModel(
                    label="Name",
                    value=format_optional(
                        diagnosis.diagnosis_name
                    ),
                ),
                PropertyFieldViewModel(
                    label="Diagnosis ID",
                    value=format_optional(
                        diagnosis.diagnosis_id
                    ),
                ),
                PropertyFieldViewModel(
                    label="Resolved Date",
                    value=format_date(
                        diagnosis.resolved_date,
                        empty_value="—",
                    ),
                ),
                PropertyFieldViewModel(
                    label="Diagnosis Date",
                    value=format_date(
                        diagnosis.diagnosed_date,
                        empty_value="—",
                    ),
                ),
                PropertyFieldViewModel(
                    label="Status",
                    value=(
                        "Active"
                        if diagnosis.resolved_date is None
                        else "Resolved"
                    ),
                ),
                PropertyFieldViewModel(
                    label="Primary",
                    value=(
                        "Yes"
                        if diagnosis.is_primary
                        else "No"
                    ),
                ),
                PropertyFieldViewModel(
                    label="Description",
                    value=(
                        diagnosis.diagnosis_description
                        if diagnosis.diagnosis_description
                        else "[No]"
                    ),
                ),
            ),
        )

    @staticmethod
    def _get_ordered_diagnoses(
            d: tuple[DiagnosisDTO, ...],
    ) -> tuple[DiagnosisDTO, ...]:
        return tuple(
            sorted(
                d,
                key=lambda diagnosis: (
                    diagnosis.is_primary,
                    diagnosis.resolved_date is None,
                    diagnosis.diagnosed_date or diagnosis.resolved_date,
                ),
                reverse=True,
            )
        )


@staticmethod
def _build_metric_grid(
        *,
        diagnoses: tuple[DiagnosisDTO, ...],
) -> CardGridViewModel:

    active_count = sum(
        1
        for diagnosis in diagnoses
        if diagnosis.resolved_date is None
    )

    resolved_count = sum(
        1
        for diagnosis in diagnoses
        if diagnosis.resolved_date is not None
    )

    primary_diagnosis = next(
        (
            diagnosis
            for diagnosis in diagnoses
            if diagnosis.is_primary
        ),
        None,
    )

    return CardGridViewModel(
        columns=3,
        cards=(
            MetricCardViewModel(
                label="Active Diagnoses",
                value=str(active_count),
            ),
            MetricCardViewModel(
                label="Resolved Diagnoses",
                value=str(resolved_count),
            ),
            MetricCardViewModel(
                label="Primary Diagnosis",
                value=(
                    primary_diagnosis.diagnosis_name
                    if primary_diagnosis is not None
                    else "—"
                ),
            ),
        ),
    )

@staticmethod
def _build_row(
        diagnosis: DiagnosisDTO,
) -> DiagnosisTableRowViewModel:

    status = (
        "Active"
        if diagnosis.resolved_date is None
        else "Resolved"
    )

    return DiagnosisTableRowViewModel(
        patient_diagnosis_id=diagnosis.patient_diagnosis_id,
        diagnosis_name=diagnosis.diagnosis_name,
        diagnosis_code=diagnosis.diagnosis_id,
        primary_display="Yes" if diagnosis.is_primary else "No",
        diagnosed_date_display=format_date(
            diagnosis.diagnosed_date,
            empty_value="—",
        ),
        resolved_date_display=format_date(
            diagnosis.resolved_date,
            empty_value="—",
        ),
        status_display=status,
    )

@staticmethod
def _build_detail_card(
        diagnosis: DiagnosisDTO,
) -> CardPropertyFieldsViewModel:

    return CardPropertyFieldsViewModel(
        id=diagnosis.patient_diagnosis_id,
        title=diagnosis.diagnosis_name,
        description=diagnosis.diagnosis_description,
        property_fields=(
            PropertyFieldViewModel(
                label="Diagnosis Code",
                value=diagnosis.diagnosis_id,
            ),
            PropertyFieldViewModel(
                label="Status",
                value=(
                    "Active"
                    if diagnosis.resolved_date is None
                    else "Resolved"
                ),
            ),
            PropertyFieldViewModel(
                label="Primary",
                value=(
                    "Yes"
                    if diagnosis.is_primary
                    else "No"
                ),
            ),
            PropertyFieldViewModel(
                label="Diagnosed",
                value=format_date(
                    diagnosis.diagnosed_date,
                    empty_value="—",
                ),
            ),
            PropertyFieldViewModel(
                label="Resolved",
                value=format_date(
                    diagnosis.resolved_date,
                    empty_value="—",
                ),
            ),
        ),
    )

@staticmethod
def _resolve_selected_diagnosis(
        *,
        diagnoses: tuple[DiagnosisDTO, ...],
        selected_patient_diagnosis_id: str | None,
) -> DiagnosisDTO | None:

    if not diagnoses:
        return None

    if selected_patient_diagnosis_id is not None:
        for diagnosis in diagnoses:
            if (
                    diagnosis.patient_diagnosis_id
                    == selected_patient_diagnosis_id
            ):
                return diagnosis

    primary = next(
        (
            diagnosis
            for diagnosis in diagnoses
            if diagnosis.is_primary
        ),
        None,
    )

    return primary or diagnoses[0]

"""

"""
selected_diagnosis = self._resolve_selected_diagnosis(
    diagnoses=ordered_diagnoses,
    selected_patient_diagnosis_id=(
        selected_patient_diagnosis_id
    ),
)

selected_diagnosis = None

return DiagnosisSectionViewModel(
    metric_grid=self._build_metric_grid(
        diagnoses=ordered_diagnoses,
    ),
    rows=tuple(
        self._build_row(diagnosis)
        for diagnosis in ordered_diagnoses
    ),
    detail_card=(
        self._build_detail_card(selected_diagnosis)
        if selected_diagnosis is not None
        else None
    ),
)
"""
