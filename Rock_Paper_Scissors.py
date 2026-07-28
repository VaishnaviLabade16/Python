import random

choices = ["Rock","Paper","Scissors"]

computer = random.choice(choices)

user = input("Enter Rock/Paper/Scissors: ")

print("Computer:", computer)

if user == computer:
    print("Draw")
elif (user=="Rock" and computer=="Scissors") or \
     (user=="Paper" and computer=="Rock") or \
     (user=="Scissors" and computer=="Paper"):
    print("You Win")
else:
    print("Computer Wins")