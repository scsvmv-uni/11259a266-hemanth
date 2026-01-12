print("\nLab Problem 3: Grade Management System")
print("=" * 50)

def calculate_weighted_average(grades, weights):
    """Calculate weighted average of grades."""
    if len(grades) != len(weights):
        raise ValueError("Grades and weights must have the same length")
    
    # Check if weights sum to 1.0 (using a tolerance for float precision)
    if abs(sum(weights) - 1.0) > 0.01:
        raise ValueError("Weights must sum to 1.0")
    
    # Mathematical formula: sum(grade * weight)
    return sum(grade * weight for grade, weight in zip(grades, weights))

def get_letter_grade(percentage):
    """Convert percentage to letter grade."""
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    else:
        return 'F'

def get_grade_point(letter_grade):
    """Convert letter grade to grade point using a dictionary lookup."""
    grade_points = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
    return grade_points.get(letter_grade, 0.0)

# Example student data
students = [
    {
        'name': 'Alice',
        'grades': [85, 92, 78, 96],
        'weights': [0.25, 0.25, 0.25, 0.25]
    },
    {
        'name': 'Bob',
        'grades': [90, 88, 95, 87],
        'weights': [0.2, 0.3, 0.2, 0.3]
    },
    {
        'name': 'Charlie',
        'grades': [70, 75, 80, 72],
        'weights': [0.25, 0.25, 0.25, 0.25]
    }
]

# Process and Display results
for student in students:
    name = student['name']
    grades = student['grades']
    weights = student['weights']
    
    try:
        average = calculate_weighted_average(grades, weights)
        letter_grade = get_letter_grade(average)
        grade_point = get_grade_point(letter_grade)
        
        print(f"\n{name}:")
        print(f"  Grades: {grades}")
        print(f"  Weights: {weights}")
        print(f"  Average: {average:.2f}%")
        print(f"  Letter Grade: {letter_grade}")
        print(f"  Grade Point: {grade_point}")
        
    except ValueError as e:
        print(f"\n{name}: Error - {e}")