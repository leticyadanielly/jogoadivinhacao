# Autor: Leticya Danielly
# Data : 12/08/2026
### Testes para o nível 2 do jogo ###

import pytest
from pages.difficulty_game import DifficultyGamePage

@pytest.mark.nivel2
def test_configuracao_de_dificuldades():
    facil = DifficultyGamePage(opcao_dificuldade="1")
    medio = DifficultyGamePage(opcao_dificuldade="2")
    dificil = DifficultyGamePage(opcao_dificuldade="3")

    assert facil.limite_tentativas == 10
    assert medio.limite_tentativas == 7
    assert dificil.limite_tentativas == 5


@pytest.mark.nivel2
def test_decremento_de_tentativas_restantes():
    game = DifficultyGamePage(opcao_dificuldade="3")
    game.numero_secreto = 50

    game.validar_palpite(10)
    game.validar_palpite(20)

    assert game.tentativas == 2
    assert game.tentativas_restantes() == 3


@pytest.mark.nivel2
def test_game_over_por_tentativas_esgotadas():
    game = DifficultyGamePage(opcao_dificuldade="3")
    game.numero_secreto = 50

    for _ in range(5):
        game.validar_palpite(10)

    assert game.tentativas_restantes() == 0
    assert game.jogo_ativo() is False
    assert game.acertou is False