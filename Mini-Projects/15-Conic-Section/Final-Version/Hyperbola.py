from Helpers import get_choice
from Helpers import get_positive_float
from Helpers import pause
import math

# =======================
# Shared Hyperbola Inputs

def get_hyperbola_info():

    a = get_positive_float("Enter transverse semi-axis length (a): ")
    b = get_positive_float("Enter conjugate semi-axis length (b): ")

    orientation = input(
        "Enter orientation (horizontal/vertical): "
    ).lower()

    while orientation not in ["horizontal", "vertical"]:
        print("Invalid orientation.")
        orientation = input(
            "Enter orientation (horizontal/vertical): "
        ).lower()

    return a, b, orientation

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

    a, b, _ = get_hyperbola_info()

    eccentricity = math.sqrt(1 + (b**2 / a**2)) 

    print(f"Eccentricity: {eccentricity:.4f}")
    pause()

def find_hyperbola_latus_rectum():
    
    a, b, _ = get_hyperbola_info()

    latus_rectum = (2 * b**2)/a

    print(f"Latus rectum: {latus_rectum:.4f}")
    pause()

def find_hyperbola_focal_length():

    a, b, _ = get_hyperbola_info()

    focal_length = math.sqrt(a**2 + b**2)

    print(f"Focal length: {focal_length:.4f}")
    pause()

def find_hyperbola_asymptotes():

    a, b, orientation = get_hyperbola_info()

    if orientation == "horizontal":
        slope = b / a

    else:
        slope = a / b

    print(f"Asymptotes: y = ±{slope:.4f}x")

    pause()

def find_hyperbola_directrix():
    
    a, b, orientation = get_hyperbola_info()

    eccentricity = math.sqrt(1 + (b**2 / a**2)) 
    directrix = a/eccentricity

    if orientation == "horizontal":
        print(f"Directrix: x = ±{directrix:.4f}")
        pause()

    else:
        print(f"Directrix: y = ±{directrix:.4f}")
        pause()

def find_hyperbola_focus_coordinate():

    a, b, orientation = get_hyperbola_info()

    c = math.sqrt(a**2 + b**2)

    if orientation == "horizontal":
        print(f"Focus coordinates: (±{c:.4f}, 0)")

    else:
        print(f"Focus coordinates: (0, ±{c:.4f})")

    pause()

def find_hyperbola_axes_length():

    a, b, _ = get_hyperbola_info()

    print(f"Transverse axis length: {2*a:.4f}")
    print(f"Conjugate axis length: {2*b:.4f}")

    pause()

def find_hyperbola_vertex():
    
    a, _, orientation = get_hyperbola_info()

    if orientation == "horizontal":
        print(f"Vertex coordinates: (±{a:.4f}, 0)")

    else:
        print(f"Vertex coordinates: (0, ±{a:.4f})")
    
    pause()

def find_hyperbola_equation():

    a, b, orientation = get_hyperbola_info()

    if orientation == "horizontal":
        print(f"x²/{a**2} - y²/{b**2} = 1")

    else:
        print(f"y²/{a**2} - x²/{b**2} = 1")

    pause()

# ==================================================
# Hyperbola Controller Function

def hyperbola_program():

    hyperbola_actions = {

        1: find_hyperbola_eccentricity,
        2: find_hyperbola_latus_rectum,
        3: find_hyperbola_focal_length,
        4: find_hyperbola_asymptotes,
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