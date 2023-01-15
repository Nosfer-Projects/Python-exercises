# Using the built-in datetime module and the date and timedelta classes from the given date 2020-01-01 00:00:00 get the date:
# postponed by 7 days
# postponed by 30 days
# shifted by 30 hours
# shifted by 15 minutes


import datetime
 
 
dt = datetime.datetime(2020, 1, 1)
 
print(dt + datetime.timedelta(days=7))
print(dt + datetime.timedelta(days=30))
print(dt + datetime.timedelta(hours=30))
print(dt + datetime.timedelta(minutes=15))