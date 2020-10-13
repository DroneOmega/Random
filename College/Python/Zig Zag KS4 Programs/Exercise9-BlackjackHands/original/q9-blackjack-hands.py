import random

def getValue(card):
    try:
        return int(card)
    except:
        if card == "J" or "Q" or "K":
            return 10
        else:
            return 11

print("Automatic Blackjack Player\n")

games = 0
gameOver=False

while not gameOver:

    deck = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] * 4
    random.shuffle(deck)

    hand = []
    score = 0

    while score < 17 and len(deck) != 0:
        card = deck.pop()
        hand.append(card)
        score = score + getValue(card)

    if score == 21:
        print("Blackjack!")
        games += 1
    if score < 21:
        print("You have scored " + str(score))
        games += 1
    else:
        print("Uh oh, you have gone bust!")
        games += 1

    print("Your cards were " + hand + "\n")

    if len(deck) < 1:
        gameOver=True

number_of_games = games
print("\nYou played " + str(number_of_games) + " games.")

input("Press enter to exit.")
