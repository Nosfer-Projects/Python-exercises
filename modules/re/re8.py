# Using the re built-in module, extract all e-mail addresses from the text and print to the console.

import re
 
 
text = (
    'Please send an email to info@template.com or '
    'sales-info@template.it'
)
print(re.findall(r"[\w\.-]+@[\w\.-]+", text))