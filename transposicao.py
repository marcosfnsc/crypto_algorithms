"""Implementacao da cifra de transposicao

funcoes publicas:
 - encriptar
 - decriptar
"""

# ===================== encriptar =====================

def encriptar(mensagem: str) -> str:
    mensagem = list(mensagem)
    code = _codificar(mensagem)

    l1 = ''.join(code[0])
    l2 = ''.join(code[1])
    return ''.join([l1, l2])

def _codificar(msg: list) -> list:
    tabela = [[], []]

    if len(msg) % 2 != 0:
        msg.append(' ')

    while len(msg) > 0:
        tabela[0].append(msg[0])
        tabela[1].append(msg[1])
        del(msg[:2])

    return tabela

# ===================== decriptar =====================

def decriptar(mensagem: str) -> str:
    mensagem = list(mensagem)
    decode = _decodificar(mensagem)

    msg = ''
    while len(decode[0]) > 0:
        msg =  ''.join([msg, decode[0][0], decode[1][0]])
        del(decode[0][0])
        del(decode[1][0])

    return msg.strip()

def _decodificar(msg: list) -> list:
    tabela = []

    metade = len(msg) // 2
    tabela.append(msg[:metade])
    tabela.append(msg[metade:])

    return tabela

if __name__ == '__main__':
    # testes
    assert encriptar('joseph climber') == 'jsp lmeoehcibr'
    assert decriptar('jsp lmeoehcibr') == 'joseph climber'
