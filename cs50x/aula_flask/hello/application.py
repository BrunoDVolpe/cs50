from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# Rota GET, lembrando que methods=["GET"] é opcional já que ele é o padrão caso o método não seja informado.
"""
@app.route("/greet")
def greet():
    return render_template("greet.html", first_name=request.args.get("first_name", "world"))
"""
# Método POST
@app.route("/greet", methods=["POST"])
def greet():
    return render_template("greet.html", first_name=request.form.get("first_name", "world"))