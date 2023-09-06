import random, os, time

greetings = ["Hello， World!", "Bonjour, Le Monde!", "¡Hola Mundo!", "你好，世界！", "!مرحبا بالعالم", "Chào thế giới!", "Selam Dünya!", "Salamu, Dunia!", "안녕하세요, 월드!", "こんにちは世界！", "Ciao mondo!", "สวัสดีชาวโลก!", "Hej världen!", "हैलो वर्ल्ड!", "ਸਤਿ ਸ੍ਰੀ ਅਕਾਲ ਦੁਨਿਆ!", "Сәлем Әлем!", "Բարեւ աշխարհ!", "Dia duit, a Dhomhanda!", "!שלום עולם", "Sawubona Mhlaba!", "Сайн уу, Дэлхий!", "မင်္ဂလာပါကမ္ဘာလောက!", "Γειά σου Κόσμε!", "Hallo Welt!", "Salom Dunyo!", "Привет, мир!", "Olá Mundo!", "नमस्कार, विश्व !", "Mo ki O Ile Aiye!"]

yes = ["yes", "oui", "si", "是"]

while True:
  random_greet = random.randint(0, len(greetings) - 1)
  print(f"{greetings[random_greet]} 🎉")
  print()
  another_greet = input("Would you like another greeting?:\n").lower().strip()
  if another_greet not in yes:
    break

