# Autor: Leticya Danielly
# Data : 12/08/2026
### Gerencia o estado do jogo e as validações do palpite ###

import random

class BaseGamePage:
    def __init__(self, min_val=1, max_val=100):
        self.min_val = min_val
        self.max_val = max_val
        self.numero_secreto = random.randint(min_val, max_val)
        self.tentativas = 0
        self.acertou = False

    def validar_palpite(self, chute: int) -> str:
        """Processa o palpite e retorna o estado ("MAIOR", "MENOR", "ACERTOU")."""
        self.tentativas += 1
        if chute == self.numero_secreto:
            self.acertou = True
            return "ACERTOU"
        elif chute < self.numero_secreto:
            return "MAIOR"
        else:
            return "MENOR"
