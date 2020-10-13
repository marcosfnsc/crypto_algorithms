import string

def _criar_tabela():
    """retona uma tabela 26x26 contendo um alfabeto de ordem alternada em cada linha"""

    alfabeto = list(string.ascii_lowercase)
    tabela = []

    for x in range(len(string.ascii_lowercase)):
        linha = alfabeto[:] # [:] slice, faz com que a passagem do objeto seja por copia
        tabela.append(linha)

        alfabeto.append(alfabeto[0])
        del(alfabeto[0])

    return tabela

def _tratar_chave(chave: str, msg: str) -> str:
    """Aumenta o tamanho da chave pra que tenha o mesmo tamanho da mensagem"""

    chave = list(chave)
    nova_chave = []
    
    for caractere in msg:
        if caractere != ' ':
            nova_chave.append(chave[0])
            chave.append(chave[0])
            del(chave[0])
        else:
            nova_chave.append(' ')

    return ''.join(nova_chave)

def encriptar(mensagem:str, chave: str) -> str:
    msg = mensagem.split()

def _codificar(msg: str, tabela: list) -> str:
    pass

def decriptar(mensagem:str, chave: str) -> str:
    pass

if __name__ == '__main__':
    pass