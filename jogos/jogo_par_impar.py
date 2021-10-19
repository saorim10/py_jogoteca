import random


def jogar():
    print()
    print('JOGO PAR OU IMPAR')
    print('=================')
    print('Digite 0 ou 1 ou dois. Depois escolha PAR ou IMPAR. Boa Sorte ;)')
    print()

    controle = False
    numero_invalido = True
    while not controle:
        escolha = ''
        numero = 3
        secreto = random.randint(0, 2)

        while numero_invalido:
            numero = (input('[0] ou [1] ou [2]'))
            if not numero.isnumeric():
                print('Somente números!')
            else:
                numero = int(numero)
                if 0 <= numero < 3:
                    break
        while escolha != 'P' and escolha != 'I':
            escolha = input("Escolha: [P]AR ou [I]MPAR").strip().upper()

        print(f'Resultado: Total foi {numero + secreto}')

        if (numero + secreto) % 2 == 0:
            resultado = 'P'
        else:
            resultado = 'I'

        if resultado == escolha:
            print('\o/  Você ganhou')
        else:
            print('he he he   Eu ganhei')

        if input('Jogar de novo? ').strip().upper() != 'S':
            controle = True

    print()
    print('Tchau...')
