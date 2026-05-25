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

def calculate_total_hand(hand):
    # Sum hand value, adjusting Aces from 11 → 1 to avoid busting

    total = sum(card[c] for c in hand)

    aces = sum(1 for c in hand if c.startswith("A"))

    while total > 21 and aces:

        total -= 10
        aces -= 1
    
    return total

def is_blackjack(hand):
    # True if hand is a natural blackjack (exactly 2 cards totalling 21)

    return len(hand) == 2 and calculate_total_hand(hand) == 21

def is_bust(hand):
    return calculate_total_hand(hand) > 21

def draw_card(existing_hand):
    # Draw one card that isn't already in the provided hand

    available = [c for c in card if c not in existing_hand]

    if not available:
        raise RuntimeError("No cards left in deck")
    
    return random.choice(available)

def display_hand(label, hand, hide_second=False):
    # Print a labelled hand; optionally conceal the second card  
      
    if hide_second:
        print(f"{label}: {hand[0]}  ?    (showing {card[hand[0]]})")

    else:
        total = calculate_total_hand(hand)
        print(f"{label}: {' '.join(hand)}    (total: {total})")

def validate_bet(bet, balance):

    # Return an error message string, or None if the bet is valid

    if bet <= 0:
        return "Bet must be greater than $0."
    
    if bet > balance:
        return f"You only have ${balance}. Can't bet ${bet}."
    
    return None

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

def get_bet_amount(balance):
    # Prompt till a valid bet in entered

    while True:
        try:
            bet = int(input(f"\nYour balance: ${balance} | Enter bet: $"))
            error = validate_bet(bet, balance)

            if error:
                print(error)
            else:
                return bet
            
        except ValueError:
            print("Please enter a whole number.")

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
    # Prompt the player for hit or stand; return 'h' or 's'

    while True:

        action = input("\nHit (h) or Stand (s)? ").strip().lower()

        if action in ("h", "s"):
            return action
        
        print("Please enter 'h' to hit or 's' to stand.")

def player_turn(player_hand):
    # Let the player hit until they stand or bust, Returns the final hand.

    while True:
        total = calculate_total_hand(player_hand)

        if total == 21:
            print("\nYou hit 21!")
            break

        if is_bust(player_hand):
            print(f"\nBust! Your total is {total}.")
            break

        action = get_player_action(player_hand)

        if action == "h":
            new_card = draw_card(player_hand)
            player_hand.append(new_card)
            print(f"\nYou drew: {new_card}")
            display_hand("Your cards ", player_hand)
        else:
            print(f"\nYou stand with {total}.")
            break

    return player_hand

def dealer_turn(dealer_hand, player_hand):
    # Reveal dealer's hidden card, then draw until total ≥ 17, Returns the final dealer hand

    print("\n=== Dealer's turn ===")
    display_hand("Dealer     ", dealer_hand)

    while calculate_total_hand(dealer_hand) < 17:

        new_card = draw_card(player_hand + dealer_hand)
        dealer_hand.append(new_card)

        print(f"Dealer drew: {new_card}")
        display_hand("Dealer     ", dealer_hand)

    total = calculate_total_hand(dealer_hand)

    if is_bust(dealer_hand):
        print(f"Dealer busts with {total}!")

    else:
        print(f"Dealer stands with {total}.")

    return dealer_hand

def update_balance(balance, result, bet_amount, blackjack = False):
    # Adjust balance; blackjack pays 1.5×

    if result == "player":
        winnings = int(bet_amount * 1.5) if blackjack else bet_amount
        balance += winnings

    elif result == "dealer":
        balance -= bet_amount

    # draw → no change
    return balance

def check_winner(player_total, dealer_total):

    if player_total > 21:
        return "dealer"
    
    elif dealer_total > 21:
        return "player"
    
    elif player_total > dealer_total:
        return "player"
    
    elif dealer_total > player_total:
        return "dealer"
    
    else:
        return "draw"

def show_result(result, blackjack = False):

    print("========== Results ==========")

    if result == "player":

        if blackjack:
            print("BLACKJACK! You win 1.5× your bet")

        else:
            print("You win!")

    elif result == "dealer":
        print("Dealer wins, Imagine losing 🥀.")

    else:
        print("It's a draw. Bet returned.")
     
    print("=============================")

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
    # Run a single round and return the updated balance
    bet = get_bet_amount(balance)
 
    player_hand, dealer_hand = deal_initial_cards()
 
    # Check player blackjack immediately
    if is_blackjack(player_hand):
        print("\nBlackjack")

        # Dealer only peeks at their hole card — no drawing
        print("\n--- Dealer reveals hole card ---")
        display_hand("Dealer     ", dealer_hand)

        if is_blackjack(dealer_hand):
            print("Dealer also has Blackjack!")
            result = "draw"

        else:
            result = "player"
            
        blackjack = (result == "player")

    else:
        # Player's turn
        player_hand = player_turn(player_hand)
 
        if is_bust(player_hand):
            result = "dealer"
            blackjack = False
        else:
            # Dealer's turn
            dealer_hand = dealer_turn(dealer_hand, player_hand)
            player_total = calculate_total_hand(player_hand)
            dealer_total = calculate_total_hand(dealer_hand)
 
            print(f"\nFinal — You: {player_total}  |  Dealer: {dealer_total}")
            result = check_winner(player_total, dealer_total)
            blackjack = False
 
    show_result(result, blackjack)
    balance = update_balance(balance, result, bet, blackjack)
    print(f"Your balance: ${balance}")
    return balance

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
                print("\nYour broke ahh is out of money")
                break

            if not play_again():
                print("🥀")

        elif choice == 2: 
            show_rules()
        
        elif choice == 3:
            print("Thanks for playing, if you found any bugs then tell me")
            break

if __name__ == "__main__":
    main()