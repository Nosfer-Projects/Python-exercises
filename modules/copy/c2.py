# Using the built-in copy module, make a deep copy of the following list of stocks:
# stocks = [['CDR', '11B'], ['PLW'], ['TEN']]
# and assign to the stocks_copied variable. Replace '11B' in the first item of the stocks list with 'CRJ'.
# Note the values ​​in the stocks_copied list. Print both lists in response: stocks and stocks_copied (each on a separate line) as shown below.

import copy


stocks = [['CDR', '11B'], ['PLW'], ['TEN']]
stocks_copied= copy.deepcopy(stocks)
stocks[0][1]= 'CRJ'
print(f"stocks: {stocks}")
print(f"stocks_copied: {stocks_copied}")