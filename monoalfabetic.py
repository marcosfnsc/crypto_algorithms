class MonoAlfabetic:
    def __init__(self):
        self.plain_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.decrypting = False

    def cipher_alphabet(self, password):
        ''' (str) -> str
        Retorna um alfabeto cifrado iniciado com
        o texto da palavra chave password
        É feita iterações na palavra-chave, e as letras únicas são colocadas em uma lista
        O índice da última letra da palavra-chave sem duplicatas (baseado no alfabeto plano) é salvo
        Na outra iteração as letras que não estiverem no alfabeto cifrado são colacadas lá, continuando desde a última letra
        '''
        ciph_alphabet = []
        password = password.upper()

        for ch in password:
            if ch not in ciph_alphabet:
                ciph_alphabet.append(ch)
                idx = self.plain_alphabet.find(ch)
        plain_alphabet = self.plain_alphabet[idx:] + self.plain_alphabet[:idx]

        for ch in plain_alphabet:
            if ch not in ciph_alphabet:
                ciph_alphabet.append(ch)
        return ''.join(ciph_alphabet)

    def encrypt(self, plaintext, password):
        '''(str, str) -> str
        Retorna o texto plano cifrado com a cifra de
        substituicao com a palavra chave password
        Para encriptar apenas se itera o texto e pega o índice do alfabeto plano, e pega a letra desse índice no alfabeto cifrado
        Para decriptar apenas as variáveis dos alfabetos são trocadas para fazer o "processo contrário"
        '''
        txt = ''
        plain_alphabet = self.plain_alphabet
        text = plaintext.replace(' ', '').upper()
        cipher = self.cipher_alphabet(password)

        if self.decrypting:
            plain_alphabet, cipher = cipher, plain_alphabet
            self.decrypting = False

        for ch in text:
            txt += cipher[plain_alphabet.find(ch)]
        return txt

    def decrypt(self, ciphertext,  password):
        '''(str, str) -> str
        Retorna o texto cifrado decifrado com a cifra de
        substituicao com a palavra chave password
        '''
        self.decrypting = True
        return self.encrypt(ciphertext, password)

crypto = MonoAlfabetic()
encrip = crypto.encrypt("if we wish to replace letters", "DKVQFIBJWPESCXHTMYAUOLRGZN")
print(encrip)
print(crypto.decrypt(encrip, "DKVQFIBJWPESCXHTMYAUOLRGZN"))
