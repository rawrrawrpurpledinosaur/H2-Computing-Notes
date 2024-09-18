from flask import Flask, request, redirect, render_template, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "capybara"


def get_cursor():
    conn = sqlite3.connect("JPFashion.db")
    return conn.cursor()


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        global email
        email = request.form["email"]
        # check if email in customer table
        c = get_cursor()
        res = c.execute(f"SELECT * FROM customer WHERE email='{email}'").fetchone()
        if res:
            flash("This email is already registered")
            return redirect(url_for("index"))
        else:
            return redirect(url_for("create"))
    return render_template("index.html")


@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        contact_number = request.form["contact_number"]
        dob = request.form["dob"]
        address = request.form["address"]
        c = get_cursor()
        c.execute(
            f"INSERT INTO customer (Email, FirstName, LastName, ContactNumber, DOB, Address) VALUES ('{email}', '{first_name}', '{last_name}', '{contact_number}', '{dob}', '{address}')"
        )
        c.connection.commit()
        flash("New account created successfully")
        return redirect(url_for("index"))
    return render_template("create.html")


@app.route("/rentalsdue", methods=["GET", "POST"])
def rentalsdue():
    if request.method == "POST":
        end_date = request.form["end_date"]
        c = get_cursor()
        res = c.execute(
            """
                  SELECT customer_rental.ID, product.CatalogueNumber, customer.Email, customer.ContactNumber 
        FROM ((customer JOIN customer_rental ON customer.Email = customer_rental.Email) 
              JOIN product_rental ON customer_rental.ID = product_rental.ID) 
        JOIN product ON product_rental.CatalogueNumber = product.CatalogueNumber 
        WHERE customer_rental.EndDate = ? AND product_rental.Returned = "FALSE"
        """,
            (end_date,),
        ).fetchall()
        return render_template("rentalsdue.html", res=res)
    return render_template("rentalsdue.html", res=None)


app.run(debug=True, port=5678)
