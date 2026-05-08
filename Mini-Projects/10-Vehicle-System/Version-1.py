class Vehicle:
    def __init__(self, brand, model, year_of_manufacture, top_speed, fuel_capacity):
        self.brand = brand
        self.model = model
        self.year_of_manufacture = year_of_manufacture
        self.top_speed = top_speed
        self.fuel_capacity = fuel_capacity

    def describe(self):
        print(f"\nBrand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year Of Manufacture: {self.year_of_manufacture}")
        print(f"Top-Speed: {self.top_speed}")
        print(f"Fuel Capacity: {self.fuel_capacity}")

class Car(Vehicle):
    def __init__(self, brand, model, year_of_manufacture, top_speed, fuel_capacity, doors_number, is_trunk_present):
        super().__init__(brand, model, year_of_manufacture, top_speed, fuel_capacity)
        self.doors_number = doors_number
        self.is_trunk_present = is_trunk_present

    def describe(self):
        super().describe()
        print(f"Number of doors: {self.doors_number}")
        print(f"Is Trunk present: {self.is_trunk_present}")

class Bike(Vehicle):
    def __init__(self, brand, model, year_of_manufacture, top_speed, fuel_capacity, helmet_required):
        super().__init__(brand, model, year_of_manufacture, top_speed, fuel_capacity)
        self.helmet_required = helmet_required

    def describe(self):
        super().describe()
        print(f"Is helmet requires: {self.helmet_required}")
    
class Truck(Vehicle):
    def __init__(self, brand, model, year_of_manufacture, top_speed, fuel_capacity, load_capacity):
        super().__init__(brand, model, year_of_manufacture, top_speed, fuel_capacity)
        self.load_capacity = load_capacity

    def describe(self):
        super().describe()
        print(f"Load capacity: {self.load_capacity}")

class ElectricCar(Vehicle):
    def __init__(self, brand, model, year_of_manufacture, top_speed, fuel_capacity, battery_level, time_to_charge):
        super().__init__(brand, model, year_of_manufacture, top_speed, fuel_capacity)
        self.battery_level = battery_level
        self.time_to_charge = time_to_charge
    
    def describe(self):
        super().describe()
        print(f"Battery Level: {self.battery_level}")
        print(f"Time to charge: {self.time_to_charge}")

car1 = Car("Toyota", "Supra", 2020, 250, 60, 2, True)
bike1 = Bike("Yamaha", "R15", 2022, 180, 15, True)
truck1 = Truck("Volvo", "FH16", 2019, 140, 300, "25 Tons")
electric1 = ElectricCar("Tesla", "Model S", 2024, 320, 0, 90, "2 Hours")

car1.describe()
bike1.describe()
truck1.describe()
electric1.describe()