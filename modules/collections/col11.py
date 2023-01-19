# Using the get() method, in the absence of the 'source' key in the dictionary, set the default value to 'NYSE' and print it to the console. Also print the quotations dictionary form.


quotations = {}
a= quotations.get('source')
if a == None:
    print("NYSE")
    print(quotations)