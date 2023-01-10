# Consider a simple encryption technique, the Caesar Cipher. It consists in replacing each letter in the text with another one, separated by a fixed number of positions in the alphabet (key - key).
# Implement a function called generate_cipher() that takes two arguments:
# alphabet - the alphabet we want to encrypt
# key - key, shift (default value 2)
# and will return the passed alphabet in encrypted form.

import string
def generate_cipher(alphabet, key):
    cipher = ''
    for letter in alphabet:
        new_idx = (alphabet.index(letter) + key) % len(alphabet)
        cipher += alphabet[new_idx]
    return cipher
        
print(generate_cipher(string.ascii_uppercase, 3))        