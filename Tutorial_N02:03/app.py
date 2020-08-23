from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

@app.route("/")
def home:
    render_template("home.html")

@app.route("/about/")
def about:
    render_template("about.html")

@app.route("/rp_calc/")
def rp_calc:
    render_template("rp_calc")