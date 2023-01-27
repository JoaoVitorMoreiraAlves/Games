import os
def iniciacao():
    linha("BEM VINDO AO JOGO DA VELHA")


def regras(opcao):
    """
    Funcao que serve para apresentar as regras do jogo da velha
    """
    from time import sleep
    validacao = True
    while validacao:
        try:
            entrada = str(input(opcao)).upper()[0]
        except (TypeError,ValueError):
            print("\033[31mErro!!!! Por favor informe entre S ou  N\033[m")
        except KeyboardInterrupt:
            print("\n\033[33mUsuário está finalizando o programa...\033[m")
            break
        except:
            print("\033[31mErro!!!! Por favor informe entre S ou  N\033[m")
        else:
            if entrada == "S":
                os.system('cls')
                print("""
    \033[33mAs Regras do jogo da velha se consiste em jogadas por turno, cada jogador joga um turno e temos dois jogadores, o jogador 1 utiliza 'X' enquanto o jogador 2 utiliza 'O'
    Para ganhar a partida o jogador deve colocar o seu simbolo em uma linha nas posições horizontal, vertical ou diagonal.
    por exemplo:
    X                                                                  
    X
    X  <-- Em Coluna (ou) Em Linha -->  X  X  X  
    (ou) Em Diagonal -->    X
                                X                                     
                                    X
    Caso todas as opções tenham sido escolhidas e nenhum jogador tenha completo uma linha horizontal, vertical ou diagonal o jogo termina em empate\033[m""")
                sleep(20)
                validacao = False
            elif entrada == "N":
                validacao = False
            else:
                print("\033[31mErro!!!! Por favor informe entre S ou  N\033[m")


def linha(msg):
    print("="*30)
    print(f"{msg}")
    print("="*30)


def linhasolo():
    print("="*55)


def menu(jogo):
    os.system('cls')
    print(f"""
          {jogo[0]} | {jogo[1]} | {jogo[2]}
        ----|---|----
          {jogo[3]} | {jogo[4]} | {jogo[5]}
        ----|---|----
          {jogo[6]} | {jogo[7]} | {jogo[8]}
        """)


def alocacao(num):
    validacao = True
    while validacao:
        #Validação do valor da lista, precisa ser entre 1 e 9
        try: 
            entrada = int(input(num))
            while entrada < 1 or entrada > 9:
                print("\033[31mErro!!!! Por favor informe entre 1 e 9\033[m")
                entrada = int(input(num))
        except(TypeError,ValueError):
            print("\033[31mErro!!!! Por favor informe entre 1 e 9\033[m")
        except KeyboardInterrupt:
            print("\n\033[33mUsuário está finalizando o programa...\033[m")
            break
        except:
            print("\033[31mErro!!!! Por favor informe entre 1 e 9\033[m")
        else:
            return entrada


def jogou(lst,num,vez):
    if vez == 0:
        lst[num-1] = "\033[35mX\033[m"
    elif vez == 1:
        lst[num-1] = "\033[36mO\033[m"


def ganhou(lst):
    #Validação se após a jogada algum jogador ganhou ou não
    #Validação de Linhas
    if (lst[0] == "\033[35mX\033[m" and lst[1] == "\033[35mX\033[m" and lst[2] == "\033[35mX\033[m") or (lst[3] == "\033[35mX\033[m" and lst[4] == "\033[35mX\033[m" and lst[5] == "\033[35mX\033[m") or (lst[6] == "\033[35mX\033[m" and lst[7] == "\033[35mX\033[m" and lst[8] == "\033[35mX\033[m"):
        return 1
    elif (lst[0] == "\033[36mO\033[m" and lst[1] == "\033[36mO\033[m" and lst[2] == "\033[36mO\033[m") or (lst[3] == "\033[36mO\033[m" and lst[4] == "\033[36mO\033[m" and lst[5] == "\033[36mO\033[m") or (lst[6] == "\033[36mO\033[m" and lst[7] == "\033[36mO\033[m" and lst[8] == "\033[36mO\033[m"):
        return 2
    
    #Validação de coluna
    elif (lst[0] == "\033[35mX\033[m" and lst[3] == "\033[35mX\033[m" and lst[6] == "\033[35mX\033[m") or (lst[1] == "\033[35mX\033[m" and lst[4] == "\033[35mX\033[m" and lst[7] == "\033[35mX\033[m") or (lst[2] == "\033[35mX\033[m" and lst[5] == "\033[35mX\033[m" and lst[8] == "\033[35mX\033[m"):
        return 1
    elif (lst[0] == "\033[36mO\033[m" and lst[3] == "\033[36mO\033[m" and lst[6] == "\033[36mO\033[m") or (lst[1] == "\033[36mO\033[m" and lst[4] == "\033[36mO\033[m" and lst[7] == "\033[36mO\033[m") or (lst[2] == "\033[36mO\033[m" and lst[5] == "\033[36mO\033[m" and lst[8] == "\033[36mO\033[m"):
        return 2
        
    #Validação de Diagonal
    elif (lst[0] == "\033[35mX\033[m" and lst[4] == "\033[35mX\033[m" and lst[8] == "\033[35mX\033[m") or (lst[2] == "\033[35mX\033[m" and lst[4] == "\033[35mX\033[m" and lst[6] == "\033[35mX\033[m"):
        return 1
    elif (lst[0] == "\033[36mO\033[m" and lst[4] == "\033[36mO\033[m" and lst[8] == "\033[36mO\033[m") or (lst[2] == "\033[36mO\033[m" and lst[4] == "\033[36mO\033[m" and lst[6] == "\033[36mO\033[m"):
        return 2
    else:
        return 0


def valida(lst,num):
    #Valida se o número informado pelo jogador ja foi utilizado ou não
    if "\033[35mX\033[m" in lst[num-1] or "O" in lst[num-1]:
        print("\033[31mERRO!! O número que você digitou ja foi jogado escolha uma casa vazia!\033[m")
        return True
    return False