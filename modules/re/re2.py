# Using the re action module works with python regular functions extract all characters with an invalid digit as a list from percent text:


import re


text = 'Python 3.8'

letters = re.findall(pattern=r"\D", string = text)
print(letters)