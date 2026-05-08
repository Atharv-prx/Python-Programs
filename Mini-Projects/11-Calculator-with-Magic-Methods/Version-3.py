# Added a helper function using 'isistance' to help validate most magical methods, also added __str__

class Calculator:
    
    def __init__(self, num): 
        if isinstance(num, (int, float)):
            self.num = num
        else:
            raise TypeError("Only numbers allowed")
        self.num = num 

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

    #Added Calculator before (self.num + other_num) so that it actually returns an object and str becomes automatically usefull 
    def __add__(self, other): 

        other_value = self._get_value(other)

        return Calculator(self.num + other_value)  
    
    def __sub__(self, other): 

        other_value = self._get_value(other)

        return Calculator(self.num - other_value)
     
    def __mul__(self, other): 

        other_value = self._get_value(other)

        return Calculator(self.num * other_value)
    
    def __truediv__(self, other): 

        other_value = self._get_value(other)

    # Validation to prevent denominator = 0
        if other_value == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return Calculator(self.num / other_value) 
    
    def __eq__(self, other):

        other_value = self._get_value(other)

        return (self.num == other_value)
    
    def __lt__(self, other):

        other_value = self._get_value(other)

        return (self.num < other_value)
    
    def __gt__(self, other):

        other_value = self._get_value(other)

        return (self.num > other_value)
    
    def __pow__(self, other):

        other_value = self._get_value(other)

        return Calculator(self.num ** other_value)
    
    # Negative Object 
    def __neg__(self):
        return Calculator(-self.num)
    
    # Absolute Value
    def __abs__(self):
        return Calculator(abs(self.num))
    
    def __iadd__(self, other):

        other_value = self._get_value(other)

        self.num += other_value

        return self
    
    def __isub__(self, other):

        other_value = self._get_value(other)

        self.num -= other_value

        return self
    
    def __imul__(self, other):

        other_value = self._get_value(other)

        self.num *= other_value

        return self
    
    def __itruediv__(self, other):
        other_value = self._get_value(other)

        if other_value == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        
        self.num /= other_value
        return self
        

num1 = Calculator(5) 
num2 = Calculator(3)
num3 = Calculator(-20)

print(num1==num2)
print(num1 < num2)
print(num1 > num2)
print(num1 ** num2)
print(-num1)
print(abs(num3))

num1 += num2
print(num1)

num1 -= num2
print(num1)

num1 *= num2
print(num1)

num1 /= num2
print(num1)