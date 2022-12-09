import user_interface as u_i
import excep
import log
import create_bd as bd
import model_import as m_im
import model_student as m_s
from os import path
import pandas as pd


def run():
    school_bd = 'school.xlsx'
    if not path.exists(school_bd):
        bd.create_students_bd()
        bd.create_teachers_bd()
        log.log_operation('BDs are created.')
    
    print('*' * 50)
    print('WELCOME TO SCHOOL DIRECTORY!')
    print('*' * 50)

    while True:
        u_i.main_menu()
        print()
        num = excep.wrong_input()
        print('-' * 50)

        if num == 1:
            print("1. Students' menu")
            print()

            while True:
                u_i.students_menu()
                print()
                num = excep.wrong_input()
                print('-' * 50)

                if num == 1:
                    print("1. Add new student")
                    log.log_operation("1. Students' menu -> 1. Add new student")
                    print(m_s.add_student())
                    print('-' * 50)
                elif num == 2:
                    print("2. Change student's data")
                    log.log_operation("1. Students' menu -> 2. Change student's data")
                    print(m_s.change_student_data())
                    print('-' * 50)
                elif num == 3:
                    print("3. Delete student")
                    print("Please, try later...")
                    print('-' * 50)
                elif num == 4:
                    print("4. Show data")
                    print()

                    while True:
                        u_i.export_student_menu()
                        print()
                        num = excep.wrong_input()
                        print('-' * 50)

                        if num == 1:
                            print("1. Show all data")
                            log.log_operation("1. Students' menu -> 4. Show data -> 1. Show all data")
                            df_students = pd.read_excel('school.xlsx', sheet_name='Students', index_col=0)
                            print()
                            print('-' * 50)
                            print(df_students)
                            print('-' * 50)
                        elif num == 2:
                            print("2. Searching by surname and name")
                            log.log_operation("1. Students' menu -> 4. Show data -> 2. Searching by surname and name")
                            print('-' * 50)
                            print(m_s.search_by_name_surname())
                            print('-' * 50)
                        elif num == 3:
                            print("3. Searching by dormitory")
                            log.log_operation("1. Students' menu -> 4. Show data -> 3. Searching by dormitory")
                            dormitory = excep.check_dormitory()
                            df_students = pd.read_excel('school.xlsx', sheet_name='Students', index_col=0)
                            df = df_students[df_students['Dormitory'] == dormitory]
                            print()
                            print('-' * 50)
                            print(df)
                            print('-' * 50)
                        elif num == 4:
                            print("4. Searching by course")
                            log.log_operation("1. Students' menu -> 4. Show data -> 4. Searching by course")
                            course = excep.check_course()
                            df_students = pd.read_excel('school.xlsx', sheet_name='Students', index_col=0)
                            df = df_students[df_students['Course'] == course]
                            print()
                            print('-' * 50)
                            print(df)
                            print('-' * 50)
                        elif num == 5:
                            print("5. Return to the previous menu")
                            print('-' * 50)
                            break
                        else:
                            print('-' * 50)
                            print("Incorrect entry! Please, choose something from the list!")
                            print('-' * 50)          

                elif num == 5:
                    print("5. Return to the Main menu")
                    print('-' * 50)
                    break
                else:
                    print('-' * 50)
                    print("Incorrect entry! Please, choose something from the list!")
                    print('-' * 50)

        elif num == 2:
            u_i.teachers_menu()
            print("Please, try later...")
            print('-' * 50)
        elif num == 3:
            print("3. Import data to csv")
            log.log_operation("3. Import data to csv")
            print()
            print(m_im.save_to_csv())
        elif num == 4:
            print('-' * 50)
            print("The programm has finished working.")
            print('-' * 50)
            break
        else:
            print('-' * 50)
            print("Incorrect entry! Please, choose something from the list!")
            print('-' * 50)
