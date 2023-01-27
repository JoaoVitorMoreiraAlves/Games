from time import sleep
from os import system, name

#Funções
def cor():
    return [{"jogador":"\033[35mJogador 1\033[m","simbolo":"\033[35mX\033[m"}, {"jogador2":"\033[36mJogador 2\033[m","simbolo":"\033[36mO\033[m"}]

def enunciado(msg):
    print(f'***************************************************\n**{msg}**\n***************************************************')

def linha_dupla(msg):
    print('-'*55)
    print(msg)
    print('-'*55)

def valida_opcao(entrada):
    while True:
        try:
            num = int(input(entrada))
        except (ValueError, TypeError):
            linha_dupla('Valor informado errado!! Digite um número entre 1 e 2')
        except KeyboardInterrupt:
            print('\n')
            linha_dupla('\033[33mUsuário está finalizando o programa...\033[m\nVolte sempre!!!')
            sleep(5)
            exit()
        except:
            linha_dupla('Erro!! Digite um número entre 1 e 2')
        else:
            if num < 1 or num > 2:
                linha_dupla('Valor digitado inválido!! Por favor informe um valor entre 1 e 2!!!')
            else:
                return num

def par_ou_impar(rodada):
    return True if rodada % 2 != 0 else False

def limpar_tela():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def regras():
    limpar_tela()
    print('*'*130)
    print('''** Dois jogadores, um com o simbolo (X) e o outro com o simbolo (O).                                                            **
** O jogador que conseguir completar o seu simbolo em 3 casas seguidas seja na horizontal, diagonal ou vertical vence a partida.**
** Caso todas as casas sejam preenchidas e nenhum jogador tiver ganho, o jogo automaticamente da Velha!!                         **
** Boa sorte e Bom Jogo                                                                                                         **''')
    print('*'*130)

def menu(tabuleiro):
    print(f"""
          {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}
        ----|---|----
          {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}
        ----|---|----
          {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}
        """)

def pode_jogar(num):
    validacao = True
    while validacao:
        #Validação do valor da lista, precisa ser entre 1 e 9
        try: 
            entrada = int(input(num))
        except(TypeError,ValueError):
            linha_dupla("\033[31mErro!!!! Por favor informe entre 1 e 9\033[m")
        except KeyboardInterrupt:
            print('\n')
            linha_dupla("\033[33mUsuário está finalizando o programa...\033[m")
            sleep(5)
            exit()
        except:
            linha_dupla("\033[31mErro!!!! Por favor informe entre 1 e 9\033[m")
        else:
            if entrada < 1 or entrada > 9:
                linha_dupla("\033[31mErro!!!! Por favor informe entre 1 e 9\033[m")
            else:
                return entrada

def pode_alocar(jogadores,vez,tabuleiro,num):
    if 'X' in tabuleiro[num-1] or 'O' in tabuleiro[num-1]:
        linha_dupla("\033[31mErro!!!! Por favor informe uma casa que não tenha sido jogada!!!\033[m")
        pode_alocar(jogadores,vez, tabuleiro, pode_jogar('Onde Deseja Jogar?: '))
    else:
        tabuleiro[num-1] = vez

def ganhou(tabuleiro,vez):
    if vez in tabuleiro[0] and vez in tabuleiro[1] and vez in tabuleiro[2] or vez in tabuleiro[3] and vez in tabuleiro[4] and vez in tabuleiro[5] or vez in tabuleiro[6] and vez in tabuleiro[7] and vez in tabuleiro[8] or vez in tabuleiro[0] and vez in tabuleiro[4] and vez in tabuleiro[8] or vez in tabuleiro[2] and vez in tabuleiro[4] and vez in tabuleiro[6] or vez in tabuleiro[0] and vez in tabuleiro[3] and vez in tabuleiro[6] or vez in tabuleiro[1] and vez in tabuleiro[4] and vez in tabuleiro[7] or vez in tabuleiro[2] and vez in tabuleiro[5] and vez in tabuleiro[8]:
        if "\033[35mX\033[m" in vez: 
            return 1
        else:
            return 2

def jogo():
    jogadores = cor()
    rodada = 1
    tabuleiro = [f'{i}' for i in range(1,10)]
    win = 0
    while True:
        vez = '\033[35mX\033[m' if par_ou_impar(rodada) == True else '\033[36mO\033[m'
        menu(tabuleiro)
        if par_ou_impar(rodada):
            print(f'Rodada {rodada} vez do jogador {jogadores[0]["jogador"]} de simbolo {jogadores[0]["simbolo"]}')
        else:
            print(f'Rodada {rodada} vez do jogador {jogadores[1]["jogador2"]} de simbolo {jogadores[1]["simbolo"]}')
        pode_alocar(jogadores,vez, tabuleiro, pode_jogar('Onde Deseja Jogar?: '))
        rodada +=1
        if rodada > 4:
            win = ganhou(tabuleiro,vez)
            if win == 1:
                menu(tabuleiro)
                linha_dupla(f'Parabéns o {jogadores[0]["jogador"]} do símbolo {vez} GANHOU!!!!')
                placar[0] += 1
                sleep(2)
                break
            elif win == 2:
                menu(tabuleiro)
                linha_dupla(f'Parabéns o {jogadores[1]["jogador2"]} do símbolo {vez} GANHOU!!!!')
                placar[1] += 1
                sleep(2)
                break
            if rodada == 10:
                menu(tabuleiro)
                print('\033[31mO jogo deu velha pois nenhum dos dois jogadores conseguiu vencer!!!\033[m')
                sleep(2)
                break

#Código Principal
enunciado('Bem Vindo Ao Player VS Player do Jogo da Velha!')
opcao = valida_opcao('Deseja Ver as Regras?\n[1] = Sim\n[2] = Não\nO que deseja?: ')
if opcao == 1:
    regras()
    sleep(20)
placar = [0,0]
while True:
    limpar_tela()
    opcao = valida_opcao('Deseja sair do jogo da Velha?\n[1] Sair\n[2] Continuar\nO que deseja?: ')
    if opcao == 1:
        break
    linha_dupla(f'                O placar está {placar[0]} a {placar[1]}')
    jogo()