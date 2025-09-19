from utils.student_utils import (add_student,add_teacher)
from utils.display_utils import dispaly_admin_options

def process_request(choise):
    if choise == 1:
        add_student()
        print("--choise--",choise)
        dispaly_admin_options()
        print("**choise**",choise)
    elif choise == 2:
        add_teacher()
        dispaly_admin_options()
