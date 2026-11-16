no=[10,20,30,70,60,50,80]

print('origi list:',no)

largest = no[0]
second_largest = None

for n in no:
    if n>largest:
        second_largest = largest
        largest = n
    elif second_largest is None or n>second_largest:
        second_largest = n
print('Largest:', largest)
print('Second Largest:', second_largest)