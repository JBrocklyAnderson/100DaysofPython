from flask import Flask, request, redirect
from replit import db
import random

app = Flask(__name__, static_url_path='/static')


# db.clear()


@app.route('/')
def index():
  page = ""
  with open("template/index.html") as f:
    page = f.read()
  return page

@app.route('/signup', methods=["POST"])
def createUser():
  keys = db.keys()
  form = request.form

  salt = random.randint(1, 1000000)
  saltedPW = f"{form['password']}{salt}"
  hashedPW = hash(saltedPW)
  
  
  if form["username"] not in keys:
    db[form["username"]] = {"name": form["name"], 
                            "salt": salt,
                            "password": hashedPW}
    return redirect('/account-success')
  else:
    return redirect('/account-already-exists')

@app.route('/signup')
def signup():
  page= ""
  with open("template/signup.html") as f:
    page = f.read()
  return page

@app.route('/login', methods=["POST"])
def verify():
  keys = db.keys()
  form = request.form

  if form["username"] not in keys:
    return redirect('/signup-request')
  else:
    salt = db[form["username"]]["salt"]
    saltedPW = f"{form['password']}{salt}"
    hashedPW = hash(saltedPW)
    
    if hashedPW == db[form["username"]]["password"]:
      return redirect('/home')
    else:
      return redirect('/auth-fail')

@app.route('/login')
def login():
  page = ""
  with open("template/login.html") as f:
    page = f.read()
  return page

@app.route('/home')
def home():
  page = ""
  with open("template/home.html") as f:
    page = f.read()
  return page

@app.route('/account-already-exists')
def accountAlreadyExists():
  page = ""
  with open("template/account-exists.html") as f:
    page = f.read()
  return page

@app.route('/signup-request')
def signupRequest():
  page = ""
  with open("template/signup-request.html") as f:
    page = f.read()
  return page

@app.route('/auth-fail')
def authFail():
  page = ""
  with open("template/auth-fail.html") as f:
    page = f.read()
  return page

@app.route('/account-success')
def accountSuccess():
  page = ""
  with open("template/account-success.html") as f:
    page = f.read()
  return page


app.run(host='0.0.0.0', port=81)
  
