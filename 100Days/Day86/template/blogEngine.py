from replit import db
from flask import Flask, redirect, request, session
import os

app = Flask(__name__, static_url_path='/static')
app.secret_key = os.environ["sessionKey"] ## setting a secure session key

def getBlogs():
  entry = "" ## read in the blog entry template
  with open("template/blog-entries.html") as f:
    entry = f.read()

  content = "" ## initialize container for processed blog entries
  keys = db.keys() 
  keys = list(keys) ## convert keys into a list to be sorted
  for key in reversed(keys): ## iterate over keys in reverse order
    thisEntry = entry ## copy the `entry` template for the current blog post being processed
    if key != "user": ## avoid calling in my login info
      thisEntry = thisEntry.replace("{title}", db[key]["title"]) ## replace the placeholders in `blog-entries.html` 
      thisEntry = thisEntry.replace("{date}", db[key]["date"])
      thisEntry = thisEntry.replace("{text}", db[key]["text"])
      content += thisEntry ## append blog entries to the container
  return content    

@app.route('/')
def index():
  if session.get("logged-in"): ## if I'm already logged in
    return redirect('/home')
    
  page = ""
  with open('template/index.html') as f:
    page = f.read()
  page = page.replace("{content}", getBlogs())
  return page

@app.route('/login', methods=["POST"])
def login():
  if session.get("logged-in"): ## if I'm already logged in
    return redirect('/home')
    
  form = request.form ## pull in form data
  saltedPW = f"{form['password']}{db['user']['salt']}"
  hashedPW = hash(saltedPW)
  if db["user"]["username"] == form["username"] and hashedPW == db["user"]["password"]: ## verifying login
    session["logged-in"] = True ## initializing session
    return redirect('/home')
  else:
    return redirect('/login-fail')

@app.route('/home')
def home():  
  if not session.get("logged-in"): ## if not logged in
    return redirect('/')
    
  page = ""
  with open('template/home.html') as f:
    page = f.read()
  page = page.replace("{content}", getBlogs())
  return page

@app.route('/login-fail')
def loginFail():
  page = ""
  with open('template/login-fail.html') as f:
    page = f.read()
  return page

@app.route('/logout')
def logout():
  session.clear() ## clearing session data
  return redirect('/')

@app.route('/add', methods=["POST"])
def add():
  if not session.get("logged-in"): ## if not logged in
    return redirect('/')
    
  form = request.form
  entry = {"title": form["title"],
           "date": form["date"],
           "text": form["text"]}
  db[form["title"]] = entry ## appending blog post as a subdictionary in the database
  return redirect('/home')
 
app.run(host='0.0.0.0', port=81)
