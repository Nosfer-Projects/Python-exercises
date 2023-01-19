# The following list is provided:
# ['Tue.', 'Wed.', 'Thu.', 'Fri.', 'Sat.']
# Using the collections built-in module, build a deque (double-ended queue) object from the given list and assign it to the daynames variable. Then add 'Mon.' at the beginning and 'Sun.' at the end of the daynames object. In response, print the daynames object to the console.


from collections import deque

daynames = deque(['Tue.', 'Wed.', 'Thu.', 'Fri.', 'Sat.'])

daynames.appendleft('Mon.')
daynames.append('Sun.')

print(daynames)