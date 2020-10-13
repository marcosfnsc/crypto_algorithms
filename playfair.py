""" modulo playfair - contem a implementacao da cifra playfair

funcoes publicas:
 - encriptar
 - decriptar

 A implementacao da cifra é capaz de decriptar e resultar em 100$ da mensagem
 original em alguns casos ideais, mensagens que só contem letras, sem acentos,
 sem simbolos, sem digitos, e sem a letra 'x' pois essa letra é usada como flag
 e ao decriptar será removida do resutlado da decifragem.

O codigo fonte é divido em tres sessoes, a primeira contem funcoes usadas nos dois
processos da cifra, a segunda sessão é contem funcoes usadas no processo de encriptacao,
e a ultima sessão contem as funcoes usadas no processo de decriptacao
"""

import string

def _criar_tabela(chave: str) -> list:
    """retorna uma tabela 5x5 prenchida com o alfabeto, com excecao da letra j"""

    chave = _tratar_chave(chave)
    tabela = []

    while len(chave) >= 5:
        tabela.append(chave[:5])
        del(chave[:5])

    return tabela

def _tratar_chave(chave: str, alfabeto='abcdefghiklmnopqrstuvwxyz') -> list:
    """remove letras repetidas da chave e retona uma lista contendo as letras"""
    alfabeto_restante = list(alfabeto)
    letras = []
    for letra in chave:
        if letra in letras:
            continue
        elif letra != 'j':
            letras.append(letra)
            del(alfabeto_restante[alfabeto_restante.index(letra)])

    return letras + alfabeto_restante

def _obter_linha_e_coluna(elemento: str, tabela: list):
    """retorna o numero da linha e coluna de um elemento na tabela"""
    
    for x in range(len(tabela)):
        if elemento in tabela[x]:
            return x, tabela[x].index(elemento)

# ===================== encriptar =====================

def encriptar(msg: str, chave: str) -> str:
    """criptografa a mensagem usando a cifra de playfair"""

    msg = list(map(_tratar_mensagem, msg.split()))
    tabela = _criar_tabela(chave)
    msg_codificada = []

    for sub_msg in msg:
        sub_msg_code = []
        for silabas in sub_msg.split():
            sub_msg_code.append(_codificar(silabas, tabela))

        msg_codificada.append(''.join(sub_msg_code))

    return ' '.join(msg_codificada)

def _tratar_mensagem(msg: str) -> str:
    """recebe a mensagem original e separa por silabas seguindo as regras de playfair"""

    x = 0
    nova_msg = []
    while x < len(msg):
        nova_msg.append(msg[x])

        if x+1 >= len(msg):
            nova_msg.append('x')
            break

        if msg[x] == msg[x+1]:
            nova_msg.append('x')
        else:
            nova_msg.append(msg[x+1])
            x += 1

        nova_msg.append(' ')
        x += 1
    return ''.join(nova_msg)

def _codificar(pares: str, tabela: list) -> str:
    """transforma as silabas originais em silabas codificadas"""

    letra1, letra2 = list(pares)
    linha1, coluna1 = _obter_linha_e_coluna(letra1, tabela)
    linha2, coluna2 = _obter_linha_e_coluna(letra2, tabela)

    if linha1 == linha2: # quando estão na mesma linha
        if coluna1 == 4:
            letra1 = tabela[linha1][0]
        else:
            letra1 = tabela[linha1][coluna1+1]
        if coluna2 == 4:
            letra2 = tabela[linha2][0]    
        else:
            letra2 = tabela[linha2][coluna2+1]
    elif coluna1 == coluna2: # quando estão na mesma coluna
        if linha1 == 4:
            letra1 = tabela[0][coluna1]
        else:
            letra1 = tabela[linha1+1][coluna1]
        if linha2 == 4:
            letra2 = tabela[0][coluna2]
        else:
            letra2 = tabela[linha2+1][coluna2]
    
    else: # caso as linhas e colunas sejam diferentes
        letra1 = tabela[linha1][coluna2]
        letra2 = tabela[linha2][coluna1]

    return ''.join([letra1, letra2])

# ===================== decriptar =====================

def decriptar(msg: str) -> str:
    msg = list(map(_tratar_mensagem_codificada, msg.split()))
    tabela = _criar_tabela()
    msg_decodificada = []
    for x in msg:
        msg_decodificada.append(''.join(map(_decodificar, x.split())))
    
    return ' '.join(msg_decodificada).replace('x', '')

def _tratar_mensagem_codificada(msg):
    msg = list(msg)
    
    x = 0
    nova_msg = []
    while x < len(msg):
        nova_msg.append(msg[x])
        nova_msg.append(msg[x+1])
        nova_msg.append(' ')
        x += 2

    return ''.join(nova_msg).strip()

def _decodificar(pares: str):
    letra1, letra2 = list(pares)
    tabela = _criar_tabela()
    linha1, coluna1 = _obter_linha_e_coluna(letra1, tabela)
    linha2, coluna2 = _obter_linha_e_coluna(letra2, tabela)

    if linha1 == linha2: # quando estão na mesma linha
        if coluna1 == 0:
            letra1 = tabela[linha1][4]
        else:
            letra1 = tabela[linha1][coluna1-1]
        if coluna2 == 0:
            letra2 = tabela[linha2][4]    
        else:
            letra2 = tabela[linha2][coluna2-1]

    elif coluna1 == coluna2: # quando estão na mesma coluna
        if linha1 == 0:
            letra1 = tabela[4][coluna1]
        else:
            letra1 = tabela[linha1-1][coluna1]
        if linha2 == 0:
            letra2 = tabela[4][coluna2]
        else:
            letra2 = tabela[linha2-1][coluna2]

    else: # caso as linhas e colunas sejam diferentes
        letra1 = tabela[linha1][coluna2]
        letra2 = tabela[linha2][coluna1]

    return ''.join([letra1, letra2])    

if __name__ == '__main__':

    # testes
    assert encriptar('hello one and all', chave='pamdemia') == 'opsmnh homz dkmy mksm'
    #assert decriptar('kcnvmp pocz clcy fqnv') == 'hello one and all'
    