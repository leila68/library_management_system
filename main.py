import sqlite3
import database_functions


if __name__ == "__main__":
    connection = database_functions.connect()

    # insert author
    database_functions.insert_author(connection)
    database_functions.tables_values(connection, 'authors')

    # # insert book
    # database_functions.insert_book(connection)
    #
    # # insert member
    # database_functions.insert_member(connection)
    #
    # # insert transaction
    # database_functions.insert_transaction(connection)
    #
    # # insert review
    # database_functions.insert_review(connection)



