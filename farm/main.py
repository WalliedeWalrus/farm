# Import what we need from flask
from flask import Flask, render_template, redirect, url_for

# Create a Flask app inside `app`
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", name_browser_tab="Index")


@app.route("/home")
def home():
    return redirect(url_for("index"))


@app.route("/farm")
def about():
    return render_template("farm.html", name_browser_tab="Farm")


@app.route("/animals")
def cow():
    return render_template("animals.html", name_browser_tab="Animals")
