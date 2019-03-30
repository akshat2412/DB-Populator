import pandas
# import MySQLdb
from collections import OrderedDict
# from secrets import host, user, password, db


def get_db_columns_string(table_dictionary):
    string = ""
    for key in table_dictionary.keys():
        string = string + key + ", "
    return string[0:string.rfind(',')]


def get_file_row_values_string(table_dictionary, row):
    string = ""
    for key in table_dictionary.keys():
        string = string + str(row[table_dictionary[key]]) + ", "
    return string[0:string.rfind(',')]

file_name = input("Enter the name of the file to parse: ")
table_name = input("Enter the name of the table to input the data: ")
df = pandas.read_csv(file_name, keep_default_na=False)

print("""Enter column name in file followed by column name
         in the file. Make sure you provide a file column name
         for every column in the table.""")

table_dictionary = OrderedDict()

table_columns_remaining = 'y'

while table_columns_remaining is 'y':
    table_column_name = input("Table column name: ")
    file_column_name = input("Corresponding file column name: ")

    table_dictionary[table_column_name] = file_column_name

    table_columns_remaining = input("\nColumns remaining (y/n)")

try:
    for index, row in df.iterrows():
        print(index)

        table_columns_string = get_db_columns_string(table_dictionary)
        file_row_values_string = get_file_row_values_string(table_dictionary, row)
        sql = (
            f"INSERT INTO {table_name}({table_columns_string}) "
            f"VALUES({file_row_values_string});"
            )
        print(sql)
        # cursor.execute(sql)

    # db.commit()
    # db.close()
except Exception as e:
    print(e)
