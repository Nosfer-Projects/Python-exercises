# Using the os built-in module, build a list called names containing alphabetically sorted filenames in the working directory with the extension .py
# Print the result to the console.

import os

names = sorted([name for name in os.listdir() if name.endswith('.py')])
print(names)