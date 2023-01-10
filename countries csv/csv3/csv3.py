# Convert the Customer.csv file to a JSON file named customer.json.
# Some early users of the customer.json file (indentation level - 4):
# {
#     "ALPHIES": {
#         "CompanyName": "Alfreds Futterkiste",
#         "ContactName": "Maria Anders",
#         "ContactTitle": "Sales Representative",
#         "Address": "Obere Str. 57",
#         "City": "Berlin",
#         "Region": "Western Europe",
#         "PostalCode": "12209",
#         "Country": "Germany",




import json
import csv

dict_csv= {}

with open("Customer.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file, delimiter=',')
    
    for row in reader:
        key = row["Id"]
        del row["Id"]
        dict_csv[key] = row

print(dict_csv)

with open("customer.json", "w") as file:
    json.dump(dict_csv, file,  indent=4)
