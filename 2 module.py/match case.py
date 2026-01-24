print("\nQuick Check 5: match/case")
print("=" * 50)

def classify(value):
    match value:
        case {"type": "point", "x": xval, "y": yval} if xval == yval:
            return "diagonal point"
        case (a, b):
            return f"tuple({a}, {b})"
        case str() as s if s.endswith("rejected"):
            return "ends with 'rejected'"
        case _:
            return "unknown"

samples = [
    {"type": "point", "x": 3, "y": 3},
    (1, 2),
    "request rejected",
    42,
]

for s in samples:
    print(s, "->", classify(s))