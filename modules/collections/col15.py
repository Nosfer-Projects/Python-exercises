# Notice that the list contains duplicate values. Using the collections built-in module and the defaultdict class, build the following object (grouping at the level of the first element; values ​​presented as a set):
# defaultdict(<class 'set'>, {'technology': {'Facebook', 'Apple'}, 'gaming': {'EA', 'CD Projekt', 'Techland'}, 'finance': {'Allianz ', 'Berkshire Hathaway'}})
# and assign to def_dict variable. Print this variable to the console.

from collections import defaultdict


data = [
    ('technology', 'Facebook'),        
    ('technology', 'Apple'),
    ('gaming', 'Techland'),
    ('finance', 'Berkshire Hathaway'),
    ('gaming', 'EA'),
    ('gaming', 'EA'),    
    ('technology', 'Facebook'),
    ('gaming', 'CD Projekt'),
    ('finance', 'Allianz')
]

def_dict = defaultdict(set)
for sector, company in data:
    def_dict[sector].add(company)
 
print(def_dict)