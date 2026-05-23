def get_int(prompt):

    while True:

        try:
            value = int(input(prompt))
            return value
        
        except ValueError:
            print("Invalid number")

def get_two_numbers():

    num1 = get_int("Enter num 1: ")
    num2 = get_int("Enter num 2: ")

    return num1, num2

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

def find_gcd(num1, num2):
    
    # Euclidean Algorithm
    num_1 = abs(num1)
    num_2 = abs(num2)
    
    while num_1 != 0:

        num_2, num_1 = num_1, num_2 % num_1

    return num_2

def find_lcm(num1, num2):
    
    a = num1
    b = num2

    gcd = find_gcd(num1, num2)

    lcm = abs(a*b) // gcd  # // ---> gives integer result

    return lcm


def main():

    while True: 
        print("======= GCD/LCM Calculator =======")
        print("1. GCD")
        print("2. LCM")
        print("3. Exit")
        choice = get_choice("Enter your choice: ", 1,3)

        if choice == 1:

            num1, num2 = get_two_numbers()
            
            if num1 == 0 and num2 == 0:
                print("GCD undefined for (0,0)")
                pause()
                continue

            result = find_gcd(num1, num2)

            print(f"GCD: {result}")
            pause()

        elif choice == 2:

            num1, num2 = get_two_numbers()

            if num1 == 0 and num2 == 0:
                print("LCM: 0")
                pause()
                continue

            result = find_lcm(num1, num2)

            print(f"LCM: {result}")
            pause()
        
        elif choice == 3:
            print("Bawwright")
            break

if __name__ == "__main__":
    main()