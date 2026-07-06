# -*- coding: utf-8 -*-
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from mchat_app.content.items import MCHAT_ITEMS, REVERSE_SCORED_IDS
from mchat_app.logic.scoring import (
    classify_final,
    classify_initial,
    compute_followup_score,
    compute_initial_score,
)


def _all_no_risk_responses() -> dict[int, str]:
    """Respostas que não pontuam risco em nenhum item (score 0)."""
    responses = {}
    for item in MCHAT_ITEMS:
        # resposta oposta à resposta de risco
        responses[item.id] = "Não" if item.risk_answer == "Sim" else "Sim"
    return responses


def test_reverse_scored_ids():
    assert REVERSE_SCORED_IDS == {2, 5, 12}


def test_score_zero_when_no_risk_answers():
    responses = _all_no_risk_responses()
    score, at_risk_ids = compute_initial_score(responses)
    assert score == 0
    assert at_risk_ids == []


def test_score_counts_reverse_scored_items_correctly():
    responses = _all_no_risk_responses()
    # Marcar item 2 (reverse scored) como risco: responder "Sim"
    responses[2] = "Sim"
    score, at_risk_ids = compute_initial_score(responses)
    assert score == 1
    assert at_risk_ids == [2]


def test_classify_initial_boundaries():
    assert classify_initial(0) == "baixo"
    assert classify_initial(2) == "baixo"
    assert classify_initial(3) == "medio"
    assert classify_initial(7) == "medio"
    assert classify_initial(8) == "alto"
    assert classify_initial(20) == "alto"


def test_compute_followup_score():
    results = {1: "PASSOU", 2: "FALHOU", 5: "FALHOU", 6: "PASSOU"}
    assert compute_followup_score(results) == 2


def test_classify_final_low_and_high_bypass_followup():
    assert classify_final("baixo") == "baixo"
    assert classify_final("alto") == "alto"


def test_classify_final_medio_pass_and_fail():
    assert classify_final("medio", followup_score=0) == "medio_pass"
    assert classify_final("medio", followup_score=1) == "medio_pass"
    assert classify_final("medio", followup_score=2) == "medio_fail"
    assert classify_final("medio", followup_score=5) == "medio_fail"


def test_all_20_items_present_and_ordered():
    assert [item.id for item in MCHAT_ITEMS] == list(range(1, 21))
