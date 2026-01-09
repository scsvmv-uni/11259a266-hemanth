print("\nQuick Check 3: Operator Precedence")
print("=" * 80)

expressions = [
    ("2 + 3 * 4", "Multiplication before addition"),
    ("(2 + 3) * 4", "Parentheses override precedence"),
    ("2 ** 3 ** 2", "Right-associative exponentiation (3**2 first)"),
    ("(2 ** 3) ** 2", "Parentheses change associativity"),
    ("10 / 3 * 3", "Left-to-right for same precedence"),
    ("10 // 3 * 3", "Floor division vs regular division"),
    ("not True and False", "not has higher precedence than and"),
    ("not (True and False)", "Parentheses change evaluation order"),
]

# Header
print(f"{'Expression':<22} | {'Result':<10} | {'Explanation'}")
print("-" * 80)

for expr, explanation in expressions:
    try:
        # eval() runs the string as Python code
        result = eval(expr)
        # Formatting result to string to handle booleans and floats properly
        print(f"{expr:<22} | {str(result):<10} | {explanation}")
    except Exception as e:
        print(f"{expr:<22} | ERROR      | {e}")