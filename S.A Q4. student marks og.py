# Define the number of students
num_students = 10

# Initialize an array to store student marks
student_marks = [0] * num_students

# Prompt the user to enter student marks for each student
for i in range(num_students):
 print(f"Enter the mark for student {i+1}:")
 student_marks[i] = float(input())

# Reverse the order of the student marks
student_marks = student_marks[::-1]

# Print the reversed student marks
print("Reversed Student Marks:")
for i in range(num_students):
 print(f"Student {i+1}: {student_marks[i]:.2f}")
