# A menu driven interface
def main():
    while True:
        print("\nSmart Study Planner Menu:")
        print("1. Add a new study task")
        print("2. View all study tasks")
        print("3. Mark a task as completed")
        print("4. Delete a task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_task_completed()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting the Smart Study Planner. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
    # add_session()
def add_session():
    # Function to add a new study session
    pass        