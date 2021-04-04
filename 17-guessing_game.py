# This is going to build a guessing game using a comination of all code elements used to date

secret_place = "Dublin"
# This is the secret place, which is the answer
guess = ""
# The guess variable stores the users guesses
guess_count = 0
# This is the starting count for user guesses which is set to 0
guess_limit = 3
# This states that the user only has 3 guesses
out_of_guesses = False
# This boolean variable whether the user is out of guesses 


while guess != secret_place and not(out_of_guesses):
# While the user has not guessed the secret word, this will keep lopping and asking for input
    if guess_count < guess_limit:
    # This checks if the user is out of guesses or not. If they still have guesses left, the "if" statement runs
        guess = input("Name a capital city in Europe: ")
        # This is asking the user for input
        guess_count += 1
        # This adds one to the guess count
    else:
        out_of_guesses = True
        # If they are out of guesses, it will move down to the else

if out_of_guesses:
    print("Out of guesses, Hard Luck!!")
    # If the users runs out of guesses, the game ends with this message
else:
    print("You guessed correctly!!")
    # If the users guesses correctly, the game ends with this message

