import random 
from datetime import datetime

class Student:

    def __init__(self, i, n, d, c):
        self.__studentID = i
        self.__name = n
        self.__dob = d
        self.__class = c
        self.__age = 0
        self.__registration = ''


    def Current_Age(self):
        today = datetime.now().year
        splitdate = self.__dob.split('/')
        self.__age = today - int(splitdate[2])
        return self.__age
        
    def registration_dates(self):
        if self.__class == "Freshman":
            self.__registration = '4/10 thru 4/12'
        elif self.__class == "Sophomore":
            self.__registration = '4/7 thru 4/9'
        elif self.__class == "Junior":
            self.__registration = '4/4 thru 4/6'
        elif self.__class == "Senior":
            self.__registration = '4/1 thru 4/3'
        else:
           self.__registration = "Invalid Dates" 
        return self.__registration

    #We need to have a set for each attribute
    
    
    #We have to have a get method for each attribute
    def get_ID(self):
        return self.__studentID
    
    def get_name(self):
        return self.__name
    
    def get_dob(self):
        return self.__dob
    
    def get_ID(self):
        return self.__class
