from flask import Flask, request, redirect, session
from replit import db
import random, os

app = Flask(__name__, static_url_path='/static')
app.secret_key = os.environ["sessionKey"] ## initialize a session key

@app.route('/')
def index():
  if session.get("loggedIn"): ## if user is logged in
    return redirect('/home')
    
  page = ""
  with open("template/index.html") as f:
    page = f.read()
  return page


@app.route('/signup', methods=["POST"])
def createUser():
  if session.get("loggedIn"): ## if user is logged in
    return redirect('/home')
  
  keys = db.keys()
  form = request.form

  salt = random.randint(1, 1000000)
  saltedPW = f"{form['password']}{salt}"
  hashedPW = hash(saltedPW)
  
  
  if form["username"] not in keys: ## storing hashed and salted passwords
    db[form["username"]] = {"name": form["name"], 
                            "salt": salt,
                            "password": hashedPW}
    return redirect('/account-success')
  else:
    return redirect('/account-already-exists')

@app.route('/signup')
def signup():
  if session.get("loggedIn"): ## if user is logged in
    return redirect('/home')
    
  page= ""
  with open("template/signup.html") as f:
    page = f.read()
  return page


## login processing page
@app.route('/login', methods=["POST"])
def verify():
  if session.get("loggedIn"): ## if user is logged in
    return redirect('/home')
    
  keys = db.keys()
  form = request.form

  if form["username"] not in keys:
    return redirect('/signup-request')
  else: ## hashing and salting
    salt = db[form["username"]]["salt"]
    saltedPW = f"{form['password']}{salt}"
    hashedPW = hash(saltedPW)
    ## checking against stored values
    if hashedPW == db[form["username"]]["password"]:
      session["loggedIn"] = db[form["username"]]["name"]
      return redirect('/home')
    else:
      return redirect('/auth-fail')

## login page
@app.route('/login')
def login():  
  if session.get("loggedIn"): ## if user is logged in
    return redirect('/home')
  
  page = ""
  with open("template/login.html") as f:
    page = f.read()
  return page

## landing page once logged in
@app.route('/home')
def home():  
  name = session.get("loggedIn")
  page = ""
  with open("template/home.html") as f:
    page = f.read()
    
  page = page.replace("{name}", name)
  return page

## the username used to sign up already exists
@app.route('/account-already-exists')
def accountAlreadyExists():  
  page = ""
  with open("template/account-exists.html") as f:
    page = f.read()
  return page

## the username used to login doesn't exist yet
@app.route('/signup-request')
def signupRequest():
  page = ""
  with open("template/signup-request.html") as f:
    page = f.read()
  return page

## either username or password are incorrect 
@app.route('/auth-fail')
def authFail():
  page = ""
  with open("template/auth-fail.html") as f:
    page = f.read()
  return page

## signup is successful
@app.route('/account-success')
def accountSuccess():
  page = ""
  with open("template/account-success.html") as f:
    page = f.read()
  return page

## to logout
@app.route('/logout')
def logout():
  session.clear()
  return redirect('/')

app.run(host='0.0.0.0', port=81)
