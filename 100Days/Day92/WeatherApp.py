### NOTE TO SELF: Update this after completing the 100 days challenge

import requests, json

timezone = "PST"
latitude = 38.5085
longitude = -121.5353

weathercodes = list(range(100))

def getCode(code):
  if code == weathercodes[0]: 
    return "Clear sky"
  elif code in weathercodes[1:4]:
    return "Mainly clear, partly cloudy, and overcast"
  elif code in weathercodes[45:49:3]:
    return "Fog and depositing rime fog"
  elif code in weathercodes[51:56:2]:
    return "Drizzle: Light, moderate, and dense intensity"
  elif code in weathercodes[56:58]:
    return "Freezing Drizzle: Light and dense intensity"
  elif code in weathercodes[61:66:2]:
    return "Rain: Slight, moderate and heavy intensity"
  elif code in weathercodes[66:68]:
    return "Freezing Rain: Light and heavy intensity"
  elif code in weathercodes[71:76:2]:
    return "Snow fall: Slight, moderate, and heavy intensity"
  elif code in weathercodes[77]:
    return "Snow grains"
  elif code in weathercodes[80:83]:
    return "Rain showers: Slight, moderate, and violent"
  elif code in weathercodes[85:87]:
    return "Snow showers slight and heavy"
  else:
    return "No such weathercode."

result = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=weathercode,temperature_2m_max,temperature_2m_min&timezone={timezone.upper()}")

user = result.json()
#print(json.dumps(user, indent=1))

date = user["daily"]["time"][0]
weatherCode = user["daily"]["weathercode"][0]
maxC = user["daily"]["temperature_2m_max"][0]
minC = user["daily"]["temperature_2m_min"][0]
maxF = round((maxC * 1.8) + 32, 1)
minF = round((minC * 1.8) + 32, 1)

print(f"\033[32m{date}\033[0m\t\033[35m{getCode(weatherCode)}\033[30m\n\n🥵: \033[31m{maxC}°C  {maxF}°F\033[0m\t🥶: \033[36m{minC}°C  {minF}°F\033[0m")