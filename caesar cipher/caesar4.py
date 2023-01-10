# We will implement a solution to this problem using the object-oriented programming (OOP) paradigm.
# Steps to follow in this exercise:
# Create a class called CaesarCipher, where in the __init__() method we will set two instance attributes: alphabet and key.
# Implementing a read-only property called cipher that will hold the cipher
# You just need to implement the CaesarCipher class with the given description. Proof tests run several test cases to validate the solution.
import string



class CaesarCipher:
 
    def __init__(self, alphabet, key):
        self.alphabet = alphabet
        self.key = key
 
    @property
    def cipher(self):
        result = ''
        for letter in self.alphabet:
            new_idx = (self.alphabet.index(letter) + self.key) % len(self.alphabet)
            result += self.alphabet[new_idx]
        return result

a = CaesarCipher(string.ascii_uppercase, key=2)
print(a.cipher)