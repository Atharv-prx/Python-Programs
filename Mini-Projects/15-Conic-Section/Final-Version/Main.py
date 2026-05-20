from Helpers import get_choice
from Ellipse import ellipse_program
from Hyperbola import hyperbola_program
from Parabola import parabola_program

def main():

    while True:

        print("\n===========================")
        print("Main Menu - Conic Sections")
        print("===========================")
        print("1. Circle")
        print("2. Parabola")
        print("3. Ellipse")
        print("4. Hyperbola")
        print("5. Exit")

        choice = get_choice("Choose an option: ", 1, 5)
        
        if choice == 2:
            parabola_program()

        elif choice == 3:
            ellipse_program()
        
        elif choice ==4: 
            hyperbola_program()
            
        elif choice == 5:
            print("Exiting program.")
            break

        else:
            print("Feature coming soon.")

if __name__ == "__main__":
    main()