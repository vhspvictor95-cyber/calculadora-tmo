# -*- coding: utf-8 -*-
"""Tela de triagem inicial: os 20 itens do M-CHAT-R."""

import streamlit as st

from mchat_app.content.attribution import CLINICAL_DISCLAIMER, INSTRUMENT_COPYRIGHT
from mchat_app.content.items import MCHAT_ITEMS
from mchat_app.logic.scoring import classify_initial, compute_initial_score

PLACEHOLDER = "Selecione..."


def render() -> None:
    st.header("Etapa 1 - M-CHAT-R (20 itens)")
    st.caption(INSTRUMENT_COPYRIGHT)
    st.info(CLINICAL_DISCLAIMER)
    st.markdown(
        "Por favor, responda as questões abaixo sobre a criança. Pense em como ela "
        "geralmente se comporta. Se você viu a criança apresentar o comportamento "
        "descrito poucas vezes, ou seja, se não for um comportamento frequente, então "
        "responda **Não**. Por favor, marque Sim ou Não para todas as questões."
    )
    st.divider()

    with st.form("screening_form"):
        responses: dict[int, str] = {}
        for item in MCHAT_ITEMS:
            responses[item.id] = st.radio(
                f"{item.id}. {item.text}",
                options=[PLACEHOLDER, "Sim", "Não"],
                key=f"screening_item_{item.id}",
                horizontal=True,
            )
        submitted = st.form_submit_button("Calcular escore e continuar")

    if not submitted:
        return

    missing = [item_id for item_id, answer in responses.items() if answer == PLACEHOLDER]
    if missing:
        st.error(
            "Por favor, responda todos os itens antes de continuar. Faltam os itens: "
            + ", ".join(str(i) for i in missing)
        )
        return

    score, at_risk_ids = compute_initial_score(responses)
    band = classify_initial(score)

    st.session_state.initial_responses = responses
    st.session_state.initial_score = score
    st.session_state.at_risk_item_ids = at_risk_ids
    st.session_state.initial_band = band

    if band == "medio":
        st.session_state.stage = "followup"
    else:
        st.session_state.final_classification = band
        st.session_state.stage = "result"
    st.rerun()
