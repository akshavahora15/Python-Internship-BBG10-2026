numbers = [10, 25, 10, 45, 25, 60, 45, 70, 10, 90, 60, 5, 25, 70, 100]

unique_numbers = []

for n in numbers:
    if n not in unique_numbers:
        unique_numbers.append(n)

print("Original List:", numbers)
print("Without Duplicates:", unique_numbers)