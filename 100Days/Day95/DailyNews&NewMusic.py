import requests, json, os, openai
from requests.auth import HTTPBasicAuth

NewsAPI_KEY = os.environ['NewsAPI_KEY']
openai.organization = os.environ['OpenAI_OrgID']
openai.api_key = os.environ['OpenAI_API_KEY']
openai.Model.list() ## send authentication request

country = "us"
url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={NewsAPI_KEY}"
response = requests.get(url) ## get results from NewsAPI query
data = response.json() ## retrieve JSON-encoded response content

max = 10
responses = []

counter = 0
for article in data["articles"]:
  counter += 1
  if counter >= max:
    break ## only print the first 10
  prompt = f"""Summarize {article['url']} in no more than four words."""
  response = openai.Completion.create(model="text-davinci-002", prompt=prompt, temperature = 0, max_tokens = 50) ## temperature is a measure of the tradeoff between coherence and creativity ## 50 tokens will generate around 38-word summaries
  #print(response["choices"][0]["text"].strip())
  responses.append[response["choices"][0]["text"].strip()]

clientId = os.environ['CLIENT_ID'] ## "username"
clientSecret = os.environ['CLIENT_SECRET'] ## "password"

url = "https://accounts.spotify.com/api/token" ## where to get the token
data = {"grant_type": "client_credentials"} ## what to get
auth = HTTPBasicAuth(clientId, clientSecret)

response = requests.post(url, data = data, auth = auth) ## stores the response
## print(response.ok) ## check if the call is working
## print(response.json())
## print(response.status_code)
accessToken = response.json()["access_token"] ## grab the token
headers = {"Authorization": f"Bearer {accessToken}"} ## ensure every request is authorized

type = "track"

for response in responses:
  headline = response.replace(" ", "%20")
  headline = response.replace(".", "")
  url = "https://api.spotify.com/v1/search" ## search endpoint
  search = f"?q={headline}&type={type}" ## scaffold the query syntax
  fullURL = f"{url}{search}"
  response = requests.get(fullURL, headers=headers) ## get the response
  data = response.json() ## pull it into JSON
 
songs = []
try:  
  songs.append(data["tracks"]["items"][0])
except:
  songs.append({"name": None, "preview_url": None})
  

for i in range(max):
  if songs[i]["name"] != None:
    print(f"""\033[32m{responses[i]}\033[0m\n{songs[i]["name"]}\n{songs[i]["preview_url"]}\n\n""")
  