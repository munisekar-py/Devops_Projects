#In this program am utilizing Built-in function and Built-in string methods without importing other 3rd Party Modules


#defining Function
def check_password_strength(password):
    feedback = []   #Create an empty list for feedback
    
    #Checking its strength using 5 rules 
    
    if len(password) < 8:
        feedback.append("Password should be at least 8 characters long.")
        #Below It loops through each character (c) in the password.
    if not any(c.isupper() for c in password):
        feedback.append("Include at least one uppercase letter.")
    if not any(c.islower() for c in password):
        feedback.append("Include at least one lowercase letter.")
    if not any(c.isdigit() for c in password):
        feedback.append("Include at least one digit.")
        # Special Character Check
    if not any(c in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for c in password):
        feedback.append("Include at least one special character (!@#$%^&* etc.)")
    
    # Returning Results
    is_strong = len(feedback) == 0
    return is_strong, feedback

# Getting Password from  User
pwd = input("Enter your password to check its strength: ")
strong, issues = check_password_strength(pwd)  #Calling the Function
if strong:
    print("Your password is strong!")
else:
    print("Your password is weak. Suggestions:")
    for issue in issues:
        print(f"- {issue}")
