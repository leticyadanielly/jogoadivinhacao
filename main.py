# Autor: Leticya Danielly
# Data : 12/08/2026
### Handles input() e print(), consumindo os objetos criados ###

from pages.score_game import ScoreGamePage

def rodar_jogo():
    print("--- JOGO DA ADIVINHAÇÃO (POM) ---")
    print("Escolha a dificuldade:\n1 - Fácil (10)\n2 - Médio (7)\n3 - Difícil (5)")
    opcao = input("Opção: ")

    game = ScoreGamePage(opcao_dificuldade=opcao)
    recorde = game.carregar_recorde()

    if recorde != float("inf"):
        print(f" Recorde atual: {recorde} tentativas")

    while game.jogo_ativo():
        print(f"\nTentativas restantes: {game.tentativas_restantes()}")
        try:
            chute = int(input("Digite seu palpite: "))
        except ValueError:
            print("Entrada inválida! Digite apenas números.")
            continue

        resultado = game.validar_palpite(chute)

        if resultado == "ACERTOU":
            print(f"\n Parabéns! Você acertou em {game.tentativas} tentativas.")
            if game.salvar_novo_recorde():
                print(" NOVO RECORDE REGISTRADO!")
            break
        elif resultado == "MAIOR":
            print(" O número secreto é MAIOR.")
        else:
            print(" O número secreto é MENOR.")

    if not game.acertou:
        print(f"\n Game Over! O número secreto era {game.numero_secreto}.")

if __name__ == "__main__":
    rodar_jogo()
