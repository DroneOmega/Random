print("Welcome to Hangman!\n")

word = list("computing")
guessed_word = list("_________")
lives = 10
wordGuessed = False

while lives>=1 and not wordGuessed:

    print(" ".join(guessed_word))

    user_guess = input( "Guess a letter/word! (" + str(lives) + \
                        " lives remaining)\n")

    # Check if letter is in the word
    letter_in_word = False
    for i in range(len(word)):
        if user_guess = word[i]:
            guessed_word[i] = user_guess
            letter_in_word = True

    if letter_in_word == False:
        lives -= 1

    if guessed_word = word:
        print(" ".join(guessed_word))
        print("You have guessed the word correctly!")
        wordGuessed=True
    elif lives > 1:
        print("You failed to guess the word correctly :(")

input("Press enter to exit.")
