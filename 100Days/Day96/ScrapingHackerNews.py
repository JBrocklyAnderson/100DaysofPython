import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

myLinks = soup.find_all("span", {"class": "titleline"})
print(len(myLinks))

keywords = ['python', 'ai', 'language', 'learning', 'amazon', 'astronomy']

for link in myLinks:
  a_tags = link.find_all('a')
  for a_tag in a_tags:
    text = a_tag.text
    href = a_tag['href']
    textList = text.split()
    containsKeyWords = any(word.lower() in keywords for word in textList)
    if containsKeyWords:
      print(f"{text}\n{href}\n")