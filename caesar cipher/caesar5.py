# Implementing the encrypt() method, which will encrypt the transmitted message (message argument)
# Implementing the decrypt() method, which will decrypt the message (message argument)
import string

class CaesarCipher:
    
    def __init__(self, alphabet, key):
        self.alphabet = alphabet
        self.key = key

    @property
    def cipher(self):
        result = ''
        for letter in self.alphabet:
            new_idx = (
                self.alphabet.index(letter) + self.key
            ) % len(self.alphabet)
            result += self.alphabet[new_idx]
        return result
    def encrypt(self, message):
        result = ''
        new_alpha = self.cipher
        for i in message:
            if i not in self.alphabet:
                result += i
            else:
                new_letter = new_alpha[(self.alphabet.index(i))]
                result += new_letter
        return result
    def decrypt(self, message): 
        result = ''
        for letter in message:
            if letter not in self.alphabet:
                result += letter
            else:
                result += self.alphabet[
                    self.cipher.index(letter)
                ]
        return result

msg = CaesarCipher(string.ascii_uppercase, 2)
print(msg.decrypt('CVVCEM CV FCYP!'))