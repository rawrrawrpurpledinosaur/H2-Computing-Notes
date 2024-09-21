import sqlite3


conn = sqlite3.connect("Trip.db")
cursor = conn.cursor()
res = cursor.execute("SELECT * FROM Flight").fetchall()
for row in res:
    print(row)
