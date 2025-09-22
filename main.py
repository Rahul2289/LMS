"""
This file is the starting file for Innomatics LMS project
Author: burrarahulgoud1999@gmail.com
Copy right: 2025@Innomatics
"""
import sys
sys.path.append('/c/Users/Rahul/innomatics-448/LMS')

from assests.data import save_data
from commons.login import login
from utils.display_utils import (dispaly_admin_options,dispaly_login_options,dispaly_student_teacher_options)
from utils.admin_utils import process_request,book_request

def main():
    print('\n')
    print("="*45)
    print("\t\tWelcome to LMS")
    print("="*45)

    status = True

    while status:

        login_status, turn_off, selected = dispaly_login_options()

        if turn_off:
            print("\nTurning off software\n")
            status = False
            save_data()
            break

        if login_status:
            if selected == "ADMIN":
                choise = dispaly_admin_options()
                process_request(choise,selected)
            elif selected == "STUDENT":
                choise = dispaly_student_teacher_options()
                book_request(choise,selected)
            elif selected == "TEACHER":
                choise = dispaly_student_teacher_options()
                book_request(choise,selected)
        else:
            print("\nUnsuccessful login, Try again later")
            save_data()

if __name__ == "__main__":
    main()
