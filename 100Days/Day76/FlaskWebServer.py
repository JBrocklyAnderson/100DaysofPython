from flask import Flask

app = Flask(__name__)


@app.route('/linktree')
def index():
  page = """
  <!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>Joseph Brockly-Anderson</title>
  <link href="/static/CSS/linktree.css" rel="stylesheet" type="text/css" />
</head>

<!-- build heading image-text package -->
<body>
  <div class="imageContainer" >
    <img src="/static/Images/professionalPhoto.jpg" >
    <p class="imageText image1Text"><b>Collaborative.</b></p>
    <p class="imageText image2Text"><b>Innovative.</b></p>
    <p class="imageText image3Text"><b>Adaptable.</b></p>
    <p class="imageText image4Text"><b>Joseph Brockly-Anderson.</b></p>
  </div>

  <!-- build a linktree -->
  <div id="linktree" >
    <ul>
      <li><a href="https://www.linkedin.com/in/joseph-brockly-anderson-438149287/" alt="LinkedIn" >LinkedIn</a></li>
      <li><a href="https://github.com/JBrocklyAnderson" >GitHub</a></li>
      <li><a href="https://replit.com/@JosephBrockly-A" >Replit</a></li>
      <li><a href="https://flask-web-server-day-76-of-100.josephbrockly-a.repl.co/showcase" >Python Showcase</a></li>
    </ul>
  </div>

  <!-- professional tagline -->
  <div class="heading" >
    <h1>Passionate Polymath: From Politics to Programming</h1>
  </div>
      <p class="main"> I am unconditionally fascinated by alll things: politics, language, philosophy, AI, astronomy, design, cybersecurity, architecture, biology, medicine, music, machinery, nature, you name it (in no particular order)! The best part about data science, computer programming, and software engineering is that these fields are capable of bringing together all of these disparate interests into a unified whole. The world is full of astonishing things to learn and I'm racing against the clock to explore it all in one life!</p>
      <p class="main">I have extensive in-depth academic training about global interdependence and international relations, comprehensive certifications in data analysis, leadership, and cultural sensitivity, professional publications for academic dissertations, project portfolios showcasing my programming proclivities, deep multilingual capacities in Chinese, French, and Spanish, specialized public-facing customer service experience, an abundant long-standing passion for innovation, collaboration, and determination, and awards for academic excellence from University of California, Davis.</p>
  <p class="main">A key challenge for society and business in the 21st century is bridging the gap between industries that have specialized so much but have neglected to learn from each other. Unfettering the combined productive force of the global economy will be the flowering of humanity. I aim to help those making that world possible.</p>  
  
</body>

</html>
  """
  return page

@app.route('/showcase') 
def showcase():
  page = """
  <html>
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width">
    <title>Python Portfolio</title>
    <link href="/static/CSS/showcase.css" rel="stylesheet" type="text/css" />
  </head>
  
  <body>
    <h1>A Collection of Python Projects </h1>
    <h2>A Journey Through the Lessons of Object-Oriented Programming</h2>
    <p>I graduated with a Bachelor's in Political Science and Mandarin Chinese. I never thought of myself as a web developer or software engineer, but I've been inspired by a personal hero to persistently challenge myself. To that end, I've been vigorously working through <a href="https://replit.com/@JosephBrockly-A">Repl.it</a>'s <b><i>100 Days of Python</i></b>.
    </p>
    <p>Though I'm not quite finished, the journey has been incredibly rewarding. I've written working computer programs that solve real world problems and provide demonstrable use to people, from Mad Libs and Loan Calculators to interactive graphic novels and minigames. This website is dedicated to showcasing my journey through the challenge and how I learned to code in Python by exploring 5 particular days.
    </p>
  
    <!-- Hyperlinks to other pages organized within an unordered list -->
    <ul>
      <li><a href="https://flask-web-server-day-76-of-100.josephbrockly-a.repl.co/linktree">Linktree</a></li>
      <li><a href="https://flask-web-server-day-76-of-100.josephbrockly-a.repl.co/showcase">Showcase</a></li>
      <li><a href = "https://flask-web-server-day-76-of-100.josephbrockly-a.repl.co/showcase/adventureGenerator">Adventure Generator</a></li>
      <li><a href = "https://flask-web-server-day-76-of-100.josephbrockly-a.repl.co/showcase/spacetime!">Spacetime!</a></li>
      <li><a href = "https://flask-web-server-day-76-of-100.josephbrockly-a.repl.co/showcase/theEventHorizon">The Event Horizon</a></li>
      <li><a href = "https://flask-web-server-day-76-of-100.josephbrockly-a.repl.co/showcase/simpleCalculator">Simple Calculator</a></li>
      <li><a href = "https://flask-web-server-day-76-of-100.josephbrockly-a.repl.co/showcase/cybersecureJournal">Cybersecure Journal</a></li>
    </ul>
  
  </body>
</html>
  """
  return page

@app.route('/showcase/adventureGenerator') 
def adGen():
  page = """
  <html>
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width">
    <title>Adventure Generator</title>
    <link href="/static/CSS/showcase.css" rel="stylesheet" type="text/css" />
  </head>
  <body>
    <h1>Day 4</h1>
    <h2>The Adventure Generator</h2>
    <p> This was one of the very first programs that I built in Repl.it that I began to think of myself as capable of learning how to program. I had programming experience in R and R Studio as a result of a capstone project I did to get professionally certified in Data Analytics, so I knew of the supposed "feud" between the two languages. My brother is an impressive programmer who prefers Python over R and his Python code, especially in this early phase of my learning, felt daunting to say the least.
    </p>
    <p>Fortunately, this challenge provided a way to build an interactive mad lib's style storytelling device. Even though it's relatively short (and full of oddly-placed spaces due to concatenating text strings and variables without using an f-string literal), I've been enamored with creative writing since my early childhood, so I immediately resonated. Needless to say, this is when I got hooked to learning Python. I knew it was going to be difficult, but I knew it would be immensely valuable, both personally and professionally. My mind had expanded just enough to continue and I'm grateful for putting in the work.
    </p>

    <!-- Image and link -->
    <a href="https://replit.com/@JosephBrockly-A/Adventure-Generator-Day-4-of-100" ><img src="/static/Images/day4.jpg" width = 1000 ></a>
    
    <!-- Hyperlinks to other pages organized within an unordered list -->
    <ul>
      <li><a href="https://flask-web-server-day-76-of-100.josephbrockly-a.repl.co/linktree">Linktree</a></li>
      <li><a href="https://flask-web-server-day-76-of-100.josephbrockly-a.repl.co/showcase">Showcase</a></li>
      <li><a href = "https://flask-web-server-day-76-of-100.josephbrockly-a.repl.co/showcase/adventureGenerator">Adventure Generator</a></li>
      <li><a href = "https://flask-web-server-day-76-of-100.josephbrockly-a.repl.co/showcase/spacetime!">Spacetime!</a></li>
      <li><a href = "https://flask-web-server-day-76-of-100.josephbrockly-a.repl.co/showcase/theEventHorizon">The Event Horizon</a></li>
      <li><a href = "https://flask-web-server-day-76-of-100.josephbrockly-a.repl.co/showcase/simpleCalculator">Simple Calculator</a></li>
      <li><a href = "https://flask-web-server-day-76-of-100.josephbrockly-a.repl.co/showcase/cybersecureJournal">Cybersecure Journal</a></li>
    </ul>

  <script src="script.js"></script>  
  </body>
</html>
  """
  return page

@app.route('/showcase/spacetime!') 
def space():
  page = """
  <!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width">
    <title>Spacetime!</title>
    <link href="/static/CSS/showcase.css" rel="stylesheet" type="text/css" />
  </head>
  <body>
    <h1>Day 17</h1>
    <h2>Spacetime!</h2>
    <p>This particular program was my first foray into the logic of while loops and if-else statements which I use in conjunction to advance an emulation of the children's game "Rock-Paper-Scissors" with 5 inputs instead of 3. It took quite a bit of thinking to encode every possible solution but the final result was definitely satisfying, especially when sharing it with my nephews and nieces.
    </p>
    
    <!-- Image and link -->
    <a href="https://replit.com/@JosephBrockly-A/Spacetime-Day-17-of-100" ><img src="/static/Images/day17.jpg" width = 1000 ></a>

    <!-- Hyperlinks to other pages organized within an unordered list -->
    <ul>
      <li><a href="https://flask-web-server-day-76-of-100.josephbrockly-a.repl.co/linktree">Linktree</a></li>
      <li><a href="https://flask-web-server-day-76-of-100.josephbrockly-a.repl.co/showcase">Showcase</a></li>
      <li><a href = "https://flask-web-server-day-76-of-100.josephbrockly-a.repl.co/showcase/adventureGenerator">Adventure Generator</a></li>
      <li><a href = "https://flask-web-server-day-76-of-100.josephbrockly-a.repl.co/showcase/spacetime!">Spacetime!</a></li>
      <li><a href = "https://flask-web-server-day-76-of-100.josephbrockly-a.repl.co/showcase/theEventHorizon">The Event Horizon</a></li>
      <li><a href = "https://flask-web-server-day-76-of-100.josephbrockly-a.repl.co/showcase/simpleCalculator">Simple Calculator</a></li>
      <li><a href = "https://flask-web-server-day-76-of-100.josephbrockly-a.repl.co/showcase/cybersecureJournal">Cybersecure Journal</a></li>
    </ul>

  <script src="script.js"></script>  
  </body>
</html>
  """
  return page

@app.route('/showcase/theEventHorizon') 
def eventHorizon():
  page = """
  <!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width">
    <title>Event Horizon</title>
    <link href="/static/CSS/showcase.css" rel="stylesheet" type="text/css" />
  </head>
  <body>
    <h1>Day 39</h1>
    <h2>The Event Horizon</h2>
    <p>By now, I had a solid grass and while-loops, for-loops, and if-else statements. I also had a little practice with subroutines, so I combined all of these basic principles and created a version of the children's word game "hangman". I thematically constructed the game around the concept of a spaceship mechanic needing to rescue the crew in a time of crisis. It was fun thinking of the narrative behind the game but quite challenging working out all the details.
    </p>
    <p> I had to display the word—randomly chosen from a laundry list of words using the random library—as a series of underscores so that players were not completely in the dark, not to mention keep track of guesses already made and separate them using the join function while decrementing variables to similate a dwindling window of time to save the spaceship. It took a long time to build but I stand by the final result. Around this time is when I became truly fascinated with the possibilities that programming and software engineering opened up for me.</p>

    <!-- Image and link -->
    <a href="https://replit.com/@JosephBrockly-A/The-Event-Horizon-Day-39-of-100" ><img src="/static/Images/day39.jpg" width = 1000 ></a>
    
    <!-- Hyperlinks to other pages organized within an unordered list -->
    <ul>
      <li><a href="https://flask-web-server-day-76-of-100.josephbrockly-a.repl.co/linktree">Linktree</a></li>
      <li><a href="https://flask-web-server-day-76-of-100.josephbrockly-a.repl.co/showcase">Showcase</a></li>
      <li><a href = "https://flask-web-server-day-76-of-100.josephbrockly-a.repl.co/showcase/adventureGenerator">Adventure Generator</a></li>
      <li><a href = "https://flask-web-server-day-76-of-100.josephbrockly-a.repl.co/showcase/spacetime!">Spacetime!</a></li>
      <li><a href = "https://flask-web-server-day-76-of-100.josephbrockly-a.repl.co/showcase/theEventHorizon">The Event Horizon</a></li>
      <li><a href = "https://flask-web-server-day-76-of-100.josephbrockly-a.repl.co/showcase/simpleCalculator">Simple Calculator</a></li>
      <li><a href = "https://flask-web-server-day-76-of-100.josephbrockly-a.repl.co/showcase/cybersecureJournal">Cybersecure Journal</a></li>
    </ul>

  <script src="script.js"></script>  
  </body>
</html>
  """
  return page

@app.route('/showcase/simpleCalculator') 
def calc():
  page = """
  <!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width">
    <title>Simple Calculator</title>
    <link href="/static/CSS/showcase.css" rel="stylesheet" type="text/css" />
  </head>
  <body>
    <h1>Day 66</h1>
    <h2>A Simple Arithmetic Calculator</h2>
    <p> This simple calculator set within a graphical user interface was an incredibly challenging program to code. I had never before used to tkinter and object-oriented programming concepts but through the process of what seemed like endless trial and error, a feasible code emerged that emulated the basic functionality of a Window's 98 calculator, coming complete with all the basic arithmetic functions and a clear button to boot.
    </p>
    <p>I ended up running into a problem that emerged as the number grew beyond the invisible grid that kept the buttons in place. Namely, the button columns separated further as the number grew longer. A tried a variety of methods to fix this problem: I changed the font and sizing of the number, the width of the buttons, and more, but nothing stopped the unwanted behavior. Eventually, as I learn more about the intracies of Python and OOP, I may very well decide to change how I pack the buttons into the GUI window to overcome this aesthetically unappealing behavior.  
    </p>
    
    <!-- Image and link -->
    <a href="https://replit.com/@JosephBrockly-A/Simple-Calculator-Day-66-of-100" ><img src="/static/Images/day66.jpg" width = 1000 ></a>

     <!-- Hyperlinks to other pages organized within an unordered list -->
    <ul>
      <li><a href="https://flask-web-server-day-76-of-100.josephbrockly-a.repl.co/linktree">Linktree</a></li>
      <li><a href="https://flask-web-server-day-76-of-100.josephbrockly-a.repl.co/showcase">Showcase</a></li>
      <li><a href = "https://flask-web-server-day-76-of-100.josephbrockly-a.repl.co/showcase/adventureGenerator">Adventure Generator</a></li>
      <li><a href = "https://flask-web-server-day-76-of-100.josephbrockly-a.repl.co/showcase/spacetime!">Spacetime!</a></li>
      <li><a href = "https://flask-web-server-day-76-of-100.josephbrockly-a.repl.co/showcase/theEventHorizon">The Event Horizon</a></li>
      <li><a href = "https://flask-web-server-day-76-of-100.josephbrockly-a.repl.co/showcase/simpleCalculator">Simple Calculator</a></li>
      <li><a href = "https://flask-web-server-day-76-of-100.josephbrockly-a.repl.co/showcase/cybersecureJournal">Cybersecure Journal</a></li>
    </ul>
    
  <script src="script.js"></script>  
  </body>
</html>
  """
  return page

@app.route('/showcase/cybersecureJournal') 
def journal():
  page = """
  <!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width">
    <title>Cybersecure Journal</title>
    <link href="/static/CSS/showcase.css" rel="stylesheet" type="text/css" />
  </head>
  <body>
    <h1>Day 72</h1>
    <h2>A Cybersecure Journal Library</h2>
    <p> This program was one of my more recent projects and it involved a tremendous amount of thinking. I won't go into all of the various challenges—both big and small—that I encountered while building it, But I will mention that it incorporates an understanding and practice of appending salts to user passwords before hashing in order to keep the journal accounts more secure than would be possible if I had merely saved user passwords into a database.
    </p>
    <p> This cybersecure journal that allows any user who forks the Repl to create something like 50,000 separate journals—each with innumerable journal entries—is not 100% safe from professional hackers. Though there are multiple layers of security built into the program Through the use of hashing and salting passwords, it is still conceivable that someone with sufficiently advanced hacking methodologies could reverse engineer the user's password. This is extraordinarily unlikely, however; the salt appended to the end of the passwords inputted ranges from one to 999,999.
    </p>
    <p> This program was probably the most exciting for me to build because I had no prior experience with anything related to cyber security and the sheer technical prowess possible with computational technology ceases to amaze me. <a href="https://replit.com/@JosephBrockly-A">Repl.it</a>'s <b><i>100 Days of Python</i></b> challenge involves building quite a few different versions of login systems that ask users for their passwords and usernames. I, of course, never entered anything beyond extremely basic usernames and passwords because I did not want to jeopardize any actual security, but I perhaps naively believed that Repl.it itself took enough precaution to protect this information. This was all before I was learned about Repl.it's Secrets tool, the concept of forking a program, hashing, precomputation, rainbow tables, salting, and pepper values (a concept I thankfully stumbled across by accident). this area of computer programming is actually deeply fascinating because it represents the truest form of a dialectical cat and mouse game where whoever maintains one step ahead becomes the winner. 
    </p>

    <!-- Image and link -->
    <a href="https://replit.com/@JosephBrockly-A/Cybersecure-Journal-Day-72-of-100" ><img src="/static/Images/day66.jpg" width = 1000 ></a>

    <!-- Hyperlinks to other pages organized within an unordered list -->
    <ul>
      <li><a href="https://flask-web-server-day-76-of-100.josephbrockly-a.repl.co/linktree">Linktree</a></li>
      <li><a href="https://flask-web-server-day-76-of-100.josephbrockly-a.repl.co/showcase">Showcase</a></li>
      <li><a href = "https://flask-web-server-day-76-of-100.josephbrockly-a.repl.co/showcase/adventureGenerator">Adventure Generator</a></li>
      <li><a href = "https://flask-web-server-day-76-of-100.josephbrockly-a.repl.co/showcase/spacetime!">Spacetime!</a></li>
      <li><a href = "https://flask-web-server-day-76-of-100.josephbrockly-a.repl.co/showcase/theEventHorizon">The Event Horizon</a></li>
      <li><a href = "https://flask-web-server-day-76-of-100.josephbrockly-a.repl.co/showcase/simpleCalculator">Simple Calculator</a></li>
      <li><a href = "https://flask-web-server-day-76-of-100.josephbrockly-a.repl.co/showcase/cybersecureJournal">Cybersecure Journal</a></li>
    </ul>
    
  <script src="script.js"></script>  
  </body>
</html>
  """
  return page

app.run('0.0.0.0', port=81)