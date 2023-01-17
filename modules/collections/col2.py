# The results of voting in two voting groups are given in the form of dictionaries:
# poll_1 = {'yes': 140, 'no': 120, None: 12}
# poll_2 = {'yes': 113, 'no': 132, None: 9}
# Dictionary keys mean respectively:
# 'yes' - vote for yes
# 'no' - vote for no
# 'None' - vote invalid
# Using the collections built-in module, build two Counter objects from the given dictionaries. Then combine these objects into one and print to the console


from collections import Counter


poll_1 = {'yes': 140, 'no': 120, None: 12}
poll_2 = {'yes': 113, 'no': 132, None: 9}

vote1 = Counter(poll_1)
vote2= Counter(poll_2)
print(vote1 + vote2)