#Imports
from random import randint as  rn
#Constants
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters += letters.lower()
numbers = "0123456789"
Symbols = "~`!@#$%^&*()_-+={[}]|\:;'<,>.?/" + '"'
AllCharacters = tuple(letters + numbers + Symbols)
#Classes

#Functions
def GeneratePassword(length = 12):
    password = ''
    for _ in range(length):
        password += AllCharacters[rn(0,len(AllCharacters) - 1)]
    
    return password

#Main
password = GeneratePassword()
print(password)
#Testing
