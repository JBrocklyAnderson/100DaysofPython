from flask import Flask, request, redirect, url_for

app = Flask(__name__, static_url_path='/static')

accounts = {}

accounts["username1"] = {"email": "username1@gmail.com", "password": "password1"}
accounts["username2"] = {"email": "username2@gmail.com", "password": "password2"}
accounts["username3"] = {"email": "username3@gmail.com", "password": "password3"}

"""
@app.route("/process", methods=["GET"])
def processGET():
  return redirect(url_for('login'))
"""

@app.route("/process", methods=["POST"])
def process():
  form = request.form
  
  realAccount = False
  details = {}
  try:
    details = accounts[form["username"]]
    realAccount = True
  except:
    return "Username, email, or password incorrect. Try again."
  if form["email"] == details["email"] and form["password"] == details["password"]:
    return "Login successful."
  else:
    return "Username, email, or password incorrect. Try again."
  




@app.route('/')
def login():
  css = "login.css"
  
  page = ""
  with open("static/html/login.html", "r") as f:
    page = f.read()

  page = page.replace("{css}", css)
  return page

  
app.run(host='0.0.0.0', port=81)