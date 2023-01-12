# However, we want to maintain an additional level of security for the support levels and move slightly away from the price levels at which the transactions took place. Implement a function called calculate_support() that will determine the support levels for the price according to the formula described below:
# moving support level = moving n-period minimum - difference * ratio
# Where difference is the difference between the highest value of the share price and the lowest value on a given trading day. Ratio, on the other hand, is an indicator that determines the significance of the difference itself when determining the level of support and is passed to the calculate_support() function as an argument.
# The calculate_support() function is supposed to take three arguments:
# prices - a list of prices to determine support
# window_size - window size - number of periods for which support
# ratio - ratio, default 0.1


import csv
 
 
with open('cdr.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    columns = next(reader)
    rows = list(reader)
    highs = list(map(lambda row: float(row[2]), rows))
    lows = list(map(lambda row: float(row[3]), rows))
    closes = list(map(lambda row: float(row[4]), rows))
 
 
def moving_min(prices, window_size):
    moving_mins = []
    idx = 0
 
    while idx < len(prices) - window_size + 1:
        current_window = closes[idx: idx + window_size]
        window_min = min(current_window)
        moving_mins.append(window_min)
        idx += 1
 
    return moving_mins
 
 
def calculate_support(prices, window_size, ratio=0.1):
    moving_mins = moving_min(prices, window_size)
    diffs = [high - low for high, low in zip(highs, lows)]
    supports = [
        round(value - (ratio * diff), 2)
        for value, diff in zip(moving_mins, diffs)
    ]
    return supports


print(calculate_support(closes, 10))