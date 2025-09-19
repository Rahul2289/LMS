from assests.data import LMS

def check_details(credentials):
    admin = credentials[0]
    name = credentials[1]
    password = credentials[2]
    if admin['name'] == name and admin['password'] == password:
        return True
    else:
        return False
   
def admin_login():
    print("\nWELCOME TO ADMIN LOGIN\n")
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    all_admins = list(zip(LMS["ADMINS"], [name]*len(LMS["ADMINS"]), [password]*len(LMS["ADMINS"]) ))
    print("--all_admins--",all_admins)
    output = list(filter(check_details,all_admins))

    if output:
        status = True
        print("\n******ADMIN LOGIN IS SCUCESSFULL******")
    else:
        status = False
        print("\n******ADMIN LOGIN IS FAIL******")

    return status

def student_login():
    pass

def teacher_login():
    pass

def login(type_of_login):
    if type_of_login == "ADMIN":
       login_status =  admin_login()
    elif type_of_login == "STUDENT":
       login_status =  student_login()
    elif type_of_login == "TEACHER":
       login_status = teacher_login()
    return login_status