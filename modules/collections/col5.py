# The following text is given:
# text = 'python programming - introduction'
# Using the collections built-in module and the Counter class, determine the three most frequently appearing characters in the given text.

from collections import Counter


text = 'python programming - introduction'

letters = Counter(text)
print(letters.most_common(3))