# Using the dictionary and the setdefault() method, build the following object (grouping at the level of the first element; values ​​presented as a list):
# {'technology': ['Apple', 'Facebook'], 'gaming': ['Techland', 'EA', 'CD Projekt'], 'finance': ['Berkshire Hathaway', 'Allianz']}
# and assign to the variable data_dict. Print this variable to the console.


data = [
    ('technology', 'Apple'),
    ('gaming', 'Techland'),
    ('finance', 'Berkshire Hathaway'),
    ('gaming', 'EA'),
    ('technology', 'Facebook'),
    ('gaming', 'CD Projekt'),
    ('finance', 'Allianz')
]

data_dict = {}
for sector, company in data:
    data_dict.setdefault(sector, []).append(company)
 
print(data_dict)