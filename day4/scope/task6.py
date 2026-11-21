def make_validator(min_value):
    def validator(num):
        return num >= min_value
    return validator

check_10 = make_validator(10)
check_50 = make_validator(50)

print(check_10(5))  
print(check_10(15))
print(check_50(30))
print(check_50(60))  