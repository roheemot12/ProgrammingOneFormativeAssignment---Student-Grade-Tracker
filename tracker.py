class GradeTracker:
    def __init__(self):
        self.assignments = [ ]

    def add_assignment(self, assignment):
            self.assignments.append(assignment)

    def list_all(self):
            return self.assignments

    def filter_by_subject(self, subject):
           return [a for a in self.assignments if a.subject.lower() == subject.lower()]
    
    def filter_by_type(self, type_name):
         return [a for a in self.assignments if type(a).__name__.lower() ==  type_name.lower()] 

    def average_percentage(self):
          graded = [a for a in self.assignments if a.score is not None]
          if not graded:
              return None
          total = sum ((a.score / a.max_score) * 100 for a in graded)
          return total / len(graded)

    def  highest(self):
          graded = [a for a in self. assignments if a.score is not None]
          if not graded:
                return None
          return max(graded, key=lambda a: a.score / a.max_score)

    def lowest(self):
          graded = [a for a in self.assignments if a.score is not None]
          if not graded:
              return None
          return min(graded, key=lambda a: a.score / a.max_score)