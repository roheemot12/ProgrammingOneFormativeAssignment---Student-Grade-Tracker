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
