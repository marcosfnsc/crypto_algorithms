import string

def _criar_tabela():
    alfabeto = list(string.ascii_lowercase)
    tabela = []

    for x in range(len(string.ascii_lowercase)):
        linha = alfabeto[:]
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