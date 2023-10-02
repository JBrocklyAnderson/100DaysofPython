from flask import Flask, request, redirect
import datetime

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
  return redirect('/homepage?theme=norm')

@app.route('/homepage', methods=["GET"])
def homepage():
  theme = request.args
  
  date = datetime.date.today()
  #imageLink = "https://"
  
  page = "" ## initialize a blank variable to store our HTML
  with open("template/homepage.html") as f: ## load the template
    page = f.read() ## read the template's HTML into the `page` variable
  
  page = page.replace("{date}", str(date))
  #page = page.replace("{imageLink}", imageLink)
  
  if theme["theme"] == "norm":
    css = "homepage.css"  
  elif theme["theme"] == "bs":
    css = "hpbs.css"
  else: 
    css = "homepage.css"
    
  page = page.replace("{css}", css)
  return page

# Enter the Void
@app.route('/EnterTheVoid', methods=["GET"])
def enterTheVoid():
  theme = request.args
  
  title = "Enter the Void"
  author = "Joseph Brockly-Anderson"
  date = "12023/09/27"
  subject = "Astronomy"
  
  text = "It is truly amazing to try to wrap your mind around the sheer immensity of the universe. I remember gazing up at the night sky as a child and thinking all those stars must not be so far away if we can see them. My father used to take me up to Yosemite with his astronomy group and we would bounce from telescope to telescope looking at galaxies, nebulae, planets, and the occasional comet. Knowing what I know now, I lived in an incredibly small universe even when I stared into the void. I couldn't have possibly fathomed the vast ocean of nothingness that is the Cosmos. The sheer distance between and size of celestial bodies did not even remotely hit me in 7th grade science class while watching Bill Nye walk down a scale model of the solar system. I hardly knew what a mile it really was, how could I use it to create a model of the universe? It was all very abstract until I started doing some actual calculations during my time in university."
  text2 = "Imagine the sun is sitting on the coffee table in front of you. It blends in perfectly with the bowl of small oranges placed in the center. With this scale in mind, How far away do you think the Earth is? How big do you think the earth is in comparison to an orange? Once we start answering these questions, some people begin to feel incredibly impossibly tiny. I see it as just the opposite. I choose to believe that the universe springs forth from an oceanic boundlessness that connects all things through matter and motion. Everything imparts its purpose on everything else. The purpose we as humans share together is already the size of the universe, Precisely because we've measured its size."
  text3 = "If the sun were the size of a small orange, the Earth—a single, fine grain of sand—would be floating a whole 17 feet away. Jupiter—that behemoth gas giant that could swallow one hundred Earth's reigning supreme in the night sky and protecting us from extinction-causing asteroids— would be smaller than a pea and dangling nearly 100 feet from the orange Sun. The very nearest orange star to our own—Alpha Centauri—flies through space more than 700 miles away. And in between our little neighborhood and an orange 700 miles away is as close to literally nothing as we can possibly imagine. The universe is a strange place. I marvel in awe at what I know about it every day because I couldn't handle marveling at what I have yet to discover."
  image = "orangeSun.jpg"
  #imageLink = "https://"
  
  page = "" ## initialize a blank variable to store our HTML
  with open("template/article.html") as f: ## load the template
    page = f.read() ## read the template's HTML into the `page` variable
  
  page = page.replace("{title}", title)
  page = page.replace("{author}", author)
  page = page.replace("{date}", date)
  page = page.replace("{subject}", subject)
  page = page.replace("{text}", text)
  page = page.replace("{text2}", text2)
  page = page.replace("{text3}", text3)
  page = page.replace("{image}", image)
  #page = page.replace("{imageLink}", imageLink)
  
  if theme["theme"] == "norm":
    css = "article.css"  
  elif theme["theme"] == "bs":
    css = "blueshift.css"
  else: 
    css = "article.css"
    
  page = page.replace("{css}", css)
  return page

@app.route('/AFutureWorthFightingFor', methods=["GET"])
def future():
  theme = request.args
  
  title = "A Future Worth Fighting For"
  author = "Joseph Brockly-Anderson"
  date = "12023/09/27"
  subject = "Environment"
  
  text = " As a young child into my teenage years, I was obsessed with this abstract concept called the future. This fit in nicely with my deep passion for astronomy and science fiction. I used to draw Conceptual ultra modern skyscrapers in cityscapes with flying cars and space elevators. I couldn't wait for the promise of teleportation and space travel and moon bases to finally be delivered as if on a silver platter. The prospect of the technological singularity kept me up at night thinking about all the ways in which we would be able to transcend our biological bodies and live a million lives at once. What are my favorite books as a teenager was the Age of Spiritual Machines. It's a book that talks about Ray Kurzweil's law of accelerating returns in technology and how by 2049, a $1000 computer (in 2005 dollars, mind you, a time when I barely knew what money really was) would Have the processing power of 10 billion human brains thinking for 10 million years in the span of a single second." 
  text2 = "I used to think that by 2020, we'd all be living in a rough approximation of this future. In many ways this has indeed come to pass. We have access to all of the world's knowledge at our fingertips, decipherable by artificially intelligent computer programs that can fool us into falling in love with them or teach us how to avoid making napalm. We have futuristic looking gadgets and sleek looking cars. Our world is populated by megalits that tower half a mile into the air, Surrounded by networks of satellites that can bean information from one corner of the world to another at lightspeed. We can travel anywhere in the world and speak into a magic box that outputs our strings of small mouth noises in real-time to someone who lives in a different linguistic universe. However, in a lot of ways—this is a mirage, isn't it?"
  text3 = "There are still entire regions on this earth that don't have access to light bulbs or clean water, to food or shelter. The organizational systems that govern every facet of our politics and economy are so convolutedly redundant as to waste and bind our collective and individual human potential. We're still forced to kill and maim each other for money, property, and access to the carrots that dangle in front of us from on high. Human beings are nothing but what they do, which is transofrm the landscape and each other for an infinite diversity of reasons. We don't hate work, we hate being forced to work for less than we're worth. We all know of the world's problems and have for centuries. Clearly, there are a lot of people—at odds with each other or not—that will fight out the rest of their days making sure this world continues as it has because it makes them a lot of money and it gives them a lot of prestige when compared to the homeless single mother outside the superstore; the same grocery store that plundered the community that single mother came from; the same superstore whose lottery on the stock market ensures that the plundered rewards would go to those who sit atop a dying world. It's often said that the system is broken, but it's not broken in the slightest. This is more or less how it was designed. It is being remolded at every waking moment to entrench itself forever, as all systems of power do. Any collective attempt to undermine and overcome the class systems that have us at each other's throat over petty bullshit has been met with demonization, misinformation, infiltration, and when needed, assassination. The state of the world requires that its solution be reflected in the mirror before it is sufficiently free to develop it's own image. Whatever solution that we can find will only work if we can organize faster, better, and with more conviction then the eight people who own half the Earth. It will necessarily look disgusting at first glance; it must, as a perfect mirror of the current state of things. The current world disorder is impossible to uphold. Our future is found in genuine social togetherness or it will be found in a dark barbarism."
  image = "solarPunk.jpg"
  
  page = "" ## initialize a blank variable to store our HTML
  with open("template/article.html") as f: ## load the template
    page = f.read() ## read the template's HTML into the `page` variable

  page = page.replace("{title}", title)
  page = page.replace("{author}", author)
  page = page.replace("{date}", date)
  page = page.replace("{subject}", subject)
  page = page.replace("{text}", text)
  page = page.replace("{text2}", text2)
  page = page.replace("{text3}", text3)
  page = page.replace("{image}", image)
  
  if theme["theme"] == "norm":
    css = "article.css"  
  elif theme["theme"] == "bs":
    css = "blueshift.css"
  else: 
    css = "article.css"
    
  page = page.replace("{css}", css)
  return page

app.run(host='0.0.0.0', port=81)