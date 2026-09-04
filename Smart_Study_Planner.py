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
    #classify_session(duration)
    def classify_session(duration):
        if duration < 30:
            return "Short"
        elif 30 <= duration <= 60:
            return "Medium"
        else:
            return "Long"
        
    # reused automatically wherever the function is called
    session["classification"] = classify_session(duration)
    # view_sessions()  
    # function that displays every logged session in a neatly formatted table
    def view_sessions():
        if not sessions:
            print("No study sessions logged yet.")
            return
        print("\nLogged Study Sessions:")
        print("{:<15} {:<20} {:<12} {:<10} {:<15}".format("Subject", "Topic", "Date", "Duration", "Classification"))
        print("-" * 75)
        for session in sessions:
            print("{:<15} {:<20} {:<12} {:<10} {:<15}".format(
                session["subject"], session["topic"], session["date"], session["duration"], session["classification"]
            ))
      


   # search_by_subject(subject)
   # function that lets the user type in a subject and returns all the sessions logged under that subject along with their details like date, duration, and classification
   def search_by_subject(subject):
    found_sessions = [session for session in sessions if session["subject"] == subject]
    if not found_sessions:
        print(f"No study sessions found for subject: {subject}")
        return
    print(f"\nStudy Sessions for Subject: {subject}")
    print("{:<15} {:<20} {:<12} {:<10} {:<15}".format("Subject", "Topic", "Date", "Duration", "Classification"))
    print("-" * 75)
    for session in found_sessions:
        print("{:<15} {:<20} {:<12} {:<10} {:<15}".format(
            session["subject"], session["topic"], session["date"], session["duration"], session["classification"]
        ))
def search_by_subject(subject):
    found_sessions = [session for session in sessions if session["subject"] == subject]


# study_statistics()
def study_statistics():
    if not sessions:
        print("No study sessions logged yet.")
        return
    total_sessions = len(sessions)
    total_duration = sum(session["duration"] for session in sessions)
    average_duration = total_duration / total_sessions
    print("\nStudy Statistics:")
    print(f"Total Study Sessions: {total_sessions}")
    print(f"Total Duration: {total_duration} minutes")
    print(f"Average Duration per Session: {average_duration:.2f} minutes")
    