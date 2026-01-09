print("\nTry This 4: Value Swapping")
print("=" * 50)

# Initial values
a = 10
b = 20
print(f"Initial values:          a = {a}, b = {b}")

# Method 1: Using a temporary variable (The classic way)
# Think of this like swapping water between two glasses using a third empty glass
temp = a
a = b
b = temp
print(f"After temp swap:         a = {a}, b = {b}")

# Method 2: Python's tuple unpacking (The best/Pythonic way)
# Python evaluates the right side (creating a tuple) then assigns to the left
a, b = b, a
print(f"After tuple unpacking:   a = {a}, b = {b}")

# Method 3: Using arithmetic (For numbers only)
# This works by using the sum to track the difference
a = a + b
b = a - b
a = a - b
print(f"After arithmetic swap:   a = {a}, b = {b}")

# Method 4: Using XOR (Bitwise operation - for integers only)
# This is a low-level computer science trick
a = a ^ b
b = a ^ b
a = a ^ b
print(f"After XOR swap:          a = {a}, b = {b}")