# Autor: Leticya Danielly
# Data : 12/08/2026
### Testes para o nível 3 do jogo ###

import pytest
from pages.score_game import ScoreGamePage

@pytest.mark.nivel3
def test_carregar_recorde_quando_arquivo_nao_existe(tmp_path):
    caminho_temp = str(tmp_path / "recorde.txt")
    score = ScoreGamePage(arquivo_score=caminho_temp)

    assert score.carregar_recorde() == float("inf")


@pytest.mark.nivel3
def test_salvar_primeiro_recorde(tmp_path):
    caminho_temp = str(tmp_path / "recorde.txt")
    score = ScoreGamePage(arquivo_score=caminho_temp)
    score.tentativas = 4

    sucesso = score.salvar_novo_recorde()

    assert sucesso is True
    assert score.carregar_recorde() == 4


@pytest.mark.nivel3
def test_nao_sobrescrever_recorde_com_pontuacao_pior(tmp_path):
    arquivo_temp = tmp_path / "recorde.txt"
    arquivo_temp.write_text("3")

    score = ScoreGamePage(arquivo_score=str(arquivo_temp))
    score.tentativas = 6

    sucesso = score.salvar_novo_recorde()

    assert sucesso is False
    assert score.carregar_recorde() == 3