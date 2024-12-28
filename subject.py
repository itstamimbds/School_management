from person import Teacher
from school import School
class Subject:
    def __init__(self,name,teacher):
        self.name=name
        self.teacher=teacher
        self.max_marks=100
        self.passed_mark=33
        
    def exam(self,students):
        for student in students:   
            mark=self.teacher.evalute_exam()
            student.marks[self.name]=mark
            student.subject_grade[self.name]=School.calculate_grade(mark)