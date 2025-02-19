"""
Author: Moïse Marc-Aurel MASSAMBA-DILUEKI

Project_title: Word Puzzle

Purpose: The purpose of this program is to create a word puzzle game where the user is given a word and they have to guess the word by entering a letter at a time.
The user has a limited number of guesses to guess the word.
I've added, a list of secret words, randomly selected secret word, hint based on the user's guess, feedback message to the user, game over message if the user runs out of attempts and A congratulatory message if the user guesses the word correctly

"""

import random

# List of secret words
secret = ["software", "python", "internet", "robot", "algorithm", "security", "cassava", "iced tea", "bubble tea", "congo"]
# Randomly select a secret word
secret = random.choice(secret)

# Welcome message
print("*" * 50)
print("\nWelcome to the Word Puzzle Game!")

# Variable initialization
guess = ""
guess_count = 0
max_guesses = 10  # Maximum allowed guesses
word = len(secret) * "_ "
print("\nYour hint is: " + word)
word = ""

# Main game loop
while guess != secret and guess_count < max_guesses:
    # Get the user's guess and convert it to lowercase
    guess = input("\nWhat is your guess? ").lower()
    guess_count += 1

    # Check if the guess length matches the secret word length
    if len(guess) != len(secret):
        print("\nYour guess is not the same length as the secret word. Please try again!")
    else:
        hint = ""
        # Generate hint based on the user's guess
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                word = guess[i].upper()  # Correct letter in the correct position
            elif guess[i] in secret:
                if guess[i] in hint:
                    if hint.count(guess[i]) < secret.count(guess[i]):
                        word = guess[i]  # Correct letter but in the wrong position
                    else:
                        word = "_"
                else:
                    word = guess[i]  # Correct letter but in the wrong position
            else:
                word = "_"  # Incorrect letter
            
            hint += word

        # Provide feedback to the user
        if guess != secret:
            print(f"Your hint is: {' '.join(hint)}")
            print(f"Attempts left: {max_guesses - guess_count}")
            print("Try again!")
        
# Check if the user has guessed the word correctly
if guess == secret:
    print("\nCongratulations! You guessed it!")
    print(f"It took you {guess_count} guesses.")
else:
    print("\nGame Over! You've run out of attempts.")
    print(f"The correct word was: {secret}")
print("*" * 50)