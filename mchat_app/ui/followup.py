# -*- coding: utf-8 -*-
"""Tela de consulta de seguimento (M-CHAT-R/F), aplicada apenas aos itens
que pontuaram risco na etapa inicial."""

import streamlit as st

from mchat_app.content.attribution import CLINICAL_DISCLAIMER, INSTRUMENT_COPYRIGHT
from mchat_app.content.items import MCHAT_ITEMS_BY_ID
from mchat_app.logic.scoring import classify_final, compute_followup_score

PLACEHOLDER = "Selecione..."


def render() -> None:
    at_risk_ids: list[int] = st.session_state.at_risk_item_ids
    initial_score: int = st.session_state.initial_score

    st.header("Etapa 2 - Consulta de Seguimento (M-CHAT-R/F)")
    st.caption(INSTRUMENT_COPYRIGHT)
    st.info(CLINICAL_DISCLAIMER)
    st.warning(
        f"Escore inicial: {initial_score}/20 (risco médio). Conduza a consulta de "
        f"seguimento apenas para os {len(at_risk_ids)} itens abaixo, nos quais a "
        "criança pontuou risco na Etapa 1. Siga o roteiro de cada item com o "
        "cuidador e registre o resultado final (PASSOU/FALHOU) com base no seu "
        "julgamento clínico, conforme orientado no manual do instrumento."
    )
    st.divider()

    with st.form("followup_form"):
        results: dict[int, str] = {}
        for item_id in at_risk_ids:
            item = MCHAT_ITEMS_BY_ID[item_id]
            st.subheader(f"Item {item.id}")
            st.markdown(f"**{item.text}**")
            st.markdown(f"*{item.followup.intro}*")
            for step in item.followup.steps:
                st.markdown(f"- {step}")
            st.caption(item.followup.scoring_note)
            results[item.id] = st.radio(
                f"Resultado do item {item.id}",
                options=[PLACEHOLDER, "PASSOU", "FALHOU"],
                key=f"followup_item_{item.id}",
                horizontal=True,
            )
            st.divider()
        submitted = st.form_submit_button("Calcular resultado final")

    if not submitted:
        return

    missing = [item_id for item_id, result in results.items() if result == PLACEHOLDER]
    if missing:
        st.error(
            "Por favor, registre o resultado (PASSOU/FALHOU) de todos os itens antes "
            "de continuar. Faltam os itens: " + ", ".join(str(i) for i in missing)
        )
        return

    followup_score = compute_followup_score(results)
    final_classification = classify_final("medio", followup_score)

    st.session_state.followup_responses = results
    st.session_state.followup_score = followup_score
    st.session_state.final_classification = final_classification
    st.session_state.stage = "result"
    st.rerun()
