# Using the built-in datetime module, determine the number of days until the end of the current year. Print the result to the console as shown below.

import datetime
today = datetime.date.today()
end_of_year = datetime.date(today.year, 12, 31)
diff = (end_of_year - today).days
print(f'Number of days until the end of the year: {diff}')