from assests.data import LMS
from utils.student_utils import (add_student,add_teacher)
from utils.display_utils import dispaly_admin_options

def process_request(initial_choice):
    status = True
    choise = initial_choice
    while status:
        if choise == 1:
            add_student()
        elif choise == 2:
            add_teacher()
        elif choise == 4:
            add_admins()
        elif choise == 5:
            print("\nLogging out from Admin...\n")
            status = False
            break
        else:
            print("Invalid choice")

        choise = dispaly_admin_options()

def add_admins():
    status = True
    while status:
        name = input("\nEnter Admin name: ")
        password = input("Enter Password: ")
        admin = {"name":name,"password":password}
        LMS["ADMINS"].append(admin)
        print("\n---- New Admin added successfully -----")
        choise = input("\nDo you want one more Admin ?(Y/N)")

        print('LMS--',LMS)
        
        if choise != 'y':
            status = False
