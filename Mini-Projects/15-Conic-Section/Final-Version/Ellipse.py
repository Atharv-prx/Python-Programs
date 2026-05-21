from Helpers import get_choice
from Helpers import get_positive_float
from Helpers import pause
import math

# =====================
# Shared Ellipse inputs

def get_ellipse_axes():

    x = get_positive_float("Enter x-axis semi-axis length: ")
    y = get_positive_float("Enter y-axis semi-axis length: ")

    return x, y

def get_ellipse_info():

    x, y = get_ellipse_axes()

    if x >= y:
        a = x
        b = y
        orientation = "horizontal"
    
    else:
        a = y
        b = x
        orientation = "vertical"

    return a, b, orientation

def is_circle(a , b):
    return math.isclose(a, b ,rel_tol = 1e-9 )

# ==================================================
# Ellipse - Menu

def ellipse_menu():
    
    print("\n=============")
    print("Ellipse Menu")
    print("=============")
    print("1.  Find Eccentricity")
    print("2.  Find Latus Rectum")
    print("3.  Find Focal Length")
    print("4.  Find Area")
    print("5.  Find Directrix")
    print("6.  Find Focus Coordinate")
    print("7.  Find Major/Minor Axis Length")
    print("8.  Find Vertex")
    print("9.  Find Equation")
    print("10. Back")

    return get_choice("Choose an option: ", 1, 10)

# ==================================================
# Ellipse Features

def find_ellipse_eccentricity():

    a, b, _ = get_ellipse_info()

    if is_circle(a,b):
        print("This is a circle, so the eccentricity is 0.")
        pause()
        return
    
    eccentricity = math.sqrt(1 - (b**2 / a**2))

    print(f"Eccentricity: {eccentricity:.4f}")
    pause()

def find_ellipse_latus_rectum():

    a, b, _ = get_ellipse_info()

    if is_circle(a, b):
        print(f"This is a circle, so latus rectum = diameter = {2*a:g}")
        pause()
        return

    latus_rectum = (2 * b**2) / a

    print(f"Latus rectum: {latus_rectum:g}")
    pause()

def find_ellipse_focal_length():

    a, b, _ = get_ellipse_info()

    if is_circle(a, b):
        print("This is a circle, so focal length = 0.")
        pause()
        return

    focal_length = math.sqrt(a**2 - b**2)

    print(f"Focal length: {focal_length:.4f}")
    pause()

def find_ellipse_area():

    a, b, _ = get_ellipse_info()

    area = math.pi * a * b

    print(f"Area: {area:.4f}")
    pause()

def find_ellipse_directrix():
    
    a, b, orientation = get_ellipse_info()

    if is_circle(a, b):
        print("Circle has no directrix.")
        pause()
        return

    eccentricity = math.sqrt(1 - (b**2 / a**2))
    directrix = a / eccentricity

    if orientation == "horizontal":
        print(f"Directrix: x = ±{directrix:.4f}")

    else:
        print(f"Directrix: y = ±{directrix:.4f}")

    pause()

def find_ellipse_focus_coordinate():

    a, b, orientation = get_ellipse_info()

    if is_circle(a, b):
        print("Circle focus is at center (0,0).")
        pause()
        return

    c = math.sqrt(a**2 - b**2)

    if orientation == "horizontal":
        print(f"Focus coordinates: (±{c:g}, 0)")

    else:
        print(f"Focus coordinates: (0, ±{c:g})")

    pause()

def find_ellipse_axes_length():

    a, b, _ = get_ellipse_info()

    print(f"Major axis length: {2*a:g}")
    print(f"Minor axis length: {2*b:g}")

    pause()

def find_ellipse_vertex():
    
    a, _, orientation = get_ellipse_info ()

    if orientation == "horizontal":
        print(f"Vertex coordinates: (±{a:g}, 0)")

    else:
        print(f"Vertex coordinates: (0, ±{a:g})")
    
    pause()

def find_ellipse_equation():

    a, b, orientation = get_ellipse_info()

    if is_circle(a, b):
        print(f"Equation: x²/{a**2:g} + y²/{a**2:g} = 1")
        pause()
        return
    
    if orientation == "horizontal":
        print(f"x²/{a**2} + y²/{b**2} = 1")

    else:
        print(f"x²/{b**2} + y²/{a**2} = 1")
    
    pause()

# ==================================================
# Ellipse Controller Function

def ellipse_program():

    ellipse_actions = {

        1: find_ellipse_eccentricity,
        2: find_ellipse_latus_rectum,
        3: find_ellipse_focal_length,
        4: find_ellipse_area,
        5: find_ellipse_directrix,
        6: find_ellipse_focus_coordinate,
        7: find_ellipse_axes_length,
        8: find_ellipse_vertex,
        9: find_ellipse_equation
    }

    while True:

        choice = ellipse_menu()

        if choice == 10:
            break

        ellipse_actions[choice]()