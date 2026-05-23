def get_int(prompt):

    while True:

        try:
            value = int(input(prompt))
            return value
        
        except ValueError:
            print("Invalid number")

def get_numbers():
 
    while True:
 
        try:
            count = int(input("How many numbers? "))
 
            if count >= 2:
                break
            print("Enter at least 2 numbers.")
 
        except ValueError:
            print("Invalid number.")
 
    numbers = []
 
    for i in range(1, count + 1):
        numbers.append(get_int(f"Enter num {i}: "))
 
    return numbers

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
    
    while num_1:

        num_2, num_1 = num_1, num_2 % num_1

    return num_2

def gcd_of_list(numbers):

    result = numbers[0]

    for n in numbers[1:]:   # [1:] is list slicing — it means "give me everything from index 1 onwards"
        result = find_gcd(result, n)
    return result

def find_lcm(num1, num2):
    
    gcd = find_gcd(num1, num2)

    return abs(num1*num2) // gcd  # // ---> gives integer result

def lcm_of_list(numbers):

    result = numbers[0]

    for n in numbers[1:]:
        result = find_lcm(result, n)
    return result

def main():

    while True: 
        print("======= GCD/LCM Calculator =======")
        print("1. GCD")
        print("2. LCM")
        print("3. Exit")
        choice = get_choice("Enter your choice: ", 1,3)

        if choice == 1:

            numbers = get_numbers()
            
            if all(n==0 for n in numbers):
                print("GCD undefined for all numbers")
                pause()
                continue

            result = gcd_of_list(numbers)

            print(f"GCD: {result}")
            pause()

        elif choice == 2:

            numbers = get_numbers()

            if any(n == 0 for n in numbers):
                print("LCM: 0")
                pause()
                continue

            result = lcm_of_list(numbers)

            print(f"LCM: {result}")
            pause()
        
        elif choice == 3:
            print("Bawwright")
            break

if __name__ == "__main__":
    main()