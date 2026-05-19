from Helpers import get_choice
from Helpers import get_positive_float
from Helpers import pause
from Helpers import get_float
import math

# =======================
# Shared Hyperbola Inputs

def get_hyperbola_info():

    x = get_positive_float("Enter x-axis semi-axis length: ")
    y = get_positive_float("Enter y-axis semi-axis length: ")

    orientation = input(
        "Enter orientation (horizontal/vertical): "
    ).lower()

    while orientation not in ["horizontal", "vertical"]:
        print("Invalid orientation.")
        orientation = input(
            "Enter orientation (horizontal/vertical): "
        ).lower()

    return x, y, orientation

# ==============
# Hyperbola Menu

def hyperbola_menu():
    print("\n===============")
    print("Hyperbola Menu")
    print("===============")
    print("1.  Find Eccentricity")
    print("2.  Find Latus Rectum")
    print("3.  Find Focal Length")
    print("4.  Find Asymptotes")
    print("5.  Find Directrix")
    print("6.  Find Focus Coordinate")
    print("7.  Find Transverse/Conjugate Axis Length")
    print("8.  Find Vertex")
    print("9.  Find Equation")
    print("10. Back")

    return get_choice("Choose an option: ", 1, 10)

# ==================
# Hyperbola Features

def find_hyperbola_eccentricity():
    pass

def find_hyperbola_latus_rectum():
    pass

def find_hyperbola_focal_length():
    pass

def find_hyperbola_asymtotes():
    pass

def find_hyperbola_directrix():
    pass

def find_hyperbola_focus_coordinate():
    pass

def find_hyperbola_axes_length():
    pass

def find_hyperbola_vertex():
    pass

def find_hyperbola_equation():
    pass

# ==================================================
# Hyperbola Controller Function

def hyperbola_program():

    hyperbola_actions = {

        1: find_hyperbola_eccentricity,
        2: find_hyperbola_latus_rectum,
        3: find_hyperbola_focal_length,
        4: find_hyperbola_asymtotes,
        5: find_hyperbola_directrix,
        6: find_hyperbola_focus_coordinate,
        7: find_hyperbola_axes_length,
        8: find_hyperbola_vertex,
        9: find_hyperbola_equation
    }

    while True:

        choice = hyperbola_menu()

        if choice == 10:
            break

        hyperbola_actions[choice]()