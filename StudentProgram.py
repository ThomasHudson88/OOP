import StudentClass as s
from datetime import datetime

def main():
    #create an instance of the student
    mystudent = s.Student('123','John','06/01/2002','Freshman')

    #Student Age
    print(f"Student age {mystudent.Current_Age()}")
    #Registration Dates
    print(f"Dates for Registration: {mystudent.registration_dates()}")

main()