import random 

card={ "A♠": 11, "2♠": 2, "3♠": 3, "4♠": 4, "5♠": 5, "6♠": 6, "7♠": 7,
    "8♠": 8, "9♠": 9, "10♠": 10, "J♠": 10, "Q♠": 10, "K♠": 10,

    "A♥": 11, "2♥": 2, "3♥": 3, "4♥": 4, "5♥": 5, "6♥": 6, "7♥": 7,
    "8♥": 8, "9♥": 9, "10♥": 10, "J♥": 10, "Q♥": 10, "K♥": 10,

    "A♦": 11, "2♦": 2, "3♦": 3, "4♦": 4, "5♦": 5, "6♦": 6, "7♦": 7,
    "8♦": 8, "9♦": 9, "10♦": 10, "J♦": 10, "Q♦": 10, "K♦": 10,

    "A♣": 11, "2♣": 2, "3♣": 3, "4♣": 4, "5♣": 5, "6♣": 6, "7♣": 7,
    "8♣": 8, "9♣": 9, "10♣": 10, "J♣": 10, "Q♣": 10, "K♣": 10
}

STARTING_BALANCE = 1000

# ================
# Helper functions

def get_choice(prompt, min_value, max_value):

    while True:

        try:
            value = int(input(prompt))

            if min_value <= value <= max_value:
                return value
            
            print(f"Enter a number between {min_value}-{max_value}.")

        except ValueError:
            print("Invalid number.")

def pause():
    input("\nPress Enter to continue...")

def claculate_total_hand():
    pass

def display_hand():
    pass

def validate_bet():
    pass

# =============
# Game Features

def menu():

    print("===== Black Jack =====")
    print("1. Play Game")
    print("2. Show Rules")
    print("3. Exit")
    return get_choice("Enter your choice: ", 1, 3)

def show_rules():
    print("======= Rules =======")

    print("\nOBJECTIVE")
    print("Get a hand value closer to 21 than the dealer without going over 21.")

    print("\nCARD VALUES")
    print("A  = 11 or 1")
    print("2-10 = Face value")
    print("J, Q, K = 10")

    print("\nHOW TO PLAY")
    print("1. Place your bet")
    print("2. You and dealer receive 2 cards")
    print("3. Dealer hides one card")
    print("4. Choose an action:")

    print("\nACTIONS")
    print("HIT  (h)  → Draw another card")
    print("PASS (p)  → Keep current hand")

    print("\nBUST")
    print("If your total goes above 21,you automatically lose.")

    print("\nDEALER RULES")
    print("Dealer must keep drawing cards until the total is at least 17.")

    print("\nWINNING")
    print("You win if:")
    print("- Your total is higher than dealer")
    print("- Dealer busts")
    print("- You hit Blackjack (21)")

    print("\nBETTING")
    print("You start with $1000")
    print("Winning increases your balance.")
    print("Losing decreases your balance.")
     
    pause()

def get_bet_amount():
    pass

def deal_initial_cards():

    all_cards = list(card.keys())
    dealt = random.sample(all_cards, 4)
    player_hand = dealt[:2]
    dealer_hand = dealt[2:]

    print()
    display_hand("Your cards ", player_hand)
    display_hand("Dealer     ", dealer_hand, hide_second=True)

    return player_hand, dealer_hand

def get_player_action(player_hand):
    pass

def player_turn(player_hand):
    pass

def dealer_turn():
    pass

def update_balance(balance, result, bet_amount):
    pass

def check_winner(player_total, dealer_total):
    pass

def show_result():
    pass

def play_again():
    
    while True:

        choice = input("\nWanna play again? (y/n): ").strip().lower()

        if choice == "y":
            return True
        
        elif choice == "n":
            return False
        
        else:
            print("Please enter 'y' or 'n'")

# ============
# Main program

def play_round(balance):
    pass

def main():
    
    balance = STARTING_BALANCE

    while True:
        choice = menu()

        if choice == 1:

            if balance <= 0:

                print("\nYour broke ahh is out of money")
                break
            
            balance = play_round(balance)

            if balance <= 0:
                print(f"\nYour broke ahh is out of money")
                break

            if not play_again():
                print(f"\nThanks for playing, if you found any bugs then tell me")

        elif choice == 2: 
            show_rules()
        
        elif choice == 3:
            print("Thanks for playing, if you found any bugs then tell me")
            break

if __name__ == "__main__":
    main()