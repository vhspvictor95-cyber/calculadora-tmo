# -*- coding: utf-8 -*-
"""Algoritmo de pontuação do M-CHAT-R/F.

Regras transcritas do manual oficial (© 2009 Robins, Fein, & Barton):

- Para todos os itens, a resposta "Não" indica risco de TEA, exceto para os
  itens 2, 5 e 12, nos quais "Sim" indica risco.
- BAIXO RISCO: escore total 0-2.
- RISCO MÉDIO: escore total 3-7; aplicar a consulta de seguimento (M-CHAT-R/F)
  apenas nos itens em que a criança pontuou risco. Escore de seguimento >= 2
  = triagem positiva; escore de seguimento 0-1 = triagem negativa.
- RISCO ELEVADO: escore total 8-20; a consulta de seguimento pode ser
  dispensada, encaminhar diretamente para avaliação diagnóstica.
"""

from typing import Literal

from mchat_app.content.items import MCHAT_ITEMS_BY_ID, RiskAnswer

InitialBand = Literal["baixo", "medio", "alto"]
FinalClassification = Literal["baixo", "medio_pass", "medio_fail", "alto"]

FOLLOWUP_FAIL_THRESHOLD = 2


def compute_initial_score(responses: dict[int, RiskAnswer]) -> tuple[int, list[int]]:
    """Retorna (escore_total, ids_dos_itens_em_risco) a partir das respostas Sim/Não."""
    at_risk_ids: list[int] = []
    for item_id, item in MCHAT_ITEMS_BY_ID.items():
        answer = responses[item_id]
        if answer == item.risk_answer:
            at_risk_ids.append(item_id)
    return len(at_risk_ids), sorted(at_risk_ids)


def classify_initial(score: int) -> InitialBand:
    if score <= 2:
        return "baixo"
    if score <= 7:
        return "medio"
    return "alto"


def compute_followup_score(followup_results: dict[int, Literal["PASSOU", "FALHOU"]]) -> int:
    """Conta quantos itens da consulta de seguimento resultaram em FALHOU."""
    return sum(1 for result in followup_results.values() if result == "FALHOU")


def classify_final(initial_band: InitialBand, followup_score: int | None = None) -> FinalClassification:
    if initial_band == "baixo":
        return "baixo"
    if initial_band == "alto":
        return "alto"
    # initial_band == "medio": requer resultado da consulta de seguimento
    assert followup_score is not None, "followup_score é obrigatório quando initial_band == 'medio'"
    return "medio_fail" if followup_score >= FOLLOWUP_FAIL_THRESHOLD else "medio_pass"
