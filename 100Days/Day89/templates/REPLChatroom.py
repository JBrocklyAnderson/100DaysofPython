from flask import Flask, request, redirect
from replit import db
from datetime import datetime as dt

app = Flask(__name__, static_url_path='/static')

#db.clear()



def getChats():
  message = ""
  with open("templates/message.html") as f:
    message = f.read() ## read in message template

  userID = request.headers["X-Replit-User-Id"] ## set up a userID variable
  
  keys = db.keys()
  keys = list(keys) ## convert keys into a list for sorting
  result = ""
  for key in reversed(keys): ## sort keys in reverse chronological order
    newMessage = message ## create copy of template
    newMessage = newMessage.replace("{profileImage}", db[key]["profilePic"]) ## overwrite template with relevant details
    newMessage = newMessage.replace("{user}", db[key]["username"])
    newMessage = newMessage.replace("{timestamp}", db[key]["date"])
    newMessage = newMessage.replace("{message}", db[key]["message"])
    
    if userID != "25656223": ## hide delete button from non-admins
      newMessage = newMessage.replace("{admin}", "")
    elif userID == "25656223": ## display delete button to admin
      newMessage = newMessage.replace("{admin}", f"""<a href='/delete?id={key}'> ⛔</a>""")
    result += newMessage ## append message to resultant page
    print(newMessage)
    print(userID)
  return result

@app.route('/')
def home():
  userID = request.headers["X-Replit-User-Id"] ## set up user ID variable
  if userID: ## Replit users will be taken to the chatroom
    return redirect('/chatroom')
  
  page = ""
  with open("templates/index.html") as f:
    page = f.read()
  return page

@app.route('/chatroom')
def chatroom():
  userID = request.headers["X-Replit-User-Id"] ## set up user ID variable
  if not userID: ## non-Replit users will be kicked out
    return redirect('/')
  
    
  with open("templates/chatroom.html") as f:
    page = f.read()
  page = page.replace("{username}", request.headers["X-Replit-User-Name"]) 
  page = page.replace("{chats}", getChats()) ## generate message logs
  return page
  
@app.route('/add', methods=["POST"])
def addChat():
  form = request.form ## pull in form data
  message = form["message"] ## access message
  date = dt.now()
  timestamp = dt.timestamp(date) ## convert datetime object into a single float
  userID = request.headers["X-Replit-User-Id"]
  username = request.headers["X-Replit-User-Name"]
  profilePic = request.headers["X-Replit-User-Profile-Image"]
  print(profilePic)  

  db[timestamp] = {"date": date.strftime('1%Y-%m-%d %H:%M:%S'), "userid": userID, "username": username, "profilePic": profilePic, "message": message} ## construct the subdictionary for the timestamp key value
  return redirect('/chatroom')

@app.route('/delete', methods=["GET"])
def delete():
  userID = request.headers["X-Replit-User-Id"] ## set up user ID variable
  if userID != "25656223": ## non-admins will be kicked back to the chatroom
    return redirect('/chatroom')
  else: 
    results = request.values["id"] ## grab the timestamp key set in the URL 
    del db[results] ## delete the key
    return redirect('/chatroom') ## return to the chatroom
    

app.run(host='0.0.0.0', port=81, debug=True)
