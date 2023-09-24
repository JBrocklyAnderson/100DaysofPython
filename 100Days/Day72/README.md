# Cybersecure Journal

This is a security update to Day 62's private journal program. I have utilized the Repl.it database's two-dimensional dictionary functionality in order to provide the user with the ability to create multiple journal accounts under different usernames and passwords. To make these journals as secure as possible, I have appended salts to the user's passwords and stored them as hashed values. 

NOTE: This system of security is not perfectly immune to sophisticated hacking methodologies, but it is robust to attempts by hackers at reverse engineering passwords through the use of precomputed rainbow tables. 