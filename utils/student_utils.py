from assests.data import LMS,save_data
from utils.display_utils import (dispaly_branch_details,display_year_details,display_sem_details)
from libs import print as rich_print,Console,Panel

console = Console()

def add_student():
    status = True
    while status:
        print("\n")
        console.print(
            Panel.fit(
            "[bold orange1]🎓  ADDING STUDENT DETAILS  🎓[/bold orange1]",
            title="👤 Student Details",
            border_style="orange1",
            padding=(1, 5)
            )
        )

        branch = dispaly_branch_details()
        year = display_year_details()
        sem = display_sem_details()

        name = input("\nEnter Student name: ")
        password = input("Enter Password: ")
        student = {"name":name,"password":password}

        LMS["STUDENTS"][branch][year][sem].append(student)
        save_data()
        choise = input("\nDo you want one more student ?(Y/N)")

        if choise != 'y':
            status = False

def add_teacher():
    status = True
    while status:

        console.print(
            Panel.fit(
            "[bold orange1]🎓  ADDING TEACHER DETAILS  🎓[/bold orange1]",
            title="👤 Teacher Details",
            border_style="orange1",
            padding=(1, 5)
            )
        )

        branch = dispaly_branch_details()
        year = display_year_details()
        sem = display_sem_details()

        name = input("\nEnter Teacher name: ")
        password = input("Enter Password: ")
        teacher = {"name":name,"password":password}

        LMS["TEACHERS"][branch][year][sem].append(teacher)
        save_data()
        choise = input("\nDo you want one more Teacher ?(Y/N)")


        if choise != 'y':
            status = False
