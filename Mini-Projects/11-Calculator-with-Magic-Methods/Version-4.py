class Calculator:
    
    def __init__(self, num): 
        if isinstance(num, (int, float)):
            self.num = num
        else:
            raise TypeError("Only numbers allowed")

    def __str__(self):
        return f"Calculator Value: {self.num}"
    
    # This is the professional version of __str__.
    # Helps in debugging, without is we get horrible memory address
    def __repr__(self):
        return f"Calculator({self.num})"
    
    # ===============
    # Helper Function
    # ===============

    def _get_value(self, other):  # prefix '_' to tell that this is "Internal helper method"

        if isinstance(other, Calculator):
            return other.num

        elif isinstance(other, (int, float)):
            return other

        else:
            raise TypeError("Invalid Type")

    # ===================
    # Calculation Methods
    # ===================

    # Addition
    def __add__(self, other): 

        other_value = self._get_value(other)

        return Calculator(self.num + other_value) 
    
    # In-Place-Add
    def __iadd__(self, other):

        other_value = self._get_value(other)

        self.num += other_value

        return self 
    
    # Substraction
    def __sub__(self, other): 

        other_value = self._get_value(other)

        return Calculator(self.num - other_value)

    # In-Place-Substraction
    def __isub__(self, other):

        other_value = self._get_value(other)

        self.num -= other_value

        return self

    # Multiplication 
    def __mul__(self, other): 

        other_value = self._get_value(other)

        return Calculator(self.num * other_value)
    
    # In-Place-Multiplication
    def __imul__(self, other):

        other_value = self._get_value(other)

        self.num *= other_value

        return self
    
    # Division
    def __truediv__(self, other): 

        other_value = self._get_value(other)

    # Validation to prevent denominator = 0
        if other_value == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return Calculator(self.num / other_value) 
    
    # In-Place-Division
    def __itruediv__(self, other):
        other_value = self._get_value(other)

        if other_value == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        
        self.num /= other_value
        return self
    
    # Equal to
    def __eq__(self, other):

        other_value = self._get_value(other)

        return (self.num == other_value)
    
    # Less than
    def __lt__(self, other):

        other_value = self._get_value(other)

        return (self.num < other_value)
    
    # Greater than
    def __gt__(self, other):

        other_value = self._get_value(other)

        return (self.num > other_value)
    
    # Power
    def __pow__(self, other):

        other_value = self._get_value(other)

        return Calculator(self.num ** other_value)
    
    # Negative Object 
    def __neg__(self):
        return Calculator(-self.num)
    
    # Absolute Value
    def __abs__(self):
        return Calculator(abs(self.num))

# ===============
# Helper function
# ===============
  
def get_choice(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            print(f"Enter a number between {min_value}-{max_value}.")
        except ValueError:
            print("Invalid number.")

def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid number.")

def main():

    while True:
        print("\n==== Calculator ====")
        print("1. Add")
        print("2. Substract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Compare")
        print("7. Find absolute value")
        print("8. Exit")

        choice = get_choice("Enter your choice: ", 1, 8)

        if choice == 1:
            num1 = get_float("Enter 1st number: ")
            num2 = get_float("Enter 2nd number: ")

            calc1 = Calculator(num1)
            calc2 = Calculator(num2)

            print(calc1 + calc2)

        elif choice == 2:
            num1 = get_float("Enter 1st number: ")
            num2 = get_float("Enter 2nd number: ")

            calc1 = Calculator(num1)
            calc2 = Calculator(num2)

            print(calc1 - calc2)

        elif choice == 3:
            num1 = get_float("Enter 1st number: ")
            num2 = get_float("Enter 2nd number: ")

            calc1 = Calculator(num1)
            calc2 = Calculator(num2)

            print(calc1 * calc2)

        elif choice == 4:
            num1 = get_float("Enter 1st number: ")
            num2 = get_float("Enter 2nd number: ")

            calc1 = Calculator(num1)
            calc2 = Calculator(num2)

            try:
                print(calc1 / calc2)

            except ZeroDivisionError as e:
                print(e)

        elif choice == 5:
            num1 = get_float("Enter 1st number: ")
            num2 = get_float("Enter 2nd number: ")

            calc1 = Calculator(num1)
            calc2 = Calculator(num2)

            print(calc1 ** calc2)

        elif choice == 6:
            num1 = get_float("Enter 1st number: ")
            num2 = get_float("Enter 2nd number: ")

            calc1 = Calculator(num1)
            calc2 = Calculator(num2)

            if calc1 == calc2:
                print("Both numbers are equal")
            
            elif calc1 > calc2:
                print(f"{num1} is bigger than {num2}")
            
            elif calc1 < calc2:
                print(f"{num1} is smaller than {num2}")               

        elif choice == 7:
            num = get_float("Enter number: ")

            calc = Calculator(num)

            print(abs(calc))

        elif choice == 8:
            print("\nGoodbye !")
            break

        else:
            print("Invalid choice")

# ===========          
# Run program
# ===========
if __name__ == "__main__":
    main()  