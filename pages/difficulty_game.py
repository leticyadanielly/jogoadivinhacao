# Autor: Leticya Danielly
# Data : 12/08/2026
### Herda do nível base e adiciona regras de limites de tentativas ###

from pages.base_game import BaseGamePage

class DifficultyGamePage(BaseGamePage):
    DIFICULDADES = {
        "1": {"nome": "Fácil", "limite": 10},
        "2": {"nome": "Médio", "limite": 7},
        "3": {"nome": "Difícil", "limite": 5}
    }

    def __init__(self, opcao_dificuldade: str = "2"):
        super().__init__()
        config = self.DIFICULDADES.get(opcao_dificuldade, self.DIFICULDADES["2"])
        self.limite_tentativas = config["limite"]

    def tentativas_restantes(self) -> int:
        return self.limite_tentativas - self.tentativas

    def jogo_ativo(self) -> bool:
        return not self.acertou and self.tentativas < self.limite_tentativas
