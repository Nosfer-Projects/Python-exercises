# Implement a solution to this problem using the object-oriented programming (OOP) paradigm. Create a class called MorseCode that will contain two static methods (the easiest way is to use the @staticmethod decorator):
# encrypt() - a method that will encrypt messages into Morse code
# decrypt() - method that will decrypt the message



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

class MorseCode:
    @staticmethod
    def encrypt(message):
        return ' '.join(
        [
            MORSE_CODE[char.upper()] if char != ' ' else '/'
            for char in message
        ]
         )
    @staticmethod
    def decrypt(message):
        result = []
        list_marks = message.split()
        print(list_marks)
        for i in list_marks:
            if i == "/":
                i = " "
                result.append(i)
            else:
                for key, value in MORSE_CODE.items():
                    if value == i:
                        result.append(key)
        return "".join(result)