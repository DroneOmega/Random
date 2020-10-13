import random
from pyisemail import is_email

def diceGame():
    dice = [1, 2, 3, 4, 5, 6]
    def rollDice():
        q = input(">>> ")
        if q == "yes":
            roll()
            print("Would you like to roll again? ")
            rollDice()
        elif q == "no":
            print("Okay thank you for rolling")
        else:
            print("Your input was invalid. Please type 'yes' or 'no'")
            rollDice()
    def roll():
        roll = random.choice(dice)
        print(roll)
    roll()
    print("Would you like to roll again? ")
    rollDice()

def fibonacci():
    n = int(input("Enter the number: "))
    n0, n1, n2 = 0, 1, 1
    if n == 0 or n == 1:
        Print("Yes")
    else:
        while n0 < n:
            n0 = n1 + n2
            n1 = n2
            n2 = n0
        if n0 == n:
            print("Yes")
        else:
            print("No")

def emailSplicer():
    email = input("Type your email here: ")
    stripedEmail = email.strip()
    search = is_email(email)
    result = is_email(email, diagnose=True)
    if search == True:
        username = stripedEmail[:stripedEmail.index("@")]
        domainname = stripedEmail[stripedEmail.index("@")+1:]
        output = "Your username is '{}' and your domain name is '@{}'".format(username,domainname)
        print(output)
    else:
        print("--------------------------------------")
        print("Invalid email address")
        print("--------------------------------------")
        emailSplicer()

def start():
    print("Projects Here:")
    print("diceGame")
    print("fibonacci")
    proj = input("What project would you like to run? ")
    if proj == "diceGame":
        diceGame()
    elif proj == "fibonacci":
        fibonacci()
    elif proj == "3":
        emailSplicer()
    else:
        print("-------------------------------------------------------------------------------------------")
        print("That is not a project. Make sure you have typed the correct project name (Case Sensitive).")
        print("-------------------------------------------------------------------------------------------")
        start()

start()
