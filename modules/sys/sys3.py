# Using the sys built-in module, build a script that will print the arguments passed to the console when the script is invoked (each argument on a separate line).


import sys

for arg in sys.argv[1:]:
    print(arg)