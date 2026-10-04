import sqlite3
import secrets
from flask import Flask
from flask import abort, url_for, redirect, render_template, request, session
from werkzeug.security import check_password_hash, generate_password_hash
import config
import db
import katas

app = Flask(__name__)
app.secret_key = config.secret_key

@app.route("/")
def index():
    katas = db.query("SELECT katas.*, users.username FROM katas JOIN users ON users.id = katas.user_id ORDER BY katas.id DESC")
    return render_template("index.html", katas=katas)

@app.route("/new_kata")
def new_kata():
    require_login()
    return render_template("new_kata.html")

@app.route("/create_kata", methods=["POST"])
def create_kata():
    require_login()
    check_csrf()
    title = request.form.get("title", "").strip()
    description = request.form.get("description", "").strip()
    if not title or len(title) > 50:
        return render_template("new_kata.html", title=title, description=description,
                               error="Nimen pituuden tulee olla 1–50 merkkiä."), 400
    if not description or len(description) > 500:
        return render_template("new_kata.html", title=title, description=description,
                               error="Kuvauksen pituuden tulee olla 1–500 merkkiä."), 400
    katas.add_kata(title, description, session["user_id"])
    return redirect("/")    

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/create", methods=["POST"])
def create():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1 != password2:
        return "VIRHE: salasanat eivät ole samat"
    password_hash = generate_password_hash(
    password1, method="pbkdf2:sha256:1000000"
    )

    try:
        sql = "INSERT INTO users (username, password_hash) VALUES (?, ?)"
        db.execute(sql, [username, password_hash])
    except sqlite3.IntegrityError:
        return "VIRHE: tunnus on jo varattu"

    return "Tunnus luotu"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        sql = "SELECT password_hash FROM users WHERE username = ?"
    password_hash = db.query(sql, [username])[0][0]

    if check_password_hash(password_hash, password):
        session["username"] = username
        return redirect("/")
    else:
        return "VIRHE: väärä tunnus tai salasana"

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")