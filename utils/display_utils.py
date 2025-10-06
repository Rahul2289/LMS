
from commons.login import login
from config import DEPTS,YEARS,SEMS
from libs import print as rich_print,Console,Panel
console = Console()
def dispaly_admin_options():
    status = True
    while status:
        rich_print("\n[bold blue]What Action you want to perform ?")
        print("\n")
        rich_print("[bold green]1.Adding Students\n2.Adding Teachers\n3.Adding Books\n4.Adding Admins\n5.Logout\n6.Delete Books\n7.Update Books\n8.Delete students\n9.Update students\n.10.Delete teachers\n11.Update teachers")
        print("\n")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            # print("\n ------ Adding Students ------\n")
            return 1
        elif choice == 2:
            # print("\n ------ Adding Teachers ------")
            return 2
        elif choice == 3:
            # print("\n ------ Adding Books ------")
            return 3
        elif choice == 4:
            console.print(Panel.fit("Adding Admins", style="bold orange1", padding=(1, 5)))
            # print("\n ------  Adding Admins ------")
            return 4
        elif choice == 5:
            print("LOG OUT")
            status = False
            return 5
        elif choice == 6:
            # print("\n ------ Delete Books ------")
            return 6
        elif choice == 7:
            # print("\n ------ Update Books ------")
            return 7
        elif choice == 8:
            # print("\n ------ Delete Students ------")
            return 8
        elif choice == 9:
            # print("\n ------ Update Students ------")
            return 9
        elif choice == 10:
            # print("\n ------ Delete Teachers ------")
            return 10
        elif choice == 11:
            # print("\n ------ Update Teachers ------")
            return 11
        
        else:
            print("Invalid choice, Try again")

def dispaly_login_options():
    status = True
    turn_off = False
    login_status = None
    selected = None
    while status:
        rich_print("\n[bold Green]Who are you select any one below ?")
        rich_print("\n[bold Blue]1.ADMIN\n2.STUDENT\n3.TEACHER\n4.TRUN OFF\n")
        choice = int(input("Enter your choice: "))
        if choice == 1:
           login_status =  login("ADMIN")
           selected = "ADMIN"
           status = False 
        elif choice == 2:
           login_status = login("STUDENT")
           selected = "STUDENT"
           status = False 
        elif choice == 3:
           login_status =  login("TEACHER")
           selected = "TEACHER"
           status = False 
        elif choice == 4:
            # print("\nTRUN OFF")
            status = False
            turn_off = True
        else:
            print("\nInvalid choice, Try again")
    return (login_status,turn_off,selected)

def dispaly_student_teacher_options():
    status = True
    while status:
        print("\n")
        rich_print("\n[bold Blue]1.View Books\n2.Take Book\n3.Return Book\n4.Logout")
        print("\n")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            # print("\n ------ View Books ------")
            return 1
        elif choice == 2:
            # print("\n ------ Take Book ------")
            return 2
        elif choice == 3:
            # print("\n ------ Return Book ------")
            return 3
        elif choice == 4:
            print("LOG OUT")
            status = False
            return 4
        else:
            print("Invalid choice, Try again")

def display_year_details():
    status = True
    while status:
        s_no = 1
        rich_print("\n[bold Green]**** YEAR DETAILS ****\n")
        for year in YEARS:
            rich_print(f"[bold blue]{s_no}.{year}")
            s_no+=1
        choise = input("\nSELECT ANY YEAR: ")

        status = True
        while status:
            try:
                choise= int(choise)
                status = False
            except:
                print("INVALID CHOICE,PLEASE ENETER NUMBERS ONLY")
        if choise in range(1,len(YEARS)+1):
            return YEARS[choise-1]

def display_sem_details():
    status = True
    while status:
        s_no = 1
        rich_print("\n[bold Green]**** SEM DETAILS ****\n")
        for sem in SEMS:
            rich_print(f"[bold blue]{s_no}.{sem}")
            s_no+=1
        choise = input("\nSELECT ANY SEMS: ")

        status = True
        while status:
            try:
                choise= int(choise)
                status = False
            except:
                print("\nsINVALID CHOICE,PLEASE ENETER NUMBERS ONLY")
        if choise in range(1,len(SEMS)+1):
            return SEMS[choise-1]

def dispaly_branch_details():
    status = True
    while status:
        s_no = 1
        rich_print("\n[bold Green]**** DEPARTMENT DETAILS ****\n")
        for dept in DEPTS:
            rich_print(f"[bold blue]{s_no}.{dept}")
            s_no+=1
        status = True
        while status:
            try:
                choise = input("\nSELECT ANY BRANCH: ")
                choise= int(choise)
                status = False
            except:
                print("\nINVALID CHOICE,PLEASE ENETER NUMBERS ONLY")
        if choise in range(1,len(DEPTS)+1):
            return DEPTS[choise-1]