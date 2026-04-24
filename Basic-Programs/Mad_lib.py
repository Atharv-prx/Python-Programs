#Mad Libs is a beginner project where you create a funny story by asking the user for different words

def story_adventure():
    name = input("Enter a name: ")
    place = input("Enter a place: ")
    object_ = input("Enter an object: ")
    verb = input("Enter a verb: ")

    print("\n--- Adventure Story ---")
    print(f"{name} went to {place} with a {object_}. Suddenly, they decided to {verb} and everything changed!")

def story_funny():
    animal = input("Enter an animal: ")
    food = input("Enter a food: ")
    adjective = input("Enter an adjective: ")
    verb = input("Enter a verb: ")

    print("\n--- Funny Story ---")
    print(f"A {adjective} {animal} was eating {food} while trying to {verb}. It was the funniest thing ever!")

def story_scifi():
    planet = input("Enter a planet: ")
    alien = input("Enter an alien name: ")
    gadget = input("Enter a futuristic gadget: ")
    verb = input("Enter a verb: ")

    print("\n--- Sci-Fi Story ---")
    print(f"On planet {planet}, an alien named {alien} used a {gadget} to {verb} across the galaxy!")
    
def main():
    while True:
        print("\n====== MAD LIBS GAME ======")
        print("1. Adventure Story")
        print("2. Funny Story")
        print("3. Sci-Fi Story")
        print("4. Exit")

        choice = input("Choose a story (1-4): ")

        if choice == "1":
            story_adventure()
        elif choice == "2":
            story_funny()
        elif choice == "3":
            story_scifi()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again!")

main()