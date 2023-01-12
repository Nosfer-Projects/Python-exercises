# One of the most characteristic candlestick patterns is the doji. A doji candlestick pattern is a market situation where the opening and closing prices are the same or close.
# We want to write a function called find_doji() that will allow us to determine the date of the daily candle closest to the doji from the given CD Projekt quotes for March 2021. For this purpose, we will introduce the concept of the body of the candle. The candle body is the distance from the opening price to the closing price. To find the candle closest to the doji, find the candle with the smallest body.
# In response, call find_doji() on the data list and print the result to the console.

import csv


with open('cdr.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    columns = next(reader)
    rows = list(reader)
    data = list(map(lambda row: (row[0], float(row[1]), float(row[4])), rows))

 
def find_doji(prices):
    diff = [
        (item[0], abs(round(item[2] - item[1], 2)))
        for item in prices
    ]
    min_diff = min(diff, key=lambda item: item[1])
    return min_diff[0]
 
 
print(find_doji(data))
