# Program to validate email address
import re
# using regression equations
def check(email):
    regex = r'^[a-zA-Z0-9._+-]+@[a-zA-Z0-9._+]+\.[a-zA-Z0-9._]+$'
    if re.match(regex, email):
        return True
    else:
        return False

if __name__ == "__main__":
    email = str(input("Enter Your Email Here:"))
    answer = check(email)
    if check(email):
        print(f"Email is Valid {email}")
    else:
        print(f"Email is Not Valid {email}")
