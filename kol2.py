#
# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.

class  Student(object):

    Student = []

    def __init__(self, name,surname):
        self.name = name
        self.surname = surname
        self.grades = []
        self.add_student()

    def add_student(self):
        self.student.append(self.name,self.surname)
        print('{} '.format(self.name,self.surname))


    def add_grades(self, grades):
        self.grades.append(grade)

    def averageCalculate(self):
        average=self.lab*0.4+self.project*0.6
        return average


