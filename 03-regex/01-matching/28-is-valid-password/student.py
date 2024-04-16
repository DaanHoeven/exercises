import re


def is_valid_password(string):
    pattern = (
        r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[-+\*/.@])"  # Conditions for digit, lowercase, uppercase, and special character
        r"(?!.*(.)\1{2})(?!.*(.)\2{3})"  # Conditions to avoid three times and four times the same character
        r".{12,}$"  # Condition for length (at least 12 characters)
    )
    return re.match(pattern, string) is not None


# Test the function
passwords = ["Abcdef12", "aaaaaaabb", "abcABC123", "Abc123456", "ABCabcA123A@+A/"]
for password in passwords:
    print(f"Password '{password}': {is_valid_password(password)}")
