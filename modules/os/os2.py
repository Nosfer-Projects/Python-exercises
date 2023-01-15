# Using the os built-in module, build a list called names containing the names of items in the working directory starting with 'e', ​​sorted alphabetically. In response, print a list of names to the console.


import os
 
 
names = sorted([name for name in os.listdir() if name.startswith('e')])
print(names)