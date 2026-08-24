# /src/interface_adapters/presenters/patient/diagnosis_section_presenter.py

from src.application.use_cases.patient.diagnosis_and_treatment_uc_dtos import (
    DiagnosisDTO,
)

from src.interface_adapters.view_models.patient.diagnosis_view_models import (
    DiagnosisSectionViewModel,
    DiagnosisTableRowViewModel,
    DiagnosisDetailViewModel,
)

from src.interface_adapters.view_models.common.card_view_models import (
    MetricCardViewModel,
    CardPropertyFieldsViewModel,
)

from src.interface_adapters.view_models.common.property_field_view_model import (
    PropertyFieldViewModel,
)

from src.interface_adapters.view_models.common.card_grid_view_model import (
    CardGridViewModel,
)

from src.interface_adapters.presenters.utils_presenters import (
    format_date,
)


class DiagnosisSectionPresenter:

    def present(
            self,
            *,
            diagnoses: tuple[DiagnosisDTO, ...],
            selected_patient_diagnosis_id: str | None = None,
    ) -> DiagnosisSectionViewModel:

        ordered_diagnoses = tuple(
            sorted(
                diagnoses,
                key=lambda diagnosis: (
                    diagnosis.is_primary,
                    diagnosis.resolved_date is None,
                    diagnosis.diagnosed_date or diagnosis.resolved_date,
                ),
                reverse=True,
            )
        )

        selected_diagnosis = self._resolve_selected_diagnosis(
            diagnoses=ordered_diagnoses,
            selected_patient_diagnosis_id=(
                selected_patient_diagnosis_id
            ),
        )

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

    def _build_metric_grid(
            self,
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

    def _build_detail_card(
            self,
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
