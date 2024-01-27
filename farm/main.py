# Import what we need from flask
from flask import Flask, render_template, redirect, url_for

# Create a Flask app inside `app`
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", title="Index")

@app.route("/home", methods=["GET"])
def home():
    return redirect(url_for("index"), 302)

@app.route("/animals", methods=["GET"])
def about():
    return render_template("animals.html", title="Animals")

@app.route("/farm", methods=["GET"])
def about():
    return render_template("farm.html", title="Farm")
