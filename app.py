import datetime, json, os
from flask import Flask, render_template, request,  redirect, url_for, flash

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")
