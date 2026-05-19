def get_choice(prompt, min_value, max_value):

    while True:

        try:
            value = int(input(prompt))

            if min_value <= value <= max_value:
                return value
            
            print(f"Enter a number between {min_value}-{max_value}.")

        except ValueError:
            print("Invalid number.")

def get_positive_float(prompt):

    while True:

        try:
            value = float(input(prompt))

            if value > 0:
                return value
            
            print("Enter a positive number.")

        except ValueError:
            print("Invalid number.")

def pause():
    input("\nPress Enter to continue...")

def get_float(prompt):

    while True:

        try:
            value = float(input(prompt))
            return value

        except ValueError:
            print("Invalid number.")