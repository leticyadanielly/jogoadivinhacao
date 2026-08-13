# Autor: Leticya Danielly
# Data : 12/08/2026
### Testes para o nível 1 do jogo ###

import pytest
from pages.base_game import BaseGamePage

@pytest.mark.nivel1
def test_palpite_menor_que_o_secreto():
    game = BaseGamePage()
    game.numero_secreto = 50
    resultado = game.validar_palpite(20)

    assert resultado == "MAIOR"
    assert game.tentativas == 1
    assert game.acertou is False


@pytest.mark.nivel1
def test_palpite_maior_que_o_secreto():
    game = BaseGamePage()
    game.numero_secreto = 50
    resultado = game.validar_palpite(80)

    assert resultado == "MENOR"
    assert game.tentativas == 1
    assert game.acertou is False


@pytest.mark.nivel1
def test_vitoria_no_palpite_correto():
    game = BaseGamePage()
    game.numero_secreto = 42
    resultado = game.validar_palpite(42)

    assert resultado == "ACERTOU"
    assert game.tentativas == 1
    assert game.acertou is True