# Using the built-in datetime module, determine the exact time left to the end of the current year. Print the result to the console as shown below.
# For example, for the date: 2020-07-21 07:39:39.188939 the value will be returned:
# 'Until the end of the year: 162 days, 16:20:20.811061'

import datetime

cur = datetime.datetime.now()
end_of_year = datetime.datetime(2024,1,1,0,0,0)

diff = end_of_year - cur

print(f"Until the end of the year: {diff}")