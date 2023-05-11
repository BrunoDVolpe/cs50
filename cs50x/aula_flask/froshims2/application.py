import os

from cs50 import SQL
from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message

app = Flask(__name__)
app.config["MAIL_DEFAULT_SENDER"] = os.getenv("MAIL_DEFAULT_SENDER") #os.getenv() é uma forma de pegar dados do sistema sem que precisem ficar explícitos no arquivo
app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")
app.config["MAIL_PORT"] = 587
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")
mail = Mail(app)

db = SQL("sqlite:///froshims.db")

SPORTS = [
    "Dodgeball",
    "Flag Football",
    "Soccer",
    "Volleyball",
    "Ultimate Frisbee",
]

# Versão 2, iterando direto com Flask
@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    if not name:
        return render_template("error.html", message="Missing name")
    email = request.form.get("email")
    if not email:
        return render_template("error.html", message="Missing email")
    sport = request.form.get("sport")
    if not sport:
        return render_template("error.html", message="Missing sport")
    if sport not in SPORTS:
        return render_template("error.html", message="Invalid sport")

    db.execute("INSERT INTO registrants (name, email, sport) VALUES(?, ?, ?)", name, email, sport)

    # David usou só o message abaixo e o send. Além disso, ele trocou name por email e tirou a página registrants.
    # Eu acrescentei email no contexto e peguei o que a documentação coloca. Como o meu os.getenv não tem email
    #  cadastrado, estou forçando aqui o bdva16...
    # Link: https://pythonbasics.org/flask-mail/
    #message = Message("You are registered!", recipients=[email])
    message = Message("You are registered!", sender = 'bdva16@hotmail.com', recipients=[email])
    message.body = "Hello Flask message sent from Flask-Mail"

    # Como o email precisa de mais configurações, coloquei uma condição de contorno
    try:
        mail.send(message)
    except:
        print("Error: Email not sent")
    return redirect("/registrants")

@app.route("/registrants")
def registrants():
    registrants = db.execute("SELECT * FROM registrants")
    return render_template("registrants.html", registrants=registrants)

"""
# Versão 1, onde tivemos o hack
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    if not request.form.get("name") or not request.form.get("sport"):
        return render_template("failure.html")
    return render_template("success.html")
"""