print("\nQuick Check 2: Comprehension Writing")
print("=" * 50)

# Sample data
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
words = ["python", "java", "javascript", "c++", "go", "rust"]

print("Original data:")
print(f"Numbers: {numbers}")
print(f"Words: {words}")

# List comprehensions
print("\nList Comprehensions:")
squares = [x**2 for x in numbers]
even_squares = [x**2 for x in numbers if x % 2 == 0]
word_lengths = [len(word) for word in words]

print(f"Squares: {squares}")
print(f"Even squares: {even_squares}")
print(f"Word lengths: {word_lengths}")

# Set comprehensions
print("\nSet Comprehensions:")
unique_lengths = {len(word) for word in words}
even_numbers_set = {x for x in numbers if x % 2 == 0}

print(f"Unique word lengths: {unique_lengths}")
print(f"Even numbers set: {even_numbers_set}")

# Dictionary comprehensions
print("\nDictionary Comprehensions:")
word_to_length = {word: len(word) for word in words}
number_to_square = {x: x**2 for x in numbers if x % 2 == 0}

print(f"Word to length: {word_to_length}")
print(f"Even number to square: {number_to_square}")