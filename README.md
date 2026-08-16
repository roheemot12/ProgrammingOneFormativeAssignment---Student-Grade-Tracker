# ProgrammingOneFormativeAssignment
This repository contains the first assignment for Programming 1

# Student Grade/Assignment Tracker

A command-line Python program that lets a student record homework and exam
results, view and filter their assignments, and see a grade summary — all
within a single terminal session.

## Features

- Add **Homework** results (title, subject, date, max score, score achieved).
- Add **Exam** results (same fields, plus an exam type such as Midterm/Final/Quiz).
- List **all** recorded assignments.
- **Filter** assignments by subject or by type (Homework/Exam).
- View a **grade summary**: total count, average score, and the
  highest/lowest scoring assignment.
- Graceful handling of invalid input (empty fields, non-numeric scores, scores
  outside the valid range, invalid menu choices) with clear feedback messages.
- Object-oriented design: `Assignment` base class with `Homework` and `Exam`
  subclasses using `super()`, and a `GradeTracker` class that manages the
  collection of assignments.

## Project Structure

ProgrammingOneFormativeAssignment/
├── main.py # Entry point: menu loop and user input handling
├── models.py # Assignment, Homework, Exam classes (OOP + inheritance)
├── tracker.py # GradeTracker class (add/list/filter/summary logic)
├── README.md # This file
├── REFLECTION.pdf # Short reflection
└── screenshots/ # Screenshots of the program running


## How to Run

1. Make sure you have **Python 3** installed.
2. Clone the repository:
```bash
   git clone https://github.com/roheemot12/ProgrammingOneFormativeAssignment---Student-Grade-Tracker.git
   cd ProgrammingOneFormativeAssignment---Student-Grade-Tracker
```
3. Run the program:
```bash
   python main.py
```
4. Follow the on-screen menu prompts.

No external libraries are required — the project only uses the Python
standard library.

## Menu Structure
========================================
Student Grade/Assignment Tracker
Add Homework
Add Exam
List All Assignments
Filter Assignments
Show Grade Summary
Exit
========================================

Choosing **4. Filter Assignments** opens a sub-menu:

-- Filter Assignments --

Filter by Subject
Filter by Type (Homework/Exam)

## Sample Interaction

Welcome to the Student Grade/Assignment Tracker!

Choose an option (1-6): 1

-- Add Homework --
Enter the title: Math HW 1
Enter the subject: Math
Enter the date (YYYY-MM-DD): 2026-08-15
Enter the maximum score: 20
Enter score achieved (0-20.0): 18
Added: Math HW 1 (Math) - 18.0/20.0 (90.0%)

Choose an option (1-6): 5

-- Grade Summary --
Total assignments: 1
Average score: 90.0%
Highest scoring assignment: Math HW 1 (Math) - 18.0/20.0 (90.0%)
Lowest scoring assignment: Math HW 1 (Math) - 18.0/20.0 (90.0%)

Choose an option (1-6): 6

Goodbye! Thanks for using the Grade Tracker.

