"""
Author: Keertikumar Kubareea
Project: Loops - Average height of a list of heights

"""

# Input a Python list of student heights
student_heights = input("Please enter heights separated by a space: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total = 0
count = 0
for stu in student_heights:
    count = count + 1
    total += stu

average = int(round(total / count, 0))
print(f"total height = {total}")
print(f"number of students = {count}")
print(f"average height = {average}")
