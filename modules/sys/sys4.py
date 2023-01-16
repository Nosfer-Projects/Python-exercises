# Using the sys built-in module, build a script called example.py that will count the sum of the first two arguments passed (we assume that the user only enters integers).


import sys
total = 0
for arg in sys.argv[1:]:
    total += arg