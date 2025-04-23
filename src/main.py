def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
    
def power(a, b):
    """
    Calculate a raised to the power of b
    
    Parameters:
    a (float): The base number
    b (float): The exponent
    
    Returns:
    float: The result of a^b
    """
    return a ** b