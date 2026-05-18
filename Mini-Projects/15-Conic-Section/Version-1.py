# Basic structure of what program will look like

import math
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

# ================
# Ellipse Features

def ellipse_menu():
    
    print("\n=============")
    print("Ellipse Menu")
    print("=============")
    print("1. Find Eccentricity")
    print("2. Find Latus rectum")
    print("3. Find focal length")
    print("4. Back to Main Menu")

    return get_choice("Choose an option: ", 1, 4)

def get_ellipse_axes():

    x = get_positive_float("Enter the length first axis (a): ")
    y = get_positive_float("Enter the length second axis (b): ")

    a = max(x, y)
    b = min(x, y)

    return a, b

def find_ellipse_eccentricity():

    a, b = get_ellipse_axes()

    if math.isclose(a, b, rel_tol=1e-9):  # Check if a and b are approximately equal
        print("This is a circle, so the eccentricity is 0.")
        pause()
        return
    
    eccentricity = (1 - (b**2 / a**2)) ** 0.5
    print(f"Eccentricity: {eccentricity:.4f}")
    pause()

def find_ellipse_latus_rectum():

    a, b = get_ellipse_axes()

    if math.isclose(a, b, rel_tol=1e-9):
        print("This is a circle, so the latus rectum is equal to the diameter 2a.")
        latus_rectum = 2 * a
        print(f"Latus rectum: {latus_rectum:.4f}")
        pause()

    else:
        latus_rectum = (2 * b**2) / a
        print(f"Latus rectum: {latus_rectum:.4f}")
        pause()
    

# =================
# Main program loop
def main():

    while True:
        print("\n===========================")
        print("Main Menu - Conic Sections")
        print("===========================")
        print("1. Circle (Coming Soon)")
        print("2. Parabola (Coming Soon)")
        print("3. Ellipse")
        print("4. Hyperbola (Coming Soon)")
        print("5. Exit")

        choice = get_choice("Choose an option: ", 1, 5)

        if choice == 3:

            while True:
                ellipse_choice = ellipse_menu()

                if ellipse_choice == 1:
                    find_ellipse_eccentricity()

                elif ellipse_choice == 2:
                    find_ellipse_latus_rectum()

                elif ellipse_choice == 3:
                    pass

                else:
                    break
        elif choice == 5:
            print("Exiting program.")
            break
        else:
            print("This feature is coming soon.")

if __name__ == "__main__":
    main()