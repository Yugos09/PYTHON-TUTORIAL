class Students:
    def __init__(self, student={}, name=None, grade=None):
        self.student = student
        self.student['name'] = name
        self.student ['grade'] = grade

        def __repr__(self):
            try:
                return f"This is a student of name{self.student['name']} and grades:{self.student['grade']}"
            except KeyError:
                return f"this is a student of name:{self.student['name']}"
            
    def add_grade(self, grade):
        self.student['grade'] = grade
        if grade < 0 or grade > 100:
            return "please enter a valid number between 0 and 100 inclusive"
        else:
            self.student['grade'] = grade

    def update_grade(self, name, grade):
        if name in self.student['name']:
            if name in self.student['name']:
                if grade < 0 or grade > 100:
                    return "please enter a valid number between 0 and 100 inclusive"
            else:
                self.student['grade'] = grade
        else:
            return f"{name} is not a student."
        
    def retrieve_grade(self, name, grade):
        if name not in self.student['name']:
            return "Name not found"
        else:
            return f"{name} has a grade of {self.student['grade']}"
        
    def delete_grade(self, name):
        if name not in self.student['name']:
            return "Name not found"
        else:
            del self.student['grade']

Ugoo = Students(name = 'Ugoo')
grade = 99
Ugoo.update_grade (99)
print(Ugoo)