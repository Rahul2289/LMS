from assests.data import LMS, save_data
from utils.display_utils import (dispaly_branch_details,display_year_details,display_sem_details)
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
import assests.data as data
console = Console()

def get_proper_selected(selected):
    if selected == "STUDENT":
        return "STUDENTS"
    elif selected == "TEACHER":
        return "TEACHERS"
    else:
        return None

def add_books():
    status = True
    while status:

        console.print(
            Panel.fit(
            "[bold orange1]🎓  ADDING BOOK DETAILS  🎓[/bold orange1]",
            title="📚 Book Details",
            border_style="orange1",
            padding=(1, 5)
            )
        )
        
        branch = dispaly_branch_details()
        year = display_year_details()
        sem = display_sem_details()

        name = input("\nEnter Book name: ")
        author = input("Enter Author name: ")
        quantity = int(input("Enter Quantity: "))
        book = {"name":name,"author":author,"quantity":quantity}
        LMS["BOOKS"][branch][year][sem].append(book)

        save_data()

        choise = input("\nDo you want one more Book ?(Y/N)")
        if choise != 'y':
            status = False

def take_a_book(selected):
    NAME = get_proper_selected(selected)

    status = True
    while status:
        print("\n")
        console.print(Panel.fit("TAKE BOOK", style="bold orange1", padding=(1, 5)))
        print("\n")
        
        branch = dispaly_branch_details()
        year = display_year_details()
        sem = display_sem_details()

        book_name = input("Enter Book name: ")

        all_books = LMS["BOOKS"][branch][year][sem]
        book_list = list(filter(lambda x: x["name"] == book_name, all_books))

        # Find the student in any branch/year/sem
        student_found = False
        for b in LMS[NAME]:
            for y in LMS[NAME][b]:
                for s in LMS[NAME][b][y]:
                    students = LMS[NAME][b][y][s]
                    if any(x["name"] == data.LOGIN_NAME for x in students):
                        student_found = True
                        break
                if student_found:
                    break
            if student_found:
                break

        if student_found and book_list:
            if book_list[0]["quantity"] > 0:
                book_list[0]["quantity"] -= 1
                print(f"\nBook '{book_name}' issued to '{data.LOGIN_NAME}' successfully")
                save_data()
            else:
                print(f"\nBook '{book_name}' is not available right now")
        else:
            if not student_found:
                print(f"\n{selected} '{data.LOGIN_NAME}' not found")
            if not book_list:
                print(f"\nBook '{book_name}' not found")

        choise = input("\nDo you want to issue one more Book ?(Y/N)")
        if choise.lower() != 'y':
            status = False

def view_books():

    all_books = LMS["BOOKS"]

    table = Table(title="Library Books", show_lines=True)
    table.add_column("Branch", style="cyan", no_wrap=True)
    table.add_column("Year", style="magenta")
    table.add_column("Semester", style="green")
    table.add_column("Book Name", style="yellow")
    table.add_column("Author", style="blue")
    table.add_column("Quantity", style="red")

    found = False
    for branch, years in all_books.items():
        for year, sems in years.items():
            for sem, books in sems.items():
                for book in books:
                    table.add_row(
                        str(branch),
                        str(year),
                        str(sem),
                        book.get("name", ""),
                        book.get("author", ""),
                        str(book.get("quantity", 0))
                    )
                    found = True

    if found:
        console.print(table)
    else:
        console.print("[bold red]No books found in the library.[/bold red]")

def return_book(selected):
    NAME = get_proper_selected(selected)
    status = True
    while status:
        print("\n")
        console.print(Panel.fit("RETURN BOOK", style="bold orange1", padding=(1, 5)))
        print("\n")
        
        branch = dispaly_branch_details()
        year = display_year_details()
        sem = display_sem_details()

        book_name = input("Enter Book name: ")

        all_books = LMS["BOOKS"][branch][year][sem]
        book_list = list(filter(lambda x: x["name"] == book_name, all_books))

        # Find the student in any branch/year/sem
        student_found = False
        for b in LMS[NAME]:
            for y in LMS[NAME][b]:
                for s in LMS[NAME][b][y]:
                    students = LMS[NAME][b][y][s]
                    if any(x["name"] == data.LOGIN_NAME for x in students):
                        student_found = True
                        break
                if student_found:
                    break
            if student_found:
                break

        if student_found and book_list:
            book_list[0]["quantity"] += 1
            print(f"\nBook '{book_name}' returned by '{data.LOGIN_NAME}' successfully")
            save_data()
        else:
            if not student_found:
                print(f"\n{selected} '{data.LOGIN_NAME}' not found")
            if not book_list:
                print(f"\nBook '{book_name}' not found")

        choise = input("\nDo you want to return one more Book ?(Y/N)")
        if choise.lower() != 'y':
            status = False
