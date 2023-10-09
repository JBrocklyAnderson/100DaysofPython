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
  msg.send_message(msg)
  del msg


schedule.every(1).days.do(sendEmail)

schedule.run_pending()
time.sleep(1) 

  

"""
def sendEmail():
	email = "Don't forget to take a break!"
	server = "smtp.gmail.com"
	port = 587 
	s = smtplib.SMTP(host=server, port=port)
	s.starttls() ## upgrade the connection to a secure TLS connection
	s.login(username, password)

	msg = MIMEMultipart() ## alias the method for ease of use
	msg["To"] = "jbrocklyanderson@gmail.com" ## define fields
	msg["From"] = "jbrocklyanderson@gmail.com"
	msg["Subject"] = "Let your eyes ReLaX"
	msg.attach(MIMEText(email, "html")) ## convert the email to HTML
	s.send_message(msg)
	del msg ## to save RAM between autosending

def isEmailing():
  print("Sending reminder...")
  sendEmail()

schedule.every(1).minutes.do(isEmailing) ## run the function every hour

while True:
	schedule.run_pending() ## to check whether it's been an hour
	time.sleep(1) # to save CPU power by preventing the above check to happen infinitely as fast as possible
 """