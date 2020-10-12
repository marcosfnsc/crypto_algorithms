def encriptar(msg: str) -> str:
    """criptografa a mensagem usando a cifra de playfair"""

    msg = list(map(_tratar_mensagem, msg.split()))
    tabela = _criar_tabela()
    msg_codificada = []
    for x in msg:
        msg_codificada.append(''.join(map(_transformar_decodificada, x.split())))

    return ' '.join(msg_codificada)

def _criar_tabela() -> list:
    """retorna uma tabela 5x5 prenchida com o alfabeto, com excecao da letra j"""
    return [
        ['a', 'b', 'c', 'd', 'e'],
        ['f', 'g', 'h', 'i', 'k'],
        ['l', 'm', 'n', 'o', 'p'],
        ['q', 'r', 's', 't', 'u'],
        ['v', 'w', 'x', 'y', 'z'],
    ]

def _tratar_mensagem(msg: str) -> str:
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

def _transformar_decodificada(pares: str) -> str:
    letra1, letra2 = list(pares)
    tabela = _criar_tabela()
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

def _transformar_codificada(pares: str):
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


def _obter_linha_e_coluna(elemento: str, tabela: list):
    """retorna o numero da linha e coluna de um elemento na tabela"""
    for x in range(len(tabela)):
        if elemento in tabela[x]:
            break
    coluna = tabela[x].index(elemento)
    return x, coluna


def decriptar(msg: str) -> str:
    msg = list(map(_tratar_mensagem_codificada, msg.split()))
    tabela = _criar_tabela()
    msg_decodificada = []
    for x in msg:
        msg_decodificada.append(''.join(map(_transformar_codificada, x.split())))
    
    return ' '.join(msg_decodificada).replace('x', '')

if __name__ == '__main__':
    msg_test = 'agua mole em pedra dura tanto bate ate que fura'

    #print(encriptar(msg_test))
    #print(_tratar_mensagem('hello one and alla'), end='')
    cifra = encriptar('hello one and all')
    print(cifra)
    print(decriptar(cifra))