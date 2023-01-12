# We want to determine the height of a single candle (one session) calculated as the distance from the highest to the lowest price. To do this, implement a function called max_min_diff(), which returns such distances calculated based on the data variable.
# In response, call the max_min_diff() function and print the result to the console.

import csv


with open('cdr.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    columns = next(reader)
    rows = list(reader)
    data = list(map(lambda row: (row[0], float(row[2]), float(row[3])), rows))



def max_min_diff(data):
    total_diff = []
    for i in data:
        diff = round(i[1]-i[2], 2)
        total_diff.append(diff)
    return total_diff

print(max_min_diff(data))