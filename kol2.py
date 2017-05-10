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

import json

class HighSchool(object):
    def __init__(self):
        super(HighSchool, self).__init__()
        self.cont=0
        self.courses={}

    def create_course(self, course):
        self.courses[course]={}

    def enroll_student_in_course(self, course, name, surname):
        self.courses[course][name]={}
        self.courses[course][name][surname]=[0,[]] # [ attendance, grade ]

    def add_grade(self,course,name,surname,grade ):
        self.courses[course][name][surname][1].append(grade)

    def attend(self,course,name,surname):
        self.courses[course][name][surname][0]+=1

    def get_course_avg(self, course):
        sum=0
        for name in self.courses[course]:
			for surname in self.courses[course][name]:
				sum=sum+self.get_student_avg_grade_in_course(course,name,surname)
        return sum/len(self.courses[course])

    def get_student_avg_grade_in_course(self,course,name,surname):
        sum=0
        self.cont+=1
        for grade in self.courses[course][name][surname][1]:
            sum= sum+grade
        sum=sum/len(self.courses[course][name][surname][1])
        return sum
    def get_total_students_avg(self):
        sum=0
        for course in self.courses:
            sum=sum+ self.get_course_avg(course)
        return sum/len(self.courses)
    def get_student_avg_in_total(self,name,surname):
        sum=0;
        self.cont=0
        for course in self.courses:
            sum=sum+self.get_student_avg_grade_in_course(course,name,surname)
        sum=sum/self.cont
        return sum
    def get_json(self):
        with open('output_file.json','w+') as fp:
            json.dump(self.courses,fp)
    def init_from_json(self):
        with open('output_file.json') as data_file:
            self.courses=json.load(data_file)
        pass
print('build')
HighSchool= HighSchool()
HighSchool.create_course('math')
HighSchool.enroll_student_in_course('math','ayda','tanik')
HighSchool.enroll_student_in_course('math','cml','trk')
HighSchool.attend('math','ayda','tanik')
HighSchool.add_grade('math','ayda','tanik',70)
HighSchool.add_grade('math','ayda','tanik',90)
HighSchool.add_grade('math','cml','trk',100)
HighSchool.add_grade('math','cml','trk',98)
HighSchool.get_json()
print(HighSchool.courses)
print(HighSchool.get_total_students_avg())
print(HighSchool.get_student_avg_in_total('ayda','tanik'))
print(HighSchool.get_student_avg_in_total('cml','trk'))
HighSchool.courses={}
HighSchool.init_from_json()
print(HighSchool.courses)
    
            
        






