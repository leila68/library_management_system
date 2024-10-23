
# my_cursor.executemany("INSERT INTO patients(NAME, EMAIL, PHONE_NUMBER, PROBLEM, DOCTOR_ID) VALUES (?,?,?,?,?)", patient_values)
# my_cursor.execute("SELECT * FROM patients")
# print(my_cursor.fetchall())

author_values = [
    (1, 'Lili', 'Iran', 1989),
]

book_values = [
    ('My life', 1, 1999, 'Biography', 10),
]

member_values = [
    ('Mike', 2010, 'mike@gmail.com', 8643450909),
]

transaction_values = [
    (1, 1, 2023, 2024, ),
]

review_values = [
    (1, 1, 'Good', 5)
]