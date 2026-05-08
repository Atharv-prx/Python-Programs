def getValidInput():
    while True:
        cardNum = input("Enter your credit card number: ")

        # Remove spaces and dashes
        cardNum = cardNum.replace("-", "").replace(" ", "")

        # Validation checks
        if not cardNum:
            print("Input cannot be empty.")
        
        elif not cardNum.isdigit():
            print("Card number must contain only digits.")
        
        elif len(cardNum) < 13 or len(cardNum) > 19:
            print("Card number must be between 13 and 19 digits.")
        
        else:
            return cardNum
        
def sumEvenDigits(cardNum):
    sumEven = 0
    for x in cardNum[1::2]: #Begin at 2nd digit
        x = int(x)*2
        if x >= 10:
            sumEven += (1+(x%10))
        else:
            sumEven += x
    return sumEven


def sumOddDigits(cardNum):
    sumOdd = 0
    for x in cardNum[::2]:
        sumOdd += int(x)
    return sumOdd

def main():
    cardNum = getValidInput()

    cardNum = cardNum[::-1]    # Reverses cardNum

    result = sumEvenDigits(cardNum) + sumOddDigits(cardNum)

    if (result % 10 == 0):
        print("Your card number is Valid!")
    else:
        print("Your card number is Invalid!")

main()