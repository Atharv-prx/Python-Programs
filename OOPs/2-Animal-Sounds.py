class Animals:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
    
    def describe(self):
        print(f"\nName: {self.name}")
        print(f"Colour: {self.colour}")

    def speak(self):
        print("This animal speaks")
    
class Dog(Animals):
    def __init__(self, name, colour):
        super().__init__(name,colour)

    def speak(self):
        print(f"{self.name} barks")

class Cat(Animals):
    def __init__(self, name, colour):
        super().__init__(name, colour)

    def speak(self):
        print(f"{self.name} meows")


class Fish(Animals):
    def __init__(self, name, colour,):
        super().__init__(name, colour)

    def speak(self):
        print(f"{self.name} sqeeks")


Animals = (Dog("Tommy", "Brown"), Cat("Puss", "Yellow"), Fish("Nemo", "Orange"))

for x in Animals:
    x.describe()
    x.speak()