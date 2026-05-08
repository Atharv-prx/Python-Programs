class Vehicle:
    def __init__(self, brand, model, year_of_manufacture, top_speed, fuel_capacity, vehicle_id):
        self.brand = brand
        self.model = model
        self.year_of_manufacture = year_of_manufacture
        self.top_speed = top_speed
        self.fuel_capacity = fuel_capacity
        self.vehicle_id = vehicle_id

    def describe(self):
        print(f"Type: {type(self).__name__}")
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
        print(f"Is helmet required: {self.helmet_required}")
    
class Truck(Vehicle):
    def __init__(self, brand, model, year_of_manufacture, top_speed, fuel_capacity, vehicle_id, load_capacity):
        super().__init__(brand, model, year_of_manufacture, top_speed, fuel_capacity, vehicle_id)
        self.load_capacity = load_capacity

    def describe(self):
        super().describe()
        print(f"Load capacity: {self.load_capacity}kg")

class ElectricVehicle(Vehicle):
    def __init__(self, brand, model, year_of_manufacture, top_speed, fuel_capacity, vehicle_id, current_battery_level, time_to_charge):
        super().__init__(brand, model, year_of_manufacture, top_speed, fuel_capacity, vehicle_id)
        self.current_battery_level = current_battery_level
        self.time_to_charge = time_to_charge
    
    def describe(self):
        super().describe()
        print(f"Current Battery Level: {self.current_battery_level}%")
        print(f"Time to charge: {self.time_to_charge} hours")


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

def get_yes_no(prompt):
    while True:
        value = input(prompt).strip().lower()

        if not value:
            print("Name cannot be empty.")
            continue

        if not value.replace(" ", "").isalpha():
            print("Name should contain only letters.")
            continue

        if value not in ("yes", "no"):
            print("You can only enter yes or no.")
            continue

        return value == "yes"
    
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

# ====================================
# Common Functions for all child class
# ====================================

def remove_vehicle():
    print("\n=== Remove Vehicle ===")

    if not vehicle_list:
        print("No Vehicle added yet.")
        return

    vehicle_id = get_int("Enter car Id to remove: ")

    removed = False

    for vehicle in vehicle_list:

        if vehicle.vehicle_id == vehicle_id:

            vehicle_list.remove(vehicle)

            print(f"\n==== {vehicle.brand} {vehicle.model} removed successfully. ====")
            removed = True
            break

    if not removed:
        print("No car found with that Id.")

def search_vehicle():

    print("\n=== Search Vehicle ===")

    if not vehicle_list:
        print("No vehicles added yet.")
        return

    vehicle_id = get_int("Enter vehicle Id to search: ")

    searched = False

    for vehicle in vehicle_list:

        if vehicle.vehicle_id == vehicle_id:
            print(f"\n==== {vehicle.brand} {vehicle.model} found . ====")
            vehicle.describe()

            searched = True
            break

    if not searched:
        print("No vehicle found with that Id.") 

def show_vehicles():
    print("\n==== Vehicle List ====")

    if not vehicle_list:
        print("No vehicle added yet!")
        return
    
    for vehicle in vehicle_list:
        vehicle.describe()  

def is_vehicle_id_exists(vehicle_id):

    for vehicle in vehicle_list:
        if vehicle.vehicle_id == vehicle_id:
            return True

    return False

# ============
# Car Features
# ============

def add_car():
    print("\n==== Add Car ====")
 
    brand = get_name("Enter brand name: ")
    model = get_name("Enter model name: ")
    year_of_manufacture = get_int("Enter year of manufacture: ")
    top_speed = get_float("Enter Top-Speed in Km/Hr: ")
    fuel_capacity = get_float("Enter fuel capacity in Litres: ")

    #To prevent duplicate id
    while True: 

        vehicle_id = get_int("Enter vehicle Id: ")

        if is_vehicle_id_exists(vehicle_id):
            print("Vehicle ID already exists.")
        else:
            break

    doors_number = get_int("Enter number of doors: ")
    is_trunk_present = get_yes_no("Is trunk present (yes/no): ")

    car = Car(brand, model, year_of_manufacture, top_speed, fuel_capacity, vehicle_id, doors_number, is_trunk_present)
    
    vehicle_list.append(car)

    print(f"{brand} {model} added successfully")

def show_cars():
    print("\n==== Car List ====")

    if not vehicle_list:
        print("No vehicle added yet!")
        return
    
    found = False

    for vehicle in vehicle_list:

        if isinstance(vehicle, Car):
            vehicle.describe()
            found = True
    
    if not found:
        print("No cars Added yet")

# =============
# Bike Features
# =============
def add_bike():
    print("\n==== Add Bike ====")
 
    brand = get_name("Enter brand name: ")
    model = get_name("Enter model name: ")
    year_of_manufacture = get_int("Enter year of manufacture: ")
    top_speed = get_float("Enter Top-Speed in Km/Hr: ")
    fuel_capacity = get_float("Enter fuel capacity in Litres: ")

    #To prevent duplicate id
    while True: 

        vehicle_id = get_int("Enter vehicle Id: ")

        if is_vehicle_id_exists(vehicle_id):
            print("Vehicle ID already exists.")
        else:
            break

    helmet_required = get_yes_no("Is the helmet required (yes/no): ")

    bike = Bike(brand, model, year_of_manufacture, top_speed, fuel_capacity, vehicle_id, helmet_required)
    
    vehicle_list.append(bike)

    print(f"{brand} {model} added successfully")

def show_bikes():
    print("\n==== Bike List ====")

    if not vehicle_list:
        print("No vehicle added yet!")
        return
    
    found = False

    for vehicle in vehicle_list:

        if isinstance(vehicle, Bike):
            vehicle.describe()
            found = True
    
    if not found:
        print("No bikes Added yet")

# ==============
# Truck Features
# ==============
def add_truck():
    print("\n==== Add Truck ====")
 
    brand = get_name("Enter brand name: ")
    model = get_name("Enter model name: ")
    year_of_manufacture = get_int("Enter year of manufacture: ")
    top_speed = get_float("Enter Top-Speed in Km/Hr: ")
    fuel_capacity = get_float("Enter fuel capacity in Litres: ")

    #To prevent duplicate id
    while True: 

        vehicle_id = get_int("Enter vehicle Id: ")

        if is_vehicle_id_exists(vehicle_id):
            print("Vehicle ID already exists.")
        else:
            break

    load_capacity = get_float("Enter the load capacity in Kg: ")

    truck = Truck(brand, model, year_of_manufacture, top_speed, fuel_capacity, vehicle_id, load_capacity)
    
    vehicle_list.append(truck)

    print(f"{brand} {model} added successfully")

def show_trucks():
    print("\n==== Truck List ====")

    if not vehicle_list:
        print("No vehicle added yet!")
        return
    
    found = False

    for vehicle in vehicle_list:

        if isinstance(vehicle, Truck):
            vehicle.describe()
            found = True
    
    if not found:
        print("No Trucks Added yet")

# =========================
# Electric Vehicle Features
# =========================
def add_ev():
    print("\n==== Add Electric Vehicle ====")
 
    brand = get_name("Enter brand name: ")
    model = get_name("Enter model name: ")
    year_of_manufacture = get_int("Enter year of manufacture: ")
    top_speed = get_float("Enter Top-Speed in Km/Hr: ")
    fuel_capacity = get_float("Enter fuel capacity in Litres: ")

    #To prevent duplicate id
    while True: 

        vehicle_id = get_int("Enter vehicle Id: ")

        if is_vehicle_id_exists(vehicle_id):
            print("Vehicle ID already exists.")
        else:
            break

    current_battery_level = get_float("What is current battery level: ")
    time_to_charge = get_int("Enter the time it take to fully charge the battery (in hours): ")

    ev = ElectricVehicle(brand, model, year_of_manufacture, top_speed, fuel_capacity, vehicle_id, current_battery_level, time_to_charge)
    
    vehicle_list.append(ev)

    print(f"{brand} {model} added successfully")

def show_evs():
    print("\n==== Electric Vehicle List ====")

    if not vehicle_list:
        print("No vehicle added yet!")
        return
    
    found = False

    for vehicle in vehicle_list:

        if isinstance(vehicle, ElectricVehicle):
            vehicle.describe()
            found = True
    
    if not found:
        print("No Electric Vehicle Added yet")

# =============
# Main Program
# =============

def main():

    while True:

        print("\n====== Vehicle System ======")
        print("---> Main Menu ")
        print("1. Manage Cars")
        print("2. Manage Bikes")
        print("3. Manage Truck")
        print("4. Manage Electric Vehicles")
        print("5. See all Vehicles")
        print("6. Exit")

        choice = get_choice("\nEnter your choice: ", 1, 6)

        # =========
        # Car Menu
        # =========                      
        if choice == 1:

            while True: 

                print("\n==== Cars Menu ====")
                print("1. Add Car")
                print("2. Show Cars")
                print("3. Remove Car")
                print("4. Search Car")
                print("5. Return to main menu")

                choice1 = get_choice("\nEnter your choice: ", 1, 5)

                if choice1 == 1:
                    add_car()

                elif choice1 == 2:
                    show_cars()

                elif choice1 == 3:
                    remove_vehicle()

                elif choice1 == 4:
                    search_vehicle()

                elif choice1 == 5:
                    print("\nReturning to Main Menu...")
                    break      

                else:
                    print("Invalid Choice!")   

        # ========
        # Bike Menu
        # ========
        elif choice == 2:

            while True: 

                print("\n==== Bikes Menu ====")
                print("1. Add Bike")
                print("2. Show Bikes")
                print("3. Remove Bike")
                print("4. Search Bike")
                print("5. Return to main menu")

                choice2 = get_choice("\nEnter your choice: ", 1, 5)

                if choice2 == 1:
                    add_bike()

                elif choice2 == 2:
                    show_bikes()

                elif choice2 == 3:
                    remove_vehicle()

                elif choice2 == 4:
                    search_vehicle()

                elif choice2 == 5:
                    print("\nReturning to Main Menu...")
                    break      

                else:
                    print("Invalid Choice!") 
        # ==========
        # Truck Menu
        # ==========
        elif choice == 3:

            while True: 

                print("\n==== Trucks Menu ====")
                print("1. Add Truck")
                print("2. Show Trucks")
                print("3. Remove Truck")
                print("4. Search Truck")
                print("5. Return to main menu")

                choice2 = get_choice("\nEnter your choice: ", 1, 5)

                if choice2 == 1:
                    add_truck()

                elif choice2 == 2:
                    show_trucks()

                elif choice2 == 3:
                    remove_vehicle()

                elif choice2 == 4:
                    search_vehicle()

                elif choice2 == 5:
                    print("\nReturning to Main Menu...")
                    break      

                else:
                    print("Invalid Choice!")    
        # =====================
        # Electric Vehicle Menu
        # =====================
        elif choice == 4:

            while True: 

                print("\n==== Electric Vehicles Menu ====")
                print("1. Add Electric Vehicle")
                print("2. Show Electric Vehicles")
                print("3. Remove Electric Vehicle")
                print("4. Search Electric Vehicle")
                print("5. Return to main menu")

                choice2 = get_choice("\nEnter your choice: ", 1, 5)

                if choice2 == 1:
                    add_ev()

                elif choice2 == 2:
                    show_evs()

                elif choice2 == 3:
                    remove_vehicle()

                elif choice2 == 4:
                    search_vehicle()

                elif choice2 == 5:
                    print("\nReturning to Main Menu...")
                    break      

                else:
                    print("Invalid Choice!")        
        
        elif choice == 5: 
            show_vehicles()

        elif choice == 6: 
            print("\nGoodbye!")
            break

        else:
            print("Invalid choice") 

# ===========          
# Run program
# ===========
if __name__ == "__main__":
    main()