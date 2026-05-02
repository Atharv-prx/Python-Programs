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

def cardType(cardNum):

    length = len(cardNum)

    if cardNum.startswith("4") and length in [13, 16, 19]:
        return "Visa"
    
    elif (51 <= int(cardNum[:2]) <= 55 or 2221 <= int(cardNum[:4]) <= 2720) and length == 16:
        return "MasterCard"
    
    elif cardNum.startswith(("34", "37")) and length == 15:
        return "American Express"
    
    elif (cardNum.startswith("6011") or cardNum.startswith("65") or 644 <= int(cardNum[:3]) <= 649) and length == 16:
        return "Discover"
    
    else:
        return "Unknown"

def main():
    cardNum = getValidInput()
    cardtype = cardType(cardNum)

    cardNum = cardNum[::-1]    # Reverses cardNum

    result = sumEvenDigits(cardNum) + sumOddDigits(cardNum)

    if (result % 10 == 0):
        print("Your card number is Valid!")
    else:
        print("Your card number is Invalid!")
        
    print(f"Your cardtype is {cardtype}")

main()