class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cart:
    def __init__(self, products: list):
        self.products = products

    @property                             #Properties should not print anything
    def total_raw(self):                  #Property only takes self
        return sum(x.price for x in self.products)

    def show_order(self):
        print("===========Your products===========")
        for x in self.products:
            print(f"{x.name} having price ${x.price}")
    
p1 = Product("Pizza", 50)
p2 = Product("Coffee", 25)
p3 = Product("Soft-Drinks", 25)

c = Cart([p1, p2, p3])

c.show_order()
print("==============Pricing==============")
print(f"Total ${c.total_raw}") 
#Can't call it like c.total_raw() cuz it's a property not a function