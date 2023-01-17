# Using the re built-in module and the appropriate regular expression, extract from the following code:
# code = '0010-000-423-22'
# a list of the following values:
# ['0010', '000', '423', '22']

import re


code = '0010-000-423-22'

list_nums = re.split("-", code)
print(list_nums)