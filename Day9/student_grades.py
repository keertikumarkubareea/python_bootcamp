"""
Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values.

The final version of the student_grades dictionary will be checked.

This is the scoring criteria:
Scores 91 - 100: Grade = "Outstanding"
Scores 81 - 90: Grade = "Exceeds Expectations"
Scores 71 - 80: Grade = "Acceptable"
Scores 70 or lower: Grade = "Fail"

"""

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
student_grades = {}
for key in student_scores:
    if student_scores[key] >= 91:
        grade = "Outstanding"
    elif student_scores[key] >= 81:
        grade = "Exceeds Expectations"
    elif student_scores[key] >= 71:
        grade = "Acceptable"
    else:
        grade = "Fail"
    student_grades[key] = grade
print(student_grades)