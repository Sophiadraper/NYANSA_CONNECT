#hello world
import requests
from flask import Flask, render_template, request


app = Flask("MyApp")

@app.route("/<name>")
def hello_someone(name):
    return render_template("hello.html", name=name.title())

@app.route("/")
def hello():
    return hello_someone("")

@app.route("/signup", methods=["POST"])
def sign_up():
    form_data = request.form
    send_simple_message(form_data["email"])
    print form_data["email"]
    return "All OK"


app.run(debug=True)
