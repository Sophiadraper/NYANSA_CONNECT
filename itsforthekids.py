@app.route("/signup", methods=["POST"])
def sign_up():
form_data = request.form
print form_data ["email"]
return "Thank you for subscribing!"

@app.route("/<name>")
def hello_someone(name):
return render_template("itsforthekids.html", name=name.title())

app = Flask("MyApp")
@app.route("/")
def hello():
return "itsforthekids.html"
@app.route("/<name>")
def hello_someone(name):

return render_template("itsforthekids.html", name=name.title())

app.run(debug=True)
