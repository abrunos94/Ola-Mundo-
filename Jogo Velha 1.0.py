tabuleiro = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"],
]

def mostrar_tabuleiro():
    for i in range(3):
        print(f" {tabuleiro[i][0]} | {tabuleiro[i][1]} | {tabuleiro[i][2]} ")
        if i < 2:
            print("---+---+---")

def verificar_vitoria(simbolo):
    # Verifica linhas
    for linha in tabuleiro:
        if all(casa == simbolo for casa in linha):
            return True
    # Verifica colunas
    for col in range(3):
        if all(tabuleiro[linha][col] == simbolo for linha in range(3)):
            return True
    # Verifica diagonais
    if all(tabuleiro[i][i] == simbolo for i in range(3)):
        return True
    if all(tabuleiro[i][2 - i] == simbolo for i in range(3)):
        return True
    return False

def jogada_valida(escolha):
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == escolha:
                return i, j
    return None

jogador_atual = "X"

for rodada in range(9):
    print(f"\nRodada {rodada + 1} - Vez do jogador {jogador_atual}")
    mostrar_tabuleiro()

    jogada = input("Escolha uma posição (1 a 9): ")
    posicao = jogada_valida(jogada)

    if posicao:
        i, j = posicao
        tabuleiro[i][j] = jogador_atual
    else:
        print("Jogada inválida! Tente novamente.")
        continue  # Repete a rodada sem trocar o jogador

    if verificar_vitoria(jogador_atual):
        mostrar_tabuleiro()
        print(f"\n🎉 Parabéns! Jogador {jogador_atual} venceu!")
        break

    # Alterna o jogador
    jogador_atual = "O" if jogador_atual == "X" else "X"
else:
    mostrar_tabuleiro()
    print("\n🤝 Empate! Ninguém venceu.")
