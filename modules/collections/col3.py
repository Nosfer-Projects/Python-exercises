# The results of voting in three voting groups are given in the form of dictionaries:
# poll_1 = {'yes': 140, 'no': 120, None: 12}
# poll_2 = {'yes': 113, 'no': 132, None: 9}
# poll_3 = {'yes': 16, 'no': 14}
# Dictionary keys mean respectively:
# 'yes' - vote for yes
# 'no' - vote for no
# 'None' - vote invalid
# Using the collections built-in module and the Counter class, enter the total number of yes votes. Print the result to the console.

from collections import Counter


poll_1 = {'yes': 140, 'no': 120, None: 12}
poll_2 = {'yes': 113, 'no': 132, None: 9}
poll_3 = {'yes': 16, 'no': 14}

v1= Counter(poll_1)
v2= Counter(poll_2)
v3= Counter(poll_3)
total = v1 + v2 +v3
print(total["yes"])