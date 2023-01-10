# The following functions have been implemented: generate_cipher() and encrypt(). The first generates the cipher, the second encrypts the message.
# You are one of Caesar's commanders and you must decipher a message that is critical to the success of the mission. Implement a function called decrypt() that takes three arguments:
# alphabet - the alphabet we use for encryption
# message - the message we want to decrypt
# key - key, shift
# and decrypts the message.
# You can use the encrypt() function for implementation.

import string


def generate_cipher(alphabet, key):
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

def decrypt(alphabet, message, key):
    cipher = generate_cipher(alphabet, key)
    result = ''
    for letter in message:
        if letter not in alphabet:
            result += letter
        else:
            result += alphabet[cipher.index(letter)]
    return result

print(decrypt(string.ascii_uppercase, 'FGBC GUR NGGNPX!', 13))
