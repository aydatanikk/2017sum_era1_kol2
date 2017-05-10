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

class  Course(object):

    def __init__(self):
        self.information={}
        self.cont=0
        
    def add_student(self, name,surname):
        self.information[name]=[surname,0,[]]
    
    def add_grade(self,surname,grade ):
        self.information[surname].append(grade)
        
    def add_attendance(self,name,surname):
        self.information[name][surname]

    def get_average_grade(self, student):
        sum=0
        self.cont+=1
        for grade in self.information[][student]:
            sum= sum+grade
        sum=sum/len(self.information[][student])
        return sum
    
    def average_Grade_Students(self,student):
        sum=0
        for st in self.information[]:
            sum=sum+self.get_average_grade(information, std)
        return sum/len(self.information[])
        
    def get_json(self):
        with open('strings.json') as json_data:
        d = json.load(json_data)
        print(d)
        
    def init_from_json(self):
        with open('strings.json') as data_file:
        self.information=json.load(data_file)
        pass   
    
            
        






