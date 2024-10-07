#9.Store and calculate the total marks of students in different subjects using a 2D array.

marks = [
    [85, 78, 92],  # Marks of Student 1 in three subjects
    [88, 90, 79],  # Marks of Student 2 in three subjects
    [75, 85, 89]   # Marks of Student 3 in three subjects
]

# Manually calculate the total marks for each student
student_1_total = marks[0][0] + marks[0][1] + marks[0][2]
student_2_total = marks[1][0] + marks[1][1] + marks[1][2]
student_3_total = marks[2][0] + marks[2][1] + marks[2][2]

# Print the total marks of each student
print("Total Marks of Students:")
print("Student 1:", student_1_total)
print("Student 2:", student_2_total)
print("Student 3:", student_3_total)
