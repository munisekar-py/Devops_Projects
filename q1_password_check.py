def check_password_strength(password):
    feedback = []
    
    #Checks its strength using 5 rules
    
    if len(password) < 8:
        feedback.append("Password should be at least 8 characters long.")
    if not any(c.isupper() for c in password):
        feedback.append("Include at least one uppercase letter.")
    if not any(c.islower() for c in password):
        feedback.append("Include at least one lowercase letter.")
    if not any(c.isdigit() for c in password):
        feedback.append("Include at least one digit.")
    if not any(c in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for c in password):
        feedback.append("Include at least one special character (!@#$%^&* etc.)")
    
    is_strong = len(feedback) == 0
    return is_strong, feedback

# Getting User input
pwd = input("Enter your password to check its strength: ")
strong, issues = check_password_strength(pwd)
if strong:
    print("Your password is strong!")
else:
    print("Your password is weak. Suggestions:")
    for issue in issues:
        print(f"- {issue}")
