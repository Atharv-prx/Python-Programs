# Added more magical method and a zero validation for __truediv__

class Calculator:
    
    def __init__(self, num): 
        self.num = num 

    def __str__(self):
        return f"Calculator Value: {self.num}"
    
    # This is the professional version of __str__.
    # Helps in debugging, without is we get horrible memory address
    def __repr__(self):
        return f"Calculator({self.num})"

    #Added Calculator before (self.num + other.num) so that it actually returns an object and str becomes automatically usefull 
    def __add__(self, other): 
        return Calculator(self.num + other.num)  
    
    def __sub__(self, other): 
        return Calculator(self.num - other.num)
     
    def __mul__(self, other): 
        return Calculator(self.num * other.num)
    
    def __truediv__(self, other): 
        if other.num == 0:
            return "Cannot Divide by 0"
        return Calculator(self.num / other.num) 
    
    def __eq__(self, other):
        return (self.num == other.num)
    
    def __lt__(self, other):
        return (self.num < other.num)
    
    def __gt__(self, other):
        return (self.num > other.num)
    
    def __pow__(self, other):
        return Calculator(self.num ** other.num)
    
    # Negative Object 
    def __neg__(self):
        return Calculator(-self.num)
    
    # Absolute Value
    def __abs__(self):
        return Calculator(abs(self.num))

    
num1 = Calculator(5) 
num2 = Calculator(3)
num3 = Calculator(-20)

print(num1==num2)
print(num1 < num2)
print(num1 > num2)
print(num1 ** num2)
print(-num1)
print(abs(num3))