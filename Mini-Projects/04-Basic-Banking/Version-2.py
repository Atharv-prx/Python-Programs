#Converted code into Class version
#Added a feature to show transaction history

class BankAccount:
    def __init__(self, balance =0):
        self.balance = balance
        self.transactions = []

    def show_balance(self):
        print(f"Your balance is ${self.balance:.2f}")
        print()

    def deposit(self, amount):

        if amount <= 0:
            print("That's not a valid amount")
            return
        else:
            self.transactions.append(f"Deposited ${amount}")
            self.balance += amount

    def withdraw(self, amount):


            if amount > self.balance:
                print("Insufficient funds")
            elif amount <= 0:
                print("Invalid input.")
            else:
                self.transactions.append(f"Withdrawn amount- ${amount}")
                self.balance -= amount

    def show_transaction(self):
        if not self.transactions:
            print("No transactions yet.")
            return
        for x in self.transactions:
            print(x)
        print()
    
def main():
    account = BankAccount()
    is_running = True

    while is_running:
        print("=====Main Menu=====")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Check transaction history")
        print("5.Exit")
        choice = input("Enter your choice (1-5): ")
        print()

        if choice == '1':
            account.show_balance()

        elif choice == '2':
            try:
                amount = float(input("Enter an amount to be deposited: "))
                print()
                account.deposit(amount)
        
            except ValueError:
                print("Invalid input.")
                return 0
            
        elif choice == '3':
            try:
                amount = float(input("Enter amount to withdraw: "))
                print()
                account.withdraw(amount)

            except ValueError:
                print("Invalid input.")
                return 0
            
        elif choice == '4':
            account.show_transaction()

        elif choice == '5':
            is_running = False

        else:
            print("That is not a valid choice")

    print("Thank you! Have a nice day!")

if __name__ == '__main__':
    main()