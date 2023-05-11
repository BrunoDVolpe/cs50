import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    # Getting user's stocks
    wallet = []
    wallet_total = 0
    rows = db.execute("SELECT symbol, shares FROM wallet WHERE user_id = ?", session["user_id"])

    # Getting info from each stock
    for stock in rows:
        quote = lookup(stock["symbol"])
        stock_total = stock["shares"] * quote["price"]
        wallet_total += stock_total

        # Joining info from user's stock
        wallet.append({
            "symbol": stock["symbol"],
            "name": quote["name"],
            "shares": stock["shares"],
            "price": usd(quote["price"]),
            "total": usd(stock_total)
        })

    # Getting user's cash
    rows = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
    cash = rows[0]['cash']

    return render_template("index.html", wallet=wallet, cash=usd(cash), total=usd(wallet_total + cash))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure symbol was submitted
        if not request.form.get("symbol"):
            return apology("Missing symbol")

        # Ensure shares value was submitted
        if not request.form.get("shares"):
            return apology("Missing shares")

        # Ensure symbol is valid
        if not lookup(request.form.get("symbol")):
            return apology("Invalid symbol. Please, try again")

        # Ensure shares are valid (positive integer number)
        if not request.form.get("shares").strip().isdecimal():
            return apology("Invalid share number.")

        # Getting user's and stock's actual data
        shares = int(request.form.get("shares").strip())
        stock = lookup(request.form.get("symbol"))
        rows = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        user_cash = rows[0]['cash']

        # Check if user has enough money for transaction
        if shares * stock['price'] > user_cash:
            return apology("Not enough money")

        # Saving transaction and updating user's cash
        db.execute("INSERT INTO transactions (user_id, op_type, symbol, company, price, shares) VALUES (?, ?, ?, ?, ?, ?)",
                   session["user_id"], "buy", stock['symbol'], stock['name'], stock['price'], shares)

        # Updating user's cash
        db.execute("UPDATE users SET cash = ? WHERE id = ?", user_cash - shares * stock['price'], session["user_id"])

        # Updating user's wallet
        rows = db.execute("SELECT * FROM wallet WHERE user_id = ? AND symbol = ?", session["user_id"], stock['symbol'])
        if len(rows) == 0:
            db.execute("INSERT INTO wallet (user_id, symbol, shares) VALUES (?, ?, ?)",
                       session["user_id"], stock['symbol'], shares)

        elif len(rows) == 1:
            updated_shares = rows[0]['shares'] + shares
            db.execute("UPDATE wallet SET shares = ? WHERE user_id = ? AND symbol = ?",
                       session["user_id"], stock['symbol'], updated_shares)
        else:
            print("wallet rows different from 0 or 1",
                  "which means something wrong in the database or updating process at buy function")
            return apology("Server error", 500)

        # Redirect user to index / home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or by redirect)
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    # Getting user's transactions
    transactions = db.execute("SELECT * FROM transactions WHERE user_id = ?", session["user_id"])

    # Changing price to display correctly
    for transaction in transactions:
        transaction["price"] = usd(transaction["price"])

    return render_template("history.html", transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    # User reached route via POST (as by submiting a form via POST)
    if request.method == "POST":

        # Ensure Symbol was submited
        if not request.form.get("symbol"):
            return apology("Must provide Stock Symbol")

        # Getting quote via API
        quote = lookup(request.form.get("symbol"))

        # Ensure Symbal is valid
        if not quote:
            return apology("Invalid Symbol")

        # Rendering information
        return render_template("quoted.html",
                               name=quote['name'], symbol=quote['symbol'], price=usd(quote['price']))

    else:
        # User reached route via GET (as by clicking a link or via redirect)
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # Ensure hash was submitted
        elif not request.form.get("password"):
            return apology("must provide password")

        # Ensure confirm password was submitted
        elif not request.form.get("confirmation"):
            return apology("must confirm password")

        # Ensure password == confirm password
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("Those passwords didn't match. Please, try again.")

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))

        # Ensure username don't exist
        if len(rows) != 0:
            return apology("That username is taken. Please, try another.")

        # Store username and password's hash
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", request.form.get("username"),
                   generate_password_hash(request.form.get("password")))

        # Get users id and remember log in from the new user
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
        session["user_id"] = rows[0]["id"]

        # Redirect new user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    # User reached route via POST (as by submitting a post form)
    if request.method == "POST":

        # Ensure symbol was submitted
        if not request.form.get("symbol"):
            return apology("must select symbol")

        # Ensure user has submitted a symbol available into his wallet
        rows = db.execute("SELECT * FROM wallet WHERE user_id = :id", id=session["user_id"])
        if request.form.get("symbol") not in [stock['symbol'] for stock in rows]:
            return apology("you don't have this symbol into your wallet")

        # Ensure shares was submited
        if not request.form.get("shares"):
            return apology("must provide number of shares")

        # Ensure shares is valid (positive integer)
        if not request.form.get("shares").isdecimal():
            return apology("must provide a positive and integer number of shares")

        # Ensure user has available quantity into his wallet
        rows = db.execute("SELECT * FROM wallet WHERE user_id = :id AND symbol = :symbol",
                          id=session["user_id"], symbol=request.form.get("symbol"))

        if len(rows) != 1:  # Validating possible db error
            return apology(code=500)

        if rows[0]["shares"] < int(request.form.get("shares")):
            return apology(
                f"Not enough shares. You only have {rows[0]['shares']} {request.form.get('symbol')} shares into your wallet")

        # stock actual quote
        quote = lookup(request.form.get("symbol"))

        # Update transactions
        db.execute("INSERT INTO transactions (user_id, op_type, symbol, company, price, shares) VALUES (?, ?, ?, ?, ?, ?)",
                   session["user_id"], "sell", quote["symbol"], quote["name"], quote["price"], int(request.form.get("shares")))

        # Update user's wallet
        stocks = db.execute("SELECT shares FROM wallet WHERE user_id = ? AND symbol = ?", session["user_id"], quote["symbol"])

        # Dropping row if 0 shares
        if stocks[0]["shares"] - int(request.form.get("shares")) == 0:
            db.execute("DELETE FROM wallet WHERE user_id = :id AND symbol = :symbol",
                       id=session["user_id"], symbol=quote["symbol"])

        else:
            db.execute("UPDATE wallet SET shares = ? WHERE user_id = ? AND symbol = ?",
                       stocks[0]["shares"] - int(request.form.get("shares")), session["user_id"], quote["symbol"])

        # Update user's cash
        rows = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        cash = rows[0]['cash']
        new_cash = cash + int(request.form.get("shares")) * quote["price"]
        db.execute("UPDATE users SET cash = :cash WHERE id = :user_id", cash=new_cash, user_id=session["user_id"])

        # Redirect user to home / index page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        # Getting user's available symbols
        rows = db.execute("SELECT symbol FROM wallet WHERE user_id = ?", session["user_id"])

        return render_template("sell.html", wallet=rows)


@app.route("/change_password", methods=["GET", "POST"])
@login_required
def change_password():
    """Change user's password"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure hash was submitted
        if not request.form.get("password"):
            return apology("must provide password")

        # Ensure new hash was submitted
        elif not request.form.get("new_password"):
            return apology("must provide new password")

        # Ensure confirm was submitted
        elif not request.form.get("confirmation"):
            return apology("must confirm new password")

        # Ensure submitted password is user's password
        rows = db.execute("SELECT hash FROM users WHERE id = ?", session["user_id"])
        if not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("Incorrect password.")

        # Ensure new_password and confirmation are the same
        elif request.form.get("new_password") != request.form.get("confirmation"):
            return apology("New password and confirmation didn't match. Please, try again.")

        # Store new password's hash
        db.execute("UPDATE users SET hash = :new_hash WHERE id = :id",
                   new_hash=generate_password_hash(request.form.get("new_password")), id=session["user_id"])

        # Redirect new user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("change_password.html")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
