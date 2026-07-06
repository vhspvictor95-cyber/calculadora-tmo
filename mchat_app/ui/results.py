# -*- coding: utf-8 -*-
"""Tela de resultado final: escore, classificação e painel de orientação clínica."""

import streamlit as st

from mchat_app.content.attribution import GUIDANCE_ATTRIBUTION_NOTE
from mchat_app.content.risk_guidance import RISK_GUIDANCE

BAND_DISPLAY = {
    "baixo": ("success", "BAIXO RISCO"),
    "medio_pass": ("warning", "RISCO MÉDIO - TRIAGEM NEGATIVA"),
    "medio_fail": ("error", "RISCO MÉDIO - TRIAGEM POSITIVA"),
    "alto": ("error", "RISCO ELEVADO"),
}


def _reset() -> None:
    for key in (
        "stage",
        "initial_responses",
        "initial_score",
        "at_risk_item_ids",
        "initial_band",
        "followup_responses",
        "followup_score",
        "final_classification",
    ):
        st.session_state.pop(key, None)
    for key in list(st.session_state.keys()):
        if key.startswith("screening_item_") or key.startswith("followup_item_"):
            del st.session_state[key]
    st.session_state.stage = "intro"


def render() -> None:
    final_classification: str = st.session_state.final_classification
    initial_score: int = st.session_state.initial_score
    guidance = RISK_GUIDANCE[final_classification]

    st.header("Resultado da Triagem")

    col1, col2 = st.columns([1, 2])
    with col1:
        st.metric(label="Escore M-CHAT-R (Etapa 1)", value=f"{initial_score}/20")
        if "followup_score" in st.session_state:
            st.metric(
                label="Escore da Consulta de Seguimento",
                value=f"{st.session_state.followup_score}",
            )
    with col2:
        style, label = BAND_DISPLAY[final_classification]
        getattr(st, style)(label)
        st.markdown(f"**{guidance.score_range_desc}**")
        st.markdown(guidance.action_summary)

    st.divider()
    st.caption(GUIDANCE_ATTRIBUTION_NOTE)

    tabs = st.tabs(
        [
            "Encaminhamento",
            "Avaliação Especializada",
            "Rotina Terapêutica",
            "Rotina Diagnóstica",
            "Diagnóstico Diferencial",
        ]
    )
    sections = (
        guidance.referrals,
        guidance.assessments,
        guidance.therapeutic_routine,
        guidance.diagnostic_routine,
        guidance.differential_diagnosis,
    )
    for tab, section_items in zip(tabs, sections):
        with tab:
            for entry in section_items:
                st.markdown(f"- {entry}")

    st.divider()
    if st.button("Reiniciar triagem"):
        _reset()
        st.rerun()
