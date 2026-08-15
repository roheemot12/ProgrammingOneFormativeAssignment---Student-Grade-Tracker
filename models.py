
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


class Homework(Assignment):
        def __init__(self, title, subject, date, max_score, score=None):
           super().__init__(title, subject, date, max_score, score)


class Exam(Assignment):
    def __init__(self, title, subject, date, max_score, score=None, exam_type="Midterm"):
        super().__init__(title, subject, date, max_score, score)
        self.exam_type = exam_type


