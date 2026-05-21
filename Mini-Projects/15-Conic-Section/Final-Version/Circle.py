from Helpers import get_choice
from Helpers import get_positive_float
from Helpers import pause
import math

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

    radius = get_circle_radius()

    area = math.pi * radius**2

    print(f"Area: {area:.4f}")

    pause()

def find_circle_circumference():

    radius = get_circle_radius()

    circumference = 2*math.pi*radius

    print(f"Circumference: {circumference:.4f}")

    pause()

def find_circle_diameter():

    radius = get_circle_radius()

    diameter = radius*2

    print(f"Diameter: {diameter:g}")

    pause()
    
def find_circle_equation():

    radius = get_circle_radius()

    print(f"Equation: x² + y² = {radius**2:g}")

    pause()

# ==========================
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