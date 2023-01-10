# Attached to the exercise is the file Customer.csv (utf-8 encoding) containing customer data for an application.
# Load the Customer.csv file and extract all the unique country names sorted alphabetically into a list and assign it to the unique_countries variable. Print the contents of the unique_countries variable to the console.






from itertools import chain
import csv

with open("Customer.csv", 'r') as file:
    reader = csv.reader(file)
    data = list(chain.from_iterable(reader))

unique_countries= list(set(data))
print(sorted(unique_countries))
