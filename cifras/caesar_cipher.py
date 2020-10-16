class CaesarCipher:
    def __init__(self):
        self.ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

    def cipher(self, message, dir, rot):
        msg = ''
        for char in message:
            if char in self.ALPHABET:
                char_index = self.ALPHABET.index(char)
                msg += self.ALPHABET[(char_index + (dir * rot)) % len(self.ALPHABET)]
            else:
                msg += char
        return msg

    def encrypt(self, message, rot):
        return self.cipher(message, 1, rot)

    def decrypt(self, message, rot):
        return self.cipher(message, -1, rot)

    def main(self):

        print("Você deseja encriptar ou decriptar a mensagem ?")
        print("1 - Encriptar\n2 - Decriptar")
        command = int(input())

        print("Digite a mensagem: ")
        message = str(input())
        
        print("Quantas rotações ?")
        rot = int(input())

        if command == 1:
            print (self.encrypt(message, rot))
        elif command == 2:
            print (self.decrypt(message, rot))
        else:
            print ("Opção inválida")

if __name__ == '__main__':
    cipher = CaesarCipher()
    cipher.main()
