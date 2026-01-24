print("\nTry This 2: Dictionary Usage")
print("=" * 50)

# Create a dictionary
student_grades = {
    "Alice": [85, 92, 78, 96],
    "Bob": [90, 88, 95, 87],
    "Charlie": [70, 75, 80, 72],
    "Diana": [95, 98, 92, 94]
}

print("Student grades:")
for student, grades in student_grades.items():
    average = sum(grades) / len(grades)
    # Using :.1f to round the average to one decimal place
    print(f"  {student}: {grades} -> Average: {average:.1f}")

# Dictionary operations
print(f"\nAll students: {list(student_grades.keys())}")
print(f"All grades: {list(student_grades.values())}")

# Dictionary comprehension
averages = {student: sum(grades) / len(grades) 
            for student, grades in student_grades.items()}
print(f"Student averages: {averages}")

# Find students with average > 85
high_achievers = {student: avg for student, avg in averages.items() 
                  if avg > 85}
print(f"High achievers: {high_achievers}")

# Nested dictionary
student_info = {
    "Alice": {"grades": [85, 92, 78, 96], "major": "Computer Science"},
    "Bob": {"grades": [90, 88, 95, 87], "major": "Mathematics"},
    "Charlie": {"grades": [70, 75, 80, 72], "major": "Physics"}
}

print(f"\nStudent info: {student_info}")
print(f"Alice's major: {student_info['Alice']['major']}")