print("\nQuick Check 4: Control Flow Logic")
print("=" * 50)

# Complex conditional example
def analyze_number(num):
    if num > 0:
        if num % 2 == 0:
            return "positive even"
        else:
            return "positive odd"
    elif num < 0:
        return "negative"
    else:
        return "zero"

test_numbers = [5, -3, 0, 8, -10]
print("Number analysis:")
for num in test_numbers:
    result = analyze_number(num)
    print(f"  {num} -> {result}")

# Loop with break and continue
print("\nLoop with break and continue:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = []

for num in numbers:
    if num % 3 == 0:
        continue  # Skip multiples of 3
    if num > 7:
        break     # Stop if number > 7
    result.append(num)

print(f"Numbers processed: {result}")