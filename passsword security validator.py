print("\nLab Problem 4: Password Security Validator")
print("=" * 50)

def validate_password_strength(password):
    """
    Validate password strength and return detailed analysis.
    
    Returns:
        dict: Analysis results with criteria and overall score
    """
    criteria = {
        'length': len(password) >= 8,
        'has_uppercase': any(c.isupper() for c in password),
        'has_lowercase': any(c.islower() for c in password),
        'has_digit': any(c.isdigit() for c in password),
        'has_special': any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password),
        'no_common_patterns': not any(pattern in password.lower() for pattern in 
                                     ['password', '123456', 'qwerty', 'abc123']),
        'no_repeated_chars': len(set(password)) >= len(password) * 0.6,
        'length_12_plus': len(password) >= 12
    }
    
    # Calculate strength score (True counts as 1, False as 0)
    score = sum(criteria.values())
    max_score = len(criteria)
    
    # Determine strength level
    if score >= 7:
        strength = "Very Strong"
    elif score >= 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"
    
    return {
        'criteria': criteria,
        'score': score,
        'max_score': max_score,
        'strength': strength,
        'percentage': (score / max_score) * 100
    }

# --- Testing the Validator ---
test_passwords = ["123456", "Pass123!", "Complex_Pass_2024!"]

for pwd in test_passwords:
    result = validate_password_strength(pwd)
    print(f"\nPassword: {pwd}")
    print(f"Strength: {result['strength']} ({result['score']}/{result['max_score']})")
    print("Failed Criteria:", [k for k, v in result['criteria'].items() if not v])