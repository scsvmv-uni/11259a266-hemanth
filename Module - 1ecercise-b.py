print("\nQuick Check 2: Type Identification")
print("=" * 55)

# Test objects
test_objects = [
    1234,           # int
    8.99,           # float
    9.0,            # float
    True,           # bool
    False,          # bool
    "hello",        # str
    None,           # NoneType
    [1, 2, 3],      # list
    (1, 2, 3),      # tuple
    {1, 2, 3},      # set
    {"a": 1},       # dict
    3 + 4j,         # complex
]

# Header for the output
print(f"{'Object':>15} | {'Type':<12} | {'Truthiness'}")
print("-" * 55)

for obj in test_objects:
    obj_type = type(obj).__name__
    truthiness = bool(obj)
    # Using !r to show the representation (like quotes around strings)
    # Increased width to 15 to accommodate brackets and braces
    print(f"{obj!r:>15} | {obj_type:<12} | {truthiness}")