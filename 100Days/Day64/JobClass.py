# create a class
class job:
  ## 
  name = None 
  salary = None
  hoursWorked = None

  def __init__(self, name, salary, hoursWorked):
    self.name = name
    self.salary = salary
    self.hoursWorked = hoursWorked

  def details(self):
    print(f"\033[36mJob\033[0m: {self.name}\nSalary: ${self.salary} per year\nHours Per Week: {self.hoursWorked}\n")

# instantiating a subclass that will inherit the parameters of its superclass
class teacher(job):
  ## define intialization method
  def __init__(self, subject, position): ## pass the proper paramaters
    self.name = "Teacher"
    self.salary = "47623"
    self.hoursWorked = "60"
    self.subject = subject
    self.position = position
  ## define print method
  def details(self):
    print(f"\033[36mJob\033[0m: {self.name}\nSalary: ${self.salary} per year\nHours Per Week: {self.hoursWorked}\nSubject: {self.subject}\nPosition: {self.position}\n")

# create subclass for "doctor"
class doctor(job):

  ## define initiatilization method
  def __init__(self, specialty, experience): # pass the proper parameters
    self.name = "Doctor"
    self.salary = "238769"
    self.hoursWorked = 55
    self.specialty = specialty 
    self.experience = experience
  ## define print method
  def details(self):
    print(f"\033[36mJob\033[0m: {self.name}\nSalary: ${self.salary} per year\nHours Per Week: {self.hoursWorked}\nSpecialty: {self.specialty}\nExperience: {self.experience} Year(s)\n")


# instatiate objects of the classes and subclasses
Lawyer = job("Lawyer", "136170", "45")
Teacher = teacher("History", "High School")
Doctor = doctor("Cardiovascular", 12)


print("\033[36mJobs Jobs Jobs!\033[0m\n")
# call the print methods
Lawyer.details()
Teacher.details()
Doctor.details()
