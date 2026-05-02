import random

options = ("R", "P", "S")
score = 0

print("====Welcome to Rock paper Scissors game====")
while True: #Play again Loop
    Computer = random.choice(options)
    Player = None
    print("Choose one of the following")

    #Input validation loop
    while True:
        Player = input("R for Rock, S for Scissors, P for Paper: ").upper()

        if Player in options:
            break
        else:
            print("Invalid input! Please Enter R, P, or S")
    print()

    #Showing user choice
    if Player == "R":
        print("You choose Rocks")
    elif Player == "S":
        print("You choose Scissors") 
    else:
        print("You choose Paper")

    #Showing computer choice
    if Computer == "R":
        print("Computer choose Rocks")
    elif Computer == "S":
        print("Computer choose Scissors") 
    else:
        print("Computer choose Paper")
    print()    

    #Winning condition
    if Player == Computer:
        print("It's a draw")
    elif (Player == "R" and Computer == "S") or (Player == "S" and Computer == "P") or (Player == "P" and Computer == "R") :
        print("You win!")
        score += 1
    else:
        print("Computer wins!")
    
    #Play again Option
    while True:
        choice = input("\nDo you want to play again? (y/n): ").lower()
        if choice in ("y", "n"):
            break
        else:
            print("Please enter 'y' or 'n' only.")
    
    if choice == "n":
        print(f"Your total score was {score}")
        print("Thanks for playing!")
        break