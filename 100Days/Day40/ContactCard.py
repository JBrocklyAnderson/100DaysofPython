import os

# get user input
name = input("Name:  ").strip().title()
profession = input("Line of Work:  ").strip().title()
tagline = input("tagline:  ").strip().capitalize()
mission = input("Mission Statement:  ").strip().capitalize()
cell = input("Cell Phone:  ").strip()
email = input("Email:  ").strip()
address = input("Address:  ").strip()
company = input("Company:  ")
workPhone = input("Work Phone:  ")

# create a dictionary with contact information
contact = {
  "name":name,
  "profession":profession,
  "tagline":tagline,
  "mission":mission,
  "cell":cell,
  "email":email,
  "address":address,
  "company":company,
  "work":workPhone
}

# print a message to the contact
os.system("cls" if os.name == "nt" else "clear")
print(f"""
🪙  Company: {contact['company']} 
🌐 Work Phone: {contact['work']} 

🪪  Name: {contact['name']} 
💼 Profession: {contact['profession']} 

🏆 Tagline: {contact['tagline']} 
⚖️  Mission Statement: {contact['mission']} 

📱 Cell Phone:  {contact['cell']} 
📧 Email: {contact['email']}""")