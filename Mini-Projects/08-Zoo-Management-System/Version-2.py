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

animal_classes = {"dog": Dog, "cat": Cat, "fish": Fish, "bird": Bird, "lion": Lion}
Animals_list = []

# Main Program
print("=============================")
print("=== Zoo Management System ===")
print("=============================")
n = get_int("How many animals do you want to add? ")

for i in range(n):
    print(f"\nAnimal {i+1}")

    while True:
        animal_type = input("Enter animal type (dog/cat/fish/bird/lion): ").lower()
        if animal_type in animal_classes:
            break
        print("Invalid type!")

    name = get_non_empty("Enter name: ")
    colour = get_non_empty("Enter colour: ")
    age = get_int("Enter age: ")
    weight = get_float("Enter weight (kg): ")

    # Dynamic extra attributes
    if animal_type == "dog":
        breed = get_non_empty("Enter breed: ")
        animal = Dog(name, colour, age, weight, breed)

    elif animal_type == "cat":
        indoor = get_yes_no("Is it an indoor cat?")
        animal = Cat(name, colour, age, weight, indoor)

    elif animal_type == "fish":
        water_type = get_non_empty("Freshwater or Saltwater: ")
        animal = Fish(name, colour, age, weight, water_type)

    elif animal_type == "bird":
        can_fly = get_yes_no("Can it fly?")
        animal = Bird(name, colour, age, weight, can_fly)

    elif animal_type == "lion":
        is_wild = get_yes_no("Is it wild?")
        animal = Lion(name, colour, age, weight, is_wild)

    Animals_list.append(animal)

print("\n--- Animal Details ---")
for animal in Animals_list:
    animal.describe()
    animal.speak()