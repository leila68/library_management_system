import sqlite3
import create_db_tables


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


def get_author_id(connection, author_name):
    cursor = connection.execute("SELECT author_id FROM members WHERE name = ?", (author_name,))
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return None


def get_book_id(connection, book_name):
    cursor = connection.execute("SELECT book_id FROM books WHERE name = ?", (book_name,))
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return None


def get_member_id(connection, member_name):
    cursor = connection.execute("SELECT member_id FROM members WHERE name = ?", (member_name,))
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return None


def insert_rows_table(connection, query, values):
    with connection:
        connection.executemany(query, values)


def insert_one_row_table(connection, query,  value):
    with connection:
        connection.execute(query, value)


def insert_author(connection):
    name = input("Enter the author's name: ")
    country = input("Enter the author's country: ")
    birth_year = input("Enter the author's birth year: ")
    author_query = "INSERT INTO authors (name, country, birth_year) VALUES (?, ?, ?);"

    try:
        # Insert into the authors table
        insert_one_row_table(connection, author_query, (name, country, int(birth_year)))
        print("Author added successfully!")
    except ValueError:
        print("Invalid input for birth year. Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")


def insert_book(connection):
    title = input("Enter the book's title: ")
    author_name = input("Enter the author's name: ")
    author_id = get_author_id(connection, author_name)
    year_published = input("Enter the year the book was published: ")

    book_query = "INSERT INTO books (title, author_id, year_published) VALUES (?, ?, ?);"

    try:
        with connection:
            insert_one_row_table(connection, book_query, (title, int(author_id), int(year_published)))
        print("Book added successfully!")
    except ValueError:
        print("Invalid input for author ID or year published. Please enter valid numbers.")
    except Exception as e:
        print(f"An error occurred: {e}")


def insert_member(connection):
    name = input("Enter the member's name: ")
    email = input("Enter the member's email: ")
    membership_date = input("Enter the membership date (YYYY-MM-DD): ")

    member_query = "INSERT INTO members (name, email, membership_date) VALUES (?, ?, ?);"

    try:
        with connection:
            insert_one_row_table(connection, member_query, (name, email, membership_date))
        print("Member added successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")


def insert_transaction(connection):
    book_name = input("Enter the book's name: ")
    book_id = get_book_id(connection, book_name)
    member_name = input("Enter the member's name: ")
    member_id = get_member_id(connection, member_name)
    borrow_date = input("Enter the borrow date (YYYY-MM-DD): ")
    return_date = input("Enter the return date (YYYY-MM-DD): ")

    transaction_query = """
        INSERT INTO transactions (book_id, member_id, borrow_date, return_date)
        VALUES (?, ?, ?, ?);
    """

    try:
        with connection:
            insert_one_row_table(connection, transaction_query, (int(book_id), int(member_id), borrow_date, return_date))
        print("Transaction added successfully!")
    except ValueError:
        print("Invalid input for book ID or member ID. Please enter valid numbers.")
    except Exception as e:
        print(f"An error occurred: {e}")


def insert_review(connection):
    book_id = input("Enter the book's ID: ")
    member_id = input("Enter the member's ID: ")
    review_text = input("Enter the review text: ")
    rating = input("Enter the rating (1-5): ")

    review_query = """
        INSERT INTO reviews (book_id, member_id, review_text, rating)
        VALUES (?, ?, ?, ?);
    """

    try:
        with connection:
            insert_one_row_table(connection,  review_query, (int(book_id), int(member_id), review_text, int(rating)))
        print("Review added successfully!")
    except ValueError:
        print("Invalid input for book ID, member ID, or rating. Please enter valid numbers.")
    except Exception as e:
        print(f"An error occurred: {e}")


def delete_author(connection):
    name = input("Enter the author's name: ")
    author_name = name.lower()

    author_query = "SELECT name FROM authors WHERE LOWER(name) = ?"

    with connection:
        cursor = connection.execute(author_query, (author_name,))
        author_exists = cursor.fetchone()

    if author_exists:
        author_query = "DELETE FROM authors WHERE LOWER(name) = ?"
        with connection:
            connection.execute(author_query, (author_name,))
        print(author_name, "has been deleted.")
    else:
        print("Author not found:", author_name)

