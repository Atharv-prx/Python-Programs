import random

def spin_row():
    symbols = ['🔔', '🍉', '⭐', '🍒', '🍋']

    return [random.choice(symbols) for x in range(3)]

# Can use this if don't wanna use list comprehension
#    results = []
#    for x in range(3):
#        results.append(random.choice(symbols))
#    return results


def print_row(row):
    print(" | ".join(row)) #Join each element with |

def get_payout(row, bet):
    if row[0] == row [1] == row[2]:
        if row[0] == '🍒':
            return bet*3
        elif row[0] == '🍉':
            return bet*4
        elif row[0] == '🍋':
            return bet*5
        elif row[0] == '🔔':
            return bet*10
        elif row[0] == '⭐':
            return bet*20
    else:
        return 0

def main():
    balance = 100
    print("=======================")
    print("Welcome to Slot Machine")
    print("Symbols: 🔔🍉⭐🍒🍋")
    print("=======================")

    while balance > 0:
        print(f"Current Balance: ${balance}")

        bet = input("Place your bet amount: ")
        if not bet.isdigit():
            print("Enter a valid number!")
            continue
        bet = int(bet)

        if bet > balance:
            print("Insufficient funds!")
            continue
        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning .....")
        print()
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won: ${payout}")
        else:
            print("Better luck next time")

        balance += payout

        play_again = input("Do you want to play again (y/n): ").lower()
        if play_again != 'y':
            break

if __name__ == '__main__':
    main()