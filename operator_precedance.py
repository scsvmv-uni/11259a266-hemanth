def run_precedence_check():
    print("\nQuick Check 3: Operator Precedence")
    print("=" * 70)
    
    expressions = [
        ("2 + 3 * 4", "Multiplication (3*4) then Addition (+2)"),
        ("(2 + 3) * 4", "Parentheses happen first"),
        ("2 ** 3 ** 2", "Right-to-Left: 2 ** (3 ** 2) = 2 ** 9"),
        ("(2 ** 3) ** 2", "Left-to-Right: (8) ** 2"),
        ("10 / 3 * 3", "Left-to-Right: (3.33...) * 3"),
        ("10 // 3 * 3", "Floor division (3) * 3"),
        ("not True and False", "'not' runs before 'and'"),
        ("not (True and False)", "Parentheses evaluated first"),
    ]
    
    # Adjusted column widths for better readability
    print(f"{'Expression':<22} | {'Result':<10} | {'Explanation'}")
    print("-" * 70)
    
    for expr, explanation in expressions:
        try:
            # eval() safely executes the string as Python code
            result = eval(expr)
            # Displaying result
            print(f"{expr:<22} | {str(result):<10} | {explanation}")
        except Exception as e:
            print(f"{expr:<22} | ERROR      | {e}")

if __name__ == "__main__":
    run_precedence_check()