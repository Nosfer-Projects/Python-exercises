# Using the dict.setdefault() method, set the default value for the 'source' key to 'NYSE'. Then print out the quotations dictionary form.
# Try setting the default value for the 'source' key again, this time to 'LSE'. Then reprint the quotations dictionary form and the value for the 'source' key (on a separate line).


quotations = {}
quotations.setdefault('source', 'NYSE')
print(quotations)
quotations.setdefault('source', 'LSE')
print(quotations)
print(quotations['source'])