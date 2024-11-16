# Schedule Manager

tasks = []

def add_task():
    """Add a new task to the schedule."""
    description = input("Enter the task description: ")
    task = {"description": description, "completed": False}
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    """Display all tasks with their status."""
    if not tasks:
        print("No tasks available.")
        return
    
    print("\n--- Schedule ---")
    for index, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{index}. {task['description']} - {status}")
    print()

def mark_task_complete():
    """Mark a task as completed."""
    view_tasks()
    task_num = int(input("Enter the task number to mark as complete: ")) - 1
    
    if 0 <= task_num < len(tasks):
        tasks[task_num]["completed"] = True
        print("Task marked as complete!")
    else:
        print("Invalid task number. Please try again.")

def delete_task():
    """Delete a task from the schedule."""
    view_tasks()
    task_num = int(input("Enter the task number to delete: ")) - 1
    
    if 0 <= task_num < len(tasks):
        removed_task = tasks.pop(task_num)
        print(f"Task '{removed_task['description']}' deleted successfully!")
    else:
        print("Invalid task number. Please try again.")

def main():
    """Main program loop."""
    while True:
        print("\nSchedule Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_task_complete()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
