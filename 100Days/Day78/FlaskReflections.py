from flask import Flask

app = Flask(__name__, static_url_path='/static')

myReflections = {} ## initialize an empty dictionary

# populate the dictionary with subdictionaries for each day and its attributes
myReflections["78"] = {"date": "September 27, 12023", "reflect": " Well it took a little bit of debugging troubleshooting and reverse engineering but finally I powered through. I don't particularly see much use in this program right now, however. Other people who went through the 100 days challenge found an intriguing solution to technically meet the requirements of the challenge without having to keep up and add a reflection every day until the end. I saw one that did this by using a message that said that the day's challenge was incredibly complicated if it was an even-numbered day and that it was smooth-sailing if it was an odd-numbered day.", "link": "https://replit.com/@JosephBrockly-A/Flask-Reflections-Day-78-of-100#main.py"}

@app.route('/')
def home():
  help = "This is left blank on purpose. To continue, type a number (78) after the URL of this webpage."
  return help

@app.route('/<pageNumber>') ## use the <> to define a variable
def index(pageNumber): ## pass the variable within the function
  css = "reflection.css"
  
  page = "" ## initialize a blank variable to store our HTML
  f = open("templates/reflection.html", "r") ## load the template
  page = f.read() ## read the template's HTML into the `page` variable
  f.close()

  page = page.replace("{day}", pageNumber)
  page = page.replace("{date}", myReflections[pageNumber]["date"])
  page = page.replace("{reflect}", myReflections[pageNumber]["reflect"])
  page = page.replace("{link}", myReflections[pageNumber]["link"])
  page = page.replace("{css}", css)
  return page

app.run(host='0.0.0.0',port=81)
