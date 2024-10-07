# 4.Create a to-do list and mark tasks as completed by removing them from the list.

todo_list = ["Buy groceries", "Clean the house", "Finish homework", "Call a friend"]

# Display the initial to-do list
print("Initial To-Do List:")
for task in todo_list:
    print(f"- {task}")

# Marking "Clean the house" as completed
task_to_remove = "Clean the house"

# Check if the task is in the list and remove it
if task_to_remove in todo_list:
    todo_list.remove(task_to_remove)
    print(f"\nTask '{task_to_remove}' marked as completed.")
else:
    print(f"\nTask '{task_to_remove}' not found in the to-do list.")

# Display the updated to-do list
print("\nUpdated To-Do List:")
for task in todo_list:
    print(f"- {task}")
