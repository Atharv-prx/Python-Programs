from Helpers import get_choice
from Helpers import pause
from Helpers import get_positive_float

# =====================
# Shared Parabola input

def get_parabola_info():

    a = get_positive_float("Enter focal parameter (a): ")

    direction = input("Enter direction of parabola opening (Left/Right/Up/Down): ").lower()

    while direction not in {"left", "right", "up", "down"}:
        print("Invalid direction")

        direction = input("Enter direction of parabola opening (Left/Right/Up/Down): ").lower()

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
    
    a, direction = get_parabola_info()

    LR = 4*a

    print(f"Length of Latus Rectum: {LR}")
    pause()

def find_parabola_focus():
    
    a, direction = get_parabola_info()

    if direction == "left":
        print(f"Focus: (-{a},0)")

    elif direction == "right":
        print(f"Focus: ({a},0)")

    elif direction == "up":
        print(f"Focus: (0,{a})")
    
    elif direction == "down":
        print(f"Focus: (0,-{a})")
    
    pause()

def find_parabola_directrix():
    
    a, direction = get_parabola_info()

    if direction == "left":
        print(f"Directrix: x = {a}")

    elif direction == "right":
        print(f"Directrix: x = -{a}")

    elif direction == "up":
        print(f"Directrix: y = -{a}")
    
    elif direction == "down":
        print(f"Directrix: y = {a}")
    
    pause()

def find_parabola_equation():

    a, direction = get_parabola_info()
    
    coefficient = 4*a

    if direction == "left":
        print(f"Equation: y² = -{coefficient:g}x")

    elif direction == "right":
        print(f"Equation: y² = {coefficient:g}x")

    elif direction == "up":
        print(f"Equation: x² = {coefficient:g}y")
    
    elif direction == "down":
        print(f"Equation: x² = -{coefficient:g}y")
    
    pause()

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