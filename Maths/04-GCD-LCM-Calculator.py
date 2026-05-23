def get_int(prompt):

    while True:
        try:
            value = int(input(prompt))
            return value
        
        except ValueError:
            print("Invalid number")

def get_choice(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            print(f"Enter a number between {min_value}-{max_value}.")
        except ValueError:
            print("Invalid number.")

def find_gcd(num1, num2):
    pass

def find_lcm(num1, num2):
    pass

def main():

    while True: 
        print("GCD/LCM Calculator")
        print("1. GCD")
        print("2. LCM")
        print("3. Exit")
        choice = get_choice("Enter your choice: ", 1,3)

        if choice == 1:
            num1 = get_int("Enter num 1: ")
            num2 = get_int("Enter num2: ")
            find_gcd(num1, num2)

        elif choice == 2:
            num1 = get_int("Enter num 1: ")
            num2 = get_int("Enter num2: ")
            find_lcm(num1, num2)
        
        elif choice == 3:
            print("Bawwright")
            break

if __name__ == "__main__":
    main()