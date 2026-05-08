import random

number = random.randint(1, 100)
tries = 0

print("Welcome to random number guess game from 1-100")

while True:
    # Making sure that user puts a number
    try:
        guess = int(input("Guess the number: "))
    except ValueError:
        print("Please enter a valid number!")
        continue
    
    #Making sure that user enters number within range
    if guess < 1 or guess > 100:
        print("Please guess between 1 and 100!")
        continue

    tries += 1

    if guess < number:
        print("Too low ")
    elif guess > number:
        print("Too high ")
    else:
        print("Correct guess!")
        break

print(f"Number of tries: {tries}")