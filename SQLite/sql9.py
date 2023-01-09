# This command is properly formatted (for better code readability). The indentations used are obtained by inserting a tab character for each successive column.
# Transform the generate_sql() function from the previous exercise so that you can achieve the code formatting described above.
# [IN]: generate_sql('Customer', ['Id', 'FirstName'], ['INTEGER PRIMARY KEY', 'TEXT NOT NULL'])
# [OUT]: 'CREATE TABLE Customer (\n\tId INTEGER PRIMARY KEY,\n\tFirstName TEXT NOT NULL\n)'


def generate_sql(table_name, col_names, constraints):
    cols = [
        " ".join((col, constraint)).strip()
        for col, constraint in zip(col_names, constraints)
    ]
    return (
        f'CREATE TABLE {table_name} (\n\t'
        + ',\n\t'.join(cols)
        + '\n)'
    )

print(generate_sql('Customer', ['Id', 'FirstName'], ['INTEGER PRIMARY KEY', 'TEXT NOT NULL']))