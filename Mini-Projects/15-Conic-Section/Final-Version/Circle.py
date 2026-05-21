from Helpers import get_choice
from Helpers import get_positive_float
from Helpers import pause

# ===================
# Shared circle input

def get_circle_radius():

    radius = get_positive_float("Enter Radius: ")
    return radius

# ===========
# Circle Menu

def circle_menu():

    print("\n===========")
    print("Circle Menu")
    print("===========")
    print("1. Find Area")
    print("2. Find Circumference")
    print("3. Find Diameter")
    print("4. Find Equation")
    print("5. Back")

    return get_choice("Choose an option: ", 1, 5)

# ===============
# Circle Features

def find_circle_area():
    pass

def find_circle_circumference():
    pass

def find_circle_diameter():
    pass

def find_circle_equation():
    pass

# ===
# Circle Controller function

def circle_program():

    circle_actions = {

        1: find_circle_area,
        2: find_circle_circumference,
        3: find_circle_diameter,
        4: find_circle_equation
    }

    while True:
        choice = circle_menu()

        if choice == 5:
            break

        circle_actions[choice]()