import re
import getpass

def evaluate_password_strength(password):
    length = len(password)
    has_uppercase = any(c.isupper() for c in password)
    has_lowercase = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    score = length + has_uppercase + has_lowercase + has_digit + has_special

    if score < 5:
        strength = "Very Weak"
    elif score < 8:
        strength = "Weak"
    elif score < 10:
        strength = "Moderate"
    elif score < 12:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return score, strength


password = getpass.getpass(prompt="Enter a password: ")

score, strength = evaluate_password_strength(password)
print(f"The strength of the password is {strength}.")
