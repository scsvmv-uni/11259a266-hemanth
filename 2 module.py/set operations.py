print("\nTry This 3: Set Operations")
print("=" * 50)
    
    # Create sets
group_a = {"Alice", "Bob", "Charlie", "Diana", "Eve"}
group_b = {"Bob", "Charlie", "Frank", "Grace", "Henry"}
group_c = {"Alice", "Diana", "Ivy", "Jack", "Kate"}
    
print(f"Group A: {group_a}")
print(f"Group B: {group_b}")
print(f"Group C: {group_c}")
    
    # Set operations
intersection_ab = group_a & group_b
union_ab = group_a | group_b
difference_ab = group_a - group_b
symmetric_diff_ab = group_a ^ group_b
    
print(f"\nSet operations:")
print(f"A ∩ B (intersection): {intersection_ab}")
print(f"A ∪ B (union): {union_ab}")
print(f"A - B (difference): {difference_ab}")
print(f"A △ B (symmetric difference): {symmetric_diff_ab}")
    
    # Multiple set operations
all_students = group_a | group_b | group_c
in_all_groups = group_a & group_b & group_c
only_in_a = group_a - group_b - group_c
    
print(f"\nMultiple set operations:")
print(f"All students: {all_students}")
print(f"In all groups: {in_all_groups}")
print(f"Only in group A: {only_in_a}")
    
    # Set comprehensions
long_names = {name for name in all_students if len(name) > 4}
names_starting_with_a = {name for name in all_students if name.startswith('A')}
    
print(f"\nSet comprehensions:")
print(f"Long names (>4 chars): {long_names}")
print(f"Names starting with 'A': {names_starting_with_a}")