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
    print("\n------ WELCOME TO ADMIN LOGIN ------\n")
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    all_admins = list(zip(LMS["ADMINS"], [name]*len(LMS["ADMINS"]), [password]*len(LMS["ADMINS"]) ))
    # print("--all_admins--",all_admins)
    output = list(filter(check_details,all_admins))

    if output:
        status = True
        print("\n****** ADMIN LOGIN IS SCUCESSFULL ******")
    else:
        status = False
        print("\n****** ADMIN LOGIN IS FAIL ******")

    return status

def student_login():
    status = True
    print("\n------ WELCOME TO STUDENT LOGIN ------\n")
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    all_students = []
    for branch in LMS["STUDENTS"]:
        for year in LMS["STUDENTS"][branch]:
            for sem in LMS["STUDENTS"][branch][year]:
                all_students.extend(LMS["STUDENTS"][branch][year][sem])
    all_students = list(zip(all_students, [name]*len(all_students), [password]*len(all_students) ))
    # print("--all_students--",all_students)
    output = list(filter(check_details,all_students))
    # print("--output--",output)
    if output:
        status = True
        print("\n****** STUDENT LOGIN IS SCUCESSFULL ******")
    else:
        status = False
        print("\n****** STUDENT LOGIN IS FAIL ******")
    return status

def teacher_login():
    status = True
    print("\n------ WELCOME TO TEACHER LOGIN ------\n")
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    all_teachers = []
    for branch in LMS["TEACHERS"]:
        for year in LMS["TEACHERS"][branch]:
            for sem in LMS["TEACHERS"][branch][year]:
                all_teachers.extend(LMS["TEACHERS"][branch][year][sem])
    all_teachers = list(zip(all_teachers, [name]*len(all_teachers), [password]*len(all_teachers) ))
    # print("--all_teachers--",all_teachers)
    output = list(filter(check_details,all_teachers))
    # print("--output--",output)
    if output:
        status = True
        print("\n****** TEACHER LOGIN IS SCUCESSFULL ******")
    else:
        status = False
        print("\n****** TEACHER LOGIN IS FAIL ******")
    return status
    

def login(type_of_login):
    if type_of_login == "ADMIN":
       login_status =  admin_login()
    elif type_of_login == "STUDENT":
       login_status =  student_login()
    elif type_of_login == "TEACHER":
       login_status = teacher_login()
    return login_status