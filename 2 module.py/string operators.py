print("\nQuick Check 3: String Operations")
print("=" * 50)

text = "   Python Programming is AWESOME!  "
print(f"Original: '{text}'")

# Basic string methods
print(f"Strip: '{text.strip()}'")
print(f"Lower: '{text.lower()}'")
print(f"Upper: '{text.upper()}'")
print(f"Title: '{text.strip().title()}'")
print(f"Replace: '{text.replace('AWESOME', 'AMAZING')}'")

# String splitting and joining
words = text.strip().lower().split()
print(f"Words: {words}")
print(f"Joined with '-': {'-'.join(words)}")

# String formatting
name = "Alice"
age = 25
score = 87.5

print(f"\nString formatting examples:")
print(f"f-string: {name} is {age} years old and scored {score:.1f}%")
print("format(): {} is {} years old and scored {:.1f}%".format(name, age, score))