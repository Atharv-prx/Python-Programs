rows = int(input("Enter number of rows: "))
column = int(input("Enter number of column: "))
symbol = input("Enter the symbol to use: ")

for x in range (rows):
    for y in range (column):
        print(symbol, end="")
    print() #prints new line