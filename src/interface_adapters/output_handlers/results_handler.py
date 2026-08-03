# /src/interface_adapters/output_handlers/results_handler.py

from pathlib import Path

from src.application.dto.run_all_use_cases_dtos import (
    RunAllUseCasesResultDTO,
)
from src.infrastructure.services.renderers.pandas_dataframe_renderer import (
    PandasDataFrameRenderer,
)
from src.infrastructure.services.writers.dataframe_console_writer import (
    DataFrameConsoleWriter,
)
from src.infrastructure.services.writers.dataframe_csv_writer import (
    DataFrameCsvWriter,
)
from src.interface_adapters.presenters.texas_facilities_presenter import (
    TexasFacilitiesPresenter,
)


WRITE_TO_SHELL: bool = False
WRITE_TO_FILE: bool = True


def handle_outputs(
    *,
    result: RunAllUseCasesResultDTO,
    presenter: TexasFacilitiesPresenter,
    dataframe_renderer: PandasDataFrameRenderer,
    console_writer: DataFrameConsoleWriter | None = None,
    csv_writer: DataFrameCsvWriter | None = None,
    csv_output_path: Path | None = None,
) -> None:

    """
    facilities = (
        result
        .build_facility_table_result
        .facilities
    )
    """


    facilities = (
        result
        .analyze_facility_table_results
        .independent_candidates
    )

    tables = presenter.present(
        facilities=facilities,
    )

    table = tables.independent_facilities_table

    dataframe = dataframe_renderer.to_dataframe(
        table=table,
    )

    if WRITE_TO_SHELL:
        if console_writer is not None:
            console_writer.write(
                dataframe,
                title=table.title,
            )

    if WRITE_TO_FILE:
        if csv_writer is not None:
            if csv_output_path is None:
                raise ValueError(
                    "csv_output_path is required when "
                    "csv_writer is provided."
                )

            written_path = csv_writer.write(
                dataframe,
                output_path=csv_output_path,
            )

            print(f"\nCSV written to: {written_path}")