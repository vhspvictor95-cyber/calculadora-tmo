# -*- coding: utf-8 -*-
"""Triagem M-CHAT-R/F com fluxo de atenção clínica.

App Streamlit independente - sem navegação cruzada com a calculadora de
prognóstico de TMO (app.py na raiz do repositório).
"""

import sys
from pathlib import Path

import streamlit as st

_REPO_ROOT = Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from mchat_app.content.attribution import (
    AGE_RANGE_NOTE,
    CLINICAL_DISCLAIMER,
    INSTRUMENT_COPYRIGHT,
    INSTRUMENT_LICENSE_NOTE,
)
from mchat_app.ui import followup, results, screening

st.set_page_config(page_title="Triagem M-CHAT-R/F", page_icon="🧩")

if "stage" not in st.session_state:
    st.session_state.stage = "intro"


def render_intro() -> None:
    st.title("🧩 Triagem M-CHAT-R/F")
    st.markdown(
        "Checklist Modificado para Autismo em Crianças Pequenas: versão revisada e "
        "consulta de seguimento."
    )
    st.info(CLINICAL_DISCLAIMER)
    st.caption(INSTRUMENT_COPYRIGHT)
    st.caption(INSTRUMENT_LICENSE_NOTE)
    st.caption(AGE_RANGE_NOTE)

    pdf_path = Path(__file__).resolve().parent / "assets" / "MCHATR_F_Brazilian_Portuguese_v2.pdf"
    if pdf_path.exists():
        with open(pdf_path, "rb") as f:
            st.download_button(
                "Baixar instrumento original (PDF)",
                data=f.read(),
                file_name=pdf_path.name,
                mime="application/pdf",
            )

    st.divider()
    if st.button("Iniciar triagem", type="primary"):
        st.session_state.stage = "screening"
        st.rerun()


STAGE_RENDERERS = {
    "intro": render_intro,
    "screening": screening.render,
    "followup": followup.render,
    "result": results.render,
}

STAGE_RENDERERS[st.session_state.stage]()
