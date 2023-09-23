# Cryptographic Basics

The program defines useful subroutines that append random salts to user inputted passwords before hashing the resultant concatenation and storing them in the database. Any number of different users can "create accounts" with the program. 

NOTE: This type of system is not perfectly secure and is only meant to demonstrate useful cryptographic concepts to build more secure systems from. Hackers could theoretically find a debug endpoint or use commands to dump your database, in which case they would have access to the usernames and their password salts and hashes. From their, this information could be subjected to decryption, so don't enter any sensitive information. 