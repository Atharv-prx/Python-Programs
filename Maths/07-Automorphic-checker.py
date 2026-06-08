def main():
    num = int(input("Enter a number: "))
    square = num ** 2
    # Calculate 10 raised to the power of the number of digits
    mod = 10 ** len(str(num))
    # Check if the last n digits of the square match the number
    if square % mod == num:
        print(f"{num} is an Automorphic Number")
    else:
        print(f"{num} is not an Automorphic Number")

if __name__ == "__main__":
    main()