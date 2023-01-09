# The following SQL command creates a table named Product with columns: Id, ProductName, SupplierId, CategoryId, Quantity, UnitPrice
# CREATE TABLE Customer (
#     id INTEGER PRIMARY KEY,
#     FirstName TEXT NOT NULL,
#     LastName TEXT NOT NULL
# )
# By adding some column constraints like primary key and NOT NULL constraint.
# Implement a function called generate_sql() that takes three arguments:
# table_name - table name (string)
# col_names - table column names (list, tuple)
# constraints - constraints for columns (list of strings), an empty string is no constraint
# The generate_sql() function is designed to generate SQL code that creates a table named table_name and columns col_names and constraints corresponding to them constraints.


def generate_sql(table_name, col_names, constraints):
    cols = [
        " ".join((col, constraint))
        for col, constraint in zip(col_names, constraints)
    ]
    return f'CREATE TABLE {table_name} (' + ', '.join(cols) + ')'


print(generate_sql('Customer', ['Id', 'FirstName'], ['INTEGER PRIMARY KEY', 'TEXT NOT NULL']))