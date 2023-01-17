# Using the built-in module re mask the given telephone number as follows '***-***-***'. Print the processed text to the console.

import re


text = "Please send an email to info@template.com or call to: 123-456-789."

number = re.findall(pattern=r'\d{3}-\d{3}-\d{3}', string=text)
n = ["*" if i.isdigit() else i for i in number[0]]




print(f'Please send an email to info@template.com or call to: {"".join(n)}.')