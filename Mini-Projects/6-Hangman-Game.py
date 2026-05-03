import random
import time

pokemon_data = { 
    # Grass / Poison
    "bulbasaur": "grass/poison",
    "ivysaur": "grass/poison",
    "venusaur": "grass/poison",

    # Fire
    "charmander": "fire",
    "charmeleon": "fire",
    "vulpix": "fire",
    "ninetales": "fire",
    "flareon": "fire",

    # Fire / Flying
    "charizard": "fire/flying",
    "moltres": "fire/flying",

    # Water
    "squirtle": "water",
    "wartortle": "water",
    "blastoise": "water",
    "psyduck": "water",
    "golduck": "water",
    "magikarp": "water",
    "vaporeon": "water",

    # Water / Flying
    "gyarados": "water/flying",

    # Bug
    "caterpie": "bug",

    # Bug / Flying
    "butterfree": "bug/flying",

    # Bug / Poison
    "weedle": "bug/poison",
    "beedrill": "bug/poison",

    # Normal
    "rattata": "normal",
    "raticate": "normal",
    "eevee": "normal",

    # Normal / Flying
    "pidgey": "normal/flying",
    "pidgeotto": "normal/flying",
    "pidgeot": "normal/flying",

    # Electric
    "pikachu": "electric",
    "raichu": "electric",
    "jolteon": "electric",

    # Electric / Flying
    "zapdos": "electric/flying",

    # Poison
    "ekans": "poison",
    "arbok": "poison",

    # Rock / Ground
    "geodude": "rock/ground",
    "graveler": "rock/ground",
    "golem": "rock/ground",
    "onix": "rock/ground",

    # Ghost / Poison
    "gastly": "ghost/poison",
    "haunter": "ghost/poison",
    "gengar": "ghost/poison",

    # Psychic
    "abra": "psychic",
    "kadabra": "psychic",
    "alakazam": "psychic",
    "mewtwo": "psychic",
    "mew": "psychic",

    # Fighting
    "machop": "fighting",
    "machoke": "fighting",
    "machamp": "fighting",

    # Ice / Flying
    "articuno": "ice/flying"
}

hangman_art = {
    0: ("   ", "   ", "   "),
    1: (" o ", "   ", "   "),
    2: (" o ", " | ", "   "),
    3: (" o ", "/| ", "   "),
    4: (" o ", "/|\\", "   "),
    5: (" o ", "/|\\", "/  "),
    6: (" o ", "/|\\", "/ \\")
}  #Can't use single backslash cuz it is a escape sequence so we use double backslash to print backslash

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
    answer = random.choice(list(pokemon_data.keys()))
    poke_type = pokemon_data[answer]

    hint = ["_"]*len(answer)
    wrong_guesses = 0
    guessed_letters = set() #Can't create a empty set with just ()
    is_running = True
    
    print("=======================================================================================")
    print("Welcome to Hangman Game")
    print("This game contains name of pokemon from season-1 ")
    print("You have to guess 1 letter at time, You only have 6 guesses to guess the correct word")
    print("=======================================================================================")

    print("Game starts in 5 seconds")
    print("Game starts in:", end=" ")
    for i in range(5, 0, -1):
        print(i, end=" ", flush=True)
        time.sleep(1)
    print("\n")

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Guess the letter: ").lower()
        
        if len(guess) != 1:             #Input validatin if user enters multiple letters
            print("Invalid Input!, You can guess only 1 letter at a time")
            continue
  
        if not guess.isalpha():         #Input validation if user enters numbers
            print("Invalid Input!, Enter a letter")
            continue
        
        if guess in guessed_letters:     #Input validation if user guesses the same guess again 
            print("Already guessed")
            continue
        
        guessed_letters.add(guess)       #Adding guessed letters to "guessed_letters" set
        
        if guess in answer:              #Game logic 
            print("Correct Guess!")
            for x in range(len(answer)):   
                if answer[x] == guess:         
                    hint[x] = guess
        else:
            print("Wrong Guess!")
            wrong_guesses += 1
            if wrong_guesses == 3:
                print("***************Special hint***************")
                print(f"Hint: This Pokémon is a {poke_type} type")
                print("******************************************")
         
        #Win condition 
        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("===You won!===")
            print(f"The pokemon was {poke_type} type")
            is_running = False
        
        #Lose condition
        elif wrong_guesses >= len(hangman_art)-1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("===You lost!===")
            print(f"The pokemon was {poke_type} type")
            is_running = False
        
if __name__ == '__main__':
    main()