# Helper functions for input validation
def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        
        except ValueError:
            print("Invalid number.")

def get_choice(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            print(f"Enter a number between {min_value}-{max_value}.")
        except ValueError:
            print("Invalid number.")

def get_linear_equation_coefficients(equation_number):

    print(f"\nEquation {equation_number}: a{equation_number}x + b{equation_number}y = c{equation_number}")
    a = get_float(f"Enter a{equation_number}: ")
    b = get_float(f"Enter b{equation_number}: ")
    c = get_float(f"Enter c{equation_number}: ")
    return a, b, c

def get_quadratic_equation_coefficients():
    print("\nQuadratic Equation: ax^2 + bx + c = 0")
    a = get_float("Enter a: ")
    b = get_float("Enter b: ")
    c = get_float("Enter c: ")
    return a, b, c

def main():

    while True:

        print("============= Main Menu ==============")
        print("1. Solve a system of linear equations")
        print("2. Solve a quadratic equation")
        print("3. Exit")

        choice = get_choice("Enter your choice (1-3): ", 1, 3)

        if choice == 1:
            a1, b1, c1 = get_linear_equation_coefficients(1)
            a2, b2, c2 = get_linear_equation_coefficients(2)

            d = (a1 * b2) - (a2 * b1)

            if d == 0:
                print("\nThe equations have no unique solution.")

            else:
                x = ((c1 * b2) - (c2 * b1)) / d
                y = ((a1 * c2) - (a2 * c1)) / d

                print("\nSolution:")
                print("x =", f"{x:.2f}")
                print("y =", f"{y:.2f}")
            
        elif choice == 2:
            a, b, c = get_quadratic_equation_coefficients()

            if a == 0:
                print("\nThis is not a quadratic equation.")
                continue

            discriminant = (b ** 2) - (4 * a * c)

            if discriminant > 0:

                root1 = (-b + (discriminant ** 0.5)) / (2 * a)
                root2 = (-b - (discriminant ** 0.5)) / (2 * a)

                print("\nTwo real roots:")
                print("Root 1 =", f"{root1:.2f}")
                print("Root 2 =", f"{root2:.2f}")

            elif discriminant == 0:

                root = -b / (2 * a)
                print("\nOne real root:")
                print("Root =", f"{root:.2f}")

            else:

                real_part = -b / (2 * a)
                imaginary_part = (abs(discriminant) ** 0.5) / (2 * a)
                print("\nTwo complex roots:")
                print(f"Root 1 = {real_part:.2f} + {imaginary_part:.2f}i")
                print(f"Root 2 = {real_part:.2f} - {imaginary_part:.2f}i")

        else:
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()