print("\nTry This 1: Getting Input and Type Conversion")
print("=" * 50)

# Simulate different input scenarios
test_inputs = ["123", "45.67", "hello", "", "   42  "]

for user_input in test_inputs:
    print(f"\nTesting input: '{user_input}'")
    print(f"Original type: {type(user_input).__name__}")
    
    # 1. Try converting to integer
    try:
        # int() fails if there is a decimal point or letters
        int_value = int(user_input)
        print(f"As integer: {int_value}")
    except ValueError:
        print("Cannot convert to integer")
    
    # 2. Try converting to float
    try:
        # float() works for whole numbers and decimals
        float_value = float(user_input)
        print(f"As float: {float_value}")
    except ValueError:
        print("Cannot convert to float")
    
    # 3. Validation Logic
    stripped = user_input.strip()  # Removes leading/trailing spaces
    if stripped.isdigit():
        print("Contains only digits")
    elif stripped.replace('.', '', 1).isdigit() and stripped.count('.') < 2:
        print("Contains only digits and one decimal point")
    else:
        print("Contains non-numeric characters or is empty")