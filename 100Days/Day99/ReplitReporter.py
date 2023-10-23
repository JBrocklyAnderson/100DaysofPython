import requests, schedule, time, os, smtplib, logging
from bs4 import BeautifulSoup ## web-scraping functionality
from replit import db ## replit database
from email.mime.text import MIMEText ## email functionality
from email.mime.multipart import MIMEMultipart ## email functionality

logging.basicConfig(level = logging.INFO, format = "%(asctime)s - %(levelname)s - %(message)s", filename = "replitScraper.log", filemode = "a") ## configure logging method

def email(title, link): ## email function
  email = os.environ['email'] ## grab email
  password = os.environ['password'] ## grab password
  host = "smtp.gmail.com" ## set host
  port = 587 ## set port
  s = smtplib.SMTP(host = host, port = port) ## configure protocol
  s.starttls() ## initiate TLS
  s.login(email, password) ## authenticate

  msg = MIMEMultipart() ## create MIME message
  msg["To"] = email
  msg["From"] = email
  msg["Subject"] = "The Replit Report" 
  text = f"""<a href="{link}">{title}</a>""" 
  msg.attach(MIMEText(text, "html")) ## attach text
  s.send_message(msg) ## send the email
  del msg ## save storage space

def repl(): ## scraping function
  url = "https://replit.com/community-hub"
  response = requests.get(url) ## get the page
  html = response.text ## download the HTML
  soup = BeautifulSoup(html, "html.parser") ## analyze the HTML
  try:
    events = soup.find_all("div", {"class": "css-1dgfpnh"}) ## extract the div elements of the specified class
    
    for event in events[:3]:
      title = event.find("span", {"class":"css-scxoy8"})
      description = event.find("span", {"class": "css-163p1p4"})
      link = event.find("a")["href"]

      if title.text not in db: ## check against existing events
        db[title.text] = link ## add the link to the database
        email(title, link) ## send the email
        logging.info(f"Successfully scraped >  {title.text}: {description.text}\n{link}\n") ## log the success
  except (AttributeError, KeyError, IndexError, TypeError) as e: ## handle errors
    logging.error(f"An error occurred: {e}") ## log the error

schedule.every(15).seconds.do(repl) 

while True:
  schedule.run_pending() ## run the schedule
  time.sleep(1) ## to prevent the CPU from wasting resources
