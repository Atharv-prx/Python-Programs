def get_positive_number():
    
    while True:

        try:
            number = int(input("Enter a positive number: "))

            if number > 1 :
                return number
            
            print("Please enter a positve number")
        
        except ValueError:
            print("Invalid number!")

def prime_factorization():
    pass

def main ():

    num = get_positive_number()

    factors = prime_factorization(num)

    print(f"\nPrime factors: {factors}")