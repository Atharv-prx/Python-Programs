from Helpers import get_choice
from Helpers import pause
from Helpers import get_positive_float
import math

# =====================
# Shared Parabola input

def get_parabola_info():

    a = get_positive_float("Enter focal parameter (a): ")

    direction = input("Enter direction (Left/Right/Up/Down): ").lower()

    while direction not in {"left", "right", "up", "down"}:
        print("Invalid direction")

        direction = input("Enter direction (Left/Right/Up/Down): ").lower()

    return a, direction

# =============
# Parabola Menu

def parabola_menu():
    
    print("\n=============")
    print("Parabola Menu")
    print("=============")
    print("1. Find Latus Rectum")
    print("2. Focus")
    print("3. Find Directrix")
    print("4. Find Equation")
    print("5. Back")
    
    return get_choice("Choose an option: ", 1, 5)
# =================
# Parabola Features

def find_parabola_latus_rectum():
    pass

def find_parabola_focus():
    pass

def find_parabola_directrix():
    pass

def find_parabola_equation():
    pass

# ============================
# Parabola Controller function

def parabola_program():

    parabola_actions = {

        1: find_parabola_latus_rectum,
        2: find_parabola_focus,
        3: find_parabola_directrix,
        4: find_parabola_equation
    }

    while True:

        choice = parabola_menu()

        if choice == 5:
            break

        parabola_actions[choice]()