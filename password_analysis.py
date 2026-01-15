import re

def validate_password_strength(password):
    """Analyzes password strength based on specific criteria."""
    criteria = {
        'length': len(password) >= 8,
        'has_uppercase': any(c.isupper() for c in password),
        'has_lowercase': any(c.islower() for c in password),
        'has_digit': any(c.isdigit() for c in password),
        'has_special': bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)),
        'no_common_patterns': password.lower() not in ["password", "123456", "qwerty"],
        'no_repeated_chars': len(set(password)) / len(password) > 0.5 if len(password) > 0 else False,
        'length_12_plus': len(password) >= 12
    }
    
    # Calculate score
    score = sum(criteria.values())
    max_score = len(criteria)
    percentage = (score / max_score) * 100
    
    # Determine strength label
    if score <= 2: strength = "Very Weak"
    elif score <= 4: strength = "Weak"
    elif score <= 6: strength = "Medium"
    elif score == 7: strength = "Strong"
    else: strength = "Very Strong"
    
    return {
        'criteria': criteria,
        'score': score,
        'max_score': max_score,
        'percentage': percentage,
        'strength': strength
    }

def display_password_analysis(password, analysis):
    """Displays the formatted results of the analysis."""
    print(f"\nPassword Analysis: '{password}'")
    print("-" * 40)
    
    criteria_descriptions = {
        'length': 'At least 8 characters',
        'has_uppercase': 'Contains uppercase letter',
        'has_lowercase': 'Contains lowercase letter',
        'has_digit': 'Contains digit',
        'has_special': 'Contains special character',
        'no_common_patterns': 'No common patterns',
        'no_repeated_chars': 'Sufficient character variety',
        'length_12_plus': 'At least 12 characters (bonus)'
    }
    
    for criterion, passed in analysis['criteria'].items():
        status = "✓" if passed else "✗"
        description = criteria_descriptions.get(criterion, criterion)
        print(f"  {status} {description}")
    
    print(f"\nStrength Score: {analysis['score']}/{analysis['max_score']} "
          f"({analysis['percentage']:.1f}%)")
    print(f"Overall Strength: {analysis['strength']}")
    
    if analysis['strength'] in ['Very Weak', 'Weak', 'Medium']:
        print("\nRecommendations:")
        for criterion, passed in analysis['criteria'].items():
            if not passed and criterion != 'length_12_plus':
                description = criteria_descriptions.get(criterion, criterion)
                print(f"  - {description}")

# --- Main Execution ---
test_passwords = [
    "password", "Password123", "Password123!", 
    "MyStr0ng!P@ssw0rd", "123456", "qwerty", "a", "Abc123!@#"
]

print("Password Security Validator")
print("=" * 30)

for pwd in test_passwords:
    results = validate_password_strength(pwd)
    display_password_analysis(pwd, results)