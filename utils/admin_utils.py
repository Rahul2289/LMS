from utils.student_utils import add_student
from utils.display_utils import dispaly_admin_options

def process_request(choise):
    if choise == 1:
        add_student()
        dispaly_admin_options()
