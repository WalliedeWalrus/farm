from flask import Flask, render_template, redirect, url_for

# Create a Flask app inside `app`
app = Flask(__name__)

# Assign a function to the different paths
@app.route("/")
def index():
    return render_template("index.html", name_browser_tab="Index")


@app.route("/home")
def home():
    return redirect(url_for("index"))


@app.route("/about")
def about():
    return render_template("about.html", name_browser_tab="About")


@app.route("/dog")
def dog():
    return render_template("dog.html", name_browser_tab="Dog")

@app.route("/pig")
def pig():
    return render_template("pig.html", name_browser_tab="Pig")