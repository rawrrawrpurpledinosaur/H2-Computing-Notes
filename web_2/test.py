import sqlite3

# show all tables in the db, and their tables and columns
conn = sqlite3.connect("JPFashion.db")
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
for table_name in tables:
    table_name = table_name[0]
    print(table_name)
    cursor.execute("PRAGMA table_info({})".format(table_name))
    columns = cursor.fetchall()
    for column in columns:
        print(" ", column)
cursor.close()
conn.close()
