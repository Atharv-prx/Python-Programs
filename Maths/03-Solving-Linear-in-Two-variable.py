def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        
        except ValueError:
            print("Invalid number.")

def get_equation_coefficients(equation_number):

    print(f"\nEquation {equation_number}: a{equation_number}x + b{equation_number}y = c{equation_number}")
    a = get_float(f"Enter a{equation_number}: ")
    b = get_float(f"Enter b{equation_number}: ")
    c = get_float(f"Enter c{equation_number}: ")
    return a, b, c

def main():

    a1, b1, c1 = get_equation_coefficients(1)

    a2, b2, c2 = get_equation_coefficients(2)

    d = (a1 * b2) - (a2 * b1)

    if d == 0:
        print("\nThe equations have no unique solution.")
    else:
        x = ((c1 * b2) - (c2 * b1)) / d
        y = ((a1 * c2) - (a2 * c1)) / d

        print("\nSolution:")
        print("x =", f"{x:.2f}")
        print("y =", f"{y:.2f}")

if __name__ == "__main__":
    main()