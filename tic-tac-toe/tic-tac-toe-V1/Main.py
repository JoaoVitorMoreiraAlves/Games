from funções import func
jogadas = vez = vencedor = 0
jogadores = [{"jogador":"\033[35mjogador1\033[m","jogadas":0,"simbolo":"\033[35mX\033[m"},{"jogador":"\033[36mjogador2\033[m","jogadas":0,"simbolo":"\033[36mO\033[m"}]
jogo = ["1","2","3",
        "4","5","6",
        "7","8","9"]

func.iniciacao()
opcao = func.regras("Deseja ver as regras? [S/N]: ")
func.menu(jogo)


while jogadas <= 9:
    if jogadas > 3:
        vencedor = func.ganhou(jogo)
        if vencedor == 1:
            print(f"PARABÉNS o jogador {jogadores[0]['jogador']} VENCEU")
            break
        elif vencedor == 2:
            print(f"PARABÉNS o jogador {jogadores[1]['jogador']} VENCEU")
            break
        elif jogadas == 9 and vencedor == 0:
            print("\033[33mFoi uma bela disputa, mas no final houve empate\033[m")
            break
    if jogadas == 0 or jogadas % 2 == 0:
        func.linhasolo()
        num = func.alocacao(f"Vez do jogador {jogadores[0]['jogador']}, irá jogador o {jogadores[0]['simbolo']} em qual posição?: ")
        func.linhasolo()
        vez = 0
        while func.valida(jogo,num):
            num = func.alocacao(f"Vez do jogador {jogadores[0]['jogador']}, irá jogador o {jogadores[0]['simbolo']} em qual posição?: ")
    else:
        vez = 1
        func.linhasolo()
        num = func.alocacao(f"Vez do jogador {jogadores[1]['jogador']}, irá jogador o {jogadores[1]['simbolo']} em qual posição?: ")
        func.linhasolo()
        while func.valida(jogo,num):
            num = func.alocacao(f"Vez do jogador {jogadores[1]['jogador']}, irá jogador o {jogadores[1]['simbolo']} em qual posição?: ")
    func.jogou(jogo,num,vez)
    jogadas += 1
    func.menu(jogo)