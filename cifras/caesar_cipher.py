import string

def fix_index(idx: int) -> int:
    '''
    caso o indice esteja fora do intervalo de simbolos
    do alfabeto, essa função incrementa ou decrementa
    o indice para caber dentro do intervalo
    '''
    while idx > len(string.ascii_letters):
        idx -= len(string.ascii_letters)
    while idx < 0:
        idx += len(string.ascii_letters)
    return idx

def cipher(message: str, rot: int):
    message = list(message)

    for (idx, character) in enumerate(message):
        idx_character = string \
                .ascii_letters \
                .find(character)
        message[idx] = string \
                .ascii_letters[fix_index(idx_character + rot)]

    return ''.join(message)

if __name__ == '__main__':
    print('Você deseja encriptar ou decriptar a mensagem ?')
    print('1 - Encriptar\n2 - Decriptar')
    command = int(input())

    print('Digite a mensagem: ', end='')
    message = input().strip()

    print('Quantas rotações?: ', end='')
    rot = int(input())

    match command:
        case 1:
            print(cipher(message, rot))
        case 2:
            print(cipher(message, rot * -1))
        case _:
            print('Opção inválida')
