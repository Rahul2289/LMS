"""
This file is the starting file for Innomatics LMS project
Author: burrarahulgoud1999@gmail.com
Copy right: 2025@Innomatics
"""
import sys
sys.path.append('/c/Users/Rahul/innomatics-448/LMS')

from assests.data import initialize_data
from commons.login import login
from utils.display_utils import (dispaly_admin_options,dispaly_login_options,dispaly_student_options,dispaly_teacher_options)
from utils.admin_utils import process_request

def main():
    print('\n')
    print("="*45)
    print("\t\tWelcome to LMS")
    print("="*45)

    status = True
    initialize_data() 

    while status:

        # print("running main loop")
        
        login_status, turn_off, selected = dispaly_login_options()

        # print('login_status,turn_off,selected--', login_status, turn_off, selected)

        if turn_off:
            print("\nTurning off software\n")
            status = False
            break

        if login_status:
            if selected == "ADMIN":
                choise = dispaly_admin_options()
                process_request(choise,selected)
            elif selected == "STUDENT":
                choise = dispaly_student_options()
                process_request(choise,selected)
            elif selected == "TEACHER":
                choise = dispaly_teacher_options()
                process_request(choise,selected)
        else:
            print("\nUnsuccessful login, Try again later")

if __name__ == "__main__":
    main()
