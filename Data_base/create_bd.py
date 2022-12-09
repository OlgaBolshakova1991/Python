import pandas as pd
from pandas.io.excel import ExcelWriter
import numpy as np


def create_students_bd():
    students_names = ['Ginny', 'Harry', 'Ron', 'Hermione', 'Neville ', 'Frad', 'George',
                    'Padma', 'Terry', 'Luna', 'Michael', 'Cho', 'Marcus',
                    'Hannah', 'Susan', 'Cedric', 'Zacharias', 'Justin',
                    'Millicent', 'Gregory', 'Blaise', 'Vincent', 'Draco', 'Marcus', 'Pansy']
    students_surnames = ['Weasley', 'Potter', 'Weasley', 'Granger', 'Longbottom', 'Weasley', 'Weasley',
                        'Patil', 'Boot', 'Lovegood', 'Corner', 'Chang', 'Belby',
                        'Abbott', 'Bones', 'Diggory', 'Smith', 'Finch-Fletchley',
                        'Bulstrode', 'Goyle', 'Zabini', 'Crabbe', 'Malfoy', 'Flint', 'Parkinson']
    students_birthdays = ['11.08.1981', '31.07.1980', '01.03.1980', '19.09.1979', '31.07.1980', '01.04.1978', '01.04.1978',
                        '04.05.1980', '09.12.1979', '13.02.1981', '15.08.1979', '13.03.1979', '21.06.1978',
                        '14.03.1979', '02.02.1980', '20.12.1977', '29.09.1979', '03.06.1980',
                        '01.08.1980', '31.10.1979', '16.02.1979', '15.09.1979', '05.06.1980', '27.04.1976', '13.05.1981']
    students_dormitories = ['Gryffindor', 'Gryffindor', 'Gryffindor', 'Gryffindor', 'Gryffindor', 'Gryffindor', 'Gryffindor',
                        'Ravenclaw', 'Ravenclaw', 'Ravenclaw', 'Ravenclaw', 'Ravenclaw', 'Ravenclaw',
                        'Hufflepuff', 'Hufflepuff', 'Hufflepuff', 'Hufflepuff', 'Hufflepuff',
                        'Slytherin', 'Slytherin', 'Slytherin', 'Slytherin', 'Slytherin', 'Slytherin', 'Slytherin']
    courses = [2, 3, 3, 3, 3, 5, 5,
            3, 3, 2, 4, 4, 5,
            4, 3, 5, 4, 3,
            3, 3, 4, 3, 3, 7, 2]

    df_students = pd.DataFrame({'Surname': students_surnames, 'Name': students_names, 
                                'Birthday': students_birthdays, 'Dormitory': students_dormitories, 'Course': courses})
    
    df_students.index = np.arange(1, len(df_students) + 1)
    df_students.to_excel('school.xlsx', sheet_name="Students")
    
    return 'Data base of students is created.'


def create_teachers_bd():
    teachers_names = ['Aurora', 'Filius', 'Remus', 'Severus', 'Cuthbert', 'Pomona', 'Minerva', 'Rolanda',
                    'Bathsheda', 'Charity', 'Septima', 'Sybill', 'Rubeus']
    teachers_surnames = ['Sinistra', 'Flitwick', 'Lupin', 'Snape', 'Binns', 'Sprout', 'McGonagall', 'Hooch',
                        'Babbling', 'Burbage', 'Vector', 'Trelawney', 'Hagrid']
    subjects = ['Astronomy', 'Charms', 'Defence against the Dark Arts', 'Potions', 'History of Magic',
                'Herbology', 'Transfiguration', 'Flying', 'Study of Ancient Runes', 'Muggle Studies',
                'Arithmancy', 'Divination', 'Care of Magical Creatures']

    df_teachers = pd.DataFrame({'Surname': teachers_surnames, 'Name': teachers_names, 'Subject': subjects})

    df_teachers.index = np.arange(1, len(df_teachers) + 1)
    
    with ExcelWriter('school.xlsx', mode="a") as writer: 
        df_teachers.to_excel(writer, sheet_name="Teachers")

    return 'Data base of teachers is created.'
