print("Quick Check 1: Collection Selection")
print("=" * 50)

scenarios = [
    {
        "description": "Store unique user IDs for fast lookup",
        "options": ["list", "tuple", "set", "dict"],
        "best_choice": "set",
        "reason": "Sets provide O(1) average lookup time for unique elements"
    },
    {
        "description": "Store coordinates (x, y) that won't change",
        "options": ["list", "tuple", "set", "dict"],
        "best_choice": "tuple",
        "reason": "Tuples are immutable and perfect for fixed data like coordinates"
    },
    {
        "description": "Store student names with their grades",
        "options": ["list", "tuple", "set", "dict"],
        "best_choice": "dict",
        "reason": "Dictionaries provide key-value mapping for associative data"
    },
    {
        "description": "Store a shopping list that can be modified",
        "options": ["list", "tuple", "set", "dict"],
        "best_choice": "list",
        "reason": "Lists are mutable and maintain order for sequential data"
    }
]

for i, scenario in enumerate(scenarios, 1):
    print(f"\n{i}. {scenario['description']}")
    print(f"   Options: {', '.join(scenario['options'])}")
    print(f"   Best choice: {scenario['best_choice']}")
    print(f"   Reason: {scenario['reason']}")