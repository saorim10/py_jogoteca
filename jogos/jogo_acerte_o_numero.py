import random


def jogar():
    print()
    print('JOGO ACERTE O NÚMERO')
    print('====================')
    print('O número está entre 1 e 100. Boa Sorte ;)')
    print()
    controle = False
    secreto = random.randint(1, 100)

    while not controle:
        chute = int(input('Digite um número: '))
        if chute == secreto:
            print(f'Você Acertou \o/. O número era {secreto}')
            controle = True
        elif chute < secreto:
            print('O número é MAIOR')
        else:
            print('O número é MENOR')
