students = [("Riya", 85), ("Aman", 95), ("Sara", 72), ("Rahul",80)]

sorted_students = sorted(students,key=lambda x: x[1],reverse=True)

print(sorted_students)