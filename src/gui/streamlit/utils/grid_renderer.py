# grid_renderer.py

from collections.abc import Sequence

from src.application.dto.filter_pipeline_uc_dtos import DisplayFieldDTO

import streamlit as st


def render_property_grid(
        *,
        fields: Sequence[DisplayFieldDTO],
        columns: int = 3,
) -> None:
    if not fields:
        return

    # Inject CSS once
    st.markdown(
        """
        <style>
        .property {
            margin-bottom: 18px;
        }

        .property-label {
            font-size: 0.82rem;
            color: #777;
            margin-bottom: 2px;
        }

        .property-value {
            margin-bottom: 0;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    cols = st.columns(columns)

    for index, field in enumerate(fields):
        with cols[index % columns]:

            if field.key in {"website", "map_url"}:
                st.markdown(
                    f"""
                    <div class="property">
                        <div class="property-label">{field.label}</div>
                        <div class="property-value">
                            <a href="{field.value}" target="_blank">
                                {field.label}
                            </a>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            else:
                st.markdown(
                    f"""
                    <div class="property">
                        <div class="property-label">{field.label}</div>
                        <div class="property-value">
                            {field.value or "—"}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
