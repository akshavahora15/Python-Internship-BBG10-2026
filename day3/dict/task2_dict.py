students = [
    {"name": "vahida", "marks": 88},
    {"name": "Aksha", "marks": 95},
    {"name": "Sara", "marks": 72},
    {"name": "vahida", "marks": 91}
]

highest_student = students[0]

for student in students:
    if student["marks"] > highest_student["marks"]:
        highest_student = student
        
print("Topper:", highest_student["name"])
print("Highest Marks:", highest_student["marks"])