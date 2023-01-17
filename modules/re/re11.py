# Using the built-in module re extract the phone number from the given message. Print the result to the console.

import re


message = 'For more information, please call: 123-456-789'

number = re.findall(pattern=r'[0-9|-]+', string=message)
print(number[0])