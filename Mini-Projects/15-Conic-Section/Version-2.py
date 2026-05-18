# Added dictionary dispatching

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
    print("4. Find Area")
    print("5. Find Directrix")
    print("6. Find Focus coordinate")
    print("7. Find major/minor axis length")
    print("8. Vertex coordinate")
    print("9. Find ellipse equation")
    print("10. Back to Main Menu")

    return get_choice("Choose an option: ", 1, 10)

def get_ellipse_axes():

    x = get_positive_float("Enter the first axis length: ")
    y = get_positive_float("Enter the second axis length: ")

    a = max(x, y)
    b = min(x, y)

    return a, b

def get_ellipse_info():

    x = get_positive_float("Enter x-axis semi-axis length: ")
    y = get_positive_float("Enter y-axis semi-axis length: ")

    if x >= y:
        a = x
        b = y
        orientation = "horizontal"

    else:
        a = y
        b = x
        orientation = "vertical"

    return a, b, orientation

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

def find_ellipse_focal_length():

    a, b = get_ellipse_axes()

    if math.isclose(a, b, rel_tol=1e-9):  
        print("This is a circle, so the focal length is 0.")
        pause()
        return
    
    focal_length = (a**2 - b**2) ** 0.5
    print(f"Focal length: {focal_length:.4f}")
    pause()

def find_ellipse_area():

    a, b = get_ellipse_axes()

    area = math.pi*a*b
    print(f"Area: {area:.4f}")
    pause()

def find_ellipse_directrix():
    
    a,b = get_ellipse_axes()

    if math.isclose(a, b, rel_tol=1e-9):  
        print("This is a circle.")
        pause()
        return
    
    eccentricity = (1 - (b**2 / a**2)) ** 0.5
    directrix = a/eccentricity

    print(f"Directrix: {directrix:.4f}")
    pause()

def find_ellipse_focus_coordinate():

    a, b, orientation = get_ellipse_info ()

    c = (a**2 - b**2) ** 0.5

    if orientation == "horizontal":
        print(f"Focus coordinates: (±{c:.4f}, 0)")

    else:
        print(f"Focus coordinates: (0, ±{c:.4f})")

    pause()

def find_ellipse_major_minor_axis():
    a, b = get_ellipse_axes()

    print(f"Major axis: {2*a:.4f}")
    print(f"Minor axis: {2*b:.4f}")
    pause()

def find_ellipse_vertex():
    a, b, orientation = get_ellipse_info ()

    if orientation == "horizontal":
        print(f"Focus coordinates: (±{a:.4f}, 0)")

    else:
        print(f"Focus coordinates: (0, ±{a:.4f})")
    
    pause()

def find_ellipse_equation():
    a, b, orientation = get_ellipse_info()

    if orientation == "horizontal":
        print(f"x²/{a**2} + y²/{b**2} = 1")

    else:
        print(f"x²/{b**2} + y²/{a**2} = 1")
    
    pause()

# =================
# Main program loop
def main():

    ellipse_actions = {
    1: find_ellipse_eccentricity,
    2: find_ellipse_latus_rectum,
    3: find_ellipse_focal_length,
    4: find_ellipse_area,
    5: find_ellipse_directrix,
    6: find_ellipse_focus_coordinate,
    7: find_ellipse_major_minor_axis,
    8: find_ellipse_vertex,
    9: find_ellipse_equation}

    while True:
        print("\n===========================")
        print("Main Menu - Conic Sections")
        print("===========================")
        print("1. Circle (Work in progress)")
        print("2. Parabola (Work in progress)")
        print("3. Ellipse")
        print("4. Hyperbola (Work in progress)")
        print("5. Exit")

        choice = get_choice("Choose an option: ", 1, 5)

        if choice == 3:
            
            while True: 

                ellipse_choice = ellipse_menu()

                if ellipse_choice == 10:
                    break

                ellipse_actions[ellipse_choice]()

        elif choice == 5:
            print("Exiting program.")
            break
        else:
            print("This feature is coming soon.")

if __name__ == "__main__":
    main()