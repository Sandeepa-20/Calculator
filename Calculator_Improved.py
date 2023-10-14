# Version 2 - Improved Calculator
def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract two numbers"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide two numbers"""
    if b == 0:
        return "Error: Division by zero"
    return a / b

if __name__ == "__main__":
    # Version 1
    print("Version 1")
    print("python code 1")
    print("def add(a, b):")
    print("    return a + b")
    print("def subtract(a, b):")
    print("    return a - b")
    print()
    print("python code 2")
    print("Version 2")
    print("def add(a, b):")
    print("    \"\"\"Add two numbers\"\"\"")
    print("    return a + b")
    print("def subtract(a, b):")
    print("    \"\"\"Subtract two numbers\"\"\"")
    print("    return a - b")
    print("def multiply(a, b):")
    print("    \"\"\"Multiply two numbers\"\"\"")
    print("    return a * b")
    print("def divide(a, b):")
    print("    \"\"\"Divide two numbers\"\"\"")
    print("    if b == 0:")
    print("        return \"Error: Division by zero\"")
    print("    return a / b")