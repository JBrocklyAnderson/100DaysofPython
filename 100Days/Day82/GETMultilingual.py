from flask import Flask, redirect, request

app = Flask(__name__, static_url_path="/static")

@app.route('/')
def english():
  return redirect("/language?lang=eng")

@app.route('/language', methods=["GET"])
def language():
  get = request.args
  
  if get["lang"] == "eng":
    return "Welcome to my website!"
  if get["lang"] == "esp":
    return "Bienvenido a mi sitio web"
  if get["lang"] == "中文":
    return "欢迎光临到我的网站！"
  if get["lang"] == "fr":
    return "Bienvenue sur mon site web!"
  

app.run(host='0.0.0.0', port=81)
