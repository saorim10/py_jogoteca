import random
import MySQLdb

conn = MySQLdb.connect(user='root', passwd='root', db='forca', host='localhost', port=3306)
cursor = conn.cursor()


def retorna_escolhida():
    cursor.execute('SELECT word, hint FROM palavras')
    lista = list(cursor.fetchall())
    escolhida = random.randint(0, (len(lista)-1))
    palavra_escolhida = lista[escolhida][0]
    dica_escolhida = lista[escolhida][1]
    return palavra_escolhida, dica_escolhida


def mostra_letra_certa(i, palavra, chute, acerto):
    for letra in palavra:
        if chute == letra:
            acerto[i] = letra
        i += 1


def inclui_palavra(palavra, dica):
    palavra = palavra.strip().upper()
    dica = dica.upper()
    sql = "INSERT INTO palavras (word, hint) VALUES (%s, %s)"
    valores = (palavra, dica)
    cursor.execute(sql, valores)
    conn.commit()


def fechar_conexoes():
    cursor.close()
    conn.close()


def verifica_numero(numero, menor, maior):
    if not numero.isnumeric():
        return False
    else:
        numero = int(numero)
        menor = int(menor)
        maior = int(maior)
        if menor <= numero <= maior:
            return True


def carta_ppt(num):
    num = int(num)
    if num == 1:
        return 'Pedra'
    elif num == 2:
        return 'Papel'
    elif num == 3:
        return 'Tesoura'


def ganhou(usuario, maquina):
    if usuario == maquina:
        return 'Empatou'
    elif usuario == 'Pedra' and maquina == 'Papel':
        return 'Ganhei'
    elif usuario == 'Pedra' and maquina == 'Tesoura':
        return 'Ganhou'
    elif usuario == 'Papel' and maquina == 'Tesoura':
        return 'Ganhei'
    elif usuario == 'Papel' and maquina == 'Pedra':
        return 'Ganhou'
    elif usuario == 'Tesoura' and maquina == 'Pedra':
        return 'Ganhei'
    elif usuario == 'Tesoura' and maquina == 'Papel':
        return 'Ganhou'

# inclui_palavra('dicionario', 'livro')
