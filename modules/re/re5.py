# Using the re built-in module and the appropriate regular expression, extract from the following code:
# code = 'PL code: XG-GH-110'
# a list of the following values:
# ['PL', '110']

import re
 
 
code = 'PL code: XG-GH-110'
print(re.findall(pattern=r"PL|\d+", string=code))