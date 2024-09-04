import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

# CREATE TABLES
c.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY,
    title TEXT,
    content TEXT,
    user_id INTEGER,
    FOREIGN KEY(user_id) REFERENCES users(id)
)
""")
# POPULATE TABLES
for i in range(10):
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (f'user{i}', f'password{i}'))
    c.execute("INSERT INTO posts (title, content, user_id) VALUES (?, ?, ?)", (f'title{i}', f'content{i}', i + 1))

conn.commit()

# Sample INNER JOIN query
query = """
    SELECT *
    FROM users
    INNER JOIN posts
    ON users.id = posts.user_id
    WHERE users.id > 5
    ORDER BY users.id ASC
"""

result = c.execute(query)
rows = result.fetchall()
if rows:
    print(rows)
else:
    print("No results found.")

c.close()
conn.close()

