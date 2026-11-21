class InvalidAgeError(Exception):
    pass

def register_user(age):
    if age < 0 or age > 120:
        raise InvalidAgeError(f"Invalid age: {age}. Age must be between 0 and 120")
    print(f"User registered with age {age}")

try:
    register_user(25)
    register_user(150)
except InvalidAgeError as e:
    print("Error:", e)