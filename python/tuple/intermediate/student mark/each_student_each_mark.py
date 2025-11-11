students = [
    ("sachin",(78,86,91)),
    ("deva",(82,94,78)),
    ("aathi",(97,76,84))
]
print("*************Task 1**************")
for student in students:
    name, marks = student
    print(f"{name}: ",end="")
    for i,mark in enumerate(marks,start=1):
        print(f" Subject {i} : {mark}",end="")
        if i < len(marks):
            print(end=",")
        else:
             print("")
    print()

print("*************Task 2**************")
for student in students:
    name, marks = student
    avg = sum(marks)/len(marks)
    print(f"{name}'s Average is {avg:.2f}")


print("*************Task 3**************")
for student in students:
    name, marks = student
    high = max(marks)
    print(f"{name}'s  Highest is {high}")

print("*************Task 4**************")

students.append(("maya",(78,86,90)))

print(students)