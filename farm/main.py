# Import what we need from flask
from flask import Flask, render_template, redirect, url_for

# Create a Flask app inside `app`
app = Flask(__name__)

@app.route("/home", methods=["GET"])
def home():
    return render_template("home.html", title="Home")

@app.route("/", methods=["GET"])
def farm():
    return render_template("farm.html", title="Farm")


@app.route("/about", methods=["GET"])
def animals():
    return render_template("animals.html", title="About")
