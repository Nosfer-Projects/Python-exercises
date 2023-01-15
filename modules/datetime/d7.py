# Using the built-in datetime module, determine the future value of the initial capital (present value) of USD 1000 at an annual interest rate of 4% (rate) and compound daily interest capitalization, assuming the duration of the investment from 2021-07-01 to 2021-12-31. For calculations, assume that a year has 365 days.
# Print the future value to the console as shown below.

import datetime
 
rate = 0.04
pv = 1000
daily_rate = rate / 365.0
 
d1 = datetime.date(2021, 7, 1)
d2 = datetime.date(2021, 12, 31)
duration = d2 - d1
 
fv = pv * (1 + daily_rate) ** duration.days
print(f'Future value: {fv:.2f} USD')