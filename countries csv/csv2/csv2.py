# Attached to the exercise is the file Customer.csv (utf-8 encoding) containing customer data for an application.
# Convert the data from the Customer.csv file to a dictionary named data_dict. The data_dict dictionary keys are to be the 'Id' values ​​from the Customer.csv file, and the values ​​for these keys will be dictionaries of the following form: ColumnName: Value supplemented with data from the Customer.csv file.


import csv
 
data_dict = {}
with open('Customer.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=',')

    for row in reader:
        key = row['Id']
        del row['Id']
        data_dict[key] = row
 
print(data_dict['BOLID'])