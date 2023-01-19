# Using the built-in collections module and the defaultdict class, build the following object (grouping at the level of the first element - user_id; cumulative values ​​- amount):
# defaultdict(<class 'int'>, {'001': 233, '003': 33, '002': 126})
# and assign to def_dict variable. Print this variable to the console.

from collections import defaultdict


transactions = [
    ('001', 100),
    ('003', 10),
    ('002', 80),
    ('001', 90),
    ('002', 46),
    ('001', 43),
    ('003', 23),
]

def_dict = defaultdict(int)
for key, value in transactions:
    def_dict[key]+= value
print(def_dict)
