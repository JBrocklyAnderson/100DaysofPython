import requests, os, json ## to pull data from the API
from flask import Flask, request ## to develop the web app
from datetime import datetime as dt
from replit import db ## to manage offsets
from requests.auth import HTTPBasicAuth ## attaches basic authentication to the given request object

def tracks(year):
  clientId = os.environ['CLIENT_ID'] ## "username"
  clientSecret = os.environ['CLIENT_SECRET'] ## "password"
  
  url = "https://accounts.spotify.com/api/token" ## where to get the token
  data = {"grant_type": "client_credentials"} ## what to get
  auth = HTTPBasicAuth(clientId, clientSecret) ## authentifies my permission to send the request
  
  response = requests.post(url, data = data, auth = auth) ## stores the response
  ## print(response.ok) ## check if the call is working
  ## print(response.json())
  ## print(response.status_code)
  accessToken = response.json()["access_token"] ## grab the token
  
  ## artist = input("Artist: ").lower() ## to transform artists whose name contains spaces into usable query syntax
  ## artist = artist.replace(" ", "%20")
  type = "track"
  limit = 10
  
  offset = 0 ## set initial offset value
  try:
    offset = db[year] ## 
    if offset >= 100:
      db[year] = 0
      offset = 0
    db[year] += 10
  except:
    db[year] = 10
  
  url = "https://api.spotify.com/v1/search" ## search endpoint
  headers = {"Authorization": f"Bearer {accessToken}"} ## ensure every request is authorized
  ## searchArtist = f"?q=artist%3A{artist}&type=track&limit=10" ## search query syntax
  searchYear = f"?q=year%3A{year}&type={type}&limit={limit}&offset={offset}" ## scaffold the query syntax
  
  fullURL = f"{url}{searchYear}" ## append the query to the endpoint
  
  response = requests.get(fullURL, headers=headers) ## get the response
  data = response.json() ## pull it into JSON 
  ## print(json.dumps(data, indent=2)) ## organize the JSON

  count = offset ## set count equal to offset
  songs = "" ## read the file into an empty variable
  with open("templates/songs.html") as f:
    songs = f.read()
  songList = "" ## initialize a container with which to append requested songs
  for track in data["tracks"]["items"]:
    count += 1 ## keep track of the song number
    newTrack = songs ## make a copy of the file
    newTrack = newTrack.replace("{name}", f"""{count}. {track['name']} by {track['artists'][0]['name']} from their album {track['album']['name']}""")
    newTrack = newTrack.replace("{url}", f"{track['preview_url']}")
    songList += newTrack ## append each new track to the song list
  return songList

#####

app = Flask(__name__, static_url_path='/static')

currentYear = dt.now() ## to use as a placeholder and maximum value
currentYear = currentYear.strftime("%Y") ## display it as a year

@app.route('/')
def index():
  page = '' ## open file into container
  with open("templates/form.html") as f:
    page = f.read()
  page = page.replace("{songs}", "") ## hide "{songs}" when none have been called
  page = page.replace("{currentYear}", currentYear)
  return page

@app.route('/', methods=["POST"])
def change():
  page = '' ## open file into container
  with open("templates/form.html") as f:
    page = f.read()
  year = request.form["year"] ## grab form data
  songs = tracks(year) ## plug the year into the API request subroutine
  page = page.replace("{year}", year)
  page = page.replace("{currentYear}", currentYear)
  page = page.replace("{songs}", songs)
  return page

app.run(host='0.0.0.0', port=81)