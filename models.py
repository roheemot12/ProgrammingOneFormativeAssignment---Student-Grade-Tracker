class Assignment:
    def __init__(self, title, subject, date, max_score, score=None):
        self.title = title
        self.subject = subject
        self.date = date
        self.max_score = max_score
        self.score = score

    def record_score(self, score):
        if score < 0:
            raise ValueError("Score cannot be negative.")
        if score > self.max_score:
            raise ValueError(f"Score cannot exceed max score of {self.max_score}.")
        self.score = score

    def __str__(self):
        if self.score is None:
            return f"{self.title} ({self.subject}) - Not graded now"
        percentage = (self.score / self.max_score) * 100
        return f"{self.title} ({self.subject}) - {self.score}/{self.max_score} ({percentage:.1f}%)"



if __name__ == "__main__":
        test_assignment = Assignment("English HW 1 ", "English", "2026-09-15", 20)
        test_assignment.record_score(15)
        print(test_assignment) 