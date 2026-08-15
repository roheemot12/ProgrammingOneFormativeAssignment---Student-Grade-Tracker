from models import Homework, Exam
from tracker import GradeTracker

# it will repeatedly asks the user to type something until they typer something (not blank).
def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print(" ! This field cannot be emmpty. Try again.")


        #It will repeatedly asks for a number grater than 0 (example: max score for an assignment)
def get_positive_float(prompt):
    while True:
        raw_value = input(prompt).strip()
        try:
            value = float(raw_value)
            if value <= 0:
                print(" ! Please enter a number grater than 0.")
                continue
            return value

        except ValueError:
            print(" ! Please enter a valid number. Try agin.")


#it will repeatedly asks for a score between 0 and max_score (inclusive)
def get_score_input(prompt, max_score) :
                while True:
                    raw_value = input(prompt).strip()
                    try:
                        value = float(raw_value)
                        if value < 0 or value > max_score:
                            print(f"  ! Please  dear enter a score between 0 and {max_score}.")
                            continue
                        return value
                    except ValueError:
                        print(" ! Please dear enter a valid number. Try again.")


#this function below will ask the user for homework details and add it to the tracker.
def add_homework(tracker):
                            print("\n--- Add Homework ---")
                            title = get_non_empty_input("Enter the title: ")
                            subject = get_non_empty_input("Enter the subject: ")
                            date = get_non_empty_input("Enter the date (YYYY-MM-DD): ")
                            max_score = get_positive_float("Enter the maximum score: ")
                            score = get_score_input(f"Enter score achieved (0-{max_score}): ", max_score)

                            homework = Homework(title, subject, date, max_score, score)
                            tracker.add_assignment(homework)
                            print(f" Added : {homework}")


#this will asks the user for exam details and adds it to the tracker also.
def add_exam(tracker):
                                print("\n--- Add Exam ---")
                                title = get_non_empty_input("Enter the title: ")
                                subject = get_non_empty_input("Enter the subject: ")
                                date = get_non_empty_input("Enter the date (YYYY-MM-DD): ")
                                max_score = get_positive_float("Enter the maximum score: ")
                                score = get_score_input(f"Enter score achieved (0-{max_score}): ", max_score)
                                exam_type = get_non_empty_input("Enter exam type (Midterm/Final/Quiz): ")

                                exam = Exam(title, subject, date, max_score, score, exam_type=exam_type)
                                tracker.add_assignment(exam)
                                print(f" Added : {exam}")


#Prints every assignments currently stored, numbered.
def list_assignments(tracker, assignments=None):
                                    items = assignments if assignments is not None else tracker.list_all()
                                    print()
                                    if not items:
                                        print(" No assignments to show.")
                                        return
                                    for i, a in enumerate(items, start=1):
                                        print(f" {i}. {a}")

#This is a sub-menu that lets the user filter by subject or by type, then shows results.
def filter_menu(tracker):
                                            while True:
                                                print("\n--- Filter Assignments ---")
                                                print(" 1. Filter by Subject")
                                                print(" 2. Filter by Type (Homework/Exam)")
                                                print(" 3. Back to Main Menu")
                                                choice = input("Choose your option: ").strip()

                                                if choice == "1":
                                                    subject = get_non_empty_input("Subject to filter by: ")
                                                    results = tracker.filter_by_subject(subject)
                                                elif choice == "2":
                                                    type_name = get_non_empty_input("Type to filter by (Homework/Exam): ")
                                                    results = tracker.filter_by_type(type_name)

                                                else:
                                                    print(" ! Invalid option.")
                                                    return

                                                list_assignments(tracker, results)

#This will prints overall statistics: counts, average, highest and lowest scoring assignment.
def show_summary(tracker):
                                                    print("\n--- Grade Summary ---")
                                                    all_items = tracker.list_all()
                                                    if not all_items:
                                                        print(" No assignments to summarize.")
                                                        return

                                                    print(f" Total assignments: {len(all_items)}")

                                                    average = tracker.average_percentage()
                                                    if average is not None:
                                                        print(f" Average score: {average:.1f}%")
                                                    else:
                                                        print(" Average score: N/A (nothing graded yet)")
                                                    top = tracker.highest()
                                                    if top is not None:
                                                        print(f" Highest scoring assignment: {top}" )

                                                    bottom = tracker.lowest()
                                                    if bottom is not None:
                                                        print(f" Lowest scoring assignment: {bottom}")

MENU_TEXT = """
========================================
   Student Grade/Assignment Tracker
========================================
  1. Add Homework
  2. Add Exam
  3. List All Assignments
  4. Filter Assignments
  5. Show Grade Summary
  6. Exit
========================================
"""
#This below will rum the menu loop until the user choose to exit.
def main():
    tracker = GradeTracker()
    print("Welcome to the Student Grade/Assignment Tracker!")


    while True:
        print(MENU_TEXT)
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_homework(tracker)
        elif choice == "2":
            add_exam(tracker)
        elif choice == "3":
            list_assignments(tracker)
        elif choice == "4":
            filter_menu(tracker)
        elif choice == "5":
            show_summary(tracker)
        elif choice == "6":
            print("Thanks for using the Grade Tracker.Goodbye!")
            break
        else:
            print(" ! Invalid option. Please choose a number between 1-6.")



if __name__ == "__main__":
    main()


                                                        


                                                        



                                                            
                                                

                                                
                                    
            
