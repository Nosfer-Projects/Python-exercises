# We want to take a 3-day moving average for the close price. Try to implement a function called moving_avg() that takes a list of closing prices as an argument and returns a list with values ​​for a 3-day moving average (individual values ​​of the average are rounded to the second decimal place). Note that the number of list items with the 3-day moving average will be 2 items shorter than the number with closing prices.
# In response, call the moving_avg() function and print the result to the console.



import csv
 
 
with open('cdr.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    columns = next(reader)
    rows = list(reader)
    closes = list(map(lambda row: float(row[4]), rows))
 
 
def moving_avg(prices):
    moving_averages = []
    idx = 0
 
    while idx < len(prices) - 2:
        current_window = prices[idx: idx + 3]
        window_average = round(sum(current_window) / 3, 2)
        moving_averages.append(window_average)
        idx += 1
 
    return moving_averages
 
 
print(moving_avg(closes))


