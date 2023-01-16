# Using the built-in string module, build a dictionary that allows you to map indices from 0 to 25 to lowercase letters of the alphabet (ascii_lowercase) and assign it to the code_map variable.
# Then replace the values ​​with the keys of the code_map dictionary and assign code_map_inv to the variable.
# A text document is given:
# docs = 'programming in python'
# Using the code_map and code_map_inv dictionaries, encode the docs document in such a way that each letter is shifted by three according to the alphabet (leave the spaces in the document unchanged). Print the encoded document to the console.



import string

def shift_letter(letter, shift):
    alphabet = string.ascii_lowercase
    shifted_index = (alphabet.index(letter) + shift) % 26
    return alphabet[shifted_index]

docs = 'programming in python'
code_map_transfer = ''
code_map_inv_transfer= ''

for i in docs:
    if i in string.ascii_lowercase:
        new_letter = shift_letter(i, 3)
        code_map_transfer += new_letter
        code_map_inv_transfer+= new_letter
    else:
        code_map_transfer += i
        code_map_inv_transfer += i

print(code_map_transfer)