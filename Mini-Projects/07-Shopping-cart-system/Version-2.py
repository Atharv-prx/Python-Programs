#Made it so that cart is interactive and there are options to choose from

class Product:
    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity

class Cart:
    def __init__(self):
        self.products = []
        self.discount = lambda total : total*0.9 
        self.tax_rate = 0.05 
    
    #Made this so that when user chooses same products with different quantity multiple times then it just increases in quantity
    #Perevents the formation of multiple address
    def add_products(self, product): 
        for x in self.products:  
            if x.name == product.name:
                x.quantity += product.quantity
                return
        self.products.append(product)

    @property                            
    def total_raw(self):                  
        return sum(x.price*x.quantity for x in self.products)
    
    @property
    def total_discounted(self):
        return self.discount(self.total_raw)
    
    @property
    def total_with_tax(self):
        return self.total_discounted * (1+self.tax_rate)   

    def show_order(self):
        print("===========Your products===========")
        for x in self.products:
            print(f"{x.quantity} {x.name} having price ${x.price}")
    
menu = {
    1: ("Pizza", 50),
    2: ("Burger", 40),
    3: ("Pasta", 60),
    4: ("Sandwich", 35),
    5: ("Fries", 30),
    6: ("Coffee", 25),
    7: ("Tea", 20),
    8: ("Cold Drink", 25),
    9: ("Milkshake", 45),
    10: ("Ice Cream", 40),
    11: ("Cake", 70),
    12: ("Donut", 30),
}

c = Cart()

while True:
    print("\n====== MENU ======")
    for key, (name, price) in menu.items():
        print(f"{key:2}. {name:<12} - ${price}")
    # key:2 --> alligns numbers nicely, name:<12 ---> keeps names alligned (left-justified), this is not neccessary but looks good
    
    print()
    print("Enter 0 to go to checkout")

    choice = int(input("Enter your choice: "))
    if choice == 0:
        break

    if choice not in menu:
        print("Invalid choice")
        continue

    quantity = int(input("Enter quantity: "))

    name, price = menu[choice]
    product = Product(name, price, quantity)

    c.add_products(product)
    print(f"Added {name}")

#Final Bill
c.show_order()
print("==============Pricing==============")
print(f"Raw total ${c.total_raw}") 
print(f"After 10% discount ${c.total_discounted}")
print(f"Final with tax: ${c.total_with_tax}")