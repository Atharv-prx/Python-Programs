# Adding 2 more features -1)= Delete animal option
#                         2)= Search animal option

class Animals:
    def __init__(self, name, colour, age, weight):
        self.name = name
        self.colour = colour
        self.age = age
        self.weight = weight
    
    def describe(self):
        print(f"\nName: {self.name}")
        print(f"Colour: {self.colour}")
        print(f"Age: {self.age} years")
        print(f"Weight: {self.weight} kg")

    def speak(self):
        print("This animal makes a sound")


class Dog(Animals):
    def __init__(self, name, colour, age, weight, breed):
        super().__init__(name, colour, age, weight)
        self.breed = breed

    def speak(self):
        print(f"{self.name} barks")

    def describe(self):
        super().describe()
        print(f"Breed: {self.breed}")


class Cat(Animals):
    def __init__(self, name, colour, age, weight, indoor):
        super().__init__(name, colour, age, weight)
        self.indoor = indoor

    def speak(self):
        print(f"{self.name} meows")

    def describe(self):
        super().describe()
        print(f"Indoor Cat: {'Yes' if self.indoor else 'No'}")


class Fish(Animals):
    def __init__(self, name, colour, age, weight, water_type):
        super().__init__(name, colour, age, weight)
        self.water_type = water_type

    def speak(self):
        print(f"{self.name} blubs")

    def describe(self):
        super().describe()
        print(f"Water Type: {self.water_type}")


class Bird(Animals):
    def __init__(self, name, colour, age, weight, can_fly):
        super().__init__(name, colour, age, weight)
        self.can_fly = can_fly

    def speak(self):
        print(f"{self.name} chirps")

    def describe(self):
        super().describe()
        print(f"Can Fly: {'Yes' if self.can_fly else 'No'}")


class Lion(Animals):
    def __init__(self, name, colour, age, weight, is_wild):
        super().__init__(name, colour, age, weight)
        self.is_wild = is_wild

    def speak(self):
        print(f"{self.name} roars")

    def describe(self):
        super().describe()
        print(f"Wild Animal: {'Yes' if self.is_wild else 'No'}")

# Helper Validations
def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Enter a positive number.")
        except ValueError:
            print("Invalid number.")

def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("Enter a positive number.")
        except ValueError:
            print("Invalid number.")

def get_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def get_yes_no(prompt):
    while True:
        value = input(prompt + " (yes/no): ").lower()
        if value in ["yes", "no"]:
            return value == "yes"
        print("Enter yes or no.")

#Core Features
def add_animal():
    print("\n--- Add Animal ---")

    while True:
        animal_type = input("Enter animal type (dog/cat/fish/bird): ").lower()
        if animal_type in animal_classes:
            break
        print("Invalid animal type! Please try again.")

    name = get_non_empty("Enter name: ")
    colour = get_non_empty("Enter colour: ")
    age = get_int("Enter age: ")
    weight = get_float("Enter weight: ")

    if animal_type == "dog":
        breed = get_non_empty("Enter breed: ")
        animal = Dog(name, colour, age, weight, breed)

    elif animal_type == "cat":
        indoor = get_yes_no("Is it indoor?")
        animal = Cat(name, colour, age, weight, indoor)

    elif animal_type == "fish":
        water_type = get_non_empty("Freshwater or Saltwater: ")
        animal = Fish(name, colour, age, weight, water_type)

    elif animal_type == "bird":
        can_fly = get_yes_no("Can it fly?")
        animal = Bird(name, colour, age, weight, can_fly)

    else:
        print("Invalid animal type!")
        return

    animals_list.append(animal)
    print("Animal added successfully!")

def view_animals():
    print("\n--- Animal List ---")
    if not animals_list:
        print("No animals added yet.")
        return

    for animal in animals_list:
        animal.describe()
        animal.speak()

def search_animals():
    print("\n--- Search Animal ---")
    if not animals_list:
        print("No animals added yet.")
        return
    
    search_name = input("Enter the animal name that you want to search: ").strip().lower()
    found = False

    for x in animals_list:
        if x.name.lower() == search_name:
            print("\nAnimal Found:")
            x.describe()
            x.speak()
            found = True
    if not found:
        print("No animal found with that name.")
    
def delete_animal():
    print("\n--- Delete Animal ---")
    if not animals_list:
        print("No animals added yet.")
        return

    delete_name = input("Enter the name of animal that you want to remove: ").strip().lower()
    removed = False

    for x in animals_list:
        if x.name.lower() == delete_name:
            animals_list.remove(x)
            print("\nRemoved animal")
            removed = True
            break
            
    if not removed:
        print("No animal found with that name.")

#Storage
animals_list = []
animal_classes = {"dog": Dog, "cat": Cat, "fish": Fish, "bird": Bird}

# Main Program
def main():
    while True:
        print("\n=== Zoo Management System ===")
        print("1. Add Animal")
        print("2. View Animals")
        print("3. Search Animal")
        print("4. Delete Animal")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_animal()
        elif choice == "2":
            view_animals()
        elif choice == "3":
            search_animals()
        elif choice == "4":
            delete_animal()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

# Run program
if __name__ == "__main__":
    main()