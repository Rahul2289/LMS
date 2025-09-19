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
    """
    Main function is a starting point for LMS
    """
    print("="*40)
    print("WElcome to LMS")
    print("="*40)

    login_status,turn_off,selected = dispaly_login_options()
    if turn_off:
        print("\nTurning off software\n")
        return #Scucessfull return
    
    if login_status:
        initialize_data()
        if selected == "ADMIN":
            choise = dispaly_admin_options()
            process_request(choise)
        elif selected == "STUDENT":
            dispaly_student_options()
        elif selected == "TEACHER":
            dispaly_teacher_options()

        status = True
        while status:
           login_status,turn_off,selected = dispaly_login_options()
           if turn_off:
             print("\nTurning of software")
             status = False
    else:
        print("\nUnsuccessful login,Try again later")
    
if __name__ == "__main__":
    main()
