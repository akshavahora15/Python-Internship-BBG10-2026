class OutOfRangeError(Exception):
    pass

while True:
    try:
        num = int(input("Enter a number between 1 and 10: "))
        if num < 1 or num > 10:
            raise OutOfRangeError("Number must be between 1 and 10")
        print(f"Valid number: {num}")
        break
    except ValueError:
        print("That is not a number, try again")
    except OutOfRangeError as e:
        print("Error:", e)