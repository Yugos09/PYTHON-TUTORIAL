
"""
Week 3 Exercise:

 1. Create a Students class with methods to add, retrieve, update, and delete student grades.
 2. Use appropriate data types and data structures
 3. Handle exceptions for cases where a student is not found or invalid grades are entered.
 4. Your class should have a well formatted __repr__ method defined.
 """

class Students:
    def __init__(self, student={}, name=None, grade=None):
        self.student = student
        self.student['name'] = name
        self.student['grade'] = grade

    def __repr__(self):
        try:
            return f"This is a student of name: {self.student['name']} and grade: {self.student['grade']}"
        except KeyError:
            return f"This is a student of name: {self.student['name']}"

    def add_grade(self, grade):
        if grade < 0 or grade > 100:
            return "Please enter a grade between 0 and 100 inclusive"
        else:
            self.student['grade'] = grade

    def retrieve_grade(self, name):
        if name not in self.student['name']:
            return "Name not found"
        else:
            return f"{name} has a grade of {self.student['grade']}"
        
    def update_grade(self, name, grade):
        if name in self.student['name']:
            if grade < 0 or grade > 100:
                return "Please enter a grade between 0 and 100 inclusive"
            else:
                self.student['grade'] = grade
        else:
            return f"{name} is not a student."
        
    def delete_grade(self, name):
        if name not in self.student['name']:
            return "Name not found"
        else:
           del self.student['grade']

Ugoo = Students(name='Ugoo', grade= [])
Ugoo.update_grade
print(Ugoo)