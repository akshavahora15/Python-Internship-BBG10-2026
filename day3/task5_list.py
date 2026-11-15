students = [("Riya", 85), ("Aman", 95), ("Sara", 72), ("Rahul", 88)]

def get_marks(student):
    return student[1]

sorted_students = sorted(students, key=get_marks, reverse=True)

print(sorted_students)