## the following modules are separated to show specific understanding of their functions
import requests ## to request external website data
import schedule ## to schedule the script to run on queue
import os ## to interact with the operating system
import time ## import time for sleep
import smtplib ## to send emails using Simple Mail Transfer Protocol
import logging ## to log messages 
from bs4 import BeautifulSoup ## to parse html
from replit import db ## to store data in replit database
from email.mime.multipart import MIMEMultipart ## to compose email using Multipurpose Internet Mail Extension
from email.mime.text import MIMEText ## to compose email using Multipurpose Internet Mail Extension

db.clear() ## clear the database
#keys = db.keys() ## view the database
#for key in keys:
  #print(db.get(key))

logging.basicConfig(level = logging.INFO, format = "%(asctime)s - %(levelname)s - %(message)s", filename = "main.log", filemode = "a") ## configure logging method

def link_to_scrape(): ## function to scrape website
  link = input("Product Link: ").strip() ## prompt user to input product link
  price = input("\nPrice Threshold: ").strip() ## prompt user to input price threshold
  try: ## try to scrape the price
    price = float(price) ## convert the price to a float
  except ValueError: ## if the formatting changes
    logging.error(f"{price} is not a valid number to convert to a float.") ## log the error
  if link.startswith("https://store.insta360.com/product/"): ## make sure the product link is from Insta360
    db[time.time()] = {"link": link, "price": None, "level": price} ## store data in replit database
  else: ## if it's not from the specified website
    raise ValueError("Invalid link.") ## log the error

#https://store.insta360.com/product/x3?insrc=INRJWRN
link_to_scrape()

def email(url, priceTag, product):
  email = os.environ['email'] ## grab email
  password = os.environ['password'] ## grab password
  host = "smtp.gmail.com" ## set host
  port = 587 ## set port
  s = smtplib.SMTP(host = host, port = port) ## configure protocol
  s.starttls() ## initiate Transport Layer Security
  s.login(email, password) ## authenticate

  msg = MIMEMultipart() ## create MIME message
  msg["To"] = email ## set recipient
  msg["From"] = email ## set sender
  msg["Subject"] = "It's the Perfect Time to Buy!" ## set subject
  text = f"""<p>{product} is now available at ${priceTag}!\n\n<a href="{url}">Buy now</a> before it's too late!</p>""" ## set body
  msg.attach(MIMEText(text, "html")) ## attach body to message as HTML
  s.send_message(msg) ## send the emial
  del msg ## delete the email to save storage space

def update():
  keys = db.keys() ## get all keys from db
  for key in keys: ## iterate through keys
    url = db[key]["link"] ## get product link
    price = db[key]["price"] ## get current price 
    level = db[key]["level"] ## get price threshold
    priceTag = None ## initialize price tag
    #print(url)
    #print(price)
    #print(level)
    try:
      response = requests.get(url) ## get response from product link
      response.raise_for_status() ## raise error if response is not 200
      print(response)
      html = response.text ## download the HTML
      soup = BeautifulSoup(html, "html.parser") ## parse the HTML
      
      product = soup.find("div", {"class": "yqRkBi0T"}) ## find the product name
      if product: 
        logging.info("Product title successfully scraped.")
      else: 
        raise ValueError("No product title found.")
      
      priceTag = soup.find("div", {"class": "ekSaJ5Z0"}) ## find the price tag
      if priceTag: ## if price tag is found
        priceTag = float(priceTag.text.replace("$", "")) ## convert price to float
        logging.info(f"Successfully scraped price for {product.text}.") ## log the success
           ## convert price to float
      else: 
        raise ValueError("Pricetag not found.") ## raise an error message
    
    except requests.exceptions.HTTPError as e: ## if request response is an HTTP error
      logging.error(f"HTTP error: {e}") ## log the error
    except requests.exceptions.RequestException as e: ## if any other request-related error fails
      logging.error(f"Network error: {e}") ## log the error
    except ValueError as e: ## if value error occurs
      logging.error(f"Data extration error: {e}") ## log the error
    except Exception as e: ## if any other error occurs
      logging.error(f"An unexpected error occurred: {e}") ## log them
    
    if priceTag != price: ## if price is not equal to current price
      db[key]["price"] = priceTag ## update price in database
    if priceTag <= level: ## if price is less than price threshold
      print("Cheap Enough")
      email(url, priceTag, product) ## execute the email function
      del key ## delete the key from the database to prevent duplicate emails
    else:
      print("Too expensive.")

schedule.every(1).days.do(update) ## schedule to scrape for product info once per day

while True:
  schedule.run_pending() ## run scheduled tasks
  time.sleep(1) ## save CPU power
