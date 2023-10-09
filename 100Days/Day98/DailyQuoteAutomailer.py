import schedule, time, os, smtplib, random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



quotes = []
"""
f = open("quotes.txt", "r")
quotes = eval(f.read())
f.close()
"""

with open("quotes.txt", "r") as f:
  content = f.read()
quotes = content.split("', '") ## parse the quotes

## accessing Replit secrets
username = os.environ['emailUsername']
password = os.environ['emailPassword']


def sendEmail():
  quote = random.choice(quotes) ## select one at random
  print(quote)
  host = "smtp.gmail.com"
  port = 587
  s = smtplib.SMTP(host=host, port=port)
  s.starttls()
  s.login(username, password)

  msg = MIMEMultipart()
  msg["To"] = username
  msg["From"] = username
  msg["Subject"] = "Daily Inspiration"
  msg.attach(MIMEText(quote, 'html'))
  
  s.send_message(msg)
  del msg


schedule.every(1).days.do(sendEmail)

while True:
  schedule.run_pending()
  time.sleep(1) 