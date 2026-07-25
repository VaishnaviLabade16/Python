import random

number = random.randint(1,100)

while True:
    guess = int(input("Guess Number: "))

    if guess == number:
        print("Correct!")
        break
    elif guess < number:
        print("Too Small")
    else:
        print("Too Large")