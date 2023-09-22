import tkinter as tk
from PIL import Image, ImageTk

# define image-finding subroutine
def showImage():
  person = text.get("1.0", "end") ## get the text from the first character (0-indexed) and the first line (indexed with 1) all the way until the end 
  if person.strip().lower() == "charlotte":
    canvas.itemconfig(container, image = charlotte)
  elif person.strip().lower() == "gerald":
    canvas.itemconfig(container, image = gerald)
  elif person.strip().lower() == "katie":
    canvas.itemconfig(container, image = katie)
  elif person.strip().lower() == "mo":
    canvas.itemconfig(container, image = mo)
  else:
    hello["text"] = "Triangulation failed. Please try again"

# open, title, and set the size of a window
window = tk.Tk()
window.title("Guess Who?") 
window.geometry("400x400") 

# add a label and pack it into the window
label = "Guess who?"
hello = tk.Label(text = label) 
hello.pack() 

# add and pack a text box to the window
text = tk.Text(window, height = 1, width = 30)
text.pack()

# add a button to initiate the image-finding subroutine
button = tk.Button(text = "Triangulate", command = showImage)
button.pack()

# open and pack a canvas to the window
canvas = tk.Canvas(window, width = 300, height=300) 
canvas.pack()

# load in images
charlotte = ImageTk.PhotoImage(Image.open(".tutorial/GuessWho/charlotte.jpg"))
gerald = ImageTk.PhotoImage(Image.open(".tutorial/GuessWho/gerald.jpg"))
katie = ImageTk.PhotoImage(Image.open(".tutorial/GuessWho/katie.jpg"))
mo = ImageTk.PhotoImage(Image.open(".tutorial/GuessWho/mo.jpg"))

# place images in canvas
container = canvas.create_image(200, 0, image = charlotte)

# run the main loop
tk.mainloop()