from flask import Flask, render_template, redirect, request, url_for
import sqlite3

app = Flask(__name__)
conn = sqlite3.connect("Trip.db", check_same_thread=False)
c = conn.cursor()


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        date = request.form["date"]
        tmp = date.split("-")
        date = tmp[2] + tmp[1] + tmp[0]
        print(date)
        res = c.execute(
            "SELECT Name, DepartCity, ArrivalCity, Seat FROM (Ticket JOIN Flight ON Ticket.FlightNO = Flight.FlightNO) JOIN Customer ON Customer.CustomerNO = Ticket.CustomerNO WHERE Date = ?",
            (date,),
        ).fetchall()
        print(res)
        return render_template("result.html", res=res)
    return render_template("index.html")


app.run(debug=True)
