def get_positive_number():
    
    while True:

        try:
            number = int(input("Enter a positive number: "))

            if number > 1 :
                return number
            
            print("Please enter a positve number")
        
        except ValueError:
            print("Invalid number!")

def prime_factorization(number):
    
    factors = []

    divisor = 2

    while divisor * divisor <= number:

        while number % divisor == 0:
            factors.append(divisor)
            number //= divisor

        divisor += 1

    # If number is still greater than 1, then it itself is a prime factor
    if number > 1:
        factors.append(number)

    return factors

def main ():

    num = get_positive_number()

    factors = prime_factorization(num)

    print(f"\nPrime factors: {factors}")

if __name__ == "__main__":
    main()