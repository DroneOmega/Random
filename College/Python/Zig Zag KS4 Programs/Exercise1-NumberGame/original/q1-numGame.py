import random

counter = 0

def guess():
    try:
        num = int(input("\u0332".join("Please enter your guess: ")))
        val = int(num)
        if num > 100:
            print("The number you have entered is too large.")
            print("Please try again.")
            guess()
        elif num < 1:
            print("your number you have entered is too small.")
            print("Please try again.")
            guess()
        else:
            return num
    except ValueError:
        print("That's not an int!")
        guess()

print("\u0332".join("Welcome to the number guessing game"))
print("The objective is to guess the number I'm thinking of.")
print("I will give you clues after your first guess.")
print("I have thought of a number from 1-100")
secretNumber = random.randint(1,100)
secretNumber = int(secretNumber)
numGuessed = guess()
while numGuessed != secretNumber:
    if numGuessed < secretNumber:
        print("Guess is too low, guess higher!")
        counter += 1
        numGuessed=guess()
    elif numGuessed > secretNumber:
        print("Guess is too high, guess lower!")
        counter += 1
        numGuessed=guess()
print("Correct! The number is {}".format(secretNumber))
counter += 1
print("It Took You {} Tries to Guess Correctly".format(counter))
