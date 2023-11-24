def add(x: int, y: int) -> int:
   return x + y

def subtract(x: int, y: int) -> int:
   return x - y

def divide(x: float, y: float) -> float:
   if y == 0:
       raise ValueError("Division by zero is not allowed.")
   return x / y

def multiply(x: int, y: int) -> int:
   return x * y

def square(x: int) -> int:
   return x ** 2

def power(x: float, y: float) -> float:
   return x ** y

def sqrt(x: float) -> float:
   if x < 0:
       raise ValueError("Cannot compute the square root of a negative number.")
   return x ** 0.5
