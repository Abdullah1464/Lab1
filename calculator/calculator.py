def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Undefined (division by zero)"
    return x / y
"""Fixed a bug."""
def modulus(x, y):
    """Calculate the modulus (remainder) of two numbers."""
    if y == 0:
        return "Cannot divide by zero"
    return x % y