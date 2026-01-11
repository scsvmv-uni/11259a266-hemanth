print("\nLab Problem 2: Enhanced Calculator")
print("=" * 50)

def get_number(prompt):
    """Get a valid number from user input."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please enter a number.")

def get_operation():
    """Get a valid operation from user."""
    valid_ops = ['+', '-', '*', '/', '**', '%']
    while True:
        op = input("Enter operation (+, -, *, /, **, %): ").strip()
        if op in valid_ops:
            return op
        print(f"Invalid operation! Choose from: {', '.join(valid_ops)}")

def calculate(num1, num2, operation):
    """Perform calculation with error handling."""
    try:
        if operation == '+':
            return num1 + num2
        elif operation == '-':
            return num1 - num2
        elif operation == '*':
            return num1 * num2
        elif operation == '/':
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero!")
            return num1 / num2
        elif operation == '**':
            return num1 ** num2
        elif operation == '%':
            if num2 == 0:
                raise ZeroDivisionError("Cannot modulo by zero!")
            return num1 % num2
    except Exception as e:
        return f"Error: {e}"

# Simulate calculator usage
print("Enhanced Calculator")
print("Enter 'quit' to exit")

# Example calculations (simulated)
test_cases = [
    (10, 3, '+'),
    (10, 3, '-'),
    (10, 3, '*'),
    (10, 3, '/'),
    (10, 3, '**'),
    (10, 3, '%'),
    (10, 0, '/'),  # Division by zero
]

for num1, num2, op in test_cases:
    result = calculate(num1, num2, op)
    print(f"{num1} {op} {num2} = {result}")