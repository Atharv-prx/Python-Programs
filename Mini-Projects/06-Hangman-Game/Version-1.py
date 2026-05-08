import random

words = ["charmander", "pikachu", "balbasaur", "squirtle"]

hangman_art = {0: ("   ",
                   "   ",
                   "   "),
                1: (" o ",
                    "   ",
                    "   "),
                2: (" o ",
                    " | ",
                    "   "),
                3: (" o ",
                    "/| ",
                    "   "),
                4: (" o ",
                    "/|\\",
                    "   "),
                5: (" o ",
                    "/|\\",
                     "/  "),
                6: (" o ",
                    "/|\\",
                    "/ \\")}   #Can't use single backslash cuz it is a escape sequence so we use double backslash to print backslash

def display_man(wrong_guesses):

    print("===")
    for x in hangman_art[wrong_guesses]:
        print(x)
    print("===")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main(): 
    answer = random.choice(words)
    hint = ["_"]*len(answer)
    wrong_guesses = 0
    guessed_letters = set() #Can't create a empty set with just ()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Guess the name of starter pokemon: ").lower()
        
        #Input validatin if user enters multiple letters
        if len(guess) != 1:
            print("Invalid Input!, You can guess only 1 letter at a time")
            continue

        #Input validation if user enters numbers
        if not guess.isalpha():
            print("Invalid Input!, Enter a single alphabet")
            continue
        
        #Input validation if user guesses the same guess again 
        if guess in guessed_letters:
            print("Already guesses")
            continue
        
        #Adding guessed letters to "guessed_letters" set
        guessed_letters.add(guess)
        
        #Check if guessed letter is in the randomly selected word 
        if guess in answer:
            for x in range(len(answer)):   
                if answer[x] == guess:         
                    hint[x] = guess
        else:
            wrong_guesses += 1
         
        #Win condition 
        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You won!")
            is_running = False
        
        #Lose condition
        elif wrong_guesses >= len(hangman_art)-1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You lost!")
            is_running = False
        
if __name__ == '__main__':
    main()