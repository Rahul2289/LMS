from assests.data import LMS
from utils.display_utils import (dispaly_branch_details,display_year_details,display_sem_details)

def add_student():
    status = True
    while status:

        print("="*45)
        print("\t\tSTUDENT DETAILS")
        print("="*45)

        branch = dispaly_branch_details()
        year = display_year_details()
        sem = display_sem_details()

        name = input("\nEnter Student name: ")
        password = input("Enter Password: ")
        student = {"name":name,"password":password}

        LMS["STUDENTS"][branch][year][sem].append(student)
        choise = input("\nDo you want one more student ?(Y/N)")

        print('LMS--',LMS)

        if choise != 'y':
            status = False

def add_teacher():
    status = True
    while status:

        print("="*45)
        print("\t\tTEACHER DETAILS")
        print("="*45)

        branch = dispaly_branch_details()
        year = display_year_details()
        sem = display_sem_details()

        name = input("\nEnter Teacher name: ")
        password = input("Enter Password: ")
        teacher = {"name":name,"password":password}

        LMS["TEACHERS"][branch][year][sem].append(teacher)

        print('\nLMS--',LMS)

        choise = input("\nDo you want one more Teacher ?(Y/N)")


        if choise != 'y':
            status = False
