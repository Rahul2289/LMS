from assests.data import LMS
from utils.display_utils import (dispaly_branch_details,display_year_details,display_sem_details)

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

        print("="*45)
        print("\t\tBOOK DETAILS")
        print("="*45)
        
        branch = dispaly_branch_details()
        year = display_year_details()
        sem = display_sem_details()

        name = input("\nEnter Book name: ")
        author = input("Enter Author name: ")
        quantity = int(input("Enter Quantity: "))
        book = {"name":name,"author":author,"quantity":quantity}
        LMS["BOOKS"][branch][year][sem].append(book)
        print('\nLMS--',LMS)
        choise = input("\nDo you want one more Book ?(Y/N)")
        if choise != 'y':
            status = False

def take_a_book(selected):
    NAME = get_proper_selected(selected)

    status = True
    while status:
        print("="*45)
        print("\t\tISSUE BOOK")
        print("="*45)
        
        branch = dispaly_branch_details()
        year = display_year_details()
        sem = display_sem_details()

        student_name = input(f"\nENTER {selected} NAME: ")
        book_name = input("Enter Book name: ")

        all_students = LMS[NAME][branch][year][sem]
        student_list = list(filter(lambda x: x["name"]==student_name, all_students))
        
        all_books = LMS["BOOKS"][branch][year][sem]
        book_list = list(filter(lambda x: x["name"]==book_name, all_books))

        print(f'\n{selected}_list--',student_list)
        print('\nbook_list--',book_list)

        if student_list and book_list:
            if book_list[0]["quantity"] > 0:
                book_list[0]["quantity"] -= 1
                print(f"\nBook '{book_name}' issued to '{student_name}' successfully")
            else:
                print(f"\nBook '{book_name}' is not available right now")
        else:
            if not student_list:
                print(f"\n{selected} '{student_name}' not found")
            if not book_list:
                print(f"\nBook '{book_name}' not found")

        print('\nLMS--',LMS)
        choise = input("\nDo you want to issue one more Book ?(Y/N)")
        if choise != 'y':
            status = False

def view_books():
    status = True
    while status:
        print("="*45)
        print("\t\tVIEW BOOKS")
        print("="*45)
        
        branch = dispaly_branch_details()
        year = display_year_details()
        sem = display_sem_details()

        all_books = LMS["BOOKS"][branch][year][sem]

        if all_books:
            print(f"\nBooks available in {branch} - {year} - {sem}:\n")
            for book in all_books:
                print(f"Name: {book['name']}, Author: {book['author']}, Quantity: {book['quantity']}")
        else:
            print(f"\nNo books found in {branch} - {year} - {sem}")

        choise = input("\nDo you want to view books for another category ?(Y/N)")
        if choise != 'y':
            status = False

def return_book(selected):
    NAME = get_proper_selected(selected)
    status = True
    while status:
        print("="*45)
        print("\t\tRETURN BOOK")
        print("="*45)
        
        branch = dispaly_branch_details()
        year = display_year_details()
        sem = display_sem_details()

        student_name = input(f"\nENTER {selected} NAME: ")
        book_name = input("Enter Book name: ")

        print(f'\nselected--{selected}, NAME--{NAME}')
        print(f'branch--{branch}, year--{year}, sem--{sem}')
        all_students = LMS[NAME][branch][year][sem]
        student_list = list(filter(lambda x: x["name"]==student_name, all_students))
        
        all_books = LMS["BOOKS"][branch][year][sem]
        book_list = list(filter(lambda x: x["name"]==book_name, all_books))

        print(f'\n{selected}_list--',student_list)
        print('\nbook_list--',book_list)

        if student_list and book_list:
            book_list[0]["quantity"] += 1
            print(f"\nBook '{book_name}' returned by '{student_name}' successfully")
        else:
            if not student_list:
                print(f"\n{selected} '{student_name}' not found")
            if not book_list:
                print(f"\nBook '{book_name}' not found")

        print('\nLMS--',LMS)
        choise = input("\nDo you want to return one more Book ?(Y/N)")
        if choise != 'y':
            status = False
