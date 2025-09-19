
from commons.login import login
from config import DEPTS,YEARS,SEMS

def dispaly_admin_options():
    # print('dispaly_admin_options')
    status = True
    while status:
        print("\n")
        print("1.Adding Students\n2.Adding Teachers\n3.Adding Books\n4.Adding Admins\n5.Logout")
        print("\n")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("\n ------ Adding Students ------\n")
            return 1
        elif choice == 2:
            print("\n ------ Adding Teachers ------")
            return 2
        elif choice == 3:
            print("\n ------ Adding Books ------")
        elif choice == 4:
            print("\n ------  Adding Admins ------")
        elif choice == 5:
            print("LOG OUT")
            status = False
        else:
            print("Invalid choice, Try again")

def dispaly_login_options():
    status = True
    turn_off = False
    login_status = None
    selected = None
    while status:
        print("\nWho are you select any one below ?")
        print("\n1.ADMIN\n2.STUDENT\n3.TEACHER\n4.TRUN OFF\n")
        choice = int(input("Enter your choice: "))
        if choice == 1:
           login_status =  login("ADMIN")
           status = False 
           selected = "ADMIN"
        elif choice == 2:
           login_status = login("STUDENT")
           selected = "STUDENT"
           status = False 
        elif choice == 3:
           login_status =  login("TEACHER")
           selected = "TEACHER"
           status = False 
        elif choice == 4:
            print("\nTRUN OFF")
            status = False
            turn_off = True
        else:
            print("\nInvalid choice, Try again")
    return (login_status,turn_off,selected)

def dispaly_student_options():
    pass

def dispaly_teacher_options():
    pass

def display_year_details():
    status = True
    while status:
        s_no = 1
        print("\n**** YEAR DETAILS ****\n")
        for year in YEARS:
            print(f"{s_no}.{year}")
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
        print("\n**** SEM DETAILS ****\n")
        for sem in SEMS:
            print(f"{s_no}.{sem}")
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
        print("\n**** DEPARTMENT DETAILS ****\n")
        for dept in DEPTS:
            print(f"{s_no}.{dept}")
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