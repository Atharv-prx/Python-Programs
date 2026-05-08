class Calculator:
    
    def __init__(self, num): 
        self.num = num 
    
    def __add__(self, other): 
        return self.num + other.num 
    
    def __sub__(self, other): 
        return self.num - other.num
     
    def __mul__(self, other): 
        return self.num * other.num 
    
    def __truediv__(self, other): 
        return self.num / other.num 
    
    
num1 = Calculator(5) 
num2 = Calculator(3) 

print(num1 + num2) 
print(num1 - num2) 
print(num1 * num2) 
print(num1 / num2) 