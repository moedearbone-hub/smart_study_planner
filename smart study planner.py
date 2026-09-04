sessions = []


# display_menu()
def display_menu():
    print("\nSmart Study Planner Menu:")
    print("1. Add a new study session")
    print("2. View all study sessions")
    print("3. Mark a session as completed")
    print("4. View statistics")
    print("5. Save and Exit")


# main()
def main():
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
            mark_completed(subject)

        elif choice == "4":
            study_statistics()

        elif choice == "5":
            save_sessions()
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


    session = {
        "subject": subject,
        "topic": topic,
        "date": date,
        "duration": duration,
    
    }

    sessions.append(session)

    print("Study session added successfully!")


# classify_session()
def classify_session(duration):
    if duration < 30:
        return "Short"
    elif 30 <= duration <= 60:
        return "Medium"
    else:
        return "Long"


# view_sessions()
def view_sessions():
    if not sessions:
        print("No study sessions logged yet.")
        return

    print("\nAll Study Sessions:")

    print("{:<15} {:<20} {:<12} {:<10} {:<15} {:<12}".format(
        "Subject", "Topic", "Date", "Duration",
        "Classification", "Status"
    ))

    print("-" * 90)

    for session in sessions:
        status = "Completed" if session["completed"] else "Pending"

        print("{:<15} {:<20} {:<12} {:<10} {:<15} {:<12}".format(
            session["subject"],
            session["topic"],
            session["date"],
            session["duration"],
            session["classification"],
            status
        ))


# search_by_subject()
def search_by_subject(subject):
    found_sessions = [
        session for session in sessions
        if session["subject"].lower() == subject.lower()
    ]

    if not found_sessions:
        print(f"No study sessions found for subject: {subject}")
        return

    print(f"\nStudy Sessions for Subject: {subject}")

    for session in found_sessions:
        status = "Completed" if session["completed"] else "Pending"

        print(
            f"Subject: {session['subject']}, "
            f"Topic: {session['topic']}, "
            f"Date: {session['date']}, "
            f"Duration: {session['duration']} minutes, "
            f"Classification: {session['classification']}, "
            f"Status: {status}"
        )


# mark_completed()
def mark_completed(subject):
    found = False

    for session in sessions:
        if session["subject"].lower() == subject.lower():
            session["completed"] = True
            found = True

    if found:
        print(f"Sessions for {subject} marked as completed.")
    else:
        print(f"No study sessions found for subject: {subject}")


# delete_session()
def delete_session(subject):
    found = False

    for session in sessions[:]:
        if session["subject"].lower() == subject.lower():
            sessions.remove(session)
            found = True

    if found:
        print(f"Sessions for {subject} deleted successfully.")
    else:
        print(f"No study sessions found for subject: {subject}")


# study_statistics()
def study_statistics():
    if not sessions:
        print("No study sessions logged yet.")
        return

    total_sessions = len(sessions)
    total_duration = sum(session["duration"] for session in sessions)
    average_duration = total_duration / total_sessions

    completed_sessions = sum(
        1 for session in sessions if session["completed"]
    )

    print("\nStudy Statistics:")
    print(f"Total Study Sessions: {total_sessions}")
    print(f"Completed Sessions: {completed_sessions}")
    print(f"Total Duration: {total_duration} minutes")
    print(f"Average Duration per Session: {average_duration:.2f} minutes")


# save_sessions()
def save_sessions():
    with open("study_sessions.txt", "w") as file:
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

    print("Study sessions saved to study_sessions.txt")


# load_sessions()
def load_sessions():
    try:
        with open("study_sessions.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")

                subject = data[0]
                topic = data[1]
                date = data[2]
                duration = int(data[3])
                classification = data[4]

                if len(data) > 5:
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

        print("Study sessions loaded from study_sessions.txt")

    except FileNotFoundError:
        print("No previous study sessions found. Starting fresh.")


# Run the program
if __name__ == "__main__":
    main()