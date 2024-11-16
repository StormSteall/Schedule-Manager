Schedule Manager
A simple console-based Python application that helps users manage their daily tasks by adding, viewing, marking tasks as complete, and deleting them as needed. The Schedule Manager is designed to be an easy-to-use tool for organizing and tracking tasks, demonstrating basic CRUD (Create, Read, Update, Delete) operations.

Features
Add Task: Add new tasks with a description.
View Tasks: View a list of all tasks with their completion status (Pending or Completed).
Mark Task as Complete: Update a task's status to "Completed."
Delete Task: Remove tasks from the list.
Simple Console Interface: Easy-to-use interface with clear prompts.


How to Use

Run the Program:

Open a terminal and run the program with:
    python schedule_manager.py

Add a Task:
    Select the "Add Task" option and provide a description for the task.
        "Enter the task description: Complete homework"
        "Task added successfully!"

View Tasks:
    Choose the "View Tasks" option to display all tasks and their statuses.
        --- Schedule ---
        1. Complete homework - Pending

Mark a Task as Complete:
    Select "Mark Task as Complete" and choose the task number.
        Task marked as complete!
        --- Schedule ---
        1. Complete homework - Completed

Delete a Task:
    Choose "Delete Task" and select the task number to delete.
        Task 'Complete homework' deleted successfully!