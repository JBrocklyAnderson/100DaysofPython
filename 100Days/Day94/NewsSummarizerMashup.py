import requests, json, os, openai

NewsAPI_KEY = os.environ['NewsAPI_KEY']
openai.organization = os.environ['OpenAI_OrgID']
openai.api_key = os.environ['OpenAI_API_KEY']
openai.Model.list() ## send authentication request

country = "us"
url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={NewsAPI_KEY}"
response = requests.get(url) ## get results from NewsAPI query
data = response.json() ## retrieve JSON-encoded response content

counter = 0
for article in data["articles"]:
  counter += 1
  if counter >= 10:
    break ## only print the first 10
  prompt = f"""Summarize {article['url']} in one sentence."""
  response = openai.Completion.create(model="text-davinci-002", prompt=prompt, temperature = 0, max_tokens = 50) ## temperature is a measure of the tradeoff between coherence and creativity ## 50 tokens will generate around 38-word summaries
  print(response["choices"][0]["text"].strip())