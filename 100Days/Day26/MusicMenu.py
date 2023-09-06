from replit import audio
import os, time

def play():
  source = audio.play_file('audio.wav')
  source.paused = False # unpause the playback
  while True:
    # Start taking user input and doing something with it
    print("Press 'p' to play/pause and 'm' to return to main menu")
    user_input = input("")
    if user_input == "p":
      source.paused = not source.paused
    elif user_input == "m":
      return 

while True:
  os.system("clear") # clear the screen 
  print("🎵 MyPOD Music Player 🎵")
  print("Press 1 to Play")
  print("Press 2 to Exit")

  choice = input("")
  if choice == "1":
    play()
  elif choice == "2":
    print("Goodbye!")
    time.sleep(1)
    break