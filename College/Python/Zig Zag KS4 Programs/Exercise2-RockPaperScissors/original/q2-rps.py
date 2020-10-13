import random

def printRules():
    print("The computer will think of either rock, paper or scissors.")
    print("You will enter r for rock, p for paper or s for scissors.")
    print("The computer will reveal it's choice and the winner.")
    print()

def playGame():
    choice = input("Enter r for rock, p for paper or s for scissors: ")
    computerChoice = random.randint(0,2) # 0=rock, 1=paper, 2=scissors

    if computerChoice == 0:
        print("The computer chose: Rock")
    elif computerChoice == 1:
        print("The computer chose: Paper")
    else:
        print("The computer chose: Scissors")

    if choice == "r" or "R":
        if computerChoice == 0:
            print("It's a draw")
        elif computerChoice == 1:
            print("Computer Wins!")
        else:
            print("Player Wins!")
    elif choice == "p" or "P":
        if computerChoice == 0:
            print("Player Wins!")
        elif computerChoice == 1:
            print("It's a draw")
        else:
            print("Computer Wins!")
    elif choice == "s" or "S":
        if computerChoice == 0:
            print("Computer Wins!")
        elif computerChoice == 1:
            print("Player Wins!")
        else:
            print("It's a draw")
    else:
        print("==========================================================================")
        print("Your have not entered either r for rock, p for paper or s for scissors")
        print("==========================================================================")
        playGame()

print("Welcome to the Rock, Paper, Scissors Game")
print("=========================================")
printRules()
playGame()
print("Would you like to play again, yes or no?")
ans = input(">>> ")
if ans == "yes":
    printRules()
    playGame()
else:
    print("Thank you for playing. :)")
