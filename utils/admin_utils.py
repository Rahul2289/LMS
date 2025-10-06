from assests.data import LMS,save_data
from utils.student_utils import (add_student,add_teacher)
from utils.display_utils import dispaly_admin_options,dispaly_student_teacher_options
from utils.book_utils import add_books,take_a_book,view_books,return_book
from libs import print as rich_print,Console,Panel

console = Console()

def process_request(initial_choice,selected):
    status = True
    choise = initial_choice
    while status:
        if choise == 1 :
            add_student()                
        elif choise == 2:
            add_teacher()
        elif choise == 3:
            add_books()
        elif choise == 4 :
            add_admins()
        elif choise == 5:
            print("\nLogging out from Admin...\n")
            status = False
            break
        else:
            print("Invalid choice")

        choise = dispaly_admin_options()

def book_request(initial_choice,selected):
    status = True
    choise = initial_choice
    while status:
        if choise == 1 :
            view_books()
        elif choise == 2:
            take_a_book(selected)
        elif choise == 3:
            return_book(selected)
        elif choise == 4 :
            print("\nLogging out from Student...\n")
            status = False
            break
        else:
            print("Invalid choice")

        choise = dispaly_student_teacher_options()


def add_admins():
    status = True
    while status:
        name = input("\nEnter Admin name: ")
        password = input("Enter Password: ")
        admin = {"name":name,"password":password}
        LMS["ADMINS"].append(admin)
        save_data()
        console.print(Panel.fit("[bold green]New Admin added successfully[/bold green]", title=":tada: Success!", border_style="green",padding=(1, 10)))
        # print("\n---- New Admin added successfully -----")
        choise = input("\nDo you want one more Admin ?(Y/N)")

        # print('LMS--',LMS)
        
        if choise != 'y':
            status = False
