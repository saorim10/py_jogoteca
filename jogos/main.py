from jogos import jogo_acerte_o_numero, jogo_par_impar, jogo_pedra_papel_tesoura, jogo_forca
from my_tools import *


# from flask import Flask
#
# app = Flask(__name__)
# app.secret_key = 'sis'
#
#
# if __name__ == '__main__':
#     app.run(debug=True)


escolha = 9
while escolha != 0:
    print()
    print('JOGOTECA')
    print('========')
    print()
    ok = False
    print('(1) - Adivinhar o Número')
    print('(2) - Par ou Ímpar')
    print('(3) - Pedra Papel Tesoura')
    print('(4) - Forca')
    print('(0) - Sair')
    print()
    while not ok:
        escolha = input('Ecolha um jogo -> ').strip()
        if verifica_numero(escolha, 0, 4):
            escolha = int(escolha)
            ok = True
    if escolha == 1:
        jogo_acerte_o_numero.jogar()
    if escolha == 2:
        jogo_par_impar.jogar()
    if escolha == 3:
        jogo_pedra_papel_tesoura.jogar()
    if escolha == 4:
        jogo_forca.jogar()

print('fim')
