"""Smart_Study_Planner program"""
DATA_FILE = "study_sessions.txt"
sessions = []


# display_menu()
def display_menu():
    """Displays the main menu of the Smart_Study_Planner program.
    """
    print("\nSmart Study Planner Menu:")
    print("1. Add a new study session")
    print("2. View all study sessions")
    print("3. Mark a session as completed")
    print("4. View statistics")
    print("5. Save and Exit")


# main()
def main():
    """"The main function of the Smart_Study_Planner program.
    It displays the menu, handles user input, and performs actions based on the user's choice."""
    load_sessions()

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_session()
        elif choice == "2":
            view_sessions()
        elif choice == "3":
            subject = input("Enter the subject of the session to mark as completed: ")
            search_by_subject(subject)
        elif choice == "4":
            study_statistics()
        elif choice == "5":
            save_sessions()
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# add_session()
def add_session():
    """Adds a new study session to the list of sessions."""
    subject = input("Enter the subject for the study session: ")
    topic = input("Enter the topic for the study session: ")
    date = input("Enter the date for the study session (YYYY-MM-DD): ")
    duration = input(
        "Enter the duration of the study session (in minutes): "
    )

    while True:
        try:
            duration = int(duration)

            if duration <= 0:
                raise ValueError("Duration must be a positive integer.")

            break

        except ValueError as k:
            print(f"Invalid input: {k}")
            duration = input(
                "Please enter a valid duration (in minutes): "
            )

    classification = classify_session(duration)

    # Store the session as a dictionary
    session = {
        "subject": subject,
        "topic": topic,
        "date": date,
        "duration": duration,
        "classification": classification,
        "completed": False
    }

    sessions.append(session)

    print("Study session added successfully!")

# classify_session()
def classify_session(duration):
    """Classifies the study session based on its duration."""
    if duration < 30:
        return "Short"
    elif duration <= 60:
        return "Medium"
    else:
        return "Long"


# view_sessions()
def view_sessions():
    """Displays all the study sessions logged in the program."""
    if not sessions:
        print("No study sessions logged yet.")
        return

    print("\nAll Study Sessions:")

    print(
        f"{'Subject':<15}"
        f" {'Topic':<20}"
        f"{'Date':<12}"
        f"{'Duration':<10}"
        f"{'Classification':<15}"
        f"{'Status':<12}"
    )

    print("-" * 90)

    for session in sessions:
        if session["completed"]:
            status = "Completed"
        else:
            status = "Pending"

        print(
            f"{session['subject']:<15}"
            f"{session['topic']:<20}"
            f"{session['date']:<12}"
            f"{session['duration']:<10}"
            f"{session['classification']:<15}"
            f"{status:<12}"
        )


# search_by_subject()
def search_by_subject(subject):
    """Searches for study sessions by subject and displays the results."""
    found_sessions = []

    for session in sessions:
        if session["subject"].lower() == subject.lower():
            found_sessions.append(session)

    if not found_sessions:
        print(f"No study sessions found for subject: {subject}")
        return

    print(f"\nStudy Sessions for Subject: {subject}")

    for session in found_sessions:
        if session["completed"]:
            status = "Completed"
        else:
            status = "Pending"

        print(
            f"Subject: {session['subject']}, "
            f"Topic: {session['topic']}, "
            f"Date: {session['date']}, "
            f"Duration: {session['duration']} minutes, "
            f"Classification: {session['classification']}, "
            f"Status: {status}"
        )

# study_statistics()
def study_statistics():
    """Calculates and displays statistics about the study sessions."""
    if not sessions:
        print("No study sessions logged yet.")
        return

    total_sessions = len(sessions)
    total_duration = sum(
        session["duration"] for session in sessions
    )

    average_duration = total_duration / total_sessions

    completed_sessions = sum(
        1 for session in sessions
        if session["completed"]
    )

    print("\nStudy Statistics:")
    print(f"Total Study Sessions: {total_sessions}")
    print(f"Completed Sessions: {completed_sessions}")
    print(f"Total Duration: {total_duration} minutes")
    print(
        f"Average Duration per Session: "
        f"{average_duration:.2f} minutes"
    )


# save_sessions()
def save_sessions():
    """Saves the study sessions to a data file."""
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        for session in sessions:
            line = (
                f"{session['subject']},"
                f"{session['topic']},"
                f"{session['date']},"
                f"{session['duration']},"
                f"{session['classification']},"
                f"{session['completed']}\n"
            )

            file.write(line)

    print(f"Study sessions saved to {DATA_FILE}")


# load_sessions()
def load_sessions():
    """Loads study sessions from the data file into the sessions list."""
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:

            for line in file:
                data = line.strip().split(",")

                if len(data) < 5:
                    continue

                subject = data[0]
                topic = data[1]
                date = data[2]
                duration = int(data[3])
                classification = data[4]

                if len(data) >= 6:
                    completed = data[5] == "True"
                else:
                    completed = False

                sessions.append({
                    "subject": subject,
                    "topic": topic,
                    "date": date,
                    "duration": duration,
                    "classification": classification,
                    "completed": completed
                })

        print(f"Study sessions loaded from {DATA_FILE}")

    except FileNotFoundError:
        print("No previous study sessions found. Starting fresh.")


# Run the program
if __name__ == "__main__":
    main()
   