from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)
conn = sqlite3.connect('students.db', check_same_thread=False)
c = conn.cursor()

# creating tables 
# c.execute("""
# CREATE TABLE IF NOT EXISTS Student (StudentID INTEGER, Name TEXT, Gender TEXT, PRIMARY KEY (StudentID)) 
# """)
#
# c.execute("""
# CREATE TABLE IF NOT EXISTS StudentHealthRecord (StudentID INTEGER, Weight INTEGER, Height INTEGER, FOREIGN KEY (StudentID) REFERENCES Student(StudentID))
# """)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/records')
def records():
    rec = c.execute("""
                    SELECT Name, Gender, Weight, Height
                    FROM Student JOIN StudentHealthRecord
                    ON Student.StudentID = StudentHealthRecord.StudentID
                    ORDER BY Gender ASC, Name DESC 
                    """).fetchall()
    print(rec)
    return render_template('records.html', records=rec)

@app.route('/stats')
def stats():
    num = c.execute("""
                    SELECT SUM(Gender = 'M' OR Gender = 'F'), AVG(Weight), AVG(Height) 
                    FROM Student JOIN StudentHealthRecord
                    ON Student.StudentID = StudentHealthRecord.StudentID
    """).fetchall()
    print(num)
    return render_template('stats.html', stats = num[0])

@app.route('/add', methods=['GET','POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        gender = request.form['gender']
        id = request.form['id']
        weight = request.form['weight']
        height = request.form['height']
        c.execute("""
        INSERT INTO Student (StudentID, Name, Gender) VALUES (?, ?, ?)
                """, (id, name, gender))
        c.execute("""
        INSERT INTO StudentHealthRecord (StudentID, Weight, Height) VALUES (?, ?, ?)
                """, (id, weight, height))
        conn.commit()
        conn.close()
        return redirect('/records')
    return render_template('add.html')

app.run(debug=True)
