import random
import string

print("Password Generator")
length=int(input("Enter the length of the password:")) # user input the length of the password
Uppercase = string.ascii_uppercase # variable Uppercase Holds the upper case letters like 
Lowercase = string.ascii_lowercase # variable Lowercase Holds the upper case letters 
Symbols = string.punctuation # Variable Symbols Holds the Symbols like @,<

characters = Uppercase+Lowercase+Symbols # Character variables the all kind of strings like @,<,A,B,C,D,E,F,G,H,,abcdef

Randompick = random.sample(characters,length) # Randomly return a random strings with a particular length
password=''.join(Randompick)  # join function is used to concatenate the random strings returned by random.sample()
print("Generated Password:",password) # finally displaying the password in the terminal