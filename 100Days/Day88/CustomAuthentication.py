from replit import db
from flask import Flask, redirect, request

app = Flask(__name__, static_url_path='/static')


def getBlogs():
  entry = "" ## read in the blog entry template
  with open("templates/blog-entries.html") as f:
    entry = f.read()

  content = "" ## initialize container for processed blog entries
  keys = db.keys() 
  keys = list(keys) ## convert keys into a list to be sorted
  for key in reversed(keys): ## iterate over keys in reverse order
    thisEntry = entry ## copy the `entry` template for the current blog post being processed
    thisEntry = thisEntry.replace("{title}", db[key]["title"]) ## replace the placeholders in `blog-entries.html` 
    thisEntry = thisEntry.replace("{date}", db[key]["date"])
    thisEntry = thisEntry.replace("{text}", db[key]["text"])
    content += thisEntry ## append blog entries to the container
  return content    

@app.route('/')
def index():
  userID = request.headers["X-Replit-User-Id"] 
  if userID == "25656223": ## if I'm already logged in
    return redirect('/home')
    
  page = ""
  with open('templates/index.html') as f:
    page = f.read()
  page = page.replace("{content}", getBlogs())
  return page

@app.route('/home')
def home():  
  userID = request.headers["X-Replit-User-Id"] 
  username = request.headers["X-Replit-User-Name"]
  if userID != "25656223": ## if I'm already logged in
    return redirect('/')
    
  page = ""
  with open('templates/home.html') as f:
    page = f.read()
  page = page.replace("{username}", username)
  page = page.replace("{content}", getBlogs())
  return page

@app.route('/add', methods=["POST"])
def add():
  userID = request.headers["X-Replit-User-Id"] 
  if userID != "25656223": ## if I'm already logged in
    return redirect('/')
    
  form = request.form
  entry = {"title": form["title"], "date": form["date"], "text": form["text"]}
  db[form["title"]] = entry ## appending blog post as a subdictionary in the database
  return redirect('/home')
 
app.run(host='0.0.0.0', port=81)