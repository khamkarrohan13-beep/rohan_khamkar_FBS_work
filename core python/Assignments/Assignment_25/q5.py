# 5. Write a Python function that takes an email address as input and uses a regular
# expression to validate if it is a valid email address. The function should return True for
# valid emails and False for invalid ones.

import re

def validate_email(email):
    pattern = r'\w+@\w+\.\w+'
    
    if re.fullmatch(pattern, email):
        return True
    else:
        return False


email = input("Enter email: ")

print(validate_email(email))