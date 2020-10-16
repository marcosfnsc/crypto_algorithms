import cifras.caesar_cipher as cesar
from cifras.monoalfabetic import MonoAlfabetic as Monoalfabetica
import cifras.playfair
import cifras.vegenere
import cifras.transposicao

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
        print('0 - sair do programa')

        print(40*'=')
        print('Qual cifra deseja usar?:')
        op = input('> ').strip()

        if op == '0':
            print('encerrando o programa...')
            break
        elif op == '1':
            msg, chave = obter_msg_key()
            sub_op = procedimento()

            cesarCifher = cesar.CaesarCipher()
            if sub_op == '1':
                resultado = cesarCifher.encrypt(msg, int(chave))
                print(f'mensagem codificada => {resultado}')
            elif sub_op == '2':
                resultado = cesarCifher.decrypt(msg, int(chave))
                print(f'mensagem decodificada => {resultado}')

            print(20*'-=')

        elif op == '2':
            msg, chave = obter_msg_key()
            sub_op = procedimento()

            monoalfabetic = Monoalfabetica()
            if sub_op == '1':
                resultado = monoalfabetic.encriptar(msg, chave)
                print(f'mensagem codificada => {resultado}')
            elif sub_op == '2':
                resultado = monoalfabetic.decriptar(msg, chave)
                print(f'mensagem decodificada => {resultado}')

            print(20*'-=')

        elif op == '3':
            msg, chave = obter_msg_key()
            sub_op = procedimento()

            if sub_op == '1':
                resultado = playfair.encriptar(msg, chave)
                print(f'mensagem codificada => {resultado}')
            elif sub_op == '2':
                resultado = playfair.decriptar(msg, chave)
                print(f'mensagem decodificada => {resultado}')

            print(20*'-=')

        elif op == '4':
            msg, chave = obter_msg_key()
            sub_op = procedimento()

            if sub_op == '1':
                resultado = vegenere.encriptar(msg, chave)
                print(f'mensagem codificada => {resultado}')
            elif sub_op == '2':
                resultado = vegenere.decriptar(msg, chave)
                print(f'mensagem decodificada => {resultado}')

            print(20*'-=')

        elif op == '5':
            msg = input('Qual a mensagem a ser codificada?: ').strip()
            sub_op = procedimento()

            if sub_op == '1':
                resultado = transposicao.encriptar(msg)
                print(f'mensagem codificada => {resultado}')
            elif sub_op == '2':
                resultado = transposicao.decriptar(msg)
                print(f'mensagem decodificada => {resultado}')

            print(20*'-=')
        else:
            print('Opcao invalida!')
            continue
        
