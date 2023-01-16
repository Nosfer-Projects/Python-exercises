# Using the re built-in module to work with regular expressions in Python, extract all the digits in the form of a list from the following text:

import re


text = 'Python 3.8'
nums = re.findall("\d+", text)
print(nums)