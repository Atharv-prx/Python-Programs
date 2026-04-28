Foods = []
Prices = []
total = 0

while True:
    food = input ("Enter a food to buy (Press q to quit): ")
    if food.lower() == "q":
        break
    else:
        Foods.append(food)
        price = float(input(f"Enter price of {food}: $"))
        Prices.append(price)
print("======Your Cart======")
for food in Foods:
    print(food)

for price in Prices:
    total += price

print(f"Your total is: ${total}")      