# The following text is given:
# text = 'python programming - introduction'
# Using the built-in collections module and the Counter class, examine the distribution of characters in the given text (create a Counter object from the given text). Print the result to the console.

from collections import Counter


text = 'python programming - introduction'

num_letters = Counter(text)
print(num_letters)