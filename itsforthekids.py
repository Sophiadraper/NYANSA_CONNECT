@app.route("/signup", methods=["POST"])
def sign_up():
form_data = request.form
print form_data["email"]
return "All OK"
