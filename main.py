import sqlite3
import create_db_tables
import insert_in_tables


def connect():
    return sqlite3.connect('library_db.db')


def tables_list(connection):
    cursor = connection.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    return tables


def tables_values(connection, table_name):
    # Check if the table exists by querying sqlite_master
    cursor = connection.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?;", (table_name,))
    table_exists = cursor.fetchone()

    if not table_exists:
        return False
    else:
        # Fetch all values from the existing table
        cursor = connection.execute(f"SELECT * FROM {table_name}")
        values = cursor.fetchall()
        return values


def create_tables(connection):
    with connection:
        connection.execute(create_db_tables.create_author_table)
        connection.execute(create_db_tables.create_book_table)
        connection.execute(create_db_tables.create_member_table)
        connection.execute(create_db_tables.create_transaction_table)
        connection.execute(create_db_tables.create_review_table)


def insert_author(connection, values):
    with connection:
        connection.executemany(insert_in_tables.insert_authors, values)


if __name__ == "__main__":
    connection = connect()
    # create_tables(connection)
    # insert_author(connection, insert_in_tables.author_values)
    table_list = tables_list(connection)
    print(table_list)
    table_vals = tables_values(connection, 'authors')
    print(table_vals)
