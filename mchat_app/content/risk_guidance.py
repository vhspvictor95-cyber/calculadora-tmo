# -*- coding: utf-8 -*-
"""Orientação clínica estruturada por faixa de risco do M-CHAT-R/F.

IMPORTANTE: este conteúdo NÃO é parte do instrumento oficial M-CHAT-R/F
(ver mchat_app/content/attribution.py). É conteúdo complementar elaborado
com base no algoritmo de pontuação oficial do M-CHAT-R/F e em diretrizes
públicas de vigilância do desenvolvimento infantil e rastreio de TEA
(Sociedade Brasileira de Pediatria e American Academy of Pediatrics),
destinado a apoiar - não substituir - o julgamento clínico do profissional.
"""

from dataclasses import dataclass, field


@dataclass(frozen=True)
class RiskGuidance:
    band_key: str
    label: str
    score_range_desc: str
    action_summary: str
    referrals: tuple[str, ...]
    assessments: tuple[str, ...]
    therapeutic_routine: tuple[str, ...]
    diagnostic_routine: tuple[str, ...]
    differential_diagnosis: tuple[str, ...]


RISK_GUIDANCE: dict[str, RiskGuidance] = {
    "baixo": RiskGuidance(
        band_key="baixo",
        label="Baixo risco",
        score_range_desc="Escore total M-CHAT-R: 0-2",
        action_summary=(
            "Nenhuma avaliação adicional é necessária, a menos que a evolução clínica "
            "indique risco de TEA. Se a criança tiver menos de 24 meses, reavaliar após "
            "o segundo aniversário."
        ),
        referrals=(
            "Nenhum encaminhamento específico indicado pelo escore.",
            "Encaminhar para avaliação do desenvolvimento independentemente do escore "
            "se houver preocupação clínica do profissional ou dos pais/cuidadores.",
        ),
        assessments=(
            "Manter vigilância do desenvolvimento nas consultas de puericultura de rotina.",
            "Confirmar triagem auditiva e visual de rotina, se ainda não realizadas.",
        ),
        therapeutic_routine=(
            "Orientar os cuidadores sobre estimulação do desenvolvimento (interação "
            "responsiva, leitura compartilhada, brincadeiras não estruturadas).",
            "Nenhuma intervenção terapêutica específica indicada pelo escore.",
        ),
        diagnostic_routine=(
            "Repetir o M-CHAT-R/F na próxima visita de puericultura se a criança tiver "
            "menos de 24 meses.",
            "Registrar o resultado no prontuário para acompanhamento longitudinal.",
        ),
        differential_diagnosis=(
            "Escore baixo não exclui TEA de forma definitiva, especialmente em crianças "
            "muito jovens (próximas a 16 meses) ou com regressão de habilidades já "
            "adquiridas - nesses casos, priorizar o julgamento clínico sobre o escore.",
        ),
    ),
    "medio_pass": RiskGuidance(
        band_key="medio_pass",
        label="Risco médio - triagem negativa após consulta de seguimento",
        score_range_desc="Escore total M-CHAT-R: 3-7; escore da consulta de seguimento (M-CHAT-R/F): 0-1",
        action_summary=(
            "Triagem negativa. Nenhuma avaliação adicional é necessária, exceto se a "
            "evolução clínica indicar risco de TEA. A criança deve ser triada novamente "
            "em futuras visitas médicas."
        ),
        referrals=(
            "Não há indicação de encaminhamento imediato para avaliação diagnóstica de "
            "TEA com base no escore.",
            "Considerar encaminhamento para avaliação de linguagem/audição se os itens "
            "inicialmente em risco envolverem comunicação ou resposta a sons.",
        ),
        assessments=(
            "Triagem auditiva (audiometria), caso ainda não tenha sido realizada - "
            "principal diagnóstico diferencial a descartar mesmo em triagem negativa.",
            "Monitorar marcos de linguagem e comunicação social nas próximas consultas.",
        ),
        therapeutic_routine=(
            "Orientação aos cuidadores sobre estimulação de linguagem e interação social.",
            "Conduta expectante com reavaliação programada (não aguardar até a próxima "
            "consulta de rotina se houver qualquer piora perceptível).",
        ),
        diagnostic_routine=(
            "Repetir o M-CHAT-R/F na próxima visita médica.",
            "Documentar quais itens pontuaram risco inicialmente, para comparação na "
            "reavaliação.",
        ),
        differential_diagnosis=(
            "Perda auditiva.",
            "Atraso transitório de linguagem.",
            "Fatores ambientais/psicossociais (estimulação limitada).",
            "Temperamento/timidez.",
        ),
    ),
    "medio_fail": RiskGuidance(
        band_key="medio_fail",
        label="Risco médio - triagem positiva após consulta de seguimento",
        score_range_desc="Escore total M-CHAT-R: 3-7; escore da consulta de seguimento (M-CHAT-R/F): ≥ 2",
        action_summary=(
            "Triagem positiva. Encaminhar a criança para avaliação diagnóstica e para "
            "intervenção precoce."
        ),
        referrals=(
            "Avaliação especializada em neurodesenvolvimento (neuropediatria, psiquiatria "
            "infantil ou pediatria do desenvolvimento).",
            "Fonoaudiologia, para avaliação de linguagem e comunicação.",
            "Triagem auditiva completa (audiometria/BERA), para descartar perda auditiva.",
            "Terapia ocupacional, para avaliação sensorial e motora.",
            "Avaliação genética se houver dismorfismos, atraso global do desenvolvimento "
            "ou história familiar relevante.",
        ),
        assessments=(
            "Instrumentos diagnósticos padronizados para TEA (ADOS-2, ADI-R), quando "
            "disponíveis e aplicados por profissional treinado.",
            "Avaliação do desenvolvimento global/cognitivo (ex.: Bayley-III, Vineland).",
            "Avaliação de linguagem receptiva e expressiva.",
            "Triagem auditiva e visual completas.",
        ),
        therapeutic_routine=(
            "Encaminhamento imediato para intervenção precoce, sem aguardar o fechamento "
            "diagnóstico.",
            "Intervenção comportamental (ex.: abordagens baseadas em ABA, modelos "
            "desenvolvimentais como o Denver Model).",
            "Fonoterapia.",
            "Terapia ocupacional com abordagem sensorial.",
            "Orientação e treinamento parental (intervenção mediada pelos pais).",
            "Avaliação de elegibilidade para serviços de estimulação precoce/educação especial.",
        ),
        diagnostic_routine=(
            "1) Confirmar acuidade auditiva e visual (descartar causas sensoriais).",
            "2) Avaliar o desenvolvimento global (motor, linguagem, cognitivo, social) para "
            "diferenciar atraso global de déficit específico de comunicação social.",
            "3) Avaliação especializada em TEA por equipe multiprofissional treinada.",
            "4) Avaliação genética conforme indicação clínica.",
            "5) Avaliação médica geral para condições associadas (epilepsia, distúrbios "
            "metabólicos, síndromes genéticas).",
        ),
        differential_diagnosis=(
            "Perda auditiva.",
            "Atraso global do desenvolvimento.",
            "Deficiência intelectual.",
            "Transtorno específico de linguagem.",
            "Transtorno de apego reativo / negligência.",
            "Mutismo seletivo ou ansiedade social (em crianças maiores).",
            "TDAH (em crianças maiores).",
        ),
    ),
    "alto": RiskGuidance(
        band_key="alto",
        label="Risco elevado",
        score_range_desc="Escore total M-CHAT-R: 8-20",
        action_summary=(
            "Não é necessário fazer a consulta de seguimento. A criança deve ser "
            "encaminhada imediatamente para avaliação diagnóstica e intervenção precoce."
        ),
        referrals=(
            "Avaliação especializada em neurodesenvolvimento (neuropediatria, psiquiatria "
            "infantil ou pediatria do desenvolvimento) com prioridade/urgência.",
            "Fonoaudiologia, para avaliação de linguagem e comunicação.",
            "Triagem auditiva completa (audiometria/BERA), para descartar perda auditiva.",
            "Terapia ocupacional, para avaliação sensorial e motora.",
            "Avaliação genética se houver dismorfismos, atraso global do desenvolvimento "
            "ou história familiar relevante.",
        ),
        assessments=(
            "Instrumentos diagnósticos padronizados para TEA (ADOS-2, ADI-R), quando "
            "disponíveis e aplicados por profissional treinado.",
            "Avaliação do desenvolvimento global/cognitivo (ex.: Bayley-III, Vineland).",
            "Avaliação de linguagem receptiva e expressiva.",
            "Triagem auditiva e visual completas.",
        ),
        therapeutic_routine=(
            "Encaminhamento imediato e prioritário para intervenção precoce, sem aguardar "
            "o fechamento diagnóstico.",
            "Intervenção comportamental (ex.: abordagens baseadas em ABA, modelos "
            "desenvolvimentais como o Denver Model).",
            "Fonoterapia.",
            "Terapia ocupacional com abordagem sensorial.",
            "Orientação e treinamento parental (intervenção mediada pelos pais).",
            "Avaliação de elegibilidade para serviços de estimulação precoce/educação especial.",
        ),
        diagnostic_routine=(
            "1) Confirmar acuidade auditiva e visual (descartar causas sensoriais).",
            "2) Avaliar o desenvolvimento global (motor, linguagem, cognitivo, social) para "
            "diferenciar atraso global de déficit específico de comunicação social.",
            "3) Avaliação especializada em TEA por equipe multiprofissional treinada, com "
            "prioridade dada a alta probabilidade pré-teste.",
            "4) Avaliação genética conforme indicação clínica.",
            "5) Avaliação médica geral para condições associadas (epilepsia, distúrbios "
            "metabólicos, síndromes genéticas).",
        ),
        differential_diagnosis=(
            "Perda auditiva.",
            "Atraso global do desenvolvimento.",
            "Deficiência intelectual.",
            "Transtorno específico de linguagem.",
            "Transtorno de apego reativo / negligência.",
            "Mutismo seletivo ou ansiedade social (em crianças maiores).",
            "TDAH (em crianças maiores).",
        ),
    ),
}
