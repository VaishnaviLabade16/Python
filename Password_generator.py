import random
import string

# Length of password
length = int(input("Enter password length: "))

# All possible characters
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = ""
for i in range(length):
    password += random.choice(characters)

print("Generated Password:", password)