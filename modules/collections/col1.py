# Using the collections built-in module, build a Counter object from the given target list. Print the result to the console.

from collections import Counter


target = ['yes', 'no', 'no', None, 'yes', 'yes', 'no', 'yes']

list_tar = Counter(target)
print(list_tar)