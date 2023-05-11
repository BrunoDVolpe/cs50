import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # TODO: Add the user's entry into the database
        name = request.form.get("name")
        if not name:
            return redirect("/")

        birthday = request.form.get("birthday")
        if birthday == '':
            return redirect("/")

        _, month, day = birthday.split("-")

        db.execute("INSERT INTO birthdays (name, month, day) VALUES (?, ?, ?)", name, int(month), int(day))
        return redirect("/")

    else:

        # TODO: Display the entries in the database on index.html
        birthdays = db.execute("SELECT * FROM birthdays")
        return render_template("index.html", birthdays=birthdays)

@app.route("/delete", methods=['POST'])
def delete():
    id = request.form.get("birthday_id")
    if not id:
        return redirect("/")
    db.execute("DELETE FROM birthdays WHERE id = ?", int(id))
    return redirect("/")

@app.route("/edit", methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        name = request.form.get("name")
        if not name:
            return redirect("/")

        birthday = request.form.get("birthday")
        if birthday == '':
            return redirect("/")

        _, month, day = birthday.split("-")

        id = request.form.get("birthday_id")
        if not id:
            return redirect("/")

        db.execute("UPDATE birthdays SET name = ?, month = ?, day = ? WHERE id = ?", name, int(month), int(day), int(id))
        return redirect("/")

    else:
        id = request.args.get("birthday_id")
        birthdays = db.execute("SELECT * FROM birthdays WHERE id = ?", int(id))

        try:
            id, name, month, day = birthdays[0].values()
        except:
            return redirect("/")
        month = f"{month:02}"
        day = f"{day:02}"
        return render_template("edit.html", id=id, name=name, month=month, day=day)