print("\nTry This 2: Variable Manipulation")
print("=" * 50)

# Example: Circle calculations
pi = 3.14159
radius = 2.2

# Initial Calculation
area = pi * radius ** 2
circumference = 2 * pi * radius

print(f"Circle with radius {radius}:")
print(f"  Area: {area:.2f}")
print(f"  Circumference: {circumference:.2f}")

# Change radius and observe effects
print(f"\nChanging radius to 5.0...")
radius = 5.0
print(f"New radius: {radius}")

# Demonstrating that variables do not 'auto-update'
print(f"Area is still: {area:.2f} (not recalculated!)")
print(f"Circumference is still: {circumference:.2f} (not recalculated!)")

# Recalculate to get updated results
area = pi * radius ** 2
circumference = 2 * pi * radius

print(f"After recalculation:")
print(f"  Area: {area:.2f}")
print(f"  Circumference: {circumference:.2f}")