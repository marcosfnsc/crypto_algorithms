def obter_msg_key():
    mensagem = input('Qual a mensagem?: ').strip()
    chave    = input('Qual a chave para a codificação?: ').strip()

    return mensagem, chave

def procedimento():
    print(40*'-')
    print('qual procedimento deseja realizar?:')
    print('1 - codificar')
    print('2 - decodificar')
    return input('> ').strip()
    
if __name__ == "__main__":
    while True:
        # menu
        print('Opcoes de cifras:')
        print('1 - cifra de cezar')
        print('2 - cifra monoalfabetica')
        print('3 - cifra de playfair')
        print('4 - cifra de vegenere')
        print('5 - cifra de transposicao (linhas)')

        print(40*'=')
        print('Qual cifra deseja usar?:')
        op = input('> ').strip()

        if op == '1':
            msg, chave = obter_msg_key()
            sub_op = procedimento()
        elif op == '2':
            msg, chave = obter_msg_key()
            sub_op = procedimento()
        elif op == '3':
            msg, chave = obter_msg_key()
            sub_op = procedimento()
        elif op == '4':
            msg, chave = obter_msg_key()
            sub_op = procedimento()
        elif op == '5':
            msg = input('Qual a mensagem a ser codificada?: ').strip()
            sub_op = procedimento()
        else:
            print('Opcao invalida!')
            continue
        
