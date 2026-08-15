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