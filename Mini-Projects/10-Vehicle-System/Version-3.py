class Vehicle:
    def __init__(self, brand, model, year_of_manufacture, top_speed, fuel_capacity, vehicle_id):
        self.brand = brand
        self.model = model
        self.year_of_manufacture = year_of_manufacture
        self.top_speed = top_speed
        self.fuel_capacity = fuel_capacity
        self.vehicle_id = vehicle_id

    def describe(self):
        print(f"\nBrand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year Of Manufacture: {self.year_of_manufacture}")
        print(f"Top-Speed: {self.top_speed}Km/Hr")
        print(f"Fuel Capacity: {self.fuel_capacity}Liters")
        print(f"Id = {self.vehicle_id}")

class Car(Vehicle):
    def __init__(self, brand, model, year_of_manufacture, top_speed, fuel_capacity, vehicle_id, doors_number, is_trunk_present):
        super().__init__(brand, model, year_of_manufacture, top_speed, fuel_capacity, vehicle_id)
        self.doors_number = doors_number
        self.is_trunk_present = is_trunk_present

    def describe(self):
        super().describe()
        print(f"Number of doors: {self.doors_number}")
        print(f"Is Trunk present: {self.is_trunk_present}")

class Bike(Vehicle):
    def __init__(self, brand, model, year_of_manufacture, top_speed, fuel_capacity, vehicle_id, helmet_required):
        super().__init__(brand, model, year_of_manufacture, top_speed, fuel_capacity, vehicle_id)
        self.helmet_required = helmet_required

    def describe(self):
        super().describe()
        print(f"Is helmet requires: {self.helmet_required}")
    
class Truck(Vehicle):
    def __init__(self, brand, model, year_of_manufacture, top_speed, fuel_capacity, vehicle_id, load_capacity):
        super().__init__(brand, model, year_of_manufacture, top_speed, fuel_capacity, vehicle_id)
        self.load_capacity = load_capacity

    def describe(self):
        super().describe()
        print(f"Load capacity: {self.load_capacity}")

class ElectricCar(Vehicle):
    def __init__(self, brand, model, year_of_manufacture, top_speed, fuel_capacity, vehicle_id, current_battery_level, time_to_charge):
        super().__init__(brand, model, year_of_manufacture, top_speed, fuel_capacity, vehicle_id)
        self.current_battery_level = current_battery_level
        self.time_to_charge = time_to_charge
    
    def describe(self):
        super().describe()
        print(f"Current Battery Level: {self.battery_level}")
        print(f"Time to charge: {self.time_to_charge}")


# =======
# Storage 
# =======
vehicle_list = []

# ===============
# Helper function
# ===============
def get_name(prompt):
    while True:
        value = input(prompt).strip()

        if not value:
            print("Name cannot be empty.")
            continue

        return value.title()

def get_true_false(prompt):
    while True:
        value = input(prompt).strip().lower()

        if not value:
            print("Name cannot be empty.")
            continue

        if not value.replace(" ", "").isalpha():
            print("Name should contain only letters.")
            continue

        if value not in ("true", "false"):
            print("You can only enter true or false.")
            continue

        return value.title()
    
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

def get_choice(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            print(f"Enter a number between {min_value}-{max_value}.")
        except ValueError:
            print("Invalid number.")
    
# ============
# Car Features
# ============
def add_cars():
    print("\n==== Add Cars ====")
 
    brand = get_name("Enter brand name: ")
    model = get_name("Enter model name: ")
    year_of_manufacture = get_int("Enter year of manufacture: ")
    top_speed = get_float("Enter Top-Speed in Km/Hr: ")
    vehicle_id = get_int("Enter vehicle Id: ")
    fuel_capacity = get_float("Enter fuel capacity in Litres: ")
    doors_number = get_int("Enter number to doors: ")
    is_trunk_present = get_true_false("Is trunck present (true/false): ")

    car = Car(brand, model, year_of_manufacture, top_speed, fuel_capacity, vehicle_id, doors_number, is_trunk_present)
    
    vehicle_list.append(car)

    print(f"{brand} {model} added successfully")

def show_cars():
    print("\n==== Car List ====")

    if not vehicle_list:
        print("No car added yet!")
        return
    
    for car in vehicle_list:
        car.describe()

def remove_car():
    print("\n=== Remove Car ===")

    if not vehicle_list:
        print("No cars added yet.")
        return

    car_id = get_int("Enter car Id to remove: ")

    removed = False

    for car in vehicle_list:

        if car.vehicle_id == car_id:

            vehicle_list.remove(car)

            print(f"\n==== {car.brand} {car.model} removed successfully. ====")
            removed = True
            break

    if not removed:
        print("No car found with that Id.") 

def search_car():
    print("\n=== Search Car ===")

    if not vehicle_list:
        print("No cars added yet.")
        return

    car_id = get_int("Enter car Id to search: ")

    searched = False

    for car in vehicle_list:

        if car.vehicle_id == car_id:
            print(f"\n==== {car.brand} {car.model} found . ====")
            car.describe()

            searched = True
            break

    if not searched:
        print("No car found with that Id.")   

# =============
# Main Program
# =============

def main():

    while True:

        print("\n====== Vehicle System ======")
        print("---> Main Menu ")
        print("1. Manage Cars")
        print("2. Exit")

        choice = get_choice("\nEnter your choice: ", 1, 2)
        # ========
        # Car Menu
        # ========

        if choice == 1:

            while True: 

                print("\n==== Cars Menu ====")
                print("1. Add Cars")
                print("2. Show Cars")
                print("3. Remove Car")
                print("4. Search Car")
                print("5. Return to main menu")

                choice1 = get_choice("\nEnter your choice: ", 1, 5)

                if choice1 == 1:
                    add_cars()

                elif choice1 == 2:
                    show_cars()

                elif choice1 == 3:
                    remove_car()

                elif choice1 == 4:
                    search_car()

                elif choice1 == 5:
                    print("\nReturning to Main Menu...")
                    break      

                else:
                    print("Invalid Choice!")             
        
        elif choice == 2: 
            print("\nGoodbye!")
            break

        else:
            print("Invalid choice")

# ===========          
# Run program
# ===========
if __name__ == "__main__":
    main() 