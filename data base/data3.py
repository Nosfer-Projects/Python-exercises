# We want to set some support levels for the price and for that we need a moving minimum. For example, a 3-day moving low for moves per session, a 10-day moving low for short-term moves, etc. Try to implement a function called moving_min() that takes two arguments:
# prices - a list of prices to calculate the moving minimum
# window_size - window size - the number of periods for which we calculate the moving minimum (for example, window_size = 15 is a 15-day moving minimum)
# and will return a list with the values ​​for the window_size rolling minimum.


import csv
 
 
with open('cdr.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    columns = next(reader)
    rows = list(reader)
    closes = list(map(lambda row: float(row[4]), rows))
 
 
def moving_min(prices, window_size):
    moving_mins = []
    idx = 0
    while idx < len(prices) - window_size + 1:
        current_window = prices[idx: idx + window_size]
        window_min = min(current_window)
        moving_mins.append(window_min)
        idx += 1
 
    return moving_mins

print(moving_min(closes, 3))