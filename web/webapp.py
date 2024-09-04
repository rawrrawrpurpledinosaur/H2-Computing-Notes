from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
conn = sqlite3.connect('database.db')
c = conn.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    return render_template('login.html')

@app.route('/register', methods=['POST'])
def register():
    return render_template('register.html')

app.run(debug=True)
