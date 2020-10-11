def encriptar(msg: str) -> str:
    """criptografa a mensagem usando a cifra de playfair"""

    msg = _tratar_mensagem(msg)
    tabela = _criar_tabela()


    return msg

def _criar_tabela():
    """retorna uma tabela 5x5 prenchida com o alfabeto, com excecao da letra j"""
    return [
        ['a', 'b', 'c', 'd', 'e'],
        ['f', 'g', 'h', 'i', 'k'],
        ['l', 'm', 'n', 'o', 'p'],
        ['q', 'r', 's', 't', 'u'],
        ['v', 'w', 'x', 'y', 'z'],
    ]

def _tratar_mensagem(msg) -> str:
    msg = msg.replace(' ', '')

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
    return ''.join(nova_msg).strip()
 
def decriptar():
    pass

if __name__ == '__main__':
    msg_test = 'agua mole em pedra dura tanto bate ate que fura'

    #print(encriptar(msg_test))
    print(_tratar_mensagem('hello one and alla'), end='')