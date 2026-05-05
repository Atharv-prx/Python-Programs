# Added a function to display wrong guesses

import random

def get_guess (guesses):
    while True:
        letter = input("Guess a letter in the word: ").lower()

        # Validation
        if len(letter) != 1:
            print("Enter only ONE letter.")
        
        elif letter in guesses:
            print("You already guessed that letter")  

        else:
            return letter  

def process_guess(letter, word, guesses, attempts):
    guesses.append(letter)

    if letter in word:
        print(f"'{letter}' is in the word.")
    else:
        print(f"'{letter}' is NOT in the word.")
        attempts -= 1

    return attempts

def display_word(word, guesses):
    display = ""
    for char in word:
        if char in guesses:
            display += char + " "
        else:
            display += "_ "
    print("Word:", display)

def check_win(word, guesses):
    return all(char in guesses for char in word)


def check_loss(attempts):
    return attempts == 0

def display_wrong_guesses(letter, word, wrongGuesses):

    if letter in word:
        return None
    else:
        wrongGuesses.append(letter)
        print("Your wrong guesses are: ")
        for x in wrongGuesses:
            print(x, end="")
        print()

#====Main Game====

def play_game():
    word = random.choice(["pikachu", "charmander", "squirtle", "balbasaur", "strawberry","apple", "banana", "orange", "grape", "pineapple", "papaya", "mango"])
    wrongGuesses = []
    guesses = []
    attempts = 10

    print("Welcome to word guess game!")
    print("You get 10 attempts to guess the word\n")

    while True:
        letter = get_guess(guesses)

        attempts = process_guess(letter, word, guesses, attempts)

        display_word(word, guesses)

        display_wrong_guesses(letter, word, wrongGuesses)

        if check_win(word, guesses):
            print("You guessed the word!")
            break

        if check_loss(attempts):
            print(f"You are out of attempts! The word was '{word}'")
            break

        print(f"You have {attempts} attempts left\n")

# Run game
play_game()