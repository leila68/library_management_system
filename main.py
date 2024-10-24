import sqlite3
import database_functions
import create_db_tables

MENU_PROMPT = """
***** Library System Management *****
Please choose one of the options:
1) Add a author:  
2) Add a book: 
3) Add a member: 
4) Insert a transaction: 
5) Insert a review: 
********************
6) Delete a author
7) Delete a book:
8) Delete a member:
9) Delete a transaction:
10) Delete a review:
*********************
11) Search for a book:
12) Search for a member:
13) Search for a Author:
**********************
14) Show the result: 
15) Exit
 Your Selection: 
"""

if __name__ == "__main__":
    connection = database_functions.connect()

    # delete a table
    # connection.execute("DROP TABLE IF EXISTS transactions")
    # connection.execute(create_db_tables.create_transaction_table)

    while (user_input := input(MENU_PROMPT)) != "15":
        if user_input == "1":
            database_functions.insert_author(connection)
        elif user_input == "2":
            database_functions.insert_book(connection)
        elif user_input == "3":
            database_functions.insert_member(connection)
        elif user_input == "4":
            database_functions.insert_transaction(connection)
        elif user_input == "5":
            database_functions.insert_review(connection)
        elif user_input == "6":
            database_functions.delete_author(connection)
        elif user_input == "7":
            database_functions.delete_book(connection)
        elif user_input == "8":
            database_functions.delete_member(connection)
        elif user_input == "9":
            database_functions.delete_transaction(connection)
        elif user_input == "10":
            database_functions.delete_review(connection)
        elif user_input == "11":
            pass
        elif user_input == "12":
            pass
        elif user_input == "13":
            pass
        elif user_input == "14":
            table_name = input("Enter the table's name: ")
            print(database_functions.tables_values(connection, table_name))







