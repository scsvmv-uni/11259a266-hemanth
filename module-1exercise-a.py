# Example names to evaluate
names_to_evaluate = [
    "user_name",               # Fixed from userName (snake_case)
    "total_count",             # Good
    "MAX_SIZE",                # Good for constants
    "get_user_data",           # Fixed from getUserData (snake_case)
    "coordinate_x",            # Fixed from 'x' to be more descriptive
    "calculate_average_grade", # Good
    "current_temp",            # Fixed from temp_var to be more descriptive
    "is_valid",                # Good
    "data",                    # Fixed from data_list (removed redundancy)
    "process_data"             # Good
]

print("Evaluate these names for PEP 8 compliance:")
for name in names_to_evaluate:
    print(f"- {name}")

print("\nGood names follow these rules:")
print("- Use snake_case for variables and functions")
print("- Use UPPER_CASE for constants")
print("- Be descriptive but concise")
print("- Avoid single letters (except in loops)")
print("- Avoid redundant words (like 'data_list')")