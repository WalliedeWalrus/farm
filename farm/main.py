# Import what we need from flask
from flask import Flask, render_template, redirect, url_for

# Create a Flask app inside `app`
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", title="Index")
