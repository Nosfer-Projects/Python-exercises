# We want to find an n-period moving average for the price. Try to implement a function called moving_avg() that takes two arguments:
# prices - a list of prices to calculate the moving average
# window_size - window size - the number of periods for which we calculate the moving average (for example, window_size = 15 is a 15-day moving average)
# and will return a list with values ​​for the moving average (individual values ​​of the average rounded to two decimal places) with the period window_size.
# Note that the number of items in a list with an n-period moving average will be shorter than the number of items in a list with prices by n - 1 items.



import csv


with open('cdr.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    columns = next(reader)
    rows = list(reader)
    closes = list(map(lambda row: float(row[4]), rows))
    
def moving_avg(prices, window_size):
    moving_averages = []
    idx = 0
 
    while idx < len(prices) - window_size + 1:
        current_window = prices[idx: idx + window_size]
        window_average = round(sum(current_window) / window_size, 2)
        moving_averages.append(window_average)
        idx += 1
 
    return moving_averages


print(moving_avg(closes, 15))