import random
from my_tools import verifica_numero, carta_ppt, ganhou


def jogar():
    print()
    print('JOGO PEDRA PAPEL TESOURA')
    print('========================')
    print('Boa Sorte ;)')
    print()
    controle = False

    while not controle:
        secreto = random.randint(1, 3)
        entrada = False
        print()
        print('Faça sua escolha')
        while not entrada:
            escolha = input('(0) Sair!   (1) Pedra   (2) Papel   (3) Tesoura -> ')
            if verifica_numero(escolha, 0, 3):
                entrada = True
            else:
                print('Entrada inválida!!!')
        if int(escolha) == 0:
            controle = True
            break
        print(f'Sua   escolha foi {carta_ppt(escolha)}.')
        print(f'Minha escolha foi {carta_ppt(secreto)}.')
        print(ganhou(carta_ppt(escolha), carta_ppt(secreto)))
