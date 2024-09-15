from flask import Flask, render_template, redirect, request, url_for
import sqlite3
import csv 

app = Flask(__name__)
conn = sqlite3.connect("Task4.db", check_same_thread = False)
c = conn.cursor()

# read books_data.txt and copies_data.txt
with open("books_data.txt", "r") as f: #file closes automatically
    data = csv.reader(f)
    for row in data:
        c.execute("""
        INSERT OR REPLACE INTO books(bookID, title, price) VALUES (?,?,?) """,(row[0], row[1], row[2])) 
        conn.commit()

with open("copies_data.txt", "r") as f1:
    data1 = csv.reader(f1)
    for row in data1:
        c.execute("""
        INSERT OR REPLACE INTO copies(copyID, bookID) VALUES (?,?)
                  """,(row[0], row[1]))
        conn.commit()






@app.route("/")
def index():
    return render_template("index.html")

@app.route("/insert", methods=["GET","POST"])
def insert():
    if request.method == "POST":
        bookID = request.form["bookID"]
        title = request.form["title"]
        price = request.form["price"]
        copies = int(request.form["copies"])
        copyID = []
        for i in range(copies): 
            num = "000" + str(i)
            copyID.append(num)
        c.execute("""
        INSERT OR REPLACE INTO books(bookID, title, price) VALUES (?, ?, ?)""", (bookID, title, price))
        conn.commit()
        for i in range(int(copies)):
            c.execute("""
            INSERT OR REPLACE INTO copies(copyID, bookID) VALUES (?,?)""", (copyID[i], bookID))
        conn.commit()
        return redirect(url_for("index"))
    return render_template("insert.html")

@app.route("/display", methods=["GET"])
def display():
    res = c.execute("""
    SELECT books.bookID, title, price, COUNT(copyID) 
    FROM books JOIN copies ON books.bookID = copies.bookID
    GROUP BY books.title
    ORDER BY title ASC
              """).fetchall()
    return render_template("display.html", res=res)

app.run(debug=True)
