@app.route("/signup", methods=["POST"])
def sign_up():
form_data = request.form
print form_data ["submit"]
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
def send_simple_message():
	return requests.post(
		"https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages",
		auth=("api", "fe701f7c75c69830c5d85c787cc9555c-52b0ea77-c0328086"),
		data={"from": "Excited User <mailgun@https://api.mailgun.net/v3/sandboxb471aba1ce164154a7799313792615aa.mailgun.org>",
			"to": ["bar@example.com", "YOU@YOUR_DOMAIN_NAME"],
			"subject": "Hello",
			"text": "Testing some Mailgun awesomness!"})
