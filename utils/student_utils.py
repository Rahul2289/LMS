from assests.data import LMS
from utils.display_utils import (dispaly_branch_details,display_year_details,display_sem_details)

def add_student():
    status = True
    while status:
        print("="*40)
        print("STUDENT DETAILS")
        print("="*40)
        print("\nBRANCH DETAILS")
        branch = dispaly_branch_details()
        print("\nYEAR DETAILS")
        year = display_year_details()
        print("\nSEM DETAILS")
        sem = display_sem_details()
        name = input("Enter Student name: ")
        password = input("Enter Password: ")
        student = {"name":name,"password":password,"age":'23'}
        LMS["STUDENTS"][branch][year][sem].append(student)
        choise = input("Do you want one more student ?(Y/N)")
        print('LMS--',LMS)
        if choise != 'y':
            status = False


