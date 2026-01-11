print("\nLab Problem 1: Temperature Converter")
print("=" * 50)

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin."""
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius."""
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    """Convert Fahrenheit to Kelvin."""
    # This reuses existing functions (a great practice!)
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))

def kelvin_to_fahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit."""
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))

# Test the conversion functions
test_temperatures = [0, 25, 100, -40, 37]  # Celsius values

print("Temperature Conversion Table:")
print(f"{'Celsius':>8} | {'Fahrenheit':>10} | {'Kelvin':>8}")
print("-" * 35)

for c in test_temperatures:
    f = celsius_to_fahrenheit(c)
    k = celsius_to_kelvin(c)
    # :7.1f means 7 spaces wide, 1 decimal place, float type
    print(f"{c:8.1f} | {f:10.1f} | {k:8.1f}")

# Test special cases
print(f"\nSpecial cases:")
print(f"Absolute zero:   {kelvin_to_celsius(0):>8.2f}°C")
print(f"Water freezing:  {celsius_to_fahrenheit(0):>8.1f}°F")
print(f"Water boiling:   {celsius_to_fahrenheit(100):>8.1f}°F")
print(f"Body temp:       {celsius_to_fahrenheit(37):>8.1f}°F")