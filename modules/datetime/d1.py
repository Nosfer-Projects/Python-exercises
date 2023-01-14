# Using the built-in datetime module, determine the exact time that has elapsed between dates:
# 2020-07-20 11:30:00
# 2021-02-20 10:25:00
# Then print the result to the console.


import datetime

a1 = datetime.datetime(2020,7,20,11,30,0)
a2 = datetime.datetime(2021,2,20,10,25,0)

diff = (a2- a1)
print(diff)