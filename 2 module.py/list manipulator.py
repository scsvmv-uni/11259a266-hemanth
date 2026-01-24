print("\nTry This 1: List Manipulation")
print("=" * 50)

# Create a sample list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original list: {numbers}")

# Advanced slicing
# Syntax: [start:stop:step]
print(f"First 5 elements: {numbers[:5]}")
print(f"Last 3 elements: {numbers[-3:]}")
print(f"Every 2nd element: {numbers[::2]}")
print(f"Reverse: {numbers[::-1]}")

# List methods
numbers_copy = numbers.copy()
numbers_copy.append(11)
numbers_copy.insert(0, 0)
numbers_copy.extend([12, 13, 14])
print(f"After modifications: {numbers_copy}")

# List comprehensions with conditions
even_numbers = [x for x in numbers if x % 2 == 0]
squares_of_odds = [x**2 for x in numbers if x % 2 != 0]

print(f"Even numbers: {even_numbers}")
print(f"Squares of odd numbers: {squares_of_odds}")

# Nested list operations (Creating a 3x3 matrix)
matrix = [[i + j for j in range(3)] for i in range(3)]
print(f"Matrix: {matrix}")

# Flatten matrix
flattened = [item for row in matrix for item in row]
print(f"Flattened matrix: {flattened}")