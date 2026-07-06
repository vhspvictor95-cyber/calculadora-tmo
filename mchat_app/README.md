# Triagem M-CHAT-R/F

App Streamlit independente que aplica o M-CHAT-R/F (Checklist Modificado
para Autismo em Crianças Pequenas, versão revisada e consulta de
seguimento) e, a partir do resultado, apresenta orientação clínica
estruturada (encaminhamento, avaliação especializada, rotina terapêutica,
rotina diagnóstica e diagnóstico diferencial).

Este app não tem nenhuma navegação em comum com o `app.py` da raiz do
repositório (calculadora de prognóstico de TMO) - são duas ferramentas
independentes no mesmo repositório.

## Como rodar

```bash
pip install -r requirements.txt
streamlit run mchat_app/app.py --server.port 8502
```

Use uma porta diferente (`8502`) da calculadora de TMO (`8501`) caso queira
rodar as duas ao mesmo tempo.

## Estrutura

```
mchat_app/
  app.py                    # entrypoint (fluxo: intro -> screening -> followup? -> result)
  content/
    items.py                # os 20 itens do M-CHAT-R + roteiro da consulta de seguimento
    risk_guidance.py         # orientação clínica estruturada por faixa de risco
    attribution.py           # citação/licença do instrumento + disclaimer clínico
  logic/
    scoring.py                # funções puras de cálculo de escore e classificação
  ui/
    screening.py, followup.py, results.py
  assets/
    MCHATR_F_Brazilian_Portuguese_v2.pdf   # documento original (fonte de verdade)
  scripts/
    extract_pdf.py            # script de desenvolvimento (não usado em runtime)
  tests/
    test_scoring.py
```

## Sobre o `pypdf` e `scripts/extract_pdf.py`

`pypdf` é usado apenas para reexecutar `scripts/extract_pdf.py`, que extrai
o texto bruto do PDF oficial durante o desenvolvimento (para conferência
manual contra o conteúdo transcrito em `content/items.py`). Não é
necessário para rodar o app em produção.

## Fidelidade clínica

- Os 20 itens e o roteiro da consulta de seguimento são reproduzidos
  literalmente do documento oficial (© 2009 Robins, Fein, & Barton;
  tradução: Losapio, Siquara, Lampreia, Lázaro, & Pondé), sem modificação
  de itens, instruções ou ordem, conforme os termos de uso do instrumento.
- A consulta de seguimento é conduzida pelo profissional: o app apresenta
  o roteiro/exemplos de cada item em risco, mas o resultado final
  (PASSOU/FALHOU) é registrado pelo profissional com base em seu
  julgamento clínico - fiel ao uso pretendido do instrumento, que já
  orienta o entrevistador a julgar respostas ambíguas.
- A orientação clínica (encaminhamento, avaliações, rotina terapêutica,
  diferencial) é conteúdo complementar elaborado pela equipe, não faz
  parte do instrumento oficial, e é rotulada como tal na tela de
  resultado.
- Esta ferramenta é um instrumento de apoio à decisão clínica e não
  substitui avaliação, diagnóstico ou julgamento de profissional de saúde
  qualificado.
- O documento original apresenta o roteiro da consulta de seguimento como
  fluxograma (caixas e setas); a extração de texto do PDF linearizou esse
  layout. As perguntas e exemplos de cada item foram conferidos
  literalmente contra o PDF; a lógica de encadeamento entre eles (ordem
  das perguntas condicionais) foi revisada item a item, mas recomenda-se
  que um profissional confira o roteiro de cada item em risco contra o
  PDF original (`assets/`) durante a consulta de seguimento.
