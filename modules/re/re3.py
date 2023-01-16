# Using the built-in module re to work with regular expressions in Python, extract all non-zero and hyphen characters in the form of a list from the following code:


import re


code = '0010-000-423'

nums = re.findall(pattern=r"[1-9]" , string= code)
print(nums)

