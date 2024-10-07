# 6.	Create a list of lists where each sublist contains the name, age, and grade of students, and sort the list by grade.
students = [
    ["Alice", 20, "B"],
    ["Bob", 19, "A"], 
    ["Charlie", 21, "C"]
    ]
students.sort(key=lambda x: x[2])
print(students)  # Output: [['Bob', 19, 'A'], ['Alice', 20, 'B'], ['Charlie', 21, 'C']]
