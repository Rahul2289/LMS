"""
This file is the starting file for Innomatics LMS project
Author: burrarahulgoud1999@gmail.com
Copy right: 2025@Innomatics
"""

import sys
sys.path.append('/c/Users/Rahul/innomatics-448/LMS')

from libs import print as rich_print,Console,Panel

from assests.data import save_data
from utils.display_utils import (dispaly_admin_options,dispaly_login_options,dispaly_student_teacher_options)
from utils.admin_utils import process_request,book_request

def main():
    print('\n')
    console = Console()
    console.print(Panel.fit("Welcome to LMS", style="bold orange1", padding=(1, 10)))

    status = True

    while status:

        login_status, turn_off, selected = dispaly_login_options()

        if turn_off:
            console.print("\n[bold orange1]Turning off software[/bold orange1]\n")
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
            console.print("\nUnsuccessful login, Try again later", style="bold red")
            save_data()

if __name__ == "__main__":
    main()
