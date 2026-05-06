#Added a multi account system

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
    accounts = {}

    while True: #Whole system Loop
        current_account = None

        #Login/Create Account Screen
        while True:
            print("=====Bank System=====")
            print("1. Create Account")
            print("2. Login")
            print("3. Exit")
            choice = input("Enter your choice (1-3): ")
            print()

            if choice == '1':
                name = input("Enter account name: ")
                
                if name in accounts:
                    print("Account already exists\n")
                else:
                    accounts[name] = BankAccount()
                    print("Account created successfully\n")

            elif choice == '2':
                name = input("Enter account name: ")

                if name in accounts:
                    current_account = accounts[name]
                    print(f"Logged in as {name}\n")
                    break
                else:
                    print("Account not found\n")
            
            elif choice == '3':
                print("Thank you! Have a nice day!")
                return
            
            else:
                print("Invalid choice\n")

        #Account Menu
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
                current_account.show_balance()

            elif choice == '2':
                try:
                    amount = float(input("Enter an amount to be deposited: "))
                    print()
                    current_account.deposit(amount)
            
                except ValueError:
                    print("Invalid input.\n")
                    return 0
                
            elif choice == '3':
                try:
                    amount = float(input("Enter amount to withdraw: "))
                    print()
                    current_account.withdraw(amount)

                except ValueError:
                    print("Invalid input.\n")
                    return 0
                
            elif choice == '4':
                current_account.show_transaction()

            elif choice == '5':
                print("Logging out...\n")
                break

            else:
                print("That is not a valid choice\n")

if __name__ == '__main__':
    main()