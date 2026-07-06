# -*- coding: utf-8 -*-
"""Conteúdo literal do M-CHAT-R/F (versão em português brasileiro).

Texto transcrito de: M-CHAT-R/F™ © 2009 Robins, Fein, & Barton.
Tradução: Losapio, Siquara, Lampreia, Lázaro, & Pondé.
Fonte: mchatscreen.com (arquivo original em mchat_app/assets/).

Conforme os termos de uso do instrumento, os itens e a ordem dos itens
não devem ser modificados. O texto abaixo reproduz o M-CHAT-R (primeira
etapa, 20 itens) e o roteiro da consulta de seguimento (M-CHAT-R/F,
segunda etapa) tal como no documento oficial.
"""

from dataclasses import dataclass, field
from typing import Literal

RiskAnswer = Literal["Sim", "Não"]


@dataclass(frozen=True)
class FollowUpGuidance:
    """Roteiro literal da entrevista de consulta de seguimento para um item.

    A consulta de seguimento é conduzida pelo profissional, que segue o
    fluxograma original e registra o resultado final (PASSOU/FALHOU) com
    base em seu julgamento clínico - o próprio manual do M-CHAT-R/F
    orienta o entrevistador a julgar respostas ambíguas ("talvez", "outro").
    """

    intro: str
    steps: tuple[str, ...]
    scoring_note: str


@dataclass(frozen=True)
class MchatItem:
    id: int
    text: str
    risk_answer: RiskAnswer
    is_reverse_scored: bool
    followup: FollowUpGuidance


MCHAT_ITEMS: tuple[MchatItem, ...] = (
    MchatItem(
        id=1,
        text=(
            "Se você apontar para algum objeto no quarto, o seu filho olha "
            "para este objeto? (POR EXEMPLO, se você apontar para um "
            "brinquedo ou animal, o seu filho olha para o brinquedo ou "
            "para o animal?)"
        ),
        risk_answer="Não",
        is_reverse_scored=False,
        followup=FollowUpGuidance(
            intro="Por favor, me dê um exemplo de como ele responde se você apontar para algo.",
            steps=(
                "Exemplos de PASSOU: olha para o objeto; aponta para o objeto; "
                "olha e comenta sobre o objeto; olha quando o genitor aponta e diz \"olhe!\".",
                "Exemplos de FALHOU: ele/ela ignora você; olha ao redor do quarto sem "
                "fixar nenhum objeto; olha para o dedo do genitor (em vez do objeto).",
                "Se houver exemplos de ambos os tipos, pergunte qual ocorre com mais frequência.",
            ),
            scoring_note="PASSOU se o comportamento mais frequente corresponder aos exemplos de PASSOU; caso contrário, FALHOU.",
        ),
    ),
    MchatItem(
        id=2,
        text="Alguma vez você se perguntou se o seu filho pode ser surdo?",
        risk_answer="Sim",
        is_reverse_scored=True,
        followup=FollowUpGuidance(
            intro="Você informou que já se perguntou se o seu filho pode ser surdo. O que o levou a esse pensamento?",
            steps=(
                "Pergunte: ele ou ela com frequência ignora sons?",
                "Pergunte: ele ou ela com frequência ignora as pessoas?",
                "Pergunte a todas as crianças (não altera a pontuação, mas deve ser registrado): "
                "o seu filho fez exame auditivo? Quais os resultados (audição na faixa normal / "
                "audição abaixo do normal / resultados não conclusivos)?",
            ),
            scoring_note="FALHOU se a resposta for \"Sim\" para qualquer uma das duas perguntas acima; PASSOU se \"Não\" para ambas.",
        ),
    ),
    MchatItem(
        id=3,
        text=(
            "O seu filho brinca de faz de contas? (POR EXEMPLO, faz de conta "
            "que bebe em um copo vazio, faz de conta que fala ao telefone, "
            "faz de conta que dá comida a uma boneca ou a um bichinho de "
            "pelúcia?)"
        ),
        risk_answer="Não",
        is_reverse_scored=False,
        followup=FollowUpGuidance(
            intro="Por favor, me dê um exemplo de uma das brincadeiras de faz de contas do seu filho.",
            steps=(
                "O seu filho alguma vez: fez de conta que bebia em uma xícara de brinquedo? "
                "fez de conta que comia com colher/garfo de brinquedo? fez de conta que falava "
                "no telefone? fez de conta que dava comida a uma boneca ou bichinho de pelúcia? "
                "brincou de empurrar um carro de brinquedo como se andasse em uma estrada? fez "
                "de conta que era um robô, avião, bailarina ou outro personagem favorito? colocou "
                "uma panela de brinquedo em um fogão de brinquedo? mexeu uma comida de mentirinha? "
                "colocou um boneco dentro de um carro/caminhão como motorista ou passageiro? fez "
                "de conta que aspirava o tapete, varria o chão ou cortava a grama? outro "
                "comportamento de faz de conta (descrever)?",
            ),
            scoring_note="PASSOU se \"Sim\" para qualquer exemplo; FALHOU se \"Não\" para todos.",
        ),
    ),
    MchatItem(
        id=4,
        text=(
            "O seu filho gosta de subir nas coisas? (POR EXEMPLO, móveis, "
            "brinquedos em parques ou escadas)"
        ),
        risk_answer="Não",
        is_reverse_scored=False,
        followup=FollowUpGuidance(
            intro="Por favor, dê um exemplo de alguma coisa na qual ele goste de subir.",
            steps=(
                "Ele gosta de subir em: escadas? cadeiras? móveis? brinquedos em parques?",
            ),
            scoring_note="PASSOU se \"Sim\" para qualquer um; FALHOU se \"Não\" para todos.",
        ),
    ),
    MchatItem(
        id=5,
        text=(
            "O seu filho faz movimentos estranhos com os dedos perto dos "
            "olhos? (POR EXEMPLO, mexe os dedos em frente aos olhos e fica "
            "olhando para os mesmos?)"
        ),
        risk_answer="Sim",
        is_reverse_scored=True,
        followup=FollowUpGuidance(
            intro="Por favor, descreva esses movimentos.",
            steps=(
                "Exemplos que NÃO indicam risco: olha para as mãos? move os dedos quando "
                "brinca de mostrar e esconder o rosto?",
                "Exemplos que indicam risco: movimenta os dedos perto dos olhos? mantém as mãos "
                "elevadas perto dos olhos? mantém as mãos ao lado dos olhos? agita as mãos perto "
                "do rosto? outro (descrever)?",
                "Se houver \"Sim\" para algum exemplo de risco, pergunte: isso acontece mais de "
                "duas vezes por semana?",
            ),
            scoring_note="FALHOU somente se houver exemplo de risco E ocorrer mais de duas vezes por semana; caso contrário, PASSOU.",
        ),
    ),
    MchatItem(
        id=6,
        text=(
            "O seu filho aponta com o dedo para pedir algo ou para conseguir "
            "ajuda? (POR EXEMPLO, aponta para um biscoito ou brinquedo fora "
            "do alcance dele?)"
        ),
        risk_answer="Não",
        is_reverse_scored=False,
        followup=FollowUpGuidance(
            intro="Se seu filho quer algo que está fora do alcance dele, o que ele faz para conseguir pegar?",
            steps=(
                "Ele: tenta alcançar o objeto com a mão? leva você até o objeto? tenta pegar o "
                "objeto sozinho? pede usando palavras ou sons?",
                "Se \"Não\" para todos os exemplos acima, pergunte: se você disser a ele \"me "
                "mostre\", ele aponta para o objeto?",
            ),
            scoring_note="PASSOU se \"Sim\" para qualquer exemplo, ou se apontar quando pedem \"me mostre\"; caso contrário, FALHOU.",
        ),
    ),
    MchatItem(
        id=7,
        text=(
            "O seu filho aponta com o dedo para mostrar algo interessante "
            "para você? (POR EXEMPLO, aponta para um avião no céu ou um "
            "caminhão grande na rua)"
        ),
        risk_answer="Não",
        is_reverse_scored=False,
        followup=FollowUpGuidance(
            intro=(
                "Acabamos de falar sobre o apontar para pedir algo. Mas, e para mostrar algo "
                "interessante para você, ele aponta com o dedo?"
            ),
            steps=(
                "Se \"Sim\": peça um exemplo (um avião no céu? um caminhão na rua? um bicho no "
                "chão? um animal no quintal?) e pergunte se ele aponta para mostrar interesse ou "
                "só para pedir ajuda.",
                "Se \"Não\": pergunte se o seu filho alguma vez já quis que você olhasse para "
                "algo interessante, usando os mesmos exemplos.",
            ),
            scoring_note=(
                "PASSOU se ele aponta (mesmo que às vezes também para pedir ajuda) para "
                "mostrar interesse em algo; FALHOU se aponta somente para pedir ajuda, ou se "
                "\"Não\" para todos os exemplos."
            ),
        ),
    ),
    MchatItem(
        id=8,
        text=(
            "O seu filho se interessa por outras crianças? (POR EXEMPLO, seu "
            "filho olha para outras crianças, sorri para elas ou se aproxima "
            "delas?)"
        ),
        risk_answer="Não",
        is_reverse_scored=False,
        followup=FollowUpGuidance(
            intro="Ele se interessa por crianças que não são irmãos dele?",
            steps=(
                "Quando vocês estão na pracinha ou no supermercado, seu filho geralmente reage "
                "a outras crianças?",
                "Como ele reage: brinca com outra criança? fala com outra criança? balbucia ou "
                "faz barulhos com a boca? olha para outra criança? sorri para outra criança? "
                "primeiro fica tímido, mas depois sorri? fica animado com a outra criança?",
                "Se \"Sim\" para qualquer exemplo, pergunte: ele reage a outras crianças mais "
                "da metade das vezes?",
            ),
            scoring_note="FALHOU se \"Não\" para todos os exemplos, ou se reage a outras crianças em menos da metade das vezes; caso contrário, PASSOU.",
        ),
    ),
    MchatItem(
        id=9,
        text=(
            "O seu filho traz coisas para mostrar para você ou as segura "
            "para que você as veja - não para conseguir ajuda, mas apenas "
            "para compartilhar? (POR EXEMPLO, para mostrar uma flor, um "
            "bichinho de pelúcia ou um caminhão de brinquedo)"
        ),
        risk_answer="Não",
        is_reverse_scored=False,
        followup=FollowUpGuidance(
            intro="Por favor, dê um exemplo de algo que ele pode trazer para mostrar para você ou segurar para que você veja.",
            steps=(
                "Seu filho às vezes traz para você: uma figura ou brinquedo para mostrar? um "
                "desenho que ele fez? uma flor que ele pegou? um bichinho que ele encontrou no "
                "chão? algumas peças que ele juntou? outro (descrever)?",
                "Se \"Sim\" para qualquer exemplo, pergunte: isso é só para mostrar a você e não "
                "para pedir ajuda?",
            ),
            scoring_note="PASSOU se \"Sim\" para algum exemplo E for apenas para compartilhar (não para pedir ajuda); FALHOU nos demais casos.",
        ),
    ),
    MchatItem(
        id=10,
        text=(
            "O seu filho responde quando você o chama pelo nome? (POR "
            "EXEMPLO, ele olha para você, fala ou emite algum som, ou para o "
            "que está fazendo quando você o chama pelo nome?)"
        ),
        risk_answer="Não",
        is_reverse_scored=False,
        followup=FollowUpGuidance(
            intro=(
                "Por favor, dê um exemplo de como ele responde quando você o chama pelo nome. "
                "Se ele não estiver ocupado com algo divertido ou interessante, o que ele faz "
                "quando você o chama pelo nome?"
            ),
            steps=(
                "Respostas de PASSOU: procura? fala ou emite algum som? para o que está fazendo?",
                "Respostas de FALHOU: não dá nenhuma resposta? parece ouvir mas ignora a "
                "pessoa? só responde se a pessoa estiver bem na sua frente? só responde se for "
                "tocado?",
                "Se houver respostas de ambos os tipos, pergunte qual ele faz com mais frequência.",
            ),
            scoring_note="PASSOU se só houver respostas de PASSOU, ou se estas forem as mais frequentes; FALHOU nos demais casos.",
        ),
    ),
    MchatItem(
        id=11,
        text="Quando você sorri para o seu filho, ele sorri de volta para você?",
        risk_answer="Não",
        is_reverse_scored=False,
        followup=FollowUpGuidance(
            intro="O que faz o seu filho sorrir?",
            steps=(
                "Exemplos de PASSOU (sorriso social/recíproco): sorri quando você sorri? sorri "
                "quando você entra no quarto? sorri quando você volta depois de ter estado fora "
                "de casa?",
                "Exemplos de FALHOU (sorriso não dirigido a você): está sempre sorrindo? sorri "
                "para um brinquedo ou atividade favorita? sorri ao acaso ou sem nenhum motivo "
                "especial?",
                "Se houver exemplos de ambos os tipos, pergunte qual ele faz com mais frequência.",
            ),
            scoring_note="PASSOU se só houver (ou predominarem) exemplos de PASSOU; FALHOU se só houver (ou predominarem) exemplos de FALHOU.",
        ),
    ),
    MchatItem(
        id=12,
        text=(
            "O seu filho fica muito incomodado com barulhos do dia a dia? "
            "(POR EXEMPLO, seu filho grita ou chora ao ouvir barulhos como "
            "os de liquidificador ou de música alta?)"
        ),
        risk_answer="Sim",
        is_reverse_scored=True,
        followup=FollowUpGuidance(
            intro="A criança tem uma reação negativa ao som de:",
            steps=(
                "Máquina de lavar? choro de bebês? aspirador de pó? secador de cabelo? "
                "trânsito? grito de bebês? música alta? toque do telefone/campainha? barulho de "
                "liquidificador? lugares barulhentos como supermercado ou restaurante? outro "
                "(descrever)?",
                "Se \"Sim\" para menos de dois desses sons, considere PASSOU diretamente. Se "
                "\"Sim\" para dois ou mais, pergunte como ele reage:",
                "Respostas de PASSOU: tampa os ouvidos calmamente? diz a você que não gosta de "
                "barulho?",
                "Respostas de FALHOU: grita? chora? tampa os ouvidos de forma aflita?",
                "Se houver respostas de ambos os tipos, pergunte qual ele faz mais frequentemente.",
            ),
            scoring_note="PASSOU se reagir a menos de dois sons, ou se a reação predominante for calma; FALHOU se reagir a dois ou mais sons com reação predominantemente aflita.",
        ),
    ),
    MchatItem(
        id=13,
        text="O seu filho anda?",
        risk_answer="Não",
        is_reverse_scored=False,
        followup=FollowUpGuidance(
            intro="Anda sem se segurar ou sem se apoiar em algo?",
            steps=(),
            scoring_note="PASSOU se \"Sim\"; FALHOU se \"Não\".",
        ),
    ),
    MchatItem(
        id=14,
        text=(
            "O seu filho olha nos seus olhos quando você está falando ou "
            "brincando com ele/ela, ou vestindo a roupa dele/dela?"
        ),
        risk_answer="Não",
        is_reverse_scored=False,
        followup=FollowUpGuidance(
            intro="Por favor, dê um exemplo de quando ele olha nos seus olhos.",
            steps=(
                "Isso ocorre: quando ele precisa de alguma coisa? quando você está brincando "
                "com ele? durante as alimentações? durante a troca das fraldas? quando você "
                "está lendo uma história para ele? quando você está falando com ele?",
                "Se \"Sim\" para apenas uma situação, pergunte: seu filho olha nos seus olhos "
                "todos os dias?",
                "Se \"Não\" para todas as situações, pergunte: nos dias em que vocês estão "
                "juntos o dia todo, ele olha nos seus olhos pelo menos 5 vezes?",
            ),
            scoring_note="PASSOU se \"Sim\" para duas ou mais situações, ou se as perguntas complementares forem respondidas \"Sim\"; FALHOU nos demais casos.",
        ),
    ),
    MchatItem(
        id=15,
        text=(
            "O seu filho tenta imitar o que você faz? (POR EXEMPLO, quando "
            "você dá tchau, ou bate palmas, ou joga um beijo, ele repete o "
            "que você faz?)"
        ),
        risk_answer="Não",
        is_reverse_scored=False,
        followup=FollowUpGuidance(
            intro="Por favor, dê um exemplo de algo que ele tenta copiar.",
            steps=(
                "O seu filho tenta lhe imitar se você: põe a língua para fora? faz um som "
                "engraçado? dá tchau? bate palmas? coloca os dedos nos lábios para sinalizar "
                "\"Xiii\"? manda um beijo? outro (descrever)?",
            ),
            scoring_note="PASSOU se \"Sim\" para dois ou mais exemplos; FALHOU se \"Sim\" para um ou nenhum.",
        ),
    ),
    MchatItem(
        id=16,
        text=(
            "Quando você vira a cabeça para olhar para alguma coisa, o seu "
            "filho olha ao redor para ver o que você está olhando?"
        ),
        risk_answer="Não",
        is_reverse_scored=False,
        followup=FollowUpGuidance(
            intro="O que ele faz quando você se vira para olhar para alguma coisa?",
            steps=(
                "Respostas de PASSOU: olha para o que você está olhando? aponta para o que "
                "você está olhando? olha ao redor para ver o que você está olhando?",
                "Respostas de FALHOU: não repara em você? olha para o seu rosto (em vez de "
                "seguir o seu olhar)?",
                "Se houver respostas de ambos os tipos, pergunte qual ele faz na maioria das vezes.",
            ),
            scoring_note="PASSOU se só houver (ou predominarem) respostas de PASSOU; FALHOU se só houver (ou predominarem) respostas de FALHOU.",
        ),
    ),
    MchatItem(
        id=17,
        text=(
            "O seu filho tenta fazer você olhar para ele/ela? (POR EXEMPLO, "
            "o seu filho olha para você para ser elogiado/aplaudido, ou diz: "
            "\"olha mãe!\" ou \"óh mãe!\")"
        ),
        risk_answer="Não",
        is_reverse_scored=False,
        followup=FollowUpGuidance(
            intro="Por favor, me dê um exemplo de como ele tenta fazer com que você olhe para ele/ela.",
            steps=(
                "Ele: diz \"Olha!\" ou \"Olha para mim!\"? emite algum som ou faz barulho para "
                "você olhar o que ele está fazendo? olha para você para ganhar elogio ou "
                "comentário? continua olhando para ver se você está olhando? outro (descrever)?",
            ),
            scoring_note="PASSOU se \"Sim\" para qualquer exemplo; FALHOU se \"Sim\" para nenhum.",
        ),
    ),
    MchatItem(
        id=18,
        text=(
            "O seu filho compreende quando você pede para ele/ela fazer "
            "alguma coisa? (POR EXEMPLO, se você não apontar, o seu filho "
            "entende quando você pede: \"coloca o copo na mesa\" ou \"liga a "
            "televisão\")?"
        ),
        risk_answer="Não",
        is_reverse_scored=False,
        followup=FollowUpGuidance(
            intro="Por favor, dê um exemplo de como ele compreendeu você.",
            steps=(
                "Se o exemplo não indicar que a criança compreende uma ordem simples sem "
                "sinais não-verbais, pergunte (até obter um \"Sim\" ou usar todos os exemplos): "
                "se você diz \"Me mostre o seu sapato\" sem apontar, gestos ou sugestões, ele "
                "mostra o sapato? se você diz \"Me traz o cobertor\" sem apontar, gestos ou "
                "sugestões, ele traz para você? se você diz \"Põe o livro na cadeira\" sem "
                "apontar, gestos ou sugestões, ele coloca o livro na cadeira?",
                "Se \"Não\" para todas, pergunte: se é hora do jantar e a comida está na mesa, "
                "e você diz ao seu filho para se sentar, ele se senta à mesa?",
            ),
            scoring_note="PASSOU se \"Sim\" para qualquer exemplo (com ou sem dica situacional); FALHOU se \"Não\" para todos.",
        ),
    ),
    MchatItem(
        id=19,
        text=(
            "Quando acontece algo novo, o seu filho olha para o seu rosto "
            "para ver como você se sente sobre o que aconteceu? (POR "
            "EXEMPLO, se ele/ela ouve um barulho estranho ou vê algo "
            "engraçado, ou vê um brinquedo novo, será que ele/ela olharia "
            "para seu rosto?)"
        ),
        risk_answer="Não",
        is_reverse_scored=False,
        followup=FollowUpGuidance(
            intro="O seu filho olha para você quando uma pessoa estranha se aproxima?",
            steps=(
                "Se o seu filho ouve um barulho estranho ou assustador, ele olha para você "
                "antes de responder?",
                "Seu filho olha para você quando ele vê algo não familiar ou que dá um pouco de medo?",
            ),
            scoring_note="PASSOU se \"Sim\" para qualquer uma das três perguntas; FALHOU se \"Não\" para todas.",
        ),
    ),
    MchatItem(
        id=20,
        text=(
            "O seu filho gosta de atividades de movimento? (POR EXEMPLO, "
            "ser balançado ou pular em seus joelhos)."
        ),
        risk_answer="Não",
        is_reverse_scored=False,
        followup=FollowUpGuidance(
            intro="Ele gosta quando alguém o faz pular ou balançar?",
            steps=(
                "Quando você balança ou joga ele para o alto, como ele reage? ri ou dá "
                "gargalhadas? fala ou emite algum som? pede mais, esticando os braços? outro "
                "(descrever)?",
            ),
            scoring_note="PASSOU se \"Sim\" para qualquer exemplo específico (ou se \"outro\" for uma resposta positiva); FALHOU se \"Não\" para todos.",
        ),
    ),
)

MCHAT_ITEMS_BY_ID: dict[int, MchatItem] = {item.id: item for item in MCHAT_ITEMS}

REVERSE_SCORED_IDS: frozenset[int] = frozenset(
    item.id for item in MCHAT_ITEMS if item.is_reverse_scored
)
