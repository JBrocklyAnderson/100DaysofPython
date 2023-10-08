import requests, os, openai
from bs4 import BeautifulSoup

url = input("Enter wikipedia URL to summarize here:\n\n")
#url = "https://en.wikipedia.org/wiki/The_Last_Question"
response = requests.get(url) ## download the page
html = response.text ## extract the HTLM
soup = BeautifulSoup(html, "html.parser") ## parse the HTML
article = soup.find_all("div", {"class": "mw-parser-output"})[0] ## grab <div> elements with specified class
content = article.find_all("p") # grab <p> tags within the article

text = ""
for p in content:
  text += p.text ## append <p> tags to
#print(text)

## validate Open AI
openai.api_key = os.environ['OpenAI_API_KEY']
openai.organization = os.environ['OpenAI_OrgID']
openai.Model.list()

## set prompt
prompt = f"Summarize the text below in no more than 3 paragraphs. {text}"

## get response
response = openai.Completion.create(model='text-davinci-002', prompt=prompt, temperature=0, max_tokens=150)

## grab references
refs = soup.find_all("ol", {"class": "references"})
for ref in refs:
  print(ref.text.replace("^ ", ""))

print(response["choices"][0]["text"].strip())
