# Upgraded version of Shopping-Cart program from OOPs folder
# Added discount, tax property

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cart:
    def __init__(self, products: list):
        self.products = products
        self.discount = lambda total : total*0.9 # Assuming 10 percent discount

    @property                            
    def total_raw(self):                  
        return sum(x.price for x in self.products)
    
    @property
    def total_discounted(self):
        return self.discount(self.total_raw)
    
    @property
    def total_with_tax(self):
        return self.total_discounted * 1.05   # Assuming 5% tax

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
print(f"Raw total ${c.total_raw}") 
print(f"After 10% discount ${c.total_discounted}")
print(f"Final with tax: ${c.total_with_tax}")