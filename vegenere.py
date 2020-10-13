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

def encriptar(mensagem:str, chave: str) -> str:
    pass

def decriptar(mensagem:str, chave: str) -> str:
    pass

if __name__ == '__main__':
    pass