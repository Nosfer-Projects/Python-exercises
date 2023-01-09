# The following SQL command creates a table named Product with columns: Id, ProductName, SupplierId, CategoryId, Quantity, UnitPrice
# CREATE TABLE Product (
#     Id,
#     productName,
#     supplierId,
#     CategoryId,
#     quantity,
#     UnitPrice
# )
# Implement a function called generate_sql() that takes two arguments:
# table_name - table name (string)
# col_names - table column names (list, tuple)
# The generate_sql() function is designed to generate SQL code that creates a table named table_name and columns col_names. In this exercise, we skip any table/column constraints in the generate_sql() implementation.


def generate_sql(table_name, col_names):
    return f'CREATE TABLE {table_name} (' + ', '.join(col_names) + ')'

print(generate_sql('Product', ['Id', 'ProductName']))