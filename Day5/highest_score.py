"""Replicating the max function using a for-loop"""

# Input a list of student scores
student_scores = input("Please enter student test scores, separated by a space: ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

max_score = student_scores[0]
for score in student_scores:
    if score > max_score:
        max_score = score

print(f"The highest score in the class is: {max_score}")
