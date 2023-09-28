import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, email):
        return True
    else:
        return False

email_address=input("enter the email address u like to check: ")
result = validate_email(email_address)
if result:
    print("Valid email address")
else:
    print("Invalid email address")
