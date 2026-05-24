def get_positive_number():

    while True:

        try:
            number = int(input("Find prime numbers up to: "))

            if number >= 2:
                return number

            print("Enter a number greater than or equal to 2.")

        except ValueError:
            print("Invalid number.")


def sieve_of_eratosthenes(limit):

    # Assume all numbers are prime initially
    is_prime = [True] * (limit + 1)

    # 0 and 1 are not prime
    is_prime[0] = False
    is_prime[1] = False

    current = 2

    while current * current <= limit:

        if is_prime[current]:

            # Mark all multiples as non-prime
            multiple = current * current

            while multiple <= limit:
                is_prime[multiple] = False
                multiple += current

        current += 1

    # Collect all prime numbers
    primes = []

    for number in range(2, limit + 1):

        if is_prime[number]:
            primes.append(number)

    return primes


limit = get_positive_number()

primes = sieve_of_eratosthenes(limit)

print(f"\nPrime numbers up to {limit}:")
print(primes)