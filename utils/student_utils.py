from assests.data import LMS,save_data
from utils.display_utils import (dispaly_branch_details,display_year_details,display_sem_details)
from libs import print as rich_print,Console,Panel

console = Console()

def add_student():
    status = True
    while status:
        print("\n")
        console.print(
            Panel.fit(
            "[bold orange1]🎓  ADDING STUDENT DETAILS  🎓[/bold orange1]",
            title="👤 Student Details",
            border_style="orange1",
            padding=(1, 5)
            )
        )

        branch = dispaly_branch_details()
        year = display_year_details()
        sem = display_sem_details()

        name = input("\nEnter Student name: ")
        password = input("Enter Password: ")
        student = {"name":name,"password":password}

        LMS["STUDENTS"][branch][year][sem].append(student)
        save_data()
        choise = input("\nDo you want one more student ?(Y/N)")

        if choise != 'y':
            status = False

def add_teacher():
    status = True
    while status:

        console.print(
            Panel.fit(
            "[bold orange1]🎓  ADDING TEACHER DETAILS  🎓[/bold orange1]",
            title="👤 Teacher Details",
            border_style="orange1",
            padding=(1, 5)
            )
        )

        branch = dispaly_branch_details()
        year = display_year_details()
        sem = display_sem_details()

        name = input("\nEnter Teacher name: ")
        password = input("Enter Password: ")
        teacher = {"name":name,"password":password}

        LMS["TEACHERS"][branch][year][sem].append(teacher)
        save_data()
        choise = input("\nDo you want one more Teacher ?(Y/N)")


        if choise != 'y':
            status = False

def delete_student():
    status = True
    while status:
        print("\n")
        console.print(
            Panel.fit(
            "[bold orange1]🎓  DELETING STUDENT DETAILS  🎓[/bold orange1]",
            title="👤 Student Details",
            border_style="orange1",
            padding=(1, 5)
            )
        )

        branch = dispaly_branch_details()
        year = display_year_details()
        sem = display_sem_details()

        name = input("\nEnter Student name to delete: ")

        all_students = LMS["STUDENTS"][branch][year][sem]
        student_list = list(filter(lambda x: x["name"] == name, all_students))

        if student_list:
            LMS["STUDENTS"][branch][year][sem] = list(filter(lambda x: x["name"] != name, all_students))
            save_data()
            console.print(Panel.fit("[bold green]Student deleted successfully[/bold green]", title=":tada: Success!", border_style="green",padding=(1, 10)))
        else:
            console.print(Panel.fit("[bold red]Student not found[/bold red]", title=":x: Error!", border_style="red",padding=(1, 10)))

        choise = input("\nDo you want one more student deletion ?(Y/N)")

        if choise != 'y':
            status = False

def update_student():
    status = True
    while status:
        print("\n")
        console.print(
            Panel.fit(
            "[bold orange1]🎓  UPDATING STUDENT DETAILS  🎓[/bold orange1]",
            title="👤 Student Details",
            border_style="orange1",
            padding=(1, 5)
            )
        )

        branch = dispaly_branch_details()
        year = display_year_details()
        sem = display_sem_details()

        name = input("\nEnter Student name to update: ")

        all_students = LMS["STUDENTS"][branch][year][sem]
        student_list = list(filter(lambda x: x["name"] == name, all_students))

        if student_list:
            new_name = input("Enter new name: ")
            new_password = input("Enter new password: ")
            for student in all_students:
                if student["name"] == name:
                    student["name"] = new_name
                    student["password"] = new_password
            save_data()
            console.print(Panel.fit("[bold green]Student updated successfully[/bold green]", title=":tada: Success!", border_style="green",padding=(1, 10)))
        else:
            console.print(Panel.fit("[bold red]Student not found[/bold red]", title=":x: Error!", border_style="red",padding=(1, 10)))

        choise = input("\nDo you want one more student update ?(Y/N)")

        if choise != 'y':
            status = False

def update_teacher():
    status = True
    while status:
        print("\n")
        console.print(
            Panel.fit(
            "[bold orange1]🎓  UPDATING TEACHER DETAILS  🎓[/bold orange1]",
            title="👤 Teacher Details",
            border_style="orange1",
            padding=(1, 5)
            )
        )

        branch = dispaly_branch_details()
        year = display_year_details()
        sem = display_sem_details()

        name = input("\nEnter Teacher name to update: ")

        all_teachers = LMS["TEACHERS"][branch][year][sem]
        teacher_list = list(filter(lambda x: x["name"] == name, all_teachers))

        if teacher_list:
            new_name = input("Enter new name: ")
            new_password = input("Enter new password: ")
            for teacher in all_teachers:
                if teacher["name"] == name:
                    teacher["name"] = new_name
                    teacher["password"] = new_password
            save_data()
            console.print(Panel.fit("[bold green]Teacher updated successfully[/bold green]", title=":tada: Success!", border_style="green",padding=(1, 10)))
        else:
            console.print(Panel.fit("[bold red]Teacher not found[/bold red]", title=":x: Error!", border_style="red",padding=(1, 10)))

        choise = input("\nDo you want one more Teacher update ?(Y/N)")

        if choise != 'y':
            status = False

def delete_teacher():
    status = True
    while status:
        print("\n")
        console.print(
            Panel.fit(
            "[bold orange1]🎓  DELETING TEACHER DETAILS  🎓[/bold orange1]",
            title="👤 Teacher Details",
            border_style="orange1",
            padding=(1, 5)
            )
        )

        branch = dispaly_branch_details()
        year = display_year_details()
        sem = display_sem_details()

        name = input("\nEnter Teacher name to delete: ")

        all_teachers = LMS["TEACHERS"][branch][year][sem]
        teacher_list = list(filter(lambda x: x["name"] == name, all_teachers))

        if teacher_list:
            LMS["TEACHERS"][branch][year][sem] = list(filter(lambda x: x["name"] != name, all_teachers))
            save_data()
            console.print(Panel.fit("[bold green]Teacher deleted successfully[/bold green]", title=":tada: Success!", border_style="green",padding=(1, 10)))
        else:
            console.print(Panel.fit("[bold red]Teacher not found[/bold red]", title=":x: Error!", border_style="red",padding=(1, 10)))

        choise = input("\nDo you want one more Teacher deletion ?(Y/N)")

        if choise != 'y':
            status = False