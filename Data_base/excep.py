from os import path
from datetime import date, datetime, timedelta


def wrong_input():
    while True:
        try:
            number = int(input("Enter a number: "))
            return number
        except ValueError:
            print('-' * 50)
            print("Incorrect entry! Please, choose something from the list!")
            print('-' * 50)


def check_not_file(text):
    while True:
        file_name = input(text)
        print('-' * 50)
        
        if path.exists(f"{file_name}.csv"):
            print("The file with this name already exists! Are you sure you want to overwrite the file?")
            
            while True:
                print("Enter 1 - if 'yes', or 2 - if 'no'.")
                print('-' * 50)
                num = wrong_input()
                print()
                
                if num == 1:
                    return file_name
                elif num == 2:
                    print("Enter new name of the file: ")
                    break
                else:
                    print('-' * 50)
                    print("Incorrect entry! Please, choose something from the list!")
                    print('-' * 50)
                    print()
        
        else:
            return file_name


def check_name(text):
    while True:
        name = input(text)
        if not name or not name.isalpha():
            print("Wrong input! The field can not be empty or contain numbers!")
        else:
            return name.capitalize()


def check_date():
    while True:
        try:
            birthday = input("Enter student's birthday (dd.mm.yyyy): ")
            max_date = date.today() - timedelta(days=4015)
            min_date = date.today() - timedelta(days=6205)
            d = datetime.strptime(birthday, '%d.%m.%Y').date()

            if not (min_date <= d <= max_date):
                print("Error! Date is out of range! Try again.")
                print()
            else:
                return birthday
        
        except ValueError:
            print("Error! Date is entered in wrong format! Try again.")
            print()


def check_dormitory():
    dormitoties = ['Gryffindor', 'Ravenclaw', 'Hufflepuff', 'Slytherin']
    while True:
        dormitory = input("Enter name of the dormitory: ")
        if dormitory not in dormitoties:
            print("Error! Entered dormitary doesn't exist! Try again.")
            print()
        else:
            return dormitory


def check_course():
    while True:
        try:
            course = int(input("Enter the course: "))
            if 1 <= course <= 7:
                return course
            else:
                print("Incorrect entry! Try again.")
                print()
        except ValueError:
            print("Incorrect entry! Try again.")
            print()
