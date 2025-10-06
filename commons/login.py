from assests.data import LMS
from rich.console import Console
from rich.panel import Panel
import assests.data as data

console = Console()

def check_details(credentials):
    admin = credentials[0]
    name = credentials[1]
    password = credentials[2]
    if admin['name'] == name and admin['password'] == password:
        data.LOGIN_NAME = name
        return True
    else:
        return False
   
def admin_login():

    print("\n")
    console.print(Panel.fit("WELCOME TO ADMIN LOGIN", style="bold orange1", padding=(1, 5), subtitle=":lock: Secure Access :lock:"))
    print("\n")

    name = input("Enter your name: ")
    password = input("Enter your password: ")
    all_admins = list(zip(LMS["ADMINS"], [name]*len(LMS["ADMINS"]), [password]*len(LMS["ADMINS"]) ))
    output = list(filter(check_details,all_admins))

    if output:
        status = True
        print("\n")
        console.print(Panel.fit("[bold green]ADMIN LOGIN IS SUCCESSFUL[/bold green]", title=":tada: Success!", border_style="green",padding=(1, 10)))
    else:
        status = False
        print("\n")
        console.print(Panel.fit("[bold red]ADMIN LOGIN IS FAIL[/bold red]", title=":x: Error", border_style="red",padding=(1, 5)))

    return status

def student_login():
    status = True
    print("\n")
    console.print(Panel.fit("WELCOME TO STUDENT LOGIN", style="bold orange1", padding=(1, 10)))
    print("\n")
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
        console.print(Panel.fit("[bold green]STUDENT LOGIN IS SUCCESSFUL[/bold green]", title=":tada: Success!", border_style="green",padding=(1, 10)))
    else:
        status = False
        console.print(Panel.fit("[bold red]STUDENT LOGIN IS FAIL[/bold red]", title=":x: Error", border_style="red",padding=(1, 5)))
    return status

def teacher_login():
    status = True
    console.print(Panel.fit("WELCOME TO TEACHER LOGIN", style="bold orange1", padding=(1, 10)))
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
        console.print(Panel.fit("[bold green]TEACHER LOGIN IS SUCCESSFUL[/bold green]", title=":tada: Success!", border_style="green",padding=(1, 10)))
    else:
        status = False
        console.print(Panel.fit("[bold red]TEACHER LOGIN IS FAIL[/bold red]", title=":x: Error", border_style="red",padding=(1, 5)))

    return status
    

def login(type_of_login):
    if type_of_login == "ADMIN":
       login_status =  admin_login()
    elif type_of_login == "STUDENT":
       login_status =  student_login()
    elif type_of_login == "TEACHER":
       login_status = teacher_login()
    return login_status