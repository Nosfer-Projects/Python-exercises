# Using the collections built-in module from the following dictionaries:
# stocks_1 = {'CDR': 400, 'PLW': 490}
# stocks_2 = {'PLW': 500, 'TEN': 550, 'BBT': 30}
# create a ChainMap object and assign it to a variable called stocks. In response, print the stocks variable to the console.

from collections import ChainMap


stocks_1 = {'CDR': 400, 'PLW': 490}
stocks_2 = {'PLW': 500, 'TEN': 550, 'BBT': 30}

stocks = ChainMap(stocks_1, stocks_2)
print(stocks)