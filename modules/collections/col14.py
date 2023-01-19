# Using the collections built-in module and the defaultdict class, build the following object (grouping at the level of the first element; values ​​presented as a list):
# defaultdict(<class 'list'>, {'technology': ['Apple', 'Facebook'], 'gaming': ['Techland', 'EA', 'CD Projekt'], 'finance': ['Berkshire Hathaway', 'Allianz']})
# and assign to def_dict variable. Print this variable to the console.


from collections import defaultdict


data = [
    ('technology', 'Apple'),
    ('gaming', 'Techland'),
    ('finance', 'Berkshire Hathaway'),
    ('gaming', 'EA'),
    ('technology', 'Facebook'),
    ('gaming', 'CD Projekt'),
    ('finance', 'Allianz')
]

def_dict = defaultdict(list)
for key,value in data:
    def_dict[key].append(value)
print(def_dict)