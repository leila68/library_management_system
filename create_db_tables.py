# import sqlite3
#
# conn = sqlite3.connect('library_db.db')
# my_cursor = conn.cursor()

# tables = books, authors, members, transactions, reviews

create_author_table = """
       CREATE TABLE IF NOT EXISTS authors(
       author_id INTEGER PRIMARY KEY,
       name TEXT NOT NULL,
       country TEXT,
       birth_year INTEGER
       );"""

create_book_table = """
    CREATE TABLE IF NOT EXISTS books(
    book_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author_id INTEGER,
    published_year INEGER,
    category TEXT,
    available_copies INTEGER,
    FOREIGN KEY(author_id) REFERENCES authors(author_id) 
);"""

create_member_table = """
      CREATE TABLE IF NOT EXISTS members(
      member_id INTEGER PRIMARY KEY,
      name TEXT NOT NULL,
      membership_data DATA,
      email TEXT,
      phone_number TEXT
      );"""

create_transaction_table = """
      CREATE TABLE IF NOT EXISTS transactions(
      transaction_id INTEGER PRIMARY KEY,
      book_id INTEGER,
      member_id INTEGER,
      borow_date DATE,
      return_date DATE,
      FOREIGN KEY(book_id) REFERENCES books(book_id),
      FOREIGN KEY (member_id) REFERENCES members(member_id)
      );"""


create_review_table = """
    CREATE TABLE IF NOT EXISTS reviews(
    review_id INTEGER PRIMARY KEY,
    book_id INTEGER,
    member_id INTEGER,
    review_text TEXT,
    rating INTEGER,
    FOREIGN KEY(book_id) REFERENCES books(book_id),
    FOREIGN KEY (member_id) REFERENCES members(member_id)
    );"""

# my_cursor.execute(create_book_table)
# my_cursor.execute(create_author_table)
# my_cursor.execute(create_members_table)
# my_cursor.execute(create_transaction_table)
# my_cursor.execute(create_review_table)

# my_cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
# print(my_cursor.fetchall())
#
# # delete a table
# my_cursor.execute("DROP TABLE IF EXISTS books")
# my_cursor.execute("DROP TABLE IF EXISTS authors")
# my_cursor.execute("DROP TABLE IF EXISTS members")
# my_cursor.execute("DROP TABLE IF EXISTS transactions")
# my_cursor.execute("DROP TABLE IF EXISTS reviews")
# print(my_cursor.fetchall())