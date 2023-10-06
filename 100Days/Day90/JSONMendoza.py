import requests, json

result = requests.get("https://randomuser.me/api/?results=10") ## grab 10 users
if result.status_code != 200: ##if unsuccessful
  print("Error: Couldn't communicate with API")
else: ## parse the JSON file
  user = result.json()
  print(json.dumps(user, indent=2)) ## print their details 

  for person in user['results']:
    name = f"{person['name']['first']}-{person['name']['last']}" ## capture full name
    
    image = f"{person['picture']['medium']}" ## grab medium-sized profile image
  
    picture = requests.get(image) ## send a GET request to capture the image's binary data
    
    with open(f"profilePics/{name}.jpg", 'wb') as f: ## save the image by writing in binary
      f.write(picture.content) 

  print(name)
