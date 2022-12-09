import excep
import pandas as pd
from pandas.io.excel import ExcelWriter
import numpy as np


def add_student():
    student_name = excep.check_name("Enter student's name: ")
    student_surname = excep.check_name("Enter student's surname: ")
    student_birthday = excep.check_date()
    dormitory = excep.check_dormitory()
    course = excep.check_course()
    
    student_data = {'Surname': student_surname, 'Name': student_name, 'Birthday': student_birthday, 
                    'Dormitory': dormitory, 'Course': course}

    df_students = pd.read_excel('school.xlsx', sheet_name='Students', index_col=0)    
    df = df_students.append(student_data, ignore_index=True)
    
    df.index = np.arange(1, len(df) + 1)
    df.to_excel('school.xlsx', sheet_name="Students")

    return "The data are written."


def change_student_data():
    df_students = pd.read_excel('school.xlsx', sheet_name='Students', index_col=0)

    while True:
        student_name = excep.check_name("Enter student's name for changing: ")
        student_surname = excep.check_name("Enter student's surname for changing: ")
        
        if student_name and student_surname in df_students.values:
            break
        else:
            print("This student does not exist! Try again.")
    
    print()
    print("Enter new data: ")
    new_student_name = excep.check_name("Enter student's name: ")
    new_student_surname = excep.check_name("Enter student's surname: ")
    new_student_birthday = excep.check_date()
    new_dormitory = excep.check_dormitory()
    new_course = excep.check_course()

    df_students['Name'] = np.where((df_students['Name'] == student_name) & (df_students['Surname'] == student_surname),
                        new_student_name, df_students['Name'])
    df_students['Surname'] = np.where((df_students['Name'] == new_student_name) & (df_students['Surname'] == student_surname), 
                        new_student_surname, df_students['Surname'])
    df_students['Birthday'] = np.where((df_students['Name'] == new_student_name) & (df_students['Surname'] == new_student_surname), 
                        new_student_birthday, df_students['Birthday'])
    df_students['Dormitory'] = np.where((df_students['Name'] == new_student_name) & (df_students['Surname'] == new_student_surname), 
                        new_dormitory, df_students['Dormitory'])
    df_students['Course'] = np.where((df_students['Name'] == new_student_name) & (df_students['Surname'] == new_student_surname), 
                        new_course, df_students['Course'])
    
    df_students.index = np.arange(1, len(df_students) + 1)
    df_students.to_excel('school.xlsx', sheet_name="Students")

    return "The data are written."



def delete_student():
    df_students = pd.read_excel('school.xlsx', sheet_name='Students', index_col=0)

    while True:
        student_name = excep.check_name("Enter student's name for delete: ")
        student_surname = excep.check_name("Enter student's surname for delete: ")
        
        if student_name and student_surname in df_students.values:
            break
        else:
            print("This student does not exist! Try again.")

    df = df_students[(df_students['Name'] != student_name) & (df_students['Surname'] != student_surname)]

    df.index = np.arange(1, len(df) + 1)
    df.to_excel('school.xlsx', sheet_name="Students")

    return "The data are written."



def search_by_name_surname():
    df_students = pd.read_excel('school.xlsx', sheet_name='Students', index_col=0)

    while True:
        student_name = excep.check_name("Enter student's name for searching: ")
        student_surname = excep.check_name("Enter student's surname for searching: ")
        
        if student_name and student_surname in df_students.values:
            break
        else:
            print("This student does not exist! Try again.")
    
    df = df_students[(df_students['Name'] == student_name) & (df_students['Surname'] == student_surname)]

    return df
