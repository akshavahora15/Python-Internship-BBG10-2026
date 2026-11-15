# Task 6 - Second Largest

n = int(input('Enter size of a list: '))
new_list = []

for x in range(1, n+1):
    str1 = int(input("Enter list elem: "))
    new_list.append(str1)

print('origi list:', new_list)

largest = new_list[0]
second_largest = new_list[0]

for num in new_list:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print('Largest:', largest)
print('Second Largest:', second_largest)