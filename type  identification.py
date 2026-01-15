def run_type_check():
    print("\nQuick Check 2: Type Identification")
    print("=" * 60)
    
    # Test objects including "Falsy" variations for better learning
    test_objects = [
        1234, 8.99, 9.0,          # Numbers
        True, False,              # Booleans
        "hello", "",              # Strings (Full vs Empty)
        None,                     # NoneType
        [1, 2, 3], [],            # Lists (Full vs Empty)
        (1, 2, 3),                # Tuple
        {"a": 1}, {},             # Dicts (Full vs Empty)
        3 + 4j,                   # Complex
    ]
    
    # Header with specific column widths
    # {<15}: Left-aligned, 15 chars | {<12}: Left-aligned, 12 chars
    header = f"{'Object':<15} | {'Type':<12} | {'Truthiness'}"
    print(header)
    print("-" * len(header))
    
    for obj in test_objects:
        obj_repr = repr(obj)
        # Truncate long representations to keep the table neat
        if len(obj_repr) > 13:
            obj_repr = obj_repr[:10] + "..."
            
        obj_type = type(obj).__name__
        truthiness = bool(obj)
        
        print(f"{obj_repr:<15} | {obj_type:<12} | {truthiness}")

if __name__ == "__main__":
    run_type_check()