# Using the sys built-in module, build a script called calculate_average.py, which will calculate the arithmetic mean (give the result to four decimal places) of the given arguments (we assume that the user enters only integers). If the user does not provide any argument, the script will return the following information:
# 'No values ​​were given.'


import sys

if len(sys.argv) >0:
    total = 0
    for i in sys.argv:
        if i.isdigit():
            total += int(i)
        else:
            continue
    print(total/len(sys.argv))
else:
    print('No values were given.')