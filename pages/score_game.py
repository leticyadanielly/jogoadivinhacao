# Autor: Leticya Danielly
# Data : 12/08/2026
###  Gerencia a persistência do recorde em arquivo ###

import os
from pages.difficulty_game import DifficultyGamePage

class ScoreGamePage(DifficultyGamePage):
    def __init__(self, opcao_dificuldade: str = "2", arquivo_score="data/recorde.txt"):
        super().__init__(opcao_dificuldade)
        self.arquivo_score = arquivo_score

    def carregar_recorde(self) -> int:
        if os.path.exists(self.arquivo_score):
            with open(self.arquivo_score, "r") as f:
                try:
                    return int(f.read().strip())
                except ValueError:
                    return float("inf")
        return float("inf")

    def salvar_novo_recorde(self) -> bool:
        recorde_atual = self.carregar_recorde()
        if self.tentativas < recorde_atual:
            os.makedirs(os.path.dirname(self.arquivo_score), exist_ok=True)
            with open(self.arquivo_score, "w") as f:
                f.write(str(self.tentativas))
            return True
        return False
