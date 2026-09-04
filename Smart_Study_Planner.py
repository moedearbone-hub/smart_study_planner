# dispaly_menu()

def display_menu():
        print("\nSmart Study Planner Menu:")
        print("1. Add a new study session")
        print("2. View all study sessions")
        print("3. Mark a session as completed")
        print("4. Delete a session")
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
            search_by_subject(subject)
        elif choice == "4":
            subject = input("Enter the subject of the session to delete: ")
            search_by_subject(subject)
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

    # store each session as a dictionary in a list
    session = {
        "subject": subject,
        "topic": topic,
        "date": date,
        "duration": duration
    }
    session.append(session)
    print("Study session added successfully!")
    
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
    print("{:<15} {:<20} {:<12} {:<10} {:<15}".format("Subject", "Topic", "Date", "Duration", "Classification"))
    print("-" * 75)
    for session in sessions:
        print("{:<15} {:<20} {:<12} {:<10} {:<15}".format(
            session["subject"], session["topic"], session["date"], session["duration"], session["classification"]
        ))

   # search_by_subject(subject) 
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

# save_sessions()
def save_sessions():
    with open("study_sessions.txt", "w") as file:
        for session in sessions:
            file.write(f"{session['subject']},{session['topic']},{session['date']},{session['duration']},{session['classification']}\n")
    print("Study sessions saved to study_sessions.txt")

# load_sessions()
def load_sessions():
    try:
        with open("study_sessions.txt", "r") as file:
            for line in file:
                subject, topic, date, duration, classification = line.strip().split(",")
                sessions.append({
                    "subject": subject,
                    "topic": topic,
                    "date": date,
                    "duration": int(duration),
                    "classification": classification
                })
        print("Study sessions loaded from study_sessions.txt")
    except FileNotFoundError:
        print("No previous study sessions found. Starting fresh.")
    if __name__ == "__main__":
        main()

