door = ["goat","goat","car"]




    if door[1] == "goat":
        otherDoor = 3
        goatDoor = 2
    elif door[2] == "goat":
        otherDoor = 2
        goatDoor = 3
elif choice == 2:
    if door[0] == "goat":
        otherDoor = 3
        goatDoor = 1
    elif door[2] == "goat":
        otherDoor = 1
        goatDoor = 3
elif choice == 3:
    if door[0] == "goat":
        otherDoor = 2
        goatDoor = 1
    elif door[1] == "goat":
        otherDoor = 1
        goatDoor = 2
switch = input("There is a goat behind door " + goatDoor + \
if switch == "y":
    choice = otherDoor
if door[choice-1] == "car":
    print("You won a car!")
else:
    print("You won a goat!")
    