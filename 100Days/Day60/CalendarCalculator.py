# import library
import datetime

# take user input for event name
event = input("What event or holiday would you like to track?\n\n").strip().title()

# capture today's date
today = datetime.date.today()

# take user input for event date
raw = input(f"\nWhen is {event}? (YYYY/MM/DD) ").strip()

# split the input and convert into date format
dateList = raw.split("/")
newDate = datetime.date(year = int(dateList[0]), month = int(dateList[1]), day = int(dateList[2]))

# find the difference between days in days
difference = (newDate - today).days

# timedelta setup
if today < newDate: 
  print(f"\nOnly {difference} days until {event}!")
elif today > newDate:
  # absolute value of "negative" days ago
  difference = abs((newDate - today).days)
  print(f"\n{event} already happened {difference} days ago.")
else:
  print(f"\nToday's the day; it's {event}!")