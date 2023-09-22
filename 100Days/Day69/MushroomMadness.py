import random
import tkinter as tk
from PIL import Image, ImageTk

# initialize a window module
window = tk.Tk()
window.title("Mushroom Madness")
window.geometry("400x700")

# create a subroutine to resize the images
def resizeImage(imagePath):
  return ImageTk.PhotoImage(Image.open(imagePath).resize((250, 250)))

labelText = """You stand before a simple
plate of mushrooms in the forest.
How do you proceed?"""

def restart():
  canvas.itemconfig(container, image = thePlate) ## reset the image
  label["text"] = labelText ## reset the initial narrative

  # reset the primary choices
  eat.pack()
  toss.pack()

  # hide secondary choices
  raw.pack_forget()
  cook.pack_forget()
  restart.pack_forget()
  
# generate a narrative based on user choices
afterEat = """You decide they look too good to pass
up. You swipe a couple from the plate.
How will you eat them?"""

afterToss = """You've seen mushrooms before.
They don't look all that
interesting. Besides, they
could be deadly..."""

heroArc = """Several years pass by before
seeing a global catastrophe play
out on the evening news. Chaos
ensues but—wait... It looks like a 
sentient mushroom superhero has
flown in with food, water, and 
other vital supplies for those
displaced by the disaster. It 
looks like you could have helped
save the world, if only you took
a chance."""

villainArc = """Several years pass by before 
seeing a global catastrophe play
out on the evenings news. Chaos
ensues and—the screen cuts to
static... Suddenly, what looks 
like a suit- and tie-wearing
sentient mushroom supervillain
has appeared on the screen making
unrealistic monetary demands upon the 
whole world. It looks like you 
could have prevented a new dark
age, if only you took a chance."""

paradiseArc = """The mushrooms tasted alright, nothing
amazing though. You relish new 
experiences so you don't mind. 
Slowly—but surely—a tickle starts
buzzing from the center of your 
forehead that envelopes you with 
every new breath. The world takes
on a new dimension of clarity and
vitality. Somehow, it feels more 
real than real ever had been. Tears 
of joy stream down your face as
frozen, dancing cottonballs caress
the universe from within you. "You"
washes away in an oceanic boundless
that is both infinitely exciting 
and eternal. Everything has become
everything else, opened up to a 
symbiotic masterpiece encapsulating
all of human artistry over the past
10,000 years within the span of a
single minute. This is paradise."""

prisonArc = """The mushrooms tasted really bad.
You regret eating them, but you
move on with your day. Slowly—but
surely—a deep anxiety creeps ever
forward until it barrels upon you
like a tidal wave. What was once a
normal day has been gripped by the
totalizing sense of impending doom.
The trees start to crack, break, 
and bruise. The air wakes up again,
every moment more furious with you.
The animals cackle in a dancing 
circle as they show you the way to
a meat grinder where you spend
eternity because you can no longer
decipher where "you" end and it
begins. This is hell. It must be."""

pastaArc = """You take the mushrooms back to
your place, dust them off, and 
begin to compose the truest form
of culinary art that has ever
sprung forth. A deep, nuanced
symphony of savory, sweet, and 
salty flavors kissed with rich 
spice melt and miander on your
tasetbuds. What a brilliant 
choice! You'll definitely be 
going back for more mushrooms."""

poisonArc = """You take the mushrooms back to
your place, dust them off, and 
throw them into a pan with butter 
to be served on a rib-eye steak. 
They're tasty, but nothing to write
home about. Several hours go by and
you start feeling sick—very sick. 
You're stomach turns and your muscles
feeling like stone. You're heart 
begins it's final dance, desparately
asking for the power it needs to
pump oxygen through your veins. But
it's all in vain. The poison spread
too far and your body has seized up
like an engine without oil. You 
won't be going back for mushrooms."""

def choices(action):
  if action == "eat": 
    if random.choice([True, False]): # randomize the output narrative
      canvas.itemconfig(container, image = theRough) # change the image
      label["text"] = afterEat # adjust narrative
    else:
      canvas.itemconfig(container, image = theReady)
      label["text"] = afterEat

    # hide primary choices
    eat.pack_forget()
    toss.pack_forget()
    # display next set of choices
    raw.pack()
    cook.pack()
  
  elif action == "toss":
    label["text"]
    if random.choice([True, False]):
      canvas.itemconfig(container, image = theHero)
      label["text"] = heroArc
    else:
      canvas.itemconfig(container, image = theVillain)
      label["text"] = villainArc
    eat.pack_forget()
    toss.pack_forget()
    restart.pack() # allow the user to reset the story

  elif action == "raw":
    if random.choice([True, False]):
      canvas.itemconfig(container, image = theParadise)
      label["text"] = paradiseArc
    else:
      canvas.itemconfig(container, image = thePrison)
      label["text"] = prisonArc
    raw.pack_forget()
    cook.pack_forget()
    restart.pack()

  elif action == "cook":
    if random.choice([True, False]):
      canvas.itemconfig(container, image = thePasta)
      label["text"] = pastaArc
    else:
      canvas.itemconfig(container, image = thePoison)
      label["text"] = poisonArc
      raw.pack_forget()
      cook.pack_forget()
      restart.pack()
    raw.pack_forget()
    cook.pack_forget()
    restart.pack()

# add a canvas
canvas = tk.Canvas(window, width = 250, height = 250)
canvas.pack()

# add and resize the images
thePlate = resizeImage("Images/thePlate.jpg")
theReady = resizeImage("Images/theReady.jpg")
theRough = resizeImage("Images/theRough.jpg")
theParadise = resizeImage("Images/theParadise.jpg")
thePasta = resizeImage("Images/thePasta.jpg")
thePrison = resizeImage("Images/thePrison.jpg")
thePoison = resizeImage("Images/thePoison.jpg")
theHero = resizeImage("Images/theHero.jpg")
theVillain = resizeImage("Images/theVillain.jpg")

# add a label to display the narrative
label = tk.Label(text = labelText)
label.pack()

# add buttons
eat = tk.Button(text = "Eat", command = lambda: choices("eat")) ## use lambda because `choices` takes an argument, but we only want this to happen when the user clicks the button
eat.pack()
toss = tk.Button(text = "Pass", command = lambda: choices("toss"))
toss.pack()
raw = tk.Button(text = "I like my mushrooms raw", command = lambda: choices("raw"))
cook = tk.Button(text = "Everything's better cooked", command = lambda: choices("cook"))
restart = tk.Button(text = "Retell the Story", command = restart) ## lambda not needed because `restart` does not expect parameters

# create a container for the images
container = canvas.create_image(130, 100, image = thePlate) ## set initial image

