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