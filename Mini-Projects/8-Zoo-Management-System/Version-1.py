#Updated version of Animal-Sounds program from OOPs
#Added better input validation

class Animals:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
    
    def describe(self):
        print(f"His name is {self.name} and his colour is {self.colour}")

    def speak(self):
        print("This animal speaks")
    

class Dog(Animals):
    def speak(self):
        print(f"{self.name} barks")


class Cat(Animals):
    def speak(self):
        print(f"{self.name} meows")


class Fish(Animals):
    def speak(self):
        print(f"{self.name} squeaks")


# Dictionary for cleaner mapping
animal_classes = {"dog": Dog, "cat": Cat, "fish": Fish}

Animals_list = []

# Validate number of animals
while True:
    try:
        n = int(input("How many animals do you want to add? "))
        if n > 0 :
            break
        else:
            print("Enter a number greater than 0.")
    except ValueError:
        print("Invalid input. Please enter a number.")


for i in range(n):
    print(f"\nAnimal {i+1}")

    # Validate animal type
    while True:
        animal_type = input("Enter animal type (dog/cat/fish): ").lower()
        if animal_type in animal_classes:
            break
        print("Invalid type! Try again.")

    # Validate name
    while True:
        name = input("Enter name: ").strip()
        if name:
            break
        print("Name cannot be empty.")

    # Validate colour
    while True:
        colour = input("Enter colour: ").strip()
        if colour:
            break
        print("Colour cannot be empty.")

    # Create object using dictionary
    animal = animal_classes[animal_type](name, colour)
    Animals_list.append(animal)


# Output
print("\n--- Animal Sounds ---")
for x in Animals_list:
    x.describe()
    x.speak()