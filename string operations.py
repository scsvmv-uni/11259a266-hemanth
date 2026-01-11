print("\nTry This 3: String Operations")
print("=" * 50)

# Basic string operations
first_name = "John"
last_name = "Doe"
age = 25

# String concatenation (Joining strings with +)
full_name = first_name + " " + last_name
print(f"Full name: {full_name}")

# String repetition (Using * to repeat characters)
separator = "=" * 30
print(separator)

# Escape sequences
# Note: Use a single backslash \ to trigger the effect
print("Escape sequences in action:")
print("1. New line effect:\n   Line A\n   Line B")
print("2. Tab effect:\tColumn1\tColumn2")
print("3. Quotes: He said \"Hello\"")
print("4. Backslash: Path: C:\\Users\\Name")

# Triple-quoted strings (Preserves formatting and line breaks)
multi_line = """
This is a multi-line string.
It can span multiple lines.
Perfect for documentation!
"""
print("\nMulti-line string output:")
print(multi_line)

# String formatting
print("String formatting styles:")
print(f"f-string (Modern): {first_name} is {age} years old")
print("format() (Older): {} is {} years old".format(first_name, age))
print("%-style (Legacy): %s is %d years old" % (first_name, age))