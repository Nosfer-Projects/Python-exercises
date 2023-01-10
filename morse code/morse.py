# Let's go back to spacing. Spacing between individual characters - three dots (represented by a ' ' space character) and spacing between groups of characters (words) - seven dots (represented as ' / ' - space + slash + space).
# Implement a function called encrypt() that will encrypt messages into Morse code. If the forwarded message contains lowercase letters, convert them to uppercase before encrypting.





MORSE_CODE = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    '&': '.-...',
    '@': '.--.-.',
    ':': '---...',
    ',': '--..--',
    '.': '.-.-.-',
    ''': '.----.',
    ''': '.-..-.',
    '?': '..--..',
    '/': '-..-.',
    '=': '-...-',
    '+': '.-.-.',
    '-': '-....-',
    '(': '-.--.',
    ')': '-.--.-',
    '!': '-.-.--',
}


def encrypt(text):
    cipher = ''
    for char in text:
        char = char.upper()
        if char != ' ':
            cipher += MORSE_CODE[char] + ' '
        else:
            cipher += '/ '
    return cipher[:-1]

print(encrypt('PYTHON 3.9'))




