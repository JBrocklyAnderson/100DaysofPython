from flask import Flask, request

## call server
app = Flask(__name__, static_url_path="/static")

## handle the form
@app.route("/process", methods=["POST"])
def process():
  form = request.form

  checkedLaws = form.getlist("laws")
  first = "First Law" in checkedLaws
  second = "Second Law" in checkedLaws
  third = "Third Law" in checkedLaws
  fourth = "Fourth Law" in checkedLaws
  fifth = "Fifth Law" in checkedLaws

  type = ["thirteen-twelve", "thirteen twelve", "one three one two", "one-three-one-two"]
  typedNumber = form["typed-number"].lower()
  
  if form["electric-dreams"] == "yes" or form["electric-dreams"] == "no": ## if form is either "yes" or "no"
    if first and second and third and not fourth and not fifth: ## and if only the three Laws are chosen
      if typedNumber not in type: ## and if the robot doesn't type correctly
        return "Bienvenue, le petit robot!"
      else:
        return "Bienvenue, cher humain!"
    else:
      return "Bienvenue, cher humain!"
  else:
    return "Bienvenue, cher humain!"

## define index page
@app.route('/')
def question():
  css = "captcha.css" 
  page = "" ## initilialize blank page

  ## read in the file
  with open("static/html/captcha.html") as f:
    page = f.read()
    
  page = page.replace("{css}", css) ## access the CSS
  return page

app.run(host="0.0.0.0", port=81) ## run server