from my_tools import retorna_escolhida, mostra_letra_certa, fechar_conexoes


def jogar():
    escolhida = retorna_escolhida()
    palavra = escolhida[0]
    dica = escolhida[1]
    chutes = []
    acertos = ['_' for _ in palavra]
    tentativas = 1
    total_tentativas = 5
    controle = False
    pontos = 0

    print()
    print('JOGO DA FORCA')
    print('=============')
    print('Três letras certas, eu te dou a dica ;)')
    print()
    nome = input('Seja bem vindo. Qual o seu nome? ')
    while not controle:
        letras_certas = len(palavra) - acertos.count('_')
        print()
        print(f'Tentativa: {tentativas}/{total_tentativas}')
        print(acertos)
        if letras_certas >= 3:
            print(f'Dica: {dica}')
        print(f'Seus chutes foram: {chutes}')
        chute = input('Digite uma letra: ').strip().upper()

        if chute in chutes:
            print("Ops! Você já tentou esta :)")
            continue
        else:
            if chute in palavra:
                print('Acertou')
                mostra_letra_certa(0, palavra, chute, acertos)
                pontos += acertos.count(chute) * 5
                if acertos.count('_') == 0:
                    print(f' \o/  Você ganhou o jogo. A palavra secreta era {palavra}. Parabéns!!')
                    controle = True
            else:
                print('Errou!')
                if pontos <= 0:
                    pontos -= 10
                tentativas += 1
                if tentativas > total_tentativas:
                    print(f':(  Você foi enforcado!!! A palavra secreta era {palavra}.')
                    controle = True
            chutes.append(chute)
    print(f'{nome}, seus pontos foram {pontos}')
    print()
    print('Acabou!')
    print('=======')

    # fechar_conexoes()
