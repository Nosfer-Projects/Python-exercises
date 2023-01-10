# Implement a function called encrypt() that takes three arguments:
# alphabet - the alphabet we want to encrypt
# message - the message we want to encrypt
# key - key, shift

import string
def generate_cipher(alphabet, key=2):
    cipher = ''
    for letter in alphabet:
        new_idx = (alphabet.index(letter) + key) % len(alphabet)
        cipher += alphabet[new_idx]
    return cipher


def encrypt(alphabet, message, key):
    cipher = generate_cipher(alphabet, key)
    result = ''
    for letter in message:
        if letter not in alphabet:
            result += letter
        else:
            result += cipher[alphabet.index(letter)]
    return result



print(encrypt(string.ascii_uppercase, 'PYTHON', 2))