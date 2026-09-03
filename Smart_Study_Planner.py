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
    subject = input("Enter the subject for the study session: ")
    topic = input("Enter the topic for the study session: ")
    date = input("Enter the date for the study session (YYYY-MM-DD): ")
    duration = input("Enter the duration of the study session (in minutes): ")
    while True:
        try:
            duration = int(duration)
            if duration <= 0:
                raise ValueError("Duration must be a positive integer.")
            break
        except ValueError as k:
            print(f"Invalid input: {k}")
            duration = input("Please enter a valid duration (in minutes): ")
    # store each session as a dictionary in a list
    session = {
        "subject": subject,
        "topic": topic,
        "date": date,
        "duration": duration
    }
    # Function to add a new study session
    pass        