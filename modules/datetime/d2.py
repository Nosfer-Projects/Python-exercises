# calculate the datetime measurement module, the datetime class and the datetime.datetime.strftime() method format the initial number:
# 2021-04-20 11:30:00
# For format:
# 2021-04-20
# 20-04-2021
# 04-2021
# April-2021
# April 20, 2021
# 2021-04-20 11:30:00
# 20/04/21 11:30:00
# 20 (Tuesday) April 2021
# Then print the formatted data given in the console.


from datetime import datetime
 
 
dt1 = datetime(2021, 4, 20, 11, 30, 00)
 
print(dt1.strftime('%Y-%m-%d'))
print(dt1.strftime('%d-%m-%Y'))
print(dt1.strftime('%m-%Y'))
print(dt1.strftime('%B-%Y'))
print(dt1.strftime('%d %B, %Y'))
print(dt1.strftime('%Y-%m-%d %H:%M:%S'))
print(dt1.strftime('%m/%d/%y %H:%M:%S'))
print(dt1.strftime('%d(%a) %B %Y'))