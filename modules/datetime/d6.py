# assign to variable dates. The dates start from 2020-01-01 00:00:00, end on 2020-01-04 16:00:00 and differ in the interval of 8h from dates list. Then print each date to the console.

import datetime

dates = [
    datetime.datetime(2020, 1, 1, 0, 0),
    datetime.datetime(2020, 1, 1, 8, 0),
    datetime.datetime(2020, 1, 1, 16, 0),
    datetime.datetime(2020, 1, 2, 0, 0),
    datetime.datetime(2020, 1, 2, 8, 0),
    datetime.datetime(2020, 1, 2, 16, 0),
    datetime.datetime(2020, 1, 3, 0, 0),
    datetime.datetime(2020, 1, 3, 8, 0),
    datetime.datetime(2020, 1, 3, 16, 0),
    datetime.datetime(2020, 1, 4, 0, 0),
    datetime.datetime(2020, 1, 4, 8, 0),
    datetime.datetime(2020, 1, 4, 16, 0),
]

for i in dates:
    print(i)