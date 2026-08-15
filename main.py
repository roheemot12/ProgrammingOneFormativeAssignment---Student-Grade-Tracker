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
